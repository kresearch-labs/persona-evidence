# EDITOR-MODE: lift PlayerStart, mark dirty explicitly, save, RELOAD, verify persistence.
import unreal, traceback

LOG = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/logs/editor_playerstart.log"

def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

w("=== EDITOR LIFT+VERIFY ===")
try:
    world = unreal.EditorLoadingAndSavingUtils.load_map("/Game/Lvl_ScalStorm")
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = eas.get_all_level_actors()
    ps = [a for a in actors if a.get_class().get_name() == "PlayerStart"]
    if not ps:
        w("NO PLAYERSTART — spawning one")
        ps = [eas.spawn_actor_from_class(unreal.PlayerStart, unreal.Vector(0, 0, 300), unreal.Rotator(0, 0, 0))]
    target = unreal.Vector(0, 0, 300)
    ps[0].set_actor_location(target, False, True)  # sweep=False, teleport=True
    w("moved -> %s (readback %s)" % (target, ps[0].get_actor_location()))
    # mark level package dirty explicitly
    try:
        unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
        w("save pass 1 done")
    except Exception:
        w("save1 fail: %s" % traceback.format_exc())

    # reload and verify persistence
    world2 = unreal.EditorLoadingAndSavingUtils.load_map("/Game/Lvl_ScalStorm")
    eas2 = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    ps2 = [a for a in eas2.get_all_level_actors() if a.get_class().get_name() == "PlayerStart"]
    w("after reload: PlayerStart at %s" % (ps2[0].get_actor_location() if ps2 else None))
    nav = [a for a in eas2.get_all_level_actors() if "NavMeshBounds" in a.get_class().get_name()]
    w("after reload: NavMeshBoundsVolumes=%d" % len(nav))
    w("=== DONE ===")
except Exception:
    w("FAIL: %s" % traceback.format_exc())
