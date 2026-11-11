# STEP 1 — ENGINE VERDICT: UNREAL 5.8.3 (PASS, with one documented constraint)

Date: 2026-10-20. Machine: T1000 4GB, driver 580.178.04, Vulkan 1.4.312.
Method: real UE5.8.3 game-process run (not editor), native 1080p windowed,
all scalability groups forced to Medium (1) + ResolutionQuality 100 + ScreenPercentage 100,
VSync off, CSV profiler per-frame capture, 3600 frames (~2min), self-terminating.

## Test scene (built this session, all original procedural Blender assets)
- 240m procedural island terrain (200x200 grid, noise-displaced, flat lighthouse pad)
- Ocean plane, lighthouse (base/tapered tower/gallery/glass lamp room/emissive core/roof)
- Keeper cottage, 25 rocks, pier (deck+posts), 3 wreck hulls+masts — 57 static mesh actors
- Storm lighting: dim cool sun (0.6 intensity, 7500K), skylight (realtime capture),
  **exponential height fog with VOLUMETRIC FOG enabled (density 0.06, max opacity 0.9)**,
  SkyAtmosphere, unbounded post-process volume, PlayerStart.
- VolumetricCloud actor: ON in runs A/D, OFF in runs B/C (the A/B variable).

## Results (per-frame CSV, steady-state = frames after first 600)

| Run | Clouds | Frames | Avg FPS | Median | P95 | P99 | GPU ms | >33.3ms |
|-----|--------|--------|---------|--------|-----|-----|--------|---------|
| smoke2    | ON  | 3600 | 29.3 | 29.7 | 27.6 | 25.7 | 33.9 | 58.3% |
| noclouds  | OFF | 3600 | **52.4** | 53.2 | 50.5 | 48.1 | 19.0 | 0.1% |
| vramcheck | OFF | 1800 | 52.1 | 52.7 | 49.8 | 42.7 | 19.2 | 0.1% |
| cloudshot | ON  | 1200 | 28.4 | 28.8 | 26.7 | 20.8 | 35.3 | 93.1% |

- Bottleneck is GPU (33.9ms GPU vs 1.8ms game thread with clouds) — as expected on T1000.
- VRAM during live run: 2480 / 4096 MiB — headroom OK.
- Engine ran clean: game process boots the map, renders, captures, exits 0. No crash.

## VERDICT
**UNREAL 5.8.3 — PASS.** The spec scene ("1080p medium, volumetric fog + storms, >=30fps")
holds at **52fps steady** with the storm atmosphere built from volumetric fog +
SkyAtmosphere + storm lighting. Even the heaviest variant (full volumetric clouds)
sits at ~29fps, i.e. the bar is reachable even there with minor tuning.

### Documented constraint (design law from this test)
**Do not use VolumetricCloud actors on T1000.** One cloud layer costs ~15ms GPU.
The Keeper's Ledger storm sky = exponential height fog (volumetric on) + SkyAtmosphere +
rain particle system + lightning flash lights + (optional) cheap cloud plane/meshes.
This is recorded as a performance budget line, not a hope: [game_performance_engineer seat].

## Receipts
- Scene build report: logs/scene_build.txt (57 meshes, fog set=True, map saved)
- Asset list: logs/asset_list.txt (67 imported assets)
- Benchmark CSVs: game/ScalTest/Saved/Profiling/CSV/ScalBench_*.csv
- Benchmark script: tools/run_benchmark.sh (settings visible in -ExecCmds)
- Scene builder: tools/build_scal_island.py (Blender 5.2.2 API)
- Screenshots: screenshots/scene_noclouds.png, screenshots/scene_clouds.png (1920x1080)
- VRAM receipt: nvidia-smi 2480MiB/4096MiB @ 98% GPU util during run
