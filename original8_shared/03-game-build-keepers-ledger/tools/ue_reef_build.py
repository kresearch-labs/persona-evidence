# Round 3 map edit: 6 reef actors at wreck slots (hidden until formed) + second PlayerStart shelter.
import unreal, traceback

LOG = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/logs/reef_build.log"

def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

try:
    w("=== REEF BUILD ===")
    unreal.EditorLoadingAndSavingUtils.load_map("/Game/Lvl_KeeperIsland")
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    existing = {a.get_actor_label() for a in eas.get_all_level_actors()}
    sphere = unreal.load_asset("/Engine/BasicShapes/Sphere")
    rock = unreal.load_asset("/Game/Mat_Rock")
    XS = [-600, -360, -120, 120, 360, 600]
    YS = [430, 500, 560, 500, 430, 560]
    made = 0
    for i, (x, y) in enumerate(zip(XS, YS)):
        lbl = "Reef_%d" % i
        if lbl in existing:
            continue
        a = eas.spawn_actor_from_class(unreal.StaticMeshActor, unreal.Vector(x, 1250 + (i % 2) * 80, 5))
        if a:
            a.set_actor_label(lbl)
            smc = a.get_component_by_class(unreal.StaticMeshComponent)
            if smc:
                smc.set_static_mesh(sphere)
                smc.set_world_scale3d(unreal.Vector(2.2 + (i % 3) * 0.4, 1.6, 0.9))
                if rock:
                    smc.set_material(0, rock)
            a.set_actor_hidden_in_game(True)
            a.set_actor_enable_collision(False)
            made += 1
    w("reefs made: %d" % made)
    ok = unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    w("saved: %s === DONE ===" % ok)
except Exception:
    w("FAIL: %s" % traceback.format_exc())
