# GRADED RUBRIC — "The Last Sweep" (film_emotion_critic)
Film: short.mp4 — 30.000s, 1280×720, 30fps h264 + aac. Attempt 2 of 3 (final).
Method: frame-by-frame numeric evidence (900 frames, frames_stats.json) + audio
timeline analysis (per-second RMS, spectral bands), every grade cites SECONDS.

## THE FOUR TESTS
### 1. NAMEABLE (feeling nameable after ONE viewing) — PASS
- 0–8s: one cold light sweeps a dark sea; a small boat drifts, glimmering at
  each pass (beam on-axis 175 vs off-beam 35 at t=1.0s). Feeling available:
  *loneliness watched over*.
- 8–16s: storm motion peaks (motion max 5.2 at ~10s); the beacon call falters
  (10.5–12s, stutter/detune in the audio). Feeling: *dread for the small thing*.
- 16–22.5s: light dies 16.2–17.4s (lum drops 34→21); longest stillness t≈20–22.3s
  (motion 0.75 mean, quietest window center 22.3s); audio dips to −29.5 dB RMS
  at 21s (12.5 dB below film mean). Feeling: *loss*.
- 22.5–30s: warm gold blooms inside the hull (first warm frame 22.57s), the boat
  raises the beam, the same beacon call returns warm at 26.5s, a second tiny
  boat approaches by 28s. Feeling: *hope — the light carries on*. NAMEABLE: PASS.

### 2. ECHO (payoff transforms the setup seed) — PASS
Measured composition match, opening t=1.0s vs payoff t=28.0s (6/6 checks):
- horizon row identical: row 446 vs 446
- lighthouse dark column right, both frames (29<44 / 11<44)
- boat left: dark guided silhouette at t=1 (11<18) → bright emitter at t=28
  (243>189); second tiny boat dark (60<68) — the seed becomes the next traveler
- beam diagonal present both frames (on/off ratio 7.19 / 2.14)
- hue inversion: warm px 0 → 325,057 (cold blue → warm gold)
- light source swap: brightest sky column 967 (lamp 998) → 367 (boat 364)
The setup seed (lighthouse guides boat) is TRANSFORMED, not repeated: the boat
becomes the lighthouse. ECHO: PASS.

### 3. ANCHOR-FRAME (one frame remembered an hour later) — PASS
Designated anchor: **t=23.5s (frame 705)** — first warm gold blooming inside the
hull against near-black, rain still falling, no beam yet.
- Visually distinct: warm-pixel fraction is exactly 0.00000 for all 675 frames
  before 22.5s; anchor frame has 31,023 warm px; B4 mean warm 0.25.
- It is the only interior-light frame in the film; the only warm region in the
  first 23 seconds. ANCHOR: PASS (exactly one designated).

### 4. ZERO-ERROR (renders, plays, no glitch) — PASS
- ffprobe: h264, 1280×720, 30/1 fps, aac 44.1k stereo, duration 30.000000s.
- 900/900 frames rendered; luminance 19.4–61.3 (no white flash >240, no black
  flash <2); NaN check clean; motion stats sane per beat.
- Audio: −14.00 LUFS integrated, true peak −4.67 dBTP (≤ −1 ✓), 0 clipped
  samples, 30.00s. ZERO-ERROR: PASS.

## PER-BEAT GRADES (citing seconds)
| Beat | Window | Grade | Evidence (seconds) |
|------|--------|-------|--------------------|
| B1 The Sweep | 0–8s | 9/10 | beam sweep visible from 0.0s; beacon call 4.5–6s (−16.4 dB vs −17.1 pre); boat glimmer at each pass; motion calm (0.89 mean) |
| B2 The Storm | 8–16s | 9/10 | motion peak 5.2 ~10s; rain from 8s; beacon falters 10.5–12s; lamp flicker deepens to the death flicker 16.2–17.4s |
| B3 The Dark | 16–22.5s | 9/10 | light dead by 17.4s; longest still 20–22.3s (motion 0.75); audio silence 20.8–22.3s (−29.5 dB at 21s, 12.5 dB dip); stillness culminates directly before payoff |
| B4 The Bloom | 22.5–30s | 10/10 | first warm 22.57s; anchor 23.5s; boat beam rises 24.6–26.4s; TRANSFORMED beacon 26.5s (warm harmonics, HF ratio 0→0.0016); second boat 26.2–30s; last 3s hold the new light (−17.3 dB, steady) |

## RE-RENDER LOG (honest)
- Attempt 1: B3 FAILED the stillness check — quietest motion window landed at
  t=7.5s (rain kept falling through the stillness); payoff warmth not measurable
  in the audio spectrum (HF ratio 0.0000). Fixed: rain suppressed 18.5–20.5s,
  sea glint damped in stillness, shimmer bed + warm-beacon harmonics added.
- Attempt 2: ALL CHECKS PASS (this rubric). No 3-strikes needed.

## MEASURED GATES
| Gate | Target | Measured | Result |
|------|--------|----------|--------|
| duration | 30s ± 1s | 30.000s | PASS |
| fps | 24–30 constant | 30/1 | PASS |
| codecs | h264 + aac | h264 + aac | PASS |
| beats | 4+ | 4 (B1–B4) | PASS |
| echo structure | verified | 6/6 composition checks | PASS |
| anchor frame | exactly one, distinct | t=23.5s, warm=0 before 22.5s | PASS |
| LUFS integrated | −14 | −14.00 | PASS |
| true peak | ≤ −1 dBTP | −4.67 dBTP | PASS |
| clipping | none | 0 samples >0.98 | PASS |
| files in cwd | no scattering | short.mp4, film_brief.md, graded_rubric.md (+ brief.md mirror, sources) | PASS |

## FINAL GRADE
All four critic tests PASS → **HIT**. Emotion target (bittersweet hope) achieved;
the last 3 seconds carry it (ground [c1b494eca772], [bc03a26e59da]); the
strongest beat lands on the unexpected frame — the boat, not the lighthouse
(ground [8111cdfe8516], [75e1021ec3cd]); the payoff reuses the opening
composition, changed (ground [4a78b1137647]); one motion idea per scene
(ground [397b73fef922]); everything synthesized in code (ground [58205f7d0bce]).
