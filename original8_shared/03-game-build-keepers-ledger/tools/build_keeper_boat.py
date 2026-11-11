# THE KEEPER'S LEDGER — keeper character + boat (Step 3)
# Run: blender -b -P build_keeper_boat.py
import bpy, math, os

OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets_blender"))
REPORT = []
def note(m): REPORT.append(m); print("[KEEPER]", m)

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

def mat(name, color, rough=0.85, metal=0.0, emit=0.0):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (*color, 1.0)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit > 0:
        for k in ("Emission Color", "Emission"):
            if k in b.inputs: b.inputs[k].default_value = (1.0,0.8,0.5,1.0); break
        if "Emission Strength" in b.inputs: b.inputs["Emission Strength"].default_value = emit
    return m

def cone(name, r1, r2, depth, loc, material, verts=16, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1, radius2=r2, depth=depth, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name; o.data.materials.append(material)
    return o

def cyl(name, r, depth, loc, material, verts=16, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name; o.data.materials.append(material)
    return o

def cube(name, size, loc, material, scale=(1,1,1), rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(size=size, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name; o.scale = scale
    o.data.materials.append(material)
    return o

def sphere(name, r, loc, material, subdiv=3):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdiv, radius=r, location=loc)
    o = bpy.context.active_object; o.name = name; o.data.materials.append(material)
    return o

# ============ KEEPER (stylized, readable silhouette — oilskin + hat) ============
def build_keeper():
    parts = []
    m_oilskin = mat("M_Oilskin", (0.13,0.16,0.15), rough=0.55)   # dark yellow-green slicker
    m_oilhat  = mat("M_OilHat",  (0.16,0.19,0.17), rough=0.5)
    m_boots   = mat("M_Boots",   (0.08,0.07,0.06), rough=0.6)
    m_skin    = mat("M_Skin",    (0.55,0.42,0.33), rough=0.7)
    m_lantern = mat("M_Lantern", (0.5,0.4,0.2), rough=0.4, metal=0.6)
    m_wick    = mat("M_WickGlow",(1.0,0.75,0.4), emit=3.0)
    # proportions: total ~1.8m, origin at feet
    # legs
    parts.append(cube("Keeper_LegL", 1, (-0.11,0,0.42), m_oilskin, scale=(0.13,0.15,0.42)))
    parts.append(cube("Keeper_LegR", 1, (0.11,0,0.42), m_oilskin, scale=(0.13,0.15,0.42)))
    # boots
    parts.append(cube("Keeper_BootL", 1, (-0.11,0.03,0.10), m_boots, scale=(0.15,0.24,0.10)))
    parts.append(cube("Keeper_BootR", 1, (0.11,0.03,0.10), m_boots, scale=(0.15,0.24,0.10)))
    # torso (oilskin coat)
    parts.append(cube("Keeper_Torso", 1, (0,0,1.05), m_oilskin, scale=(0.34,0.22,0.42)))
    # coat skirt
    parts.append(cube("Keeper_CoatSkirt", 1, (0,0,0.78), m_oilskin, scale=(0.36,0.24,0.14)))
    # arms
    parts.append(cube("Keeper_ArmL", 1, (-0.24,0,1.02), m_oilskin, scale=(0.10,0.12,0.38)))
    parts.append(cube("Keeper_ArmR", 1, (0.24,0,1.02), m_oilskin, scale=(0.10,0.12,0.38)))
    # hands
    parts.append(sphere("Keeper_HandL", 0.07, (-0.24,0,0.80), m_skin, subdiv=2))
    parts.append(sphere("Keeper_HandR", 0.07, (0.24,0,0.80), m_skin, subdiv=2))
    # head + sou'wester hat
    parts.append(sphere("Keeper_Head", 0.14, (0,0,1.42), m_skin, subdiv=3))
    parts.append(cone("Keeper_Hat", 0.17, 0.05, 0.12, (0,0,1.53), m_oilhat, verts=12))
    parts.append(cyl("Keeper_HatBrim", 0.20, 0.03, (0,0,1.48), m_oilhat, verts=12))
    # lantern in right hand (the keeper's signature prop)
    parts.append(cyl("Keeper_LanternBody", 0.06, 0.12, (0.24,0,0.70), m_lantern, verts=10))
    parts.append(cyl("Keeper_LanternFlame", 0.025, 0.05, (0.24,0,0.70), m_wick, verts=8))
    parts.append(cyl("Keeper_LanternRing", 0.045, 0.015, (0.24,0,0.78), m_lantern, verts=10))
    note("keeper done (%d parts)" % len(parts))
    return parts

# ============ SUPPLY BOAT (the boat that stopped coming — story prop at pier) ============
def build_boat():
    parts = []
    m_hull = mat("M_BoatHull", (0.18,0.22,0.24), rough=0.6)
    m_deck = mat("M_BoatDeck", (0.35,0.28,0.20), rough=0.85)
    m_cabin= mat("M_BoatCabin",(0.25,0.28,0.30), rough=0.7)
    m_glass= mat("M_BoatGlass",(0.6,0.7,0.75), rough=0.2)
    # hull: tapered box via scaled cubes (stylized)
    parts.append(cube("Boat_HullBase", 1, (0,0,0.35), m_hull, scale=(1.1,3.2,0.5)))
    parts.append(cube("Boat_Bow", 1, (0,3.0,0.45), m_hull, scale=(0.7,1.2,0.4), rot=(0,0,0)))
    parts.append(cube("Boat_Stern", 1, (0,-3.0,0.45), m_hull, scale=(0.9,0.8,0.4)))
    parts.append(cube("Boat_GunwaleL", 1, (-1.05,0,0.75), m_hull, scale=(0.12,6.2,0.35)))
    parts.append(cube("Boat_GunwaleR", 1, (1.05,0,0.75), m_hull, scale=(0.12,6.2,0.35)))
    parts.append(cube("Boat_Deck", 1, (0,0,0.62), m_deck, scale=(1.9,5.8,0.06)))
    # cabin
    parts.append(cube("Boat_Cabin", 1, (0,-1.6,1.05), m_cabin, scale=(1.3,1.6,0.7)))
    parts.append(cube("Boat_CabinGlass", 1, (0,-0.78,1.15), m_glass, scale=(1.1,0.06,0.4)))
    # mast + boom (cargo crane feel)
    parts.append(cyl("Boat_Mast", 0.07, 3.4, (0,1.2,2.2), m_cabin, verts=10, rot=(math.radians(-18),0,0)))
    parts.append(cyl("Boat_Boom", 0.05, 2.2, (0,2.4,1.5), m_cabin, verts=8, rot=(math.radians(55),0,0)))
    # mooring rope hint
    parts.append(cyl("Boat_Cleat", 0.05, 0.3, (1.0,2.2,0.85), m_cabin, verts=8, rot=(0,math.pi/2,0)))
    note("boat done (%d parts)" % len(parts))
    return parts

clear_scene()
keeper = build_keeper()
boat = build_boat()

def export(path, objs):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.export_scene.fbx(filepath=path, use_selection=True, apply_unit_scale=True,
                             apply_scale_options='FBX_SCALE_NONE', object_types={'MESH'},
                             add_leaf_bones=False, bake_anim=False, mesh_smooth_type='OFF')
    note("exported %s (%d objs, %d bytes)" % (os.path.basename(path), len(objs), os.path.getsize(path)))

export(os.path.join(OUT, "game_keeper.fbx"), keeper)
export(os.path.join(OUT, "game_boat.fbx"), boat)

with open(os.path.join(OUT, "keeper_report.txt"), "w") as f:
    f.write("\n".join(REPORT) + "\n")
print("[KEEPER] ALL DONE")
