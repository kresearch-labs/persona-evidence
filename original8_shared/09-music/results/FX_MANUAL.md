# FX_MANUAL.md — studio v3 FX layer (`studio.api_v3_fx`)

> Studio law: read this manual FIRST, before any composition decision.
> This engagement copy mirrors the studio master at
> `C:/Users/agent/work/project/studio/FX_MANUAL.md` and documents the exact
> API surface verified by probe during FINAL PASS (all signatures called
> successfully in `render_*_p12.py` / `mixdown_p12.py`).

Import BOTH layers every pass:

```python
import sys; sys.path.insert(0, "C:/Users/agent/work/project/studio")
import api as st        # final: samples / vital / sidechain / master / measure
import api_v3_fx as fx  # v3: the FX layer (this manual)
```

SR = 44100. Buffers are float32 stereo, shape **(2, N)**.

---

## 1. THE LAWS (graded)

1. **TONE-CHAIN LAW** — every stem gets a documented chain:
   `preset -> EQ -> saturation -> send-bus levels`. A chain that is all
   zeros is a defect. Print the chain in the brief.
2. **SEND-BUS LAW** — shared returns only (`fx.send_reverb` / `fx.send_delay`).
   One believable space for the song (e.g. a 2.2 s hall), plus at most one
   contrast space (e.g. a 3.4 s cathedral for the breakdown). Never a
   different wet blob per stem.
3. **CONTRAST LAW** — kick, hook and low anchors stay DRY; reverb/delay push
   pads/atmos back. Space reads only next to dryness.
4. **AUTOMATION LAW** — `filter_sweep` on builds; reverb decay/width must
   differ between breakdown and drop; micro-breaks (1-beat mutes) before
   drops. A section with static tone from first bar to last is a defect.
5. **MIX-DESK: HPF** — HPF the wet tail (send_reverb `hz_low`) so reverb mud
   never covers the low anchor.
6. **MICRO-BREAKS: MUTE** — the break beat is hard-zeroed POST-master
   (limiter tail rings back otherwise), with 2 ms fades.
7. **TONE FLATNESS** — `fx.spectral_balance(x)` must be printed for every
   stem AND the master. Smooth monotonic low->air profiles pass; resonant
   humps / harsh tops are the measured failure.

---

## 2. VERIFIED API SURFACE (v3)

### Synthesis
- `fx.render_synth(preset, notes, bpm, tail=...)` — render a Vital preset.
  `notes = [(pitch_midi, vel, start_beat, dur_beats), ...]`, beats relative
  to the buffer start. Returns (2, N) float32.
- `fx.list_presets()` — all Vital presets ("author/Name.vital").
- Probe before use (preset rotation law): peak > 0.3 = alive.

### Tone shaping
- `fx.tone_chain(x, name)` — named channel-strip preset
  (`"lead"`, `"pad"`, `"pluck"`, `"drum_bus"`, ...): HPF + tilt + image.
- `fx.eq(x, low_cut=Hz, mud_db=dB, mud_hz=Hz, presence_db=dB,
  presence_hz=Hz, high_cut=Hz, low_boost_db=dB)` — mix-desk EQ.
- `fx.saturate(x, drive_db, tone="clean"|"crush")` — harmonic saturation.
- `fx.width(x, amount)` — stereo width (1.0 = unchanged).
- `fx.chorus(x, mix)` — chorus/doubler, `mix` 0..1.
- `fx.filter_sweep(x, hz_from, hz_to, dur_s)` — automated filter sweep
  across `dur_s` seconds from the start of the buffer (builds).
- `fx.phaser(x, ...)` — phaser mod effect.
- `fx.pitch_shift(x, ...)` — pitch shift.

### Send buses (shared space — LAW 2)
- `fx.send_reverb(*stems, decay_s, wet, hz_low, pre_delay_ms)` — shared
  reverb return; `hz_low` HPFs the wet tail (LAW 5); long `pre_delay_ms`
  separates source from space.
- `fx.send_delay(*stems, beats, wet, feedback, bpm)` — tempo-synced shared
  delay return (`beats=0.75` -> dotted-8th pingpong feel).

### Bus / master
- `fx.bus_compression(x, thresh_db, ratio, makeup_db)` — bus glue
  (drum bus: thresh -20, ratio 2.5, makeup +1.5).
- `fx.spectral_balance(x)` — band profile dict:
  `{"low": dB, "mid": dB, "high": dB, "air": dB}`. Print per stem + master.

