"""AURA STUDIO v2 — the instrument layer.
Aura's render scripts import THIS instead of hand-building oscillators for
drums/FX, and use vita (Vital engine) for synths.

    from studio import api as st
    kick = st.load("bd/BD0000.wav")            # real one-shot, stereo float32
    out  = st.place(buf, kick, at_sample, gain=1.0, pan=0.0)
    saw  = st.synth("presets/SomePreset.vital", [(60, 0.9, 0.0, 1.0)], bpm=126)
    final = st.master(mix, sr=44100)

RVC vocal: harness-side (rvc_convert.py), not part of this module.
"""
import os, json, glob, functools
import numpy as np

SR = 44100
ROOT = os.path.dirname(os.path.abspath(__file__))  # studio/
SAMPLES = os.path.join(ROOT, "samples", "dirt")
PRESETS = os.path.join(ROOT, "vital_presets")


# ---------- samples ----------
def _find(name):
    """name: 'bd' or 'bd/BD0000.wav' -> absolute path"""
    name = name.strip("/")
    p = os.path.join(SAMPLES, name)
    if os.path.isfile(p):
        return p
    if os.path.isdir(p):
        files = sorted(glob.glob(os.path.join(p, "*.wav")))
        if files:
            return files[0]
    hits = sorted(glob.glob(os.path.join(SAMPLES, "**", name + "*.wav"), recursive=True))
    if hits:
        return hits[0]
    hits = sorted(glob.glob(os.path.join(SAMPLES, "**", name), recursive=True))
    if hits and os.path.isdir(hits[0]):
        files = sorted(glob.glob(os.path.join(hits[0], "*.wav")))
        if files:
            return files[0]
    raise FileNotFoundError(f"no sample for {name!r}")


def load(name, gain=1.0):
    """Load one-shot -> (2, N) float32 @ SR."""
    import soundfile as sf
    import librosa
    path = _find(name)
    x, sr = sf.read(path, dtype="float32", always_2d=False)
    if x.ndim == 1:
        x = np.stack([x, x], axis=0)
    else:
        x = x.T
    if sr != SR:
        x = librosa.resample(x, orig_sr=sr, target_sr=SR)
    x = np.nan_to_num(x.astype(np.float32))
    return x * gain

load.cache_clear = lambda: None

def place(buf, smp, at, gain=1.0, pan=0.0):
    """Place sample into (2,N) buffer at sample offset. pan -1..1."""
    n = min(buf.shape[1] - at, smp.shape[1])
    if n <= 0:
        return buf
    l = np.cos((pan + 1) * np.pi / 4)
    r = np.sin((pan + 1) * np.pi / 4)
    buf[0, at:at + n] += smp[0, :n] * gain * l
    buf[1, at:at + n] += smp[1, :n] * gain * r
    return buf


def kit(names=None):
    """List available sample folder names (or files in one)."""
    if names is None:
        return sorted(os.listdir(SAMPLES))
    return sorted(os.listdir(os.path.join(SAMPLES, names)))


# ---------- synth (Vital via vita) ----------
def synth(preset, notes, bpm=126.0, sr=SR, tail=1.0):
    """Render notes through a .vital preset.
    notes: [(midi_pitch, velocity 0-1, start_beats, dur_beats), ...]
    -> (2, N) float32"""
    import vita
    s = vita.Synth()
    s.set_sample_rate(sr)
    s.set_bpm(bpm)
    if preset:
        path = preset if os.path.isabs(preset) else os.path.join(PRESETS, preset)
        s.load_preset(path)
    spb = 60.0 / bpm
    for pitch, vel, start_b, dur_b in notes:
        start_s = start_b * spb
        dur_s = dur_b * spb
        seg = s.render(pitch, float(vel), dur_s, dur_s + tail)
        start_i = int(start_s * sr)
        seg = np.asarray(seg, dtype=np.float32)
        yield start_i, seg  # caller sums into a buffer


def render_synth(preset, notes, bpm=126.0, sr=SR, tail=1.0, dur_s=None):
    sax = dur_s if dur_s else (max(st_b + d for _, _, st_b, d in notes) * 60.0 / bpm + tail)
    out = np.zeros((2, int(sax * sr)), dtype=np.float32)
    for start_i, seg in synth(preset, notes, bpm, sr, tail):
        n = min(out.shape[1] - start_i, seg.shape[1])
        if n > 0:
            out[:, start_i:start_i + n] += seg[:, :n]
    return out


