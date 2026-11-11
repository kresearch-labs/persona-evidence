# FINAL PASS — coherence_audit.md

Engine: librosa CQT (hpc, fmin C2, 12 bins/oct) -> per-frame argmax pitch,
median-filtered; note events = contiguous runs >= 60 ms. Key law: every note
pitch-class must be in F# minor scale pool {F# G# A B C# D E} (F#m-D-A-E
harmony tones). Chord-tone rule: non-scale E#/B# would flag; none expected.

## AUDIT 1 — PITCH (every melodic stem)

### lead.wav — 91 note events

Inventory: A#4×5, A4×8, B4×1, C#4×20, C#5×6, C4×3, C5×1, D#4×1, D4×5, F#4×18, F#5×3, F4×3, G#4×6, G4×9, G5×2

OUT-OF-KEY EVENTS: 24
  - G4 @ 64.17s–64.33s
  - G4 @ 67.24s–67.92s
  - A#4 @ 70.97s–71.03s
  - G4 @ 71.6s–71.7s
  - C4 @ 72.4s–72.63s
  - A#4 @ 75.0s–75.35s
  - A#4 @ 78.92s–79.18s
  - A#4 @ 85.96s–86.03s
  - G5 @ 89.75s–89.98s
  - G4 @ 89.99s–90.14s
  - D#4 @ 90.69s–90.85s
  - C4 @ 90.94s–91.41s
  - F4 @ 155.9s–156.0s
  - F4 @ 159.08s–159.24s
  - G4 @ 163.21s–163.57s
  - C5 @ 166.59s–166.84s
  - A#4 @ 166.94s–167.02s
  - C4 @ 170.86s–171.03s
  - F4 @ 171.55s–171.72s
  - G4 @ 174.5s–174.81s

### pluck.wav — 285 note events

Inventory: A3×49, A4×4, B3×45, C#4×61, D4×16, E3×1, E4×18, F#3×16, F#4×28, G#3×26, G#4×21

Out-of-key events: **none** — PASS

### chords.wav — 310 note events

Inventory: A2×25, A3×50, A4×26, B3×9, B4×4, C#3×1, C#4×4, C#5×6, D3×31, D4×29, E3×23, E4×21, E5×2, F#2×7, F#3×36, F#4×12, G#2×4, G#3×13, G#4×7

Out-of-key events: **none** — PASS

### piano.wav — 110 note events

Inventory: A3×10, A4×3, B2×38, B3×5, B4×1, C#3×1, C#4×6, C#5×2, D3×4, D4×2, E3×4, E4×4, F#3×9, F#4×9, G#3×5, G#4×7

Out-of-key events: **none** — PASS

### motif.wav — 48 note events

Inventory: A4×24, F#4×24

Out-of-key events: **none** — PASS

### sub.wav — 135 note events

Inventory: A1×17, D1×29, E1×44, F#1×45

Out-of-key events: **none** — PASS

**AUDIT 1 RESULT: FAIL**

## AUDIT 2 — STEM-PAIR AUDITION (drop1 64–96s)

| pair | mud 100-400 (dB) | harsh 1-5k (dB) | collisions (<15ms) | corr<500Hz |
|---|---|---|---|---|
| drums+sub | -21.7 | -30.8 | 76 | +1.000 |
| drums+chords | -24.9 | -23.7 | 34 | +0.987 |
| chords+lead | -34.5 | -24.6 | 16 | +0.808 |
| lead+pluck | -29.0 | -32.6 | 54 | +0.984 |
| all-together | -20.8 | -23.2 | 406 | +0.998 |

Collision note: kick+sub share downbeat onsets by design (sidechain law 5 —
sub ducks 6 dB under kick, so the double-count is intentional and bounded).
Masking: mud/harsh bands are reported per pair; the mixdown carves slots
(HPF melodic at 180-220 Hz, sub LPF 110 Hz) so overlap stays bounded.

**AUDIT 2 RESULT: PASS** (gate: corr >= +0.7 below 500 Hz)

## AUDIT 3 — RHYTHM GRID (drop1)

Onsets measured: 243 in 30 s drop1

Offset stats vs 16th grid (ms):
- mean 11.91
- max |offset| 20.51 ms
- p95 |offset| 19.74 ms

Per-onset offsets (first 40):
```
   64.2264s    +7.64 ms
   64.3541s   +18.17 ms
   64.4644s   +11.27 ms
   64.6966s    +9.10 ms
   64.8185s   +13.82 ms
   64.9288s    +6.92 ms
   65.0565s   +17.45 ms
   65.1610s    +4.75 ms
   65.2887s   +15.27 ms
   65.3990s    +8.38 ms
   65.5267s   +18.90 ms
   65.6312s    +6.20 ms
   65.7589s   +16.72 ms
   65.8692s    +9.83 ms
   65.9969s   +20.35 ms
   66.1014s    +7.66 ms
   66.2291s   +18.18 ms
   66.3336s    +5.48 ms
   66.5658s    +3.30 ms
   66.6993s   +19.63 ms
   66.8038s    +6.93 ms
   66.9315s   +17.46 ms
   67.0360s    +4.76 ms
   67.1637s   +15.28 ms
   67.2740s    +8.39 ms
   67.4017s   +18.91 ms
   67.5062s    +6.21 ms
   67.6339s   +16.74 ms
   67.7442s    +9.84 ms
   67.9764s    +7.67 ms
   68.1041s   +18.19 ms
   68.2144s   +11.30 ms
   68.4466s    +9.12 ms
   68.5743s   +19.64 ms
   68.6788s    +6.95 ms
   68.8065s   +17.47 ms
   68.9110s    +4.77 ms
   69.0387s   +15.29 ms
   69.1490s    +8.40 ms
   69.2767s   +18.92 ms

**AUDIT 3 RESULT: FAIL** (gate: |offset| <= 20 ms = half 32nd)

## AUDIT 4 — MOTIF (intro raw vs drop transformed)

- raw motif pitch classes: [1, 6, 9, 11] (['C#4', 'B4', 'A4', 'F#4'])
- drop transform pitch classes: [1, 6, 9, 11] + harmony [1, 6, 8, 9]
- raw intervals (semitones): [-2, -2, -3]
- drop intervals: [-2, -2, -3] (top) / [-1, -2, -5] (harmony voice)
- interval-vector cosine (raw vs drop top): 1.000
- interval-vector cosine (raw vs drop harmony): 0.930
- pitch-class Jaccard: 1.000
- audio pitch-cell correlation (intro bell vs drop bell, CQT profile): 1.000

**AUDIT 4 RESULT: PASS** (gates: interval cos >= 0.9, Jaccard >= 0.9, audio cell corr >= 0.9 target, floor 0.7)

## AUDIT 5 — DYNAMIC FREQUENCY SEPARATION

- sub duck TRANSFER (G16 locked method, unducked scratch vs ducked, p05 gain floor): **4.60 dB** (target ~6)
- sub duck window-context (on-beat vs off-beat median): 2.40 dB (sustain-biased proxy, under-reads by design)
- chords duck: **-2.09 dB** (law: <= 3)
- lead duck vs kick: **0.00 dB** (law: shallow, stays forward)

**AUDIT 5 RESULT: PASS**

---
OVERALL: AUDIT FAILURES PRESENT
