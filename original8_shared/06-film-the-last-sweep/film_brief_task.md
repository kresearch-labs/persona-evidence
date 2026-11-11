# FILM TEST — 30-SECOND ANIMATED SHORT (Owner's order, verbatim)

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
