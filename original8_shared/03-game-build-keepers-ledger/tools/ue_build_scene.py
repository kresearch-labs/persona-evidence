# UE5.8.3 headless editor script: import FBX, assemble storm island scene, save map.
# Run: UnrealEditor-Cmd ScalTest.uproject -run=pythonscript -script=<this file> -nullrhi
# Writes a build report to logs/scene_build.txt (stdout capture is unreliable).
import unreal, os

BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
ASSETS = os.path.join(BASE, "assets_blender")
REPORT = os.path.join(BASE, "logs", "scene_build.txt")
rep_lines = []

def note(msg):
    rep_lines.append(msg)
    unreal.log("[SCAL] %s" % msg)

# --- imports (idempotent: replace_existing) ---
TASKS = []
def import_fbx(filename, dest):
    task = unreal.AssetImportTask()
    task.filename = os.path.join(ASSETS, filename)
    task.destination_path = "/Game/ScalContent/" + dest
    task.destination_name = dest
    task.automated = True
    task.save = True
    task.replace_existing = True
    TASKS.append(task)

import_fbx("env.fbx", "SM_Env")
import_fbx("lighthouse.fbx", "SM_Lighthouse")
import_fbx("props.fbx", "SM_Props")
unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(TASKS)
note("imports done")

def meshes_under(folder):
    out = []
    for a in unreal.EditorAssetLibrary.list_assets(folder, recursive=True):
        obj = unreal.EditorAssetLibrary.load_asset(a)
        if obj and obj.get_class().get_name() == "StaticMesh":
            out.append(obj)
    return out

env_meshes = meshes_under("/Game/ScalContent/SM_Env")
lh_meshes = meshes_under("/Game/ScalContent/SM_Lighthouse")
prop_meshes = meshes_under("/Game/ScalContent/SM_Props")
note("meshes env=%d lh=%d props=%d" % (len(env_meshes), len(lh_meshes), len(prop_meshes)))

# --- level (idempotent) ---
map_path = "/Game/Lvl_ScalStorm"
try:
    unreal.EditorLevelLibrary.new_level(map_path)
except Exception as e:
    note("new_level failed (%s), loading existing" % e)
    unreal.EditorLevelLibrary.load_level(map_path)

def spawn(cls, name, loc, rot=(0, 0, 0)):
    sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    a = sub.spawn_actor_from_class(cls, unreal.Vector(*loc), unreal.Rotator(*rot))
    if a:
        a.set_actor_label(name)
    return a

def set_prop(obj, prop, val):
    try:
        obj.set_editor_property(prop, val)
        return True
    except Exception as e:
        note("prop %s failed: %s" % (prop, e))
        return False

# --- environment meshes ---
spawned = 0
actor_sub = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
for sm in env_meshes + lh_meshes + prop_meshes:
    a = actor_sub.spawn_actor_from_class(unreal.StaticMeshActor, unreal.Vector(0, 0, 0))
    if not a:
        note("spawn failed (class): %s" % sm.get_name())
        continue
    comp = a.get_editor_property("static_mesh_component")
    ok = False
    try:
        ok = comp.set_static_mesh(sm)
    except Exception:
        try:
            info = unreal.MeshComponentStaticLightingInfo()
            ok = comp.set_static_mesh(sm, info)
        except Exception as e:
            note("set_static_mesh failed %s: %s" % (sm.get_name(), e))
    if ok:
        a.set_actor_label("Env_" + sm.get_name())
        spawned += 1
    else:
        note("mesh set failed: %s" % sm.get_name())
note("mesh actors spawned=%d" % spawned)

# --- storm lighting ---
sun = spawn(unreal.DirectionalLight, "StormSun", (0, 0, 500), (-35, 140, 0))
if sun:
    comp = sun.get_editor_property("root_component")
    set_prop(comp, "intensity", 0.6)
    set_prop(comp, "light_source_angle", 8.0)
    set_prop(comp, "use_temperature", True)
    set_prop(comp, "temperature", 7500.0)

skylight = spawn(unreal.SkyLight, "StormSky", (0, 0, 300))
if skylight:
    comp = skylight.get_editor_property("root_component")
    if not set_prop(comp, "real_time_capture", True):
        set_prop(comp, "bRealTimeCapture", True)

fog = spawn(unreal.ExponentialHeightFog, "StormFog", (0, 0, 0))
if fog:
    comp = fog.get_editor_property("component")
    setv = set_prop(comp, "b_enable_volumetric_fog", True)
    if not setv:
        setv = set_prop(comp, "bEnableVolumetricFog", True)
    set_prop(comp, "fog_density", 0.06)
    set_prop(comp, "fog_max_opacity", 0.9)
    note("volumetric fog set=%s" % setv)

try:
    clouds = spawn(unreal.VolumetricCloud, "StormClouds", (0, 0, 0))
    note("clouds spawned=%s" % (clouds is not None))
except Exception as e:
    note("clouds failed: %s" % e)

spawn(unreal.SkyAtmosphere, "StormAtmosphere", (0, 0, 0))

pp = spawn(unreal.PostProcessVolume, "StormPP", (0, 0, 0))
if pp:
    set_prop(pp, "unbound", True)

spawn(unreal.PlayerStart, "PlayerStart", (0, 45, 6), (0, 180, 0))

ctrl = unreal.EditorLevelLibrary.get_editor_world()
unreal.EditorLoadingAndSavingUtils.save_map(ctrl, map_path)
note("map saved")

with open(REPORT, "w") as f:
    f.write("\n".join(rep_lines) + "\n")
note("BUILD DONE")
