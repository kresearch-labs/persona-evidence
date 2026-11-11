#!/bin/bash
# UE5.8.3 scalability benchmark — The Keeper's Ledger (Step 1 verify)
# Storm island scene, native 1080p, all scalability groups = Medium (1),
# volumetric fog + clouds + Lumen + VSM active.
# CSV profiler captures per-frame stats for N frames, then exits cleanly.
# Usage: run_benchmark.sh <frames> <tag>
FRAMES=${1:-3600}
TAG=${2:-run}
BASE=C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210
export DISPLAY=:0
export LIBGL_ALWAYS_SOFTWARE=0
cd "$BASE"

C:/Users/agent/work/apps/Unreal5.8.3/Engine/Binaries/Linux/UnrealEditor \
  "$BASE/game/ScalTest/ScalTest.uproject" \
  /Game/Lvl_ScalStorm \
  -game -windowed -ResX=1920 -ResY=1080 \
  -ExecCmds="t.MaxFPS 0,r.VSync 0,sg.ResolutionQuality 100,sg.ViewDistanceQuality 1,sg.AntiAliasingQuality 1,sg.ShadowQuality 1,sg.GlobalIlluminationQuality 1,sg.ReflectionQuality 1,sg.PostProcessQuality 1,sg.TextureQuality 1,sg.EffectsQuality 1,sg.FoliageQuality 1,sg.ShadingQuality 1,r.VolumetricCloud 1,r.ScreenPercentage 100,CsvProfile EXITONCOMPLETION,CsvProfile STARTFILE=ScalBench_$TAG,CsvProfile FRAMES=$FRAMES" \
  -ExitAfterCsvProfiling \
  -seconds=600 \
  -nosplash -unattended -nopause -stdout -fullstdlogwrite \
  > logs/bench_$TAG.log 2>&1
echo "EXIT=$?"
find "$BASE/game/ScalTest/Saved" -name 'ScalBench*' 2>/dev/null | head -5
