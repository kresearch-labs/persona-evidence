These 5 are your pblocks for this task: film_narrative_director, film_visual_style, film_motion_choreographer, film_sound_composer, film_emotion_critic.\n\n# FILM TEST — 30-SECOND ANIMATED SHORT (Owner's order, verbatim)

"Make a 30-sec animated short video that tells a story and leaves viewer
with strong emotion. Make every frame and sound in code, with no stock
assets."

## THE FULL FLOW (binding, from ALL_REMAINING_PLAN.md Item 3)

1. BRIEF-FIRST: you (film_narrative_director, LEAD) lock the story FIRST —
   echo structure (setup seed -> turn -> payoff TRANSFORMS the seed),
   the emotion target, the anchor frame, the section map (30s, 4+ beats).
   WRITE THE BRIEF TO brief.md before any rendering.
2. FRAME ENGINE (code-only, no stock assets): procedural scenes —
   gradients, geometry, particle systems, noise fields (numpy +
   PIL/pygame offscreen render, 24-30fps). Camera grammar per
   film_motion_choreographer (eases, parallax, the longest still before
   the payoff). Palette per film_visual_style (3 colors max, peak color
   at the peak).
3. SOUND ENGINE (studio v3 — C:/Users/agent/work/project/studio/api.py
   + api_v3_fx.py, p15_common-era architecture): every element
   synthesized — pads/tones via oscillators + fx layer; 1-2s of silence
   before the payoff; ONE signature sound transformed at the end.
4. ASSEMBLY: frames -> ffmpeg (h264, 30fps) + synthesized track -> mp4.
5. EMOTION_CRITIC LOOP (film_emotion_critic grades frame-by-frame,
   citing seconds): nameable test (feeling nameable after ONE viewing),
   echo test (payoff transforms the setup seed), anchor-frame test (one
   frame remembered an hour later), zero-error (renders, plays, no
   glitch). FAILING BEATS RE-RENDER — 3 CHANCES, then the honest
   3-strikes report.
6. DELIVERY: short.mp4 + film_brief.md + graded_rubric.md in this
   directory. The mp4 must PLAY (verify with ffprobe: duration ~30s,
   h264, aac audio present).

## QUALITY BAR (the checklist law)
- Every frame and every sound from code. Zero stock assets, zero downloads.
- The emotion critic's grades cite SECONDS and name the test result.
- Honest failures: if a beat fails 3 times, log it in the rubric — do
  not fake the grade.
- The final grade is only HIT if all four critic tests pass.

## FINAL REPLY (3 lines)
1. mp4 path + duration + resolution
2. the story in one sentence + the emotion target + whether it HIT
3. critic scores per beat

== THE MEASURED GATES ==
- 30s ± 1s duration, 24-30fps constant, h264 + aac
- 4+ story beats, echo structure verified by the critic
- anchor frame: exactly one designated, visually distinct
- audio: -14 LUFS integrated, true peak <= -1 dBTP, no clipping
- all files in the CURRENT directory; no subdirectory scattering
\n\nENVIRONMENT NOTE: citation ledger tool provided (sources_ledger.py add/list/verify/render).\n\n### TASK CONTEXT
Current task: Film Brief Task
Work ONLY from the verified context below. If something is not here, say so explicitly instead of inventing it.

### GROUND FROM FILM_NARRATIVE_DIRECTOR PERSONA
- [c1b494eca772] contrast/overwhelming: the last 3 seconds decide the emotion (outcome: 1.0)
- [8111cdfe8516] dramatic-irony/subtle: the strongest beat lands on the unexpected frame (outcome: 1.0)
- [b39707a4dddb] dramatic-irony/subtle: the last 3 seconds decide the emotion (outcome: 1.0)
- [bc03a26e59da] contrast/overwhelming: the last 3 seconds decide the emotion (outcome: 1.0)
- [75e1021ec3cd] contrast/overwhelming: the strongest beat lands on the unexpected frame (outcome: 1.0)

### GROUND FROM FILM_VISUAL_STYLE PERSONA
- [4a78b1137647] dramatic-irony/overwhelming: the payoff frame reuses the opening composition, changed (outcome: 1.0)
- [e3e9af6c8ccd] dramatic-irony/subtle: the payoff frame reuses the opening composition, changed (outcome: 1.0)
- [d35303cf2774] dramatic-irony/subtle: the payoff frame reuses the opening composition, changed (outcome: 1.0)
- [8eadbb631d22] dramatic-irony/overwhelming: the payoff frame reuses the opening composition, changed (outcome: 1.0)
- [366686772042] dramatic-irony/subtle: the payoff frame reuses the opening composition, changed (outcome: 1.0)

