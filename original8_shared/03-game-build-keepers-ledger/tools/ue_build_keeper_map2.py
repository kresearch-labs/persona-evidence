# EDITOR-MODE: extend Lvl_KeeperIsland with the Keeper's Ledger set dressing:
# lighthouse tower + beam, 4 duty stations, 8 ship proxies, 6 wreck proxies,
# reef, 3 story notes. All engine basic shapes (original, procedural).
import unreal, traceback

LOG = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/logs/editor_mapbuild.log"

def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

def spawn(eas, cls, loc, label, scale=None, rot=None):
    a = eas.spawn_actor_from_class(cls, loc, rot or unreal.Rotator(0, 0, 0))
    if a and label:
        a.set_actor_label(label)
    if a and scale:
        a.set_actor_scale3d(scale)
    return a

w("=== EXTEND Lvl_KeeperIsland ===")
try:
    world = unreal.EditorLoadingAndSavingUtils.load_map("/Game/Lvl_KeeperIsland")
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    existing = eas.get_all_level_actors()
    labels = set()
    for a in existing:
        try:
            labels.add(a.get_actor_label())
        except Exception:
            pass
    w("existing actors: %d" % len(existing))

    SMA = unreal.StaticMeshActor
    plane_mesh = unreal.load_asset("/Engine/BasicShapes/Plane")
    cube_mesh = unreal.load_asset("/Engine/BasicShapes/Cube")
    cyl_mesh = unreal.load_asset("/Engine/BasicShapes/Cylinder")
    sphere_mesh = unreal.load_asset("/Engine/BasicShapes/Sphere")

    def mesh_actor(cls, loc, label, scale, mesh):
        a = spawn(eas, cls, loc, label, scale)
        if a and mesh:
            smc = a.get_component_by_class(unreal.StaticMeshComponent)
            if smc:
                smc.set_static_mesh(mesh)
        return a

    # ---- LIGHTHOUSE at (300, 0) ----
    LX, LY = 300, 0
    if "Tower_Base" not in labels:
        for i in range(6):
            mesh_actor(SMA, unreal.Vector(LX, LY, 25 + i * 50), "Tower_Seg_%d" % i,
                       unreal.Vector(0.55 - i * 0.03, 0.55 - i * 0.03, 0.5), cyl_mesh)
        mesh_actor(SMA, unreal.Vector(LX, LY, 310), "LampRoom", unreal.Vector(0.9, 0.9, 0.7), cube_mesh)
        mesh_actor(SMA, unreal.Vector(LX, LY, 345), "Tower_Roof", unreal.Vector(0.7, 0.7, 0.25), cyl_mesh)
        w("lighthouse tower built (6 segs + lamp room + roof)")
    else:
        w("lighthouse already present")

    # beam spotlight (rotates at night)
    if "BeamLight" not in labels:
        beam = eas.spawn_actor_from_class(unreal.SpotLight, unreal.Vector(LX, LY, 312), unreal.Rotator(0, 0, 0))
        if beam:
            beam.set_actor_label("BeamLight")
        w("BeamLight: %s" % bool(beam))
    # tower glow
    if "TowerGlow" not in labels:
        glow = eas.spawn_actor_from_class(unreal.PointLight, unreal.Vector(LX, LY, 305), unreal.Rotator(0, 0, 0))
        if glow:
            glow.set_actor_label("TowerGlow")
        w("TowerGlow: %s" % bool(glow))

    # ---- DUTY STATIONS ----
    if "Station_Lamp" not in labels:
        mesh_actor(SMA, unreal.Vector(LX - 120, LY + 60, 40), "Station_Lamp", unreal.Vector(0.4, 0.4, 1.2), cyl_mesh)
        mesh_actor(SMA, unreal.Vector(120, 180, 40), "Station_Lens", unreal.Vector(1.6, 0.9, 0.8), cube_mesh)
        mesh_actor(SMA, unreal.Vector(-60, -220, 45), "Station_Oil", unreal.Vector(0.7, 0.7, 0.9), cyl_mesh)
        mesh_actor(SMA, unreal.Vector(220, -160, 40), "Station_Log", unreal.Vector(1.4, 0.9, 0.7), cube_mesh)
        w("4 duty stations placed")
    else:
        w("stations already present")

    # ---- SHIP PROXIES (hidden, sea line y=1400) ----
    n_ships = len([l for l in labels if l.startswith("Ship_")])
    if n_ships < 8:
        for i in range(8):
            s = mesh_actor(SMA, unreal.Vector(-1800, 1400 + (i % 3) * 60, 40), "Ship_%d" % i,
                           unreal.Vector(0.5, 2.2, 0.6), cube_mesh)
            if s:
                s.set_actor_hidden_in_game(True)
                s.set_actor_enable_collision(False)
        w("8 ship proxies placed (hidden)")

    # ---- WRECK PROXIES (hidden, shore y~950) ----
    n_wrecks = len([l for l in labels if l.startswith("Wreck_")])
    if n_wrecks < 6:
        for i in range(6):
            wr = mesh_actor(SMA, unreal.Vector(-600 + i * 240, 920 + (i % 2) * 60, 30), "Wreck_%d" % i,
                            unreal.Vector(1.6, 0.9, 0.5), cube_mesh)
            if wr:
                wr.set_actor_hidden_in_game(True)
                wr.set_actor_enable_collision(False)
        w("6 wreck proxies placed (hidden)")

    # ---- REEF ----
    if "Reef_0" not in labels:
        r = mesh_actor(SMA, unreal.Vector(200, 1250, 5), "Reef_0", unreal.Vector(2.4, 1.6, 0.8), sphere_mesh)
        if r:
            r.set_actor_hidden_in_game(True)
        w("reef placed (hidden)")

    # ---- STORY NOTES ----
    if "Note_Lens" not in labels:
        mesh_actor(SMA, unreal.Vector(360, 140, 35), "Note_Lens", unreal.Vector(0.15, 0.15, 0.5), cube_mesh)
        mesh_actor(SMA, unreal.Vector(-40, -140, 35), "Note_Oil", unreal.Vector(0.15, 0.15, 0.5), cube_mesh)
        mesh_actor(SMA, unreal.Vector(240, -240, 35), "Note_Report", unreal.Vector(0.15, 0.15, 0.5), cube_mesh)
        w("3 story notes placed")

    ok = unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    w("saved: %s" % ok)
    w("=== EXTEND DONE ===")
except Exception:
    w("FAIL: %s" % traceback.format_exc())
