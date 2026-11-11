# Visual pass: materials for all set dressing + volumetric fog beam.
import unreal, traceback

LOG = "C:/Users/agent/work/project/test-runs/test3-gamedesigner/t3-keepers-20261020-140210/logs/visual_pass.log"

def w(m):
    with open(LOG, "a") as f:
        f.write(m + "\n")

def make_color_mat(path, name, color, emissive=None, emissive_strength=1.0):
    try:
        existing = unreal.load_asset(path)
        if existing:
            return existing
        at = unreal.AssetToolsHelpers.get_asset_tools()
        mat = at.create_asset(name, "/Game", unreal.Material, unreal.MaterialFactoryNew())
        if mat is None:
            w("mat %s factory FAIL" % name)
            return None
        try:
            unreal.EditorAssetLibrary.rename_asset(mat.get_path_name(), path)
        except Exception:
            pass
        node = unreal.MaterialEditingLibrary.create_material_expression(
            mat, unreal.MaterialExpressionConstant3Vector, -200, 0)
        node.constant = unreal.LinearColor(r=color[0], g=color[1], b=color[2], a=1.0)
        unreal.MaterialEditingLibrary.connect_material_property(
            node, "", unreal.MaterialProperty.MP_BASE_COLOR)
        if emissive:
            en = unreal.MaterialEditingLibrary.create_material_expression(
                mat, unreal.MaterialExpressionConstant3Vector, -200, 200)
            en.constant = unreal.LinearColor(r=emissive[0] * emissive_strength,
                                             g=emissive[1] * emissive_strength,
                                             b=emissive[2] * emissive_strength, a=1.0)
            unreal.MaterialEditingLibrary.connect_material_property(
                en, "", unreal.MaterialProperty.MP_EMISSIVE_COLOR)
        unreal.MaterialEditingLibrary.recompile_material(mat)
        w("mat %s ok" % name)
        return mat
    except Exception:
        w("mat %s FAIL: %s" % (name, traceback.format_exc()))
        return None

try:
    w("=== VISUAL PASS ===")
    MATS = {
        "ground": make_color_mat("/Game/Mat_Ground", "Mat_Ground", (0.16, 0.20, 0.12)),
        "tower": make_color_mat("/Game/Mat_Tower", "Mat_Tower", (0.85, 0.82, 0.74)),
        "lamp": make_color_mat("/Game/Mat_Lamp", "Mat_Lamp", (0.15, 0.13, 0.10),
                               emissive=(1.0, 0.72, 0.38), emissive_strength=4.0),
        "sea": make_color_mat("/Game/Mat_Sea", "Mat_Sea", (0.05, 0.09, 0.13)),
        "hull": make_color_mat("/Game/Mat_Hull", "Mat_Hull", (0.10, 0.10, 0.13)),
        "rust": make_color_mat("/Game/Mat_Rust", "Mat_Rust", (0.38, 0.19, 0.10)),
        "paper": make_color_mat("/Game/Mat_Paper", "Mat_Paper", (0.88, 0.83, 0.68)),
        "rock": make_color_mat("/Game/Mat_Rock", "Mat_Rock", (0.13, 0.14, 0.15)),
    }
    unreal.EditorLoadingAndSavingUtils.load_map("/Game/Lvl_KeeperIsland")
    eas = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
    actors = eas.get_all_level_actors()

    def mat_for(lbl):
        if lbl.startswith("Tower_Seg") or lbl in ("Tower_Roof",):
            return MATS["tower"]
        if lbl == "LampRoom":
            return MATS["lamp"]
        if lbl.startswith("Ship_"):
            return MATS["hull"]
        if lbl.startswith("Wreck_"):
            return MATS["rust"]
        if lbl.startswith("Note_"):
            return MATS["paper"]
        if lbl.startswith("Reef_"):
            return MATS["rock"]
        if lbl.startswith("Station_"):
            return MATS["rust"] if "Oil" in lbl else MATS["tower"]
        return None

    n = 0
    for a in actors:
        try:
            lbl = a.get_actor_label()
        except Exception:
            continue
        if lbl == "Ground":
            m = MATS["ground"]
        else:
            m = mat_for(lbl)
        if not m:
            continue
        smc = a.get_component_by_class(unreal.StaticMeshComponent)
        if smc:
            smc.set_material(0, m)
            n += 1
    w("materials assigned to %d actors" % n)

    # volumetric fog: the beam becomes a real shaft
    for a in actors:
        try:
            if a.get_actor_label() != "StormFog":
                continue
            comp = a.get_component_by_class(unreal.ExponentialHeightFogComponent)
            if comp:
                for prop in ("volumetric_fog", "b_volumetric_fog"):
                    try:
                        comp.set_editor_property(prop, True)
                        w("volumetric fog via %s" % prop)
                        break
                    except Exception:
                        continue
                try:
                    comp.set_editor_property("volumetric_fog_scattering_distribution", 0.85)
                except Exception:
                    pass
        except Exception:
            pass

    # beam light: warm, strong, tight inner cone
    for a in actors:
        try:
            if a.get_actor_label() != "BeamLight":
                continue
            comp = a.get_component_by_class(unreal.SpotLightComponent)
            if comp:
                comp.set_editor_property("intensity", 15.0)
                comp.set_light_color(unreal.LinearColor(r=1.0, g=0.78, b=0.45, a=1.0))
                try:
                    comp.set_editor_property("inner_cone_angle", 18.0)
                    comp.set_editor_property("outer_cone_angle", 34.0)
                except Exception:
                    pass
                w("BeamLight tuned")
        except Exception:
            pass

    ok = unreal.EditorLoadingAndSavingUtils.save_dirty_packages(True, True)
    w("saved: %s === VISUAL PASS DONE ===" % ok)
except Exception:
    w("FAIL: %s" % traceback.format_exc())
