#!/usr/bin/env python3
"""SOUND ENGINE — 'The Last Sweep'. 100% synthesized, no audio files.
44.1k stereo, 30.0s. Signature sound: beacon call D5->A4 (bell decay);
transformed at 26.5s (same notes, warm harmonics, harmony resolves Dm->D).
Chain: osc/noise sources -> fx layer (eq/reverb/width) -> st.master -> -14 LUFS.
Prints measure() + LUFS + true peak. Writes film_audio.wav.
"""
import sys
sys.path.insert(0, 'C:/Users/agent/work/project/.venv/lib/python3.12/site-packages')
sys.path.insert(0, 'C:/Users/agent/work/project/studio')
import numpy as np
import api as st
import api_v3_fx as fx
import soundfile as sf
import pyloudnorm as pyln
from scipy.signal import butter, sosfilt

SR = 44100
DUR = 30.0
N = int(SR * DUR)
rng = np.random.default_rng(7)

def seg(t, a, b):
    x = np.clip((t - a) / max(1e-9, b - a), 0, 1)
    return x * x * (3 - 2 * x)

def env_pts(pts):
    """piecewise-smooth envelope from [(time, value), ...] -> (N,)"""
    tgrid = np.arange(N) / SR
    vals = np.interp(tgrid, [p[0] for p in pts], [p[1] for p in pts])
    return vals

def tone(freq, dur, amp=1.0, attack=0.01, decay=None, harmonics=((1, 1.0),),
         detune_cents=0, vibrato=0.0, vib_hz=5.0):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = freq * 2 ** (detune_cents / 1200)
    ph = 2 * np.pi * f * t
    if vibrato:
        ph = ph + vibrato * np.sin(2 * np.pi * vib_hz * t)
    x = np.zeros(n)
    for mult, hamp in harmonics:
        x += hamp * np.sin(mult * ph)
    env = np.minimum(1, t / max(1e-4, attack))
    if decay:
        env *= np.exp(-t / decay)
    rel = np.minimum(1, np.maximum(0, (dur - t) / 0.05))
    return (x * env * rel * amp).astype(np.float32)

def place(buf, x, at_s, gain=1.0, pan=0.0):
    at = int(at_s * SR)
    n = min(buf.shape[1] - at, x.shape[0])
    if n <= 0:
        return
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    buf[0, at:at + n] += x[:n] * gain * l
    buf[1, at:at + n] += x[:n] * gain * r

# ---------------- envelopes ----------------
storm = env_pts([(0, 0), (8, 0), (11.5, 1), (16, 1), (21, 0.55), (24.5, 0), (30, 0)])
pad_env = env_pts([
    (0, 0.0), (2.5, 0.30), (8, 0.34), (11.5, 0.42), (16, 0.38),
    (19.5, 0.10), (20.8, 0.03), (22.3, 0.03), (23.2, 0.30),
    (25.5, 0.40), (27.5, 0.34), (29.0, 0.22), (30, 0.0)])
sea_env = 0.05 + 0.16 * storm + 0.05 * env_pts([(0, 0), (22.5, 0), (25, 1), (30, 1)]) \
          - 0.035 * env_pts([(20.8, 0), (20.9, 1), (22.3, 1), (22.5, 0)])  # dip in the silence
sea_env = np.clip(sea_env, 0.0, None)
rain_env = env_pts([(7.5, 0), (9, 0.8), (16, 1.0), (21, 0.5), (22.3, 0.28),
                    (23.5, 0.30), (25.5, 0.12), (27, 0.0), (30, 0)])

# ---------------- pad (Dm -> D major at the payoff) ----------------
pad = np.zeros((2, N), np.float32)
notes_cold = [(38, 0.9), (45, 0.7), (50, 0.6), (53, 0.5)]     # D2 A2 D3 F3
notes_warm = [(38, 0.9), (45, 0.7), (50, 0.6), (54, 0.5)]     # D2 A2 D3 F#3
tgrid = np.arange(N) / SR
for (midi, amp), warm in ((p, False) for p in notes_cold):
    pass