### GROUND FROM FILM_MOTION_CHOREOGRAPHER PERSONA
- [397b73fef922] contrast/overwhelming: one motion idea per scene (outcome: 1.0)
- [1818e8ed9a00] dramatic-irony/overwhelming: one motion idea per scene (outcome: 1.0)
- [194aefdaa155] stillness-impact/overwhelming: one motion idea per scene (outcome: 1.0)
- [4d6e610885ad] transformed-echo/overwhelming: one motion idea per scene (outcome: 1.0)
- [d334d4ed4f70] stillness-impact/subtle: one motion idea per scene (outcome: 1.0)

### GROUND FROM FILM_SOUND_COMPOSER PERSONA
- [58205f7d0bce] dramatic-irony/moderate: everything synthesized in code - no audio files (outcome: 1.0)
- [396d70654ef4] dramatic-irony/overwhelming: everything synthesized in code - no audio files (outcome: 1.0)
- [e0f129be1024] dramatic-irony/moderate: everything synthesized in code - no audio files (outcome: 1.0)
- [1dfa0347b33c] dramatic-irony/overwhelming: everything synthesized in code - no audio files (outcome: 1.0)
- [58c9d2d5ce31] dramatic-irony/subtle: everything synthesized in code - no audio files (outcome: 1.0)

### GROUND FROM FILM_EMOTION_CRITIC PERSONA
- [fb40736ec334] contrast/overwhelming: grade frame-by-frame, cite seconds (outcome: 1.0)
- [00218a2c8e36] dramatic-irony/subtle: grade frame-by-frame, cite seconds (outcome: 1.0)
- [28cef84a8f80] contrast/subtle: grade frame-by-frame, cite seconds (outcome: 1.0)
- [d65aa17d106b] transformed-echo/overwhelming: grade frame-by-frame, cite seconds (outcome: 1.0)
- [2a53059315a4] contrast/subtle: grade frame-by-frame, cite seconds (outcome: 1.0)

### AGENT INPUT
These 5 are your pblocks for this task: film_narrative_director, film_visual_style, film_motion_choreographer, film_sound_composer, film_emotion_critic.\n\n# FILM TEST — 30-SECOND ANIMATED SHORT (Owner's order, verbatim)

"Make a 30-sec animated short video that tells a story and leaves viewer
with strong emotion. Make every frame and sound in code, with no stock
assets."

## THE FULL FLOW (binding, from ALL_REMAINING_PLAN.md Item 3)

1. BRIEF-FIRST: you (film_narrative_director, LEAD) lock the story FIRST —
   echo structure (setup seed -> turn -> payoff TRANSFORMS the seed),
   the emotion target, the anchor frame, the section map (30s, 4+ beats).
   WRITE THE BRIEF TO brief.md before any rendering.
2. FRAME ENGINE (code-only, no stock assets): procedural scenes —
   gradients, geometry, particle systems, noise fields (numpy +
   PIL/pygame offscreen render, 24-30fps). Camera grammar per
   film_motion_choreographer (eases, parallax, the longest still before
   the payoff). Palette per film_visual_style (3 colors max, peak color
   at the peak).
3. SOUND ENGINE (studio v3 — C:/Users/agent/work/project/studio/api.py
   + api_v3_fx.py, p15_common-era architecture): every element
   synthesized — pads/tones via oscillators + fx layer; 1-2s of silence
   before the payoff; ONE signature sound transformed at the end.
4. ASSEMBLY: frames -> ffmpeg (h264, 30fps) + synthesized track -> mp4.
5. EMOTION_CRITIC LOOP (film_emotion_critic grades frame-by-frame,
   citing seconds): nameable test (feeling nameable after ONE viewing),
   echo test (payoff transforms the setup seed), anchor-frame test (one
   frame remembered an hour later), zero-error (renders, plays, no
   glitch). FAILING BEATS RE-RENDER — 3 CHANCES, then the honest
   3-strikes report.
6. DELIVERY: short.mp4 + film_brief.md + graded_rubric.md in this
   directory. The mp4 must PLAY (verify with ffprobe: duration ~30s,
   h264, aac audio present).

## QUALITY BAR (the checklist law)
- Every frame and every sound from code. Zero stock assets, zero downloads.
- The emotion critic's grades cite SECONDS and name the test result.
- Honest failures: if a beat fails 3 times, log it in the rubric — do
  not fake the grade.
- The final grade is only HIT if all four critic tests pass.

## FINAL REPLY (3 lines)
1. mp4 path + duration + resolution
2. the story in one sentence + the emotion target + whether it HIT
3. critic scores per beat

== THE MEASURED GATES ==
- 30s ± 1s duration, 24-30fps constant, h264 + aac
- 4+ story beats, echo structure verified by the critic
- anchor frame: exactly one designated, visually distinct
- audio: -14 LUFS integrated, true peak <= -1 dBTP, no clipping
- all files in the CURRENT directory; no subdirectory scattering


### RULES
1. Use the ground above as reference; cite when a claim is influenced by it.
2. If a required fact is missing, say 'NOT IN MY CONTEXT'.
3. Cite which ground item each claim rests on.