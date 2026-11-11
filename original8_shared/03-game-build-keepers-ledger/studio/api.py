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