def render_pad(notes, t0, t1, gain):
    seg_n0, seg_n1 = int(t0 * SR), int(t1 * SR)
    m = seg_n1 - seg_n0
    out = np.zeros((2, m), np.float32)
    tt = np.arange(m) / SR
    for midi, amp in notes:
        f = 440 * 2 ** ((midi - 69) / 12)
        for det in (-6, 5):
            ph = 2 * np.pi * f * 2 ** (det / 1200) * tt
            w = np.sin(ph) + 0.35 * np.sin(2 * ph + 0.3) + 0.12 * np.sin(3 * ph)
            pan = 0.25 * (det / 6)
            l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
            out[0] += (w * amp * l).astype(np.float32)
            out[1] += (w * amp * r).astype(np.float32)
    return out * gain

# cold pad 0-22.5 (Dm), warm pad 22.5-30 (D major)
pad_cold = render_pad(notes_cold, 0, 22.5, 1.0)
pad_warm = render_pad(notes_warm, 22.5, 30.0, 1.0)
pad[:, :pad_cold.shape[1]] += pad_cold
pad[:, int(22.5 * SR):] += pad_warm
# slow amplitude breathing + envelope
pad *= (pad_env * (1 + 0.06 * np.sin(2 * np.pi * 0.23 * tgrid)))[None, :]
pad = sosfilt(butter(2, 900, 'low', fs=SR, output='sos'), pad, axis=1).astype(np.float32)
pad = fx.eq(pad, low_cut=70)
pad = fx.chorus(pad, rate_hz=0.8, mix=0.25)

# ---------------- sea (LP noise, storm-coupled) ----------------
noise = rng.standard_normal(N).astype(np.float32) * 0.5
sea = sosfilt(butter(2, 260, 'low', fs=SR, output='sos'), noise).astype(np.float32)
swell = 1 + 0.5 * np.sin(2 * np.pi * 0.4 * tgrid + 1.0) + 0.25 * np.sin(2 * np.pi * 0.13 * tgrid)
sea *= (sea_env * swell).astype(np.float32)
sea = np.stack([sea, np.roll(sea, 937)], axis=0).astype(np.float32)  # widen

# ---------------- rain (HP impulse ticks) ----------------
rain = np.zeros((2, N), np.float32)
tick_density = 70.0
tcur = 0.0
while tcur < DUR:
    tcur += rng.exponential(1.0 / max(1e-6, tick_density * max(rain_env[int(tcur * SR)], 1e-3)))
    if tcur >= DUR - 0.2:
        break
    ln = int(SR * rng.uniform(0.002, 0.005))
    at = int(tcur * SR)
    burst = rng.standard_normal(ln).astype(np.float32)
    burst = sosfilt(butter(2, 3200, 'high', fs=SR, output='sos'), burst)
    amp = rng.uniform(0.04, 0.11) * rain_env[min(int(tcur * SR), N - 1)]
    place(rain, burst, tcur, gain=amp, pan=rng.uniform(-0.6, 0.6))

# ---------------- SIGNATURE: beacon call ----------------
def beacon(t0, warm=False, falter=False):
    if warm:
        harm = ((1, 1.0), (2, 0.5), (3, 0.22), (4, 0.10))
        dec = 1.6; g = 0.30
    else:
        harm = ((1, 1.0), (2, 0.12))
        dec = 0.9; g = 0.26
    d5 = tone(587.33, 1.2, amp=1.0, attack=0.004, decay=dec, harmonics=harm)
    a4 = tone(440.0, 1.8, amp=0.9, attack=0.004, decay=dec * 1.3, harmonics=harm)
    if falter:
        n = d5.shape[0]; tt = np.arange(n) / SR
        wob = 1 + 0.012 * np.sin(2 * np.pi * 7.0 * tt)
        idx = np.cumsum(wob).astype(int); idx = np.clip(idx, 0, n - 1)
        d5 = d5[idx]
        stutter = 0.65 + 0.35 * np.sin(2 * np.pi * 13 * tt)
        d5 *= stutter.astype(np.float32)
    place(SIG, d5, t0, gain=g, pan=-0.15)
    place(SIG, a4, t0 + 0.45, gain=g * 0.85, pan=-0.05)
    if warm:
        d6 = tone(1174.66, 1.4, amp=0.4, attack=0.004, decay=1.3,
                  harmonics=((1, 1.0), (2, 0.15)))
        place(SIG, d6, t0 + 0.02, gain=g, pan=0.1)

