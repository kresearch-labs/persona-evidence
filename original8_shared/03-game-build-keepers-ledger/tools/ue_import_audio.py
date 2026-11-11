# Import the synthesized SFX WAVs into the project as SoundWave assets.
import unreal, os, traceback

LOG = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/logs/audio_import.log"

def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

try:
    src_dir = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/game/ScalTest/Content/Audio"
    at = unreal.AssetToolsHelpers.get_asset_tools()
    tasks = []
    names = ["storm_bed", "beam_hum", "dark_drone", "ship_bell",
             "salvage_clank", "interact_blip", "ship_lost"]
    for n in names:
        t = unreal.AssetImportTask()
        t.filename = os.path.join(src_dir, n + ".wav")
        t.destination_path = "/Game/Audio"
        t.destination_name = n
        t.automated = True
        t.save = True
        t.replace_existing = True
        tasks.append(t)
    at.import_asset_tasks(tasks)
    # looping flags for the 3 beds
    for n in ("storm_bed", "beam_hum", "dark_drone"):
        a = unreal.load_asset("/Game/Audio/%s" % n)
        if a:
            a.set_editor_property("looping", True)
            w("%s looping=True" % n)
        else:
            w("MISSING %s" % n)
    for n in names:
        a = unreal.load_asset("/Game/Audio/%s" % n)
        w("%s -> %s" % (n, a.get_name() if a else "FAIL"))
    w("=== IMPORT DONE ===")
except Exception:
    w("FAIL: %s" % traceback.format_exc())