def list_presets():
    return [os.path.relpath(p, PRESETS) for p in glob.glob(os.path.join(PRESETS, "**", "*.vital"), recursive=True)]


# ---------- dynamics ----------
def sidechain(target, trigger_buf, depth=0.8, attack=0.002, release=0.12, sr=SR):
    """Duck `target` where `trigger_buf` is loud (kick-driven pump)."""
    env = np.abs(trigger_buf).max(axis=0)
    # simple envelope follower
    a, r = np.exp(-1 / (attack * sr)), np.exp(-1 / (release * sr))
    e = np.zeros_like(env)
    prev = 0.0
    up = a
    dn = r
    for i in range(len(env)):
        v = env[i]
        prev = v + up * (prev - v) if v > prev else v + dn * (prev - v)
        e[i] = prev
    if e.max() > 0:
        e /= e.max()
    duck = 1.0 - depth * e
    return target * duck


# ---------- mastering ----------
def master(x, sr=SR, ceiling_db=-1.0, comp_thresh_db=-18.0, comp_ratio=3.0):
    """Pedalboard chain: HPF 30Hz -> bus comp -> limiter -> ceiling."""
    from pedalboard import Pedalboard, Compressor, Limiter, HighpassFilter, Gain
    board = Pedalboard([
        HighpassFilter(cutoff_frequency_hz=30),
        Compressor(threshold_db=comp_thresh_db, ratio=comp_ratio,
                   attack_ms=10, release_ms=120),
        Gain(gain_db=1.5),
        Limiter(threshold_db=ceiling_db, release_ms=80),
    ])
    y = board(x, sr)
    peak = np.abs(y).max()
    if peak > 0.98:
        y *= 0.98 / peak
    return y.astype(np.float32)


def measure(x, sr=SR):
    peak = float(np.abs(x).max())
    rms = float(np.sqrt((x ** 2).mean()))
    clipped = int((np.abs(x) > 0.98).sum())
    return {"peak": round(peak, 4), "rms": round(rms, 4), "clipped": clipped,
            "dur_s": round(x.shape[1] / sr, 1)}


# =====================================================================
# STUDIO v3 — the FX LAYER (the tone tools; research-backed defaults)
# Every function: (2, N) float32 in -> (2, N) float32 out. SR global.
# EDM-sane defaults from the production research: HPF'd reverb returns,
# pre-delay'd leads, tempo-synced delays, mono-ish low end.
# =====================================================================

def _pb():
    import pedalboard
    return pedalboard


def _as_stereo(x):
    x = np.asarray(x, dtype=np.float32)
    if x.ndim == 1:
        x = np.stack([x, x], axis=0)
    return x


def reverb(x, sr=SR, decay_s=1.8, pre_delay_ms=25.0, wet=0.3,
           hz_low=250.0, hz_high=None):
    """Plate/hall reverb on a SEND-style return: pre-delay keeps the dry
    transient clear; the WET tail is high-passed (research: reverb mud
    lives below 200-300 Hz). Mix = dry + wet*wet."""
    x = _as_stereo(x)
    P = _pb()
    pre = int(pre_delay_ms / 1000 * sr)
    dry = x.copy()
    dry[:, pre:] = x[:, :x.shape[1] - pre]
    board = P.Pedalboard([P.Reverb(room_size=min(1.0, decay_s / 4.0),
                                   damping=0.4, wet_level=1.0, dry_level=0.0,
                                   width=1.0)])
    wet_buf = board(x, sr).astype(np.float32)
    sos = _butter_hp(hz_low, sr)
    from scipy.signal import sosfilt
    wet_buf = sosfilt(sos, wet_buf, axis=1).astype(np.float32)
    if hz_high:
        sos2 = _butter_lp(hz_high, sr)
        wet_buf = sosfilt(sos2, wet_buf, axis=1).astype(np.float32)
    out = dry + wet_buf * wet
    return np.nan_to_num(out).astype(np.float32)


def _butter_hp(hz, sr, order=2):
    from scipy.signal import butter
    return butter(order, hz, "highpass", fs=sr, output="sos")


def _butter_lp(hz, sr, order=2):
    from scipy.signal import butter
    return butter(order, hz, "lowpass", fs=sr, output="sos")


