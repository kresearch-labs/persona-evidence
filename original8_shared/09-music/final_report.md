# FINAL PASS — FINAL LANDING REPORT (MAINSTAGE)

Pass: **FRESH COMPOSITION** — Festival Progressive House / Cinematic EDM,
128 BPM, F# minor, 104 bars, 195.0 s (Owner map: intro 1–17 / build1 18–34 /
drop1 35–51 downbeat 63.75 s ≈ 1:04 / break1 52–67 / build2 68–83 / drop2
84–99 / outro 100–104).

Written in FINAL-LANDING mode after empty-reply recovery. This file is a
readback-consolidation of the verified on-disk state — **no gate was
re-measured and no stem re-rendered in this session** (resume-mode law: no
re-assessment). All numbers below are from `gates_p17_r1_table.txt` (FINAL)
and `coherence_audit.md` (FINAL), verified on disk.

---

## 1. SHIP DECISION: **NOT SHIPPED**

Owner rule: ship only on all-gates-pass; max 3 iterations. The 3-iteration
loop is SPENT (rounds 1–3 executed, trajectory 15/23 → 16/23 → 14/23
line-items). Round 3 ended with 6 gate line-items open → the pass lands as
the honest 3-strikes result. `.home/agent/Music/MAINSTAGE_final pass.mp3` is
**correctly ABSENT** (§4-9: mp3 only on all-gates-pass).

---

## 2. Final gate table — 14/23 line-items (round-3 master)

