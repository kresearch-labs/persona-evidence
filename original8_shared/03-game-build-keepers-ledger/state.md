
## STEP 1 — ENGINE VERDICT
UE5.8.3 scalability verify COMPLETE on T1000 4GB. Method: real game-process run, 1080p native, all sg groups=Medium(1)+ResQ100, VSync off, CSV per-frame profiler, 3600 frames. Scene: procedural Blender island+lighthouse+cottage+pier+wrecks (57 SM actors) + storm lighting + VOLUMETRIC FOG + SkyAtmosphere (+/- VolumetricCloud A/B). RESULTS: clouds ON 29.3fps avg (GPU 33.9ms); clouds OFF 52.4fps avg / 53.2 steady, p95 50.5, GPU 19.0ms; repeat run 52.1fps (reproducible). VRAM 2480/4096MiB. VERDICT: UNREAL 5.8.3 PASS with documented constraint: no VolumetricCloud actors (15ms GPU cost) — storm sky = volumetric fog + SkyAtmosphere + rain particles + lightning lights. Full data: design/step1_engine_verdict.md. Note: brief said a scalability test was 'in flight' — none was running; this session built the scene and ran the benchmark from scratch (4 runs, all clean exits).

## Architecture verdict
RUNTIME ARCHITECTURE SOLVED (probe v17, logs/rt_probe.txt):
- unreal.register_slate_post_tick_callback(fn) = game loop. Fires EVERY frame on game thread in -game mode with delta_seconds. 256 frames/5s verified, ~50fps, clean quit EXIT=0.
- init_unreal.py (Content/Python/) auto-runs AFTER map load in -game mode = bootstrap hook.
- HUD: SystemLibrary.print_string PASS. Input: pc.is_input_key_down(Key) exists (Key ctor property name TBD).
- DEAD ENDS (do not run): PyActor/PyPawn classes absent; timers via SystemLibrary.set_timer_delegate (delegate has no world context -> RuntimeWarning, never fires); background-thread unreal API access hard-blocked (all 3 PythonCommandExecutionMode members raise "can only be called from game thread"); EditorLevelLibrary.get_game_world() SEGFAULTS in -game mode (use guarded ObjectIterator scan for World class instead); new_object cannot nativize delegate types; GameplayStatics has no spawn/timer fns in 5.8.3 python.
- Map Lvl_ScalStorm lacks PlayerStart -> pawn None. Fix: editor-mode python adds PlayerStart, saves map. Template BP_ThirdPersonCharacter + Enhanced Input already in project (movement free).
- Next: PlayerStart editor run -> game probe (Key props, pawn, E-key poll) -> BUILD THE GAME.

## round2
ROUND 2 COMPLETE (Keeper's Ledger, UE 5.8.3): audio + menu/settings + visual pass all verified live. Full-truth ending score 103 (30 saved/0 lost/3 notes/14 salvaged/0 dark), EXIT=0, 3 fresh 1280x720 screenshots (19-29KB, non-trivial). Audio: 7 studio-v3 synthesized WAVs (storm bed/beam hum/dark drone/bell/clank/blip/lost-hull), 8 bed activations across 7 nights. Menu: title + volume/subtitles/camera settings [299af5f81d60]. Visual: 8 programmatic materials on 31 actors, volumetric fog, warm beam. Scores: self 8.9 / qa-critic 8.6 → binding 8.6 = PASS. Remaining gaps for round 3 (polish): keeper character mesh, path-erosion island memory, tutorial diegetic checklist.