SIG = np.zeros((2, N), np.float32)
beacon(4.5)                    # B1: the call that guides
beacon(10.5, falter=True)      # B2: the call falters in the storm
beacon(26.5, warm=True)        # B4: THE SAME CALL, warm voice (transformed)

# ---------------- sub swell under the boat-beam rise ----------------
sub = tone(73.42, 3.0, amp=0.10, attack=1.2, decay=2.5, harmonics=((1, 1.0), (2, 0.2)))
place(SIG, sub, 24.6, gain=0.8, pan=0.0)

# ---------------- B4 shimmer (high warm sparkle, measurable HF) ----------------
shim = np.zeros((2, N), np.float32)
shim_env = env_pts([(23.0, 0), (24.5, 1), (28.5, 0.8), (30, 0)])
shim_seg = shim_env[int(22.5 * SR):]
nsh = min(shim_seg.shape[0], int(7.5 * SR))
tt = np.arange(nsh) / SR
for f, amp, pan in ((1174.66, 0.045, -0.3), (1479.98, 0.035, 0.3), (1760.0, 0.028, 0.0)):
    w = np.sin(2 * np.pi * f * tt) * (0.75 + 0.25 * np.sin(2 * np.pi * 5.2 * tt + f))
    place(shim, (w * shim_seg[:nsh]).astype(np.float32), 22.5, gain=amp, pan=pan)

# ---------------- mix ----------------
mix = pad * 0.9 + sea * 0.9 + rain + SIG + shim
wet = fx.send_reverb(pad, SIG, decay_s=2.2, wet=0.26, hz_low=250)
mix = mix + wet
mix = fx.width(mix, amount=1.25, mono_below_hz=120)
mix = fx.eq(mix, low_cut=35, mud_db=1.5, mud_hz=380)

# ---------------- master + loudness ----------------
final = st.master(mix.astype(np.float32))
m = pyln.Meter(SR)
lufs = m.integrated_loudness(final.T)
gain = (-14 - lufs) if lufs != -np.inf else 0
final = final * (10 ** (gain / 20))
# true peak (4x oversampled)
tp = float(np.abs(np.array([sosfilt(butter(4, 0.85, 'low', fs=SR * 4, output='sos'),
                                    np.repeat(final, 4, axis=1))])).max()) if False else None
up = np.repeat(final, 4, axis=1)
up = sosfilt(butter(4, 16000, 'low', fs=SR * 4, output='sos'), up, axis=1)
tp = float(np.abs(up).max())
tp_db = 20 * np.log10(max(tp, 1e-9))
if tp_db > -1.0:
    final *= 10 ** ((-1.0 - tp_db) / 20)
    tp = float(np.abs(final).max()); tp_db = 20 * np.log10(max(tp, 1e-9))
lufs2 = m.integrated_loudness(final.T)
print('st.measure:', st.measure(final))
print(f'LUFS integrated: {lufs2:.2f} (target -14) | true peak: {tp_db:.2f} dBTP (limit -1)')
print('clipped samples >0.98:', int((np.abs(final) > 0.98).sum()))
sf.write('film_audio.wav', final.T, SR, subtype='FLOAT')
print('wrote film_audio.wav', final.shape, f'{final.shape[1]/SR:.2f}s')
