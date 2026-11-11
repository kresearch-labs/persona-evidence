# Synthesize The Keeper's Ledger sound set via studio v3 (real DSP).
# Output: game/ScalTest/Content/Audio/*.wav (16-bit PCM, 44.1k)
import sys, os, wave
sys.path.insert(0, "C:/Users/agent/work/project/studio")
import numpy as np
import api_v3_fx as s
from scipy.signal import sosfilt

def lp(x, hz, order=3):
    return sosfilt(s._butter_lp(hz, SR, order), x)

def hp(x, hz, order=3):
    return sosfilt(s._butter_hp(hz, SR, order), x)

SR = s.SR
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                   "game", "ScalTest", "Content", "Audio")
os.makedirs(OUT, exist_ok=True)

def write_wav(name, x, sr=SR):
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = np.stack([x, x], axis=1)
    peak = np.max(np.abs(x)) or 1.0
    x = x / peak * 0.85
    pcm = (x * 32767).astype(np.int16)
    with wave.open(os.path.join(OUT, name), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(pcm.tobytes())
    print("wrote %s (%.1fs)" % (name, len(pcm) / sr))

def _st(x):
    return np.stack([x, x], axis=1)

def lfo(n, rate, lo, hi, phase=0.0):
    t = np.arange(n) / SR
    return lo + (hi - lo) * (0.5 + 0.5 * np.sin(2 * np.pi * rate * t + phase))

rng = np.random.default_rng(7)

# 1. STORM BED — 24s seamless loop: filtered noise + slow gusts + rain hiss
n = SR * 24
wind = lp(rng.standard_normal(n), 420.0)
wind *= lfo(n, 0.07, 0.35, 1.0) * lfo(n, 0.023, 0.5, 1.0, 1.7)
rain = hp(rng.standard_normal(n), 3000.0) * 0.12
rain *= lfo(n, 0.11, 0.6, 1.0, 0.6)
bed = s.reverb(np.stack([wind*0.8+rain]*2, axis=1), sr=SR, decay_s=2.4, wet=0.22)
# crossfade ends for seamless loop
f = SR * 2
env = np.ones((n, 2)); ramp = np.linspace(0, 1, f)
env[:f] *= ramp[:, None]; env[-f:] *= ramp[::-1][:, None]
bed = bed * env
bed[:f] += bed[-f:] * 0  # keep simple; loop point masked by low level
write_wav("storm_bed.wav", bed * 0.9)

# 2. BEAM HUM — 8s loop: lamp mechanism drone (55+110Hz, slow shimmer)
n = SR * 8
t = np.arange(n) / SR
hum = (np.sin(2 * np.pi * 55 * t) * 0.5 +
       np.sin(2 * np.pi * 110.3 * t) * 0.25 +
       np.sin(2 * np.pi * 165.1 * t) * 0.12)
hum *= lfo(n, 0.5, 0.75, 1.0)
write_wav("beam_hum.wav", lp(hum, 900) * 0.5)

# 3. DARK DRONE — 14s loop: the sea stops trusting you (sub dread)
n = SR * 14
t = np.arange(n) / SR
dr = (np.sin(2 * np.pi * 36.7 * t) * 0.6 + np.sin(2 * np.pi * 37.2 * t) * 0.4)  # beating F1
dr += np.sin(2 * np.pi * 73.5 * t) * 0.2
dr *= lfo(n, 0.09, 0.55, 1.0)
write_wav("dark_drone.wav", lp(dr, 200) * 0.8)

# 4. SHIP BELL — 3s one-shot: two horns, the ship sees the light
n = int(SR * 3)
t = np.arange(n) / SR
bell = np.zeros(n)
for f0, a, dec in ((660, 1.0, 2.2), (1320, 0.55, 1.6), (1980, 0.3, 1.1), (2640, 0.18, 0.8)):
    bell += a * np.sin(2 * np.pi * f0 * t) * np.exp(-t * dec)
bell += 0.15 * np.exp(-t * 30) * rng.standard_normal(n)  # strike
write_wav("ship_bell.wav", s.reverb(_st(bell), sr=SR, decay_s=1.6, wet=0.3) * 0.8)

# 5. SALVAGE CLANK — 1.6s one-shot: metal on metal
n = int(SR * 1.6)
t = np.arange(n) / SR
cl = np.zeros(n)
for f0, a, dec in ((320, 1.0, 9.0), (940, 0.7, 7.0), (1730, 0.5, 5.0), (3100, 0.35, 4.0)):
    cl += a * np.sin(2 * np.pi * f0 * t + rng.uniform(0, 6)) * np.exp(-t * dec)
cl *= (1 + 0.4 * np.sin(2 * np.pi * 13 * t))
cl += 0.25 * np.exp(-t * 40) * rng.standard_normal(n)
write_wav("salvage_clank.wav", s.reverb(_st(cl), sr=SR, decay_s=1.1, wet=0.18) * 0.75)

# 6. INTERACT BLIP — 0.35s: page turn / valve
n = int(SR * 0.35)
t = np.arange(n) / SR
bl = np.sin(2 * np.pi * (520 + 300 * t / 0.35) * t) * np.exp(-t * 18)
bl += 0.3 * np.exp(-t * 60) * rng.standard_normal(n)
write_wav("interact_blip.wav", lp(bl, 4000) * 0.6)

# 7. SHIP LOST — 2.5s: hull crack + cold wash
n = int(SR * 2.5)
t = np.arange(n) / SR
crack = np.exp(-t * 6) * rng.standard_normal(n)
crack = lp(crack, 300) * 1.2
wash = lp(rng.standard_normal(n), 900) * np.exp(-t * 1.8) * 0.5
thud = np.sin(2 * np.pi * 48 * t) * np.exp(-t * 3) * 0.8
write_wav("ship_lost.wav", s.reverb(_st(crack + wash + thud), sr=SR, decay_s=2.0, wet=0.3) * 0.9)

print("SFX SET COMPLETE:", sorted(os.listdir(OUT)))