| # | Gate | Target | Final | Verdict |
|---|------|--------|-------|---------|
| G1 | drop1 onsets | >= 18/s | 9.92 | **FAIL** (−8.1/s) |
| G1 | drop2 onsets | >= 18/s | 9.94 | **FAIL** (−8.1/s) |
| G2 | drop1 valley/peak | <= 0.60 | 0.331 | PASS |
| G2 | drop2 valley/peak | <= 0.60 | 0.510 | PASS |
| G3 | drop1 duty-cycle | <= 0.5 | 0.459 | PASS |
| G3 | drop2 duty-cycle | <= 0.5 | 0.458 | PASS |
| G4 | drop1 RMS (stereo program) | >= 0.45 | 0.3497 | **FAIL** (−0.100) |
| G4 | drop2 RMS (stereo program) | >= 0.45 | 0.3779 | **FAIL** (−0.072) |
| G5 | drop1 crest (mono-sum RMS) | >= 2.2 | 3.33 | PASS |
| G5 | drop2 crest (mono-sum RMS) | >= 2.2 | 2.64 | PASS |
| G6 | drop1 10–20k (butter8+filtfilt) | <= −48 dBFS | −44.38 | **FAIL** (+3.62) |
| G6 | drop2 10–20k (butter8+filtfilt) | <= −48 dBFS | −46.98 | **FAIL** (+1.02) |
| G7 | sub side <120 Hz | < 8% | 4.39% | PASS |
| G8 | sub LUFS (drop window) | −14 ±1 | −14.36 | PASS |
| G9 | contrast break vs drop | >= 6 dB | 3.22 | **FAIL** (−2.78) |
| G10 | master peak | <= 0.9683 | 0.9681 | PASS |
| G10 | clipped samples | 0 | 0 | PASS |
| G11 | chain 40 ms / 2:1 / no-tanh | True | True | PASS |
| G12 | audit-1 pitch (F#m pool) | 0 out-of-key | 24 events | **FAIL** |
| G13 | audit-2 stem-pair phase | corr >= +0.7 <500 Hz | PASS | PASS |
| G14 | audit-3 rhythm grid | max ≤ 20 ms | 20.51 ms | **FAIL** (+0.51) |
| G15 | audit-4 motif identity | cos ≥ 0.9 / Jaccard ≥ 0.9 / cell ≥ 0.9 | PASS | PASS |
| G16 | audit-5 duck separation | 6 dB sub / ≤3 dB mids | 4.60 dB sub, chords −2.09, lead 0.00 | PASS |

---

## 3. THREE-STRIKES DELTAS (honest, with root causes)

| gate | target | final | delta / root cause |
|------|--------|-------|--------------------|
| G1 onsets d1/d2 | >= 18/s | 9.92 / 9.94 | −8.1/s — needs denser drop **ARRANGEMENT** (32nd rolls, fills, stab layers); mix moves exhausted |
| G4 drop RMS d1/d2 | >= 0.45 | 0.3497 / 0.3779 | −0.100 / −0.072 — lead gate cost > side-boost gain; premaster/makeup no-ops post-limiter (P7/P8/final law re-confirmed) |
| G6 10–20k d1/d2 | <= −48 dBFS | −44.38 / −46.98 | +3.62 / +1.02 — d1 needs 10–14k subtraction ~0.95 + lead-gate edge smoothing |
| G9 contrast | >= 6 dB | 3.22 | −2.78 — drop RMS fell with gated lead; break −13 dB makeup already at floor |
| G12 pitch | 0 events | 24 | lead 35 ms gate windows smear CQT — needs >= 60 ms window or per-note gate aligned to lead notes |
| G14 grid | <= 20 ms | 20.51 ms | +0.51 ms — marginal; velocity-shaded hats shifted flux centroids |

---

## 4. Coherence audits — FINAL 3/5

- Audit 1 PITCH: **FAIL** — 24 out-of-key events (lead CQT smear from 35 ms
  gate windows; G4/C/F/A#/D# reads in drop + breakdown windows).
- Audit 2 STEM-PAIR: **PASS** — corr <500 Hz +0.808..+1.000 all pairs;
  mud/harsh bands bounded; kick+sub downbeat collision intentional (duck law).
- Audit 3 RHYTHM GRID: **FAIL** — 243 onsets/30 s, mean 11.91 ms, max
  |offset| 20.51 ms vs 20 ms gate.
- Audit 4 MOTIF: **PASS** — interval cosine 1.000 (top), Jaccard 1.000,
  audio pitch-cell corr 1.000.
- Audit 5 DYN SEPARATION: **PASS** — sub duck transfer 4.60 dB (locked G16
  method), chords −2.09 dB (≤3 law), lead 0.00 dB.

---

## 5. Round trajectory (3-iteration loop, spent)

- Round 1 (E1–E8 Owner-map propagation, 8 stems): audits 2/5, gates 15/23.
- Round 2 (preset switches lead/piano/bell, engine fixes, mono-ize <500):
  audits 5/5 mid-session, gates 16/23.
- Round 3 (drop makeup +2 dB, velocity-shaded hats, band-limited side-boost):
  16/23 at run time, but the final audit run exposed stale G12/G14 →
  **TRUE FINAL 14/23**. Loop-discipline law re-confirmed: audits run after
  EVERY stem change before gates (G12–G16 read coherence_audit.md).

---

## 6. Deliverable ledger (verified on disk this session)

| deliverable | on-disk state |
|-------------|---------------|
| song_final pass.wav | EXISTS — 68,796,088 B, 195.00 s, round-3 WIP master (peak 0.9681, 0 clipped, chain 40 ms / 2:1 / 0-tanh). **NOT a shipped deliverable.** |
| stems/ | 9 files — 8 Owner-map stems + `_sub_unducked.wav` G16 scratch; all non-silent |
| coherence_audit.md | FINAL 3/5 (§4 above) |
| gates_p17_r1_table.txt | FINAL 14/23 (§2 above) |
| measure_final pass.md | §1 defs locked pre-render; §12 round log + 3-strikes; §13/§15/§16 stamps |
| remix_log.md | FINAL PASS section FINAL — session-7 round log + 7 laws learned |
| .home/agent/Music/MAINSTAGE_final pass.mp3 | **CORRECTLY ABSENT** — Owner §4-9: mp3 only on all-gates-pass (6 line-items open) |

**PENDING (clearly marked):** MAINSTAGE_final pass.mp3 — blocked on an all-pass
master; ship itself — blocked on the 6 open line-items above.

---

## 7. Resume pointer (NEW pass decision for Owner — max-3 law spent)

Any further gate work is a NEW pass, in this order:

1. **G12 first** — lead gate window >= 60 ms (or per-note gate aligned to
   lead notes) → run audit 1.
2. **G1** — drop re-render with denser arrangement (32nd rolls, fills, stab
   layers); onsets are arrangement-determined, not mix-determined.
3. **G4** — wider (decorrelated) drop content per the §1 feasibility pairing
   (stereo program RMS 0.45 needs wide content; premaster/makeup are no-ops).
4. **G6** — 10–14k subtraction ~0.95 on drop1 + lead-gate edge smoothing.
5. **G9** — recovers with G4 (drop RMS up) without touching the break floor.
6. **G14** — +0.51 ms marginal; re-check after any drum touch.

Loop law for the new pass: coherence audits run after EVERY stem change,
before gates.
