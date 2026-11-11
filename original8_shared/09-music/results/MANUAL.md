# AURA STUDIO final — MANUAL (read fully before composing)

You have a REAL studio now. Do NOT hand-build drums/FX from oscillators.
Use this module for everything it covers; only synthesize by hand what it
cannot do (e.g. the formant guide vocal).

IMPORT (mandatory first lines of every render script):
    import sys
    sys.path.insert(0, "C:/Users/agent/work/project/studio")
    from studio import api as st
    import numpy as np

Interpreter: C:/Users/agent/work/RECOVERED_FROM_CARVE/experiments_rebuilt/.venv/bin/python

## 1. REAL SAMPLES (drums, 808s, perc, FX) — 222 kits
    kits = st.kit()                      # list all kit names
    st.kit("bd")                         # list files inside a kit
    kick = st.load("bd")                 # first sample in kit
    kick = st.load("bd/BT0A0D3.wav")     # exact file
    buf  = st.place(buf, kick, at_sample, gain=1.0, pan=0.0)
Useful kits: bd (24 kicks), hh (13 hats), sd, cp, 808bd/808sd/808hc/808oh,
bass1 (31 one-shots), ride, crash, clap aliases cp/clash, plus hundreds of
percussion/texture/FX kits — RUN st.kit() and CHOOSE deliberately.
Layer real one-shots; place off-grid for human feel; all float32 stereo 44.1k.

## 2. VITAL SYNTH ENGINE (pro wavetable synth, real presets)
    seg = st.render_synth("Category/Name.vital", notes, bpm=126)
          # notes: [(midi, vel 0-1, start_beats, dur_beats), ...] -> (2,N)
    st.list_presets()                    # every .vital preset in the library
Use for: supersaws, plucks, pads, keys, bass-bodies (before layering sub sine).
Pick presets by NAME search in list_presets() output; render chords as
note-lists; unison/detune lives INSIDE the preset — trust it.

VERIFIED-HOT presets (render 0.4-1.5 peak on a C chord probe, Oct 16):
  musinous/Musinous_-_Lead_Supersaw.vital     (1.47)
  charliejr/ARP_EDM.vital                     (1.08)
  musinous/Musinous_-_Chords_Supersaw.vital   (1.03)
  mch/SuperSaw_Pluck.vital                    (0.90)
  bluesheep33/BS.SU_Supersaw_Bass.vital       (0.90)
  slack/Supersaw_FutureBass.vital             (0.43)
CAUTION: some archived presets are dead (render 0.0 — they reference wavetables
not bundled). ALWAYS print st.measure(probe) per preset you pick; if peak==0,
pick another. Prefer the verified-hot list or presets from these same authors.

## 3. SIDECHAIN PUMP
    bass = st.sidechain(bass_buf, kick_buf, depth=0.8)   # kick ducks the bass

## 4. MASTERING (mandatory final stage)
    final = st.master(mix)               # HPF30 -> bus comp -> +1.5dB -> limiter
    print(st.measure(final))             # {peak, rms, clipped, dur_s} — ALWAYS print

## 5. RULES
- Drums/FX MUST be real samples (st.load/place), never synthesized.
- Synths SHOULD be Vital presets; the init preset is not a sound selection.
- The SINGER still needs your formant guide vocal (vocal_guide.wav dry,
  plus song_noVocal.wav) — that part is unchanged; harness does RVC after.
- Everything else (composition, arrangement, hooks, structure) is yours.
- Print st.measure for every stem and the master; gates unchanged
  (peak <= 0.98, 0 clipped, RMS >= 0.18 overall / >= 0.25 drops).
