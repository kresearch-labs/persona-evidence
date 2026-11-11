# EDITOR-MODE: build Lvl_KeeperIsland from scratch — flat ground, PlayerStart,
# lights, navmesh bounds, rebuild nav, save, set as GameDefaultMap.
import unreal, traceback

LOG = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/logs/editor_mapbuild.log"

def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

w("=== BUILD Lvl_KeeperIsland ===")
try:
    # new empty map
    world = unreal.EditorLoadingAndSavingUtils.new_blank_map(True)
    w("blank map: %s" % world)
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

    # 1. ground plane (engine basic shape, 100x100m scaled)
    plane_cls = unreal.StaticMeshActor
    plane = eas.spawn_actor_from_class(plane_cls, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))
    if plane:
        mesh = unreal.load_asset("/Engine/BasicShapes/Plane")
        plane.set_actor_label("Ground")
        smc = plane.get_component_by_class(unreal.StaticMeshComponent)
        if smc and mesh:
            smc.set_static_mesh(mesh)
            plane.set_actor_scale3d(unreal.Vector(20.0, 20.0, 1.0))  # 2000x2000 units = 200m? plane is 100x100 base
        w("ground plane: %s scale=%s" % (plane.get_name(), plane.get_actor_scale3d()))

    # 2. PlayerStart
    ps = eas.spawn_actor_from_class(unreal.PlayerStart, unreal.Vector(0, 0, 200), unreal.Rotator(0, 0, 0))
    w("PlayerStart: %s at %s" % (ps.get_name() if ps else None, ps.get_actor_location() if ps else None))

    # 3. lights
    dl = eas.spawn_actor_from_class(unreal.DirectionalLight, unreal.Vector(500, 500, 800), unreal.Rotator(-45, 30, 0))
    if dl:
        dl.set_actor_label("Sun")
    sl = eas.spawn_actor_from_class(unreal.SkyLight, unreal.Vector(0, 0, 900), unreal.Rotator(0, 0, 0))
    if sl:
        sl.set_actor_label("SkyLight")
    sky = None
    try:
        sky = eas.spawn_actor_from_class(unreal.SkyAtmosphere, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))
        if sky:
            sky.set_actor_label("Atmosphere")
    except Exception:
        w("SkyAtmosphere fail: %s" % traceback.format_exc())
    w("lights: dl=%s sl=%s sky=%s" % (bool(dl), bool(sl), bool(sky)))

    # 4. fog + exponential height fog for mood
    try:
        fog = eas.spawn_actor_from_class(unreal.ExponentialHeightFog, unreal.Vector(0, 0, 0), unreal.Rotator(0, 0, 0))
        if fog:
            fog.set_actor_label("StormFog")
            w("fog added")
    except Exception:
        w("fog fail: %s" % traceback.format_exc())

    # 5. navmesh bounds
    nv = eas.spawn_actor_from_class(unreal.NavMeshBoundsVolume, unreal.Vector(0, 0, 100), unreal.Rotator(0, 0, 0))
    if nv:
        nv.set_actor_scale3d(unreal.Vector(60.0, 60.0, 10.0))
        w("navmesh volume scaled %s" % nv.get_actor_scale3d())

    # 6. rebuild nav
    try:
        unreal.SystemLibrary.execute_console_command(world, "RebuildNavigation")
        w("nav rebuilt")
    except Exception:
        w("nav rebuild fail: %s" % traceback.format_exc())

    # 7. save as new asset
    ok = unreal.EditorLoadingAndSavingUtils.save_map(world, "/Game/Lvl_KeeperIsland")
    w("save result: %s" % ok)
    w("=== DONE ===")
except Exception:
    w("FAIL: %s" % traceback.format_exc())