def delay(x, sr=SR, bpm=126.0, beats=0.75, feedback=0.35, wet=0.25,
          pingpong=True, darkening=0.85):
    """Tempo-synced delay. beats=0.75 -> dotted 1/8 (the trance gallop).
    pingpong bounces L/R; 'darkening' low-passes each repeat."""
    x = _as_stereo(x)
    n = x.shape[1]
    d = int(beats * 60.0 / bpm * sr)
    out = x.copy()
    tap = x.copy()
    import math
    from scipy.signal import sosfilt
    dampen = _butter_lp(4500.0 * darkening, sr)
    times = int(min(12, (n // max(d, 1)) + 1))
    for i in range(1, times + 1):
        g = feedback ** i * wet
        if g < 0.01:
            break
        off = d * i
        if off >= n:
            break
        tap = sosfilt(dampen, tap, axis=1).astype(np.float32)
        seg = tap[:, :n - off]
        if pingpong and (i % 2 == 0):
            out[:, off:] += seg[[1, 0], :]
        else:
            out[:, off:] += seg
    return np.nan_to_num(out).astype(np.float32)


def eq(x, sr=SR, low_cut=None, high_cut=None, low_boost_db=0.0,
       low_boost_hz=100.0, presence_db=0.0, presence_hz=3500.0,
       mud_db=0.0, mud_hz=380.0):
    """Per-stem EQ: the mix-desk basics. low_cut = HPF; presence/low/mid
    boosts via shelving + peak filters."""
    x = _as_stereo(x)
    P = _pb()
    chain = []
    if low_cut:
        chain.append(P.HighpassFilter(cutoff_frequency_hz=low_cut))
    if high_cut:
        chain.append(P.LowpassFilter(cutoff_frequency_hz=high_cut))
    if low_boost_db:
        chain.append(P.LowShelfFilter(cutoff_frequency_hz=low_boost_hz,
                                      gain_db=low_boost_db))
    if presence_db:
        chain.append(P.PeakFilter(cutoff_frequency_hz=presence_hz,
                                  gain_db=presence_db, q=1.0))
    if mud_db:
        chain.append(P.PeakFilter(cutoff_frequency_hz=mud_hz,
                                  gain_db=-abs(mud_db), q=1.0))
    if not chain:
        return x
    board = P.Pedalboard(chain)
    return np.nan_to_num(board(x, sr)).astype(np.float32)


def saturate(x, sr=SR, drive_db=6.0, tone="clean"):
    """Harmonic saturation (the 'expensive' harmonic bite). tone:
    'clean' soft clip, 'crush' harder, 'tape' even harmonics bias."""
    x = _as_stereo(x)
    P = _pb()
    g = 10 ** (drive_db / 20.0)
    y = x * g
    if tone == "crush":
        board = P.Pedalboard([P.Distortion(drive_db=drive_db)])
        y = board(x, sr)
    else:
        y = np.tanh(y)
    # level-compensate so saturate() doesn't just equal 'louder'
    peak_in = np.abs(x).max() or 1.0
    peak_out = np.abs(y).max()
    if peak_out > 0:
        y *= peak_in / peak_out
    return y.astype(np.float32)


def width(x, sr=SR, amount=1.0, mono_below_hz=120.0):
    """Stereo width: mid/side widening of the highs, mono-ize the lows
    (research law: bass stays mono). amount 0=mono, 1=normal, 2=double."""
    x = _as_stereo(x)
    from scipy.signal import sosfilt
    mid = x.mean(axis=0)
    side = x[0] - x[1]
    sos = _butter_lp(mono_below_hz, sr)
    side_lp = sosfilt(sos, side, axis=0).astype(np.float32)
    side_hp = side - side_lp
    L = mid + side_hp * amount + side_lp
    R = mid - side_hp * amount - side_lp
    return np.stack([L, R], axis=0).astype(np.float32)


def chorus(x, sr=SR, rate_hz=1.5, depth_ms=3.0, mix=0.4):
    """Ensemble thickening for pads/plucks."""
    x = _as_stereo(x)
    P = _pb()
    board = P.Pedalboard([P.Chorus(rate_hz=rate_hz, depth=depth_ms / 10.0,
                                   centre_delay_ms=8.0, mix=mix)])
    return np.nan_to_num(board(x, sr)).astype(np.float32)


def phaser(x, sr=SR, rate_hz=0.6, mix=0.3):
    x = _as_stereo(x)
    P = _pb()
    board = P.Pedalboard([P.Phaser(rate_hz=rate_hz, mix=mix)])
    return np.nan_to_num(board(x, sr)).astype(np.float32)


def pitch_shift(x, semitones, sr=SR):
    """Shift a stem (the octave-lift trick) without changing tempo."""
    x = _as_stereo(x)
    P = _pb()
    board = P.Pedalboard([P.PitchShift(semitones=semitones)])
    return np.nan_to_num(board(x, sr)).astype(np.float32)


def filter_sweep(x, sr=SR, hz_from=200.0, hz_to=12000.0, dur_s=None,
                 shape="exp"):
    """Automated filter open (the build tension tool): piecewise one-pole
    lowpass, cutoff ramping hz_from -> hz_to across the buffer."""
    x = _as_stereo(x)
    n = x.shape[1] if dur_s is None else min(x.shape[1], int(dur_s * sr))
    y = x[:, :n].copy()
    steps = 64
    seg = max(n // steps, 1)
    acc = np.zeros(2, dtype=np.float64)
    for k in range(steps):
        f = hz_from * (hz_to / hz_from) ** ((k + 1) / steps)
        f = min(f, sr * 0.45)
        w = 2.0 * np.pi * f / sr
        alpha = float(1.0 - np.exp(-w))
        lo, hi = k * seg, min(n, (k + 1) * seg)
        if hi <= lo:
            break
        chunk = y[:, lo:hi]
        for ch in range(2):
            a = acc[ch]
            c = chunk[ch]
            for i in range(c.shape[0]):
                a += alpha * (c[i] - a)
                c[i] = a
            acc[ch] = a
    if n < x.shape[1]:
        tail = np.zeros((2, x.shape[1] - n), dtype=np.float32)
        y = np.concatenate([y, tail], axis=1)
    return np.nan_to_num(y).astype(np.float32)


def send_reverb(*stems, sr=SR, decay_s=2.0, wet=0.25, hz_low=250.0,
                pre_delay_ms=25.0):
    """The shared-verb BUS: glue several stems into one space.
    Usage: mix = st.send_reverb(lead, pads, chords, decay_s=2.2, wet=0.3)"""
    total = _sum_stems(*stems)
    return reverb(total, sr=sr, decay_s=decay_s, wet=wet, hz_low=hz_low,
                  pre_delay_ms=pre_delay_ms)


def send_delay(*stems, sr=SR, bpm=126.0, beats=0.75, feedback=0.35, wet=0.22):
    total = _sum_stems(*stems)
    return delay(total, sr=sr, bpm=bpm, beats=beats, feedback=feedback,
                 wet=wet)


def _sum_stems(*stems):
    out = None
    for s in stems:
        s = _as_stereo(s)
        if out is None:
            out = np.zeros_like(s)
        n = min(out.shape[1], s.shape[1])
        out[:, :n] += s[:, :n]
    return out


def bus_compression(x, sr=SR, thresh_db=-20.0, ratio=2.5, attack_ms=15.0,
                    release_ms=150.0, makeup_db=0.0):
    """Gentle glue compressor for a stem group (before master())."""
    x = _as_stereo(x)
    P = _pb()
    board = P.Pedalboard([P.Compressor(threshold_db=thresh_db, ratio=ratio,
                                       attack_ms=attack_ms, release_ms=release_ms),
                          P.Gain(gain_db=makeup_db)])
    return np.nan_to_num(board(x, sr)).astype(np.float32)


def tone_chain(x, chain="lead", sr=SR):
    # NOTE: sr is the keyword-named sample rate; forward as sr=sr into eq()
    """Research-backed per-role presets. chain: lead|pad|pluck|drum_bus.
    Each is a documented starting point — override freely per style."""
    presets = {
        "lead":    dict(low_cut=180, presence_db=2.0, mud_db=2.0),
        "pad":     dict(low_cut=220, presence_db=0.0, mud_db=1.5),
        "pluck":   dict(low_cut=220, presence_db=3.0, mud_db=1.0),
        "drum_bus": dict(low_cut=30, presence_db=1.0, mud_db=1.0),
    }
    return eq(x, sr=sr, **presets.get(chain, {}))


def spectral_balance(x, sr=SR):
    """MEASURE helper: energy in low/mid/high bands (the 'same tone'
    detector). Returns dict of band RMS dBFS."""
    x = _as_stereo(x).mean(axis=0)
    X = np.abs(np.fft.rfft(x)) ** 2
    f = np.fft.rfftfreq(x.shape[0], 1 / sr)
    def band(a, b):
        m = (f >= a) & (f < b)
        e = X[m].mean() + 1e-12
        return round(float(10 * np.log10(e)), 1)
    return {"low_20_120": band(20, 120), "mid_120_2k": band(120, 2000),
            "high_2k_8k": band(2000, 8000), "air_8k_16k": band(8000, 16000)}