### Utility
- `fx.measure(x)` — `{"peak", "rms", "dur_s", ...}`.
- `fx.place(buf, smp, at_sample, gain)` — place a sample into a buffer.
- `fx.kit(...)` — drum kit listing.
- `fx.reverb(x, ...)`, `fx.delay(x, ...)` — inline (non-send) versions;
  prefer the send buses.

---

## 3. final LAYER (`studio.api`) — what the FX layer plugs into

- `st.load("folder/file.wav", gain=...)` — one-shot sample
  (`st.samples/dirt/<folder>/`).
- `st.sidechain(target, trigger, depth=...)` — duck `target` against the
  kick trigger buffer. Depth map (ground: deep sidechain on everything but
  the lead): chords .68, stabs .6, arp .6, pluck .55, pad .55, keys .5,
  choir .5, bell .45, lead 0.
- `st.master(x, ceiling_db=-1.0, comp_thresh_db=0, comp_ratio=1)` —
  limiter + bus comp. Pass `comp_thresh_db=0, comp_ratio=1` to keep bus
  comp OFF (it eats drop RMS); do per-section makeup instead.
- `st.measure(x)` — gate numbers.

---

## 4. FINAL PASS REFERENCE CHAINS (as built; brief §5 has the full table)

```
VERB_A "main hall":    decay 2.2s, pre-delay 30ms, hz_low 250  (drops/groove)
VERB_B "cathedral":    decay 3.4s, pre-delay 40ms, hz_low 250  (breakdown only)
DLY_A: 3/16 dotted-8th, fb .38   DLY_B: 1/4 straight, fb .30

lead:   wide_saw -> tone_chain lead -> saturate 3 clean -> width 1.25
        -> eq low_cut 180 / presence +3 @3.5k / mud -2 @380
        -> VERB_A wet .13 -> DLY_A wet .10            (near-dry anchor)
chords: versitile_pad -> tone_chain pad -> chorus .22 -> saturate 3.5
        -> eq low_cut 150 / mud -2.5 @350 -> SC .68 -> VERB_A .22 -> DLY_B .08
stabs:  ProphetBrassStab -> tone_chain pluck -> saturate 5 crush
        -> eq low_cut 220 / mud -3 @400 -> SC .60 -> VERB_A .14
pluck:  SuperSaw_Pluck -> tone_chain pluck -> saturate 2.5
        -> eq low_cut 200 / presence +1.5 @4k -> SC .55 -> DLY_A .22 -> VERB_A .16
arp:    ANOTHER_ARP -> eq low_cut 250 / presence +2 @5k -> SC .60
        -> DLY_A .18 -> VERB_A .15  (+filter_sweep in builds)
keys:   Cold_Keys -> tone_chain pad -> chorus .3 -> VERB_B .34
strings: deep_vib_strings -> eq low_cut 300 -> width 1.3 -> VERB_B .36
choir:  unsuccessful_choir -> width 1.5 -> eq low_cut 350 -> VERB_B .42
pad:    Lusions_Pad -> tone_chain pad -> eq low_cut 160 -> VERB_B .38 -> DLY_B .08
bell:   Untouched_Bell -> eq low_cut 400 -> DLY_A .28 -> VERB_A .22
drums:  house kit -> tone_chain drum_bus -> bus_compression -20/2.5/+1.5
        (kick DRY; clap/snare VERB_A .08; crash VERB_A .12)
booms/stomps: DRY low anchors, no sends
```

Automation: filter_sweep 300->12k on builds 1/2/3; VERB_A (2.2s) in drops vs
VERB_B (3.4s, wider) in breakdown; micro-break mutes before each drop,
hard-zeroed post-master.

---

## 5. ENGINEERING GOTCHAS (learned this pass)

- `dsp_common.write_wav` wants **(N, 2)** C-contiguous — transpose studio
  buffers `(2, N)` before writing (`np.ascontiguousarray(x.T)`).
- soundfile 0.13.x fails on non-C-contiguous arrays — always
  `np.ascontiguousarray`.
- `st.master` signature: `ceiling_db=-1.0, comp_thresh_db=0, comp_ratio=1`.
- FX kwarg names: `low_cut`, `mud_db`, `mud_hz`, `presence_db`,
  `presence_hz`, `beats`, `hz_from`, `hz_to`, `mix`, `tone` — not
  `low_cut_hz` / `drive_style` / `time_beats`.
- Limiter tail rings back into muted beats: hard-zero break beats
  POST-master, then 2 ms fades.
- Pad stacks can float-clip internally: normalize each stem to peak < 1.0
  before write (mixdown renormalizes anyway).
