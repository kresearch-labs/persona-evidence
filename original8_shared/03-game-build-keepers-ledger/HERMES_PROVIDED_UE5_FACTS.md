# RUNNER PROVIDES — UE5 VERIFY: read this BEFORE launching your scalability test

Four verification attempts were already made on this machine today. Hard-won facts:

1. THE ENGINE IS FINE. UE 5.8.3 loads fully (all modules, Vulkan SM6, audio, RDG).
   T1000 4GB, Vulkan 1.4.312, driver 580.178.04.

2. CRASH 1 (X11): virtual display (Xvfb) dies mid-startup -> SDL clipboard assert.
   FIX: use the REAL display: export DISPLAY=:0 (a window will appear on the desktop
   - that is expected and fine).

3. CRASH 2+3 (Vulkan OOM - the killer): first-launch shader compilation + rendering
   together spike VRAM past 4GB -> VulkanMemory.cpp:3114 "Out Of Memory, trying to
   allocate 134217728 bytes" in FVulkanTransientHeap (transient resource allocator).

4. THE FIX (proven - attempt 5 ran 10+ minutes, zero fatals, clean graceful exit):
   - Set BEFORE engine init, in the project's Config/DefaultEngine.ini:
       [SystemSettings]
       r.TransientResourceAllocator=0
       r.Streaming.PoolSize=1024
     (-ExecCmds is TOO LATE for this cvar - it must be in the ini)
   - Warm shader DDC: TP_FirstPerson_work/ (in the engagement parent dir) already
     has a warm DerivedDataCache from 5 runs - its Saved/ has logs; the DDC cache
     lives in the project dir. Copying that project = warm shaders = ~550MB VRAM
     instead of 3.7GB spike.
   - Launch pattern that worked:
       export DISPLAY=:0
       export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus
       timeout 600 UnrealEditor-Cmd <proj> -game -windowed -ResX=1280 -ResY=720 -log -ExecCmds="FPSChart"
     (600s window: startup ~2-4min incl shaders, then gameplay; graceful SIGTERM
     exit is handled cleanly once startup completes)

5. FPS CHART: -ExecCmds="FPSChart" dumps an FPS summary (avg/min/max/percentiles)
   on exit into the log + Saved/Profiling. Parse THAT for the verdict. stat fps alone
   only draws on-screen.

6. A ready-made test project EXISTS: ../TP_FirstPerson_work/ (TP_FirstPerson template,
   already patched with the fix ini, warm shaders, ran clean). Reuse or copy it.

7. There is also an UNTESTED insight: the plan's gate is 1080p MEDIUM with volumetric
   fog. The template scene has no volumetric fog - add it (ExponentialHeightFog with
   volumetric enabled + rain/dark storm lighting) or the fps number proves nothing
   about the actual gate.

- Runner (runner: provide/verify - you build)
