# Scalability test scene builder — The Keeper's Ledger (Step 1 verify)
# Builds: storm island terrain + ocean + lighthouse + props. Exports FBX for UE import.
# Run: blender -b -P build_scal_island.py
import bpy, math, random, os
from mathutils import noise, Vector

random.seed(1337)
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets_blender")
OUT = os.path.abspath(OUT)
os.makedirs(OUT, exist_ok=True)

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras):
        for b in list(block):
            if b.users == 0:
                block.remove(b)

def mat(name, color, rough=0.9, metal=0.0, emit=0.0, emit_color=(1.0,0.75,0.4), glass=False):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes.get("Principled BSDF")
    bsdf.inputs["Base Color"].default_value = (*color, 1.0)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    if emit > 0.0:
        for key in ("Emission Color", "Emission"):
            if key in bsdf.inputs:
                bsdf.inputs[key].default_value = (*emit_color, 1.0)
                break
        if "Emission Strength" in bsdf.inputs:
            bsdf.inputs["Emission Strength"].default_value = emit
    if glass:
        for key in ("Transmission Weight", "Transmission"):
            if key in bsdf.inputs:
                bsdf.inputs[key].default_value = 1.0
                break
        bsdf.inputs["Roughness"].default_value = 0.05
    return m

def terrain_h(x, y):
    r = math.hypot(x, y)
    base = max(0.0, 1.0 - (r / 80.0)) ** 1.5
    n  = noise.noise(Vector((x * 0.05, y * 0.05, 0.0)))
    n2 = noise.noise(Vector((x * 0.15, y * 0.15, 7.3)))
    h = base * (6.0 + 4.0 * n + 1.5 * n2) - 1.2
    if r < 9.0:
        h = 2.0
    elif r < 12.0:
        t = (r - 9.0) / 3.0
        h = 2.0 * (1.0 - t) + h * t
    return h

def build_terrain():
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=200, y_subdivisions=200, size=240)
    obj = bpy.context.active_object
    obj.name = "IslandTerrain"
    for v in obj.data.vertices:
        v.co.z = terrain_h(v.co.x, v.co.y)
    obj.data.materials.append(mat("M_Rock", (0.28, 0.27, 0.24), rough=0.95))
    bpy.ops.object.shade_smooth()
    return obj

def build_ocean():
    bpy.ops.mesh.primitive_plane_add(size=900, location=(0, 0, -0.6))
    obj = bpy.context.active_object
    obj.name = "Ocean"
    obj.data.materials.append(mat("M_Ocean", (0.02, 0.07, 0.10), rough=0.25))
    return obj

def build_lighthouse():
    parts = []
    def cyl(name, r1, r2, depth, z, material, verts=32):
        if abs(r1 - r2) < 1e-6:
            bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r1,
                                                depth=depth, location=(0, 0, z))
        else:
            bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1, radius2=r2,
                                            depth=depth, location=(0, 0, z))
        o = bpy.context.active_object; o.name = name
        o.data.materials.append(material); parts.append(o); return o
    m_white = mat("M_TowerWhite", (0.75, 0.73, 0.68), rough=0.7)
    m_dark  = mat("M_TowerDark",  (0.10, 0.10, 0.11), rough=0.6)
    m_glass = mat("M_LampGlass",  (0.8, 0.85, 0.9), glass=True)
    m_lamp  = mat("M_LampCore",   (1.0, 0.85, 0.55), emit=8.0)
    cyl("LH_Base",    3.2, 3.2, 0.6, 2.3,  m_dark)
    cyl("LH_Tower",   2.6, 1.9, 16.0, 10.6, m_white)
    cyl("LH_Gallery", 2.7, 2.7, 0.35, 18.85, m_dark)
    cyl("LH_LampRoom",1.7, 1.7, 2.2, 20.2, m_glass)
    cyl("LH_LampCore",0.5, 0.5, 1.2, 20.2, m_lamp)
    bpy.ops.mesh.primitive_cone_add(radius1=1.9, radius2=0.08, depth=1.4, location=(0, 0, 22.0))
    roof = bpy.context.active_object; roof.name = "LH_Roof"
    roof.data.materials.append(m_dark); parts.append(roof)
    return parts

def build_props():
    parts = []
    # keeper cottage
    bpy.ops.mesh.primitive_cube_add(size=1, location=(20, 10, 3.0))
    c = bpy.context.active_object; c.name = "CottageBody"; c.scale = (4.0, 2.8, 1.6)
    c.data.materials.append(mat("M_Wood", (0.35, 0.24, 0.15), rough=0.85)); parts.append(c)
    bpy.ops.mesh.primitive_cube_add(size=1, location=(20, 10, 4.4))
    r = bpy.context.active_object; r.name = "CottageRoof"; r.scale = (4.3, 3.1, 0.25)
    r.data.materials.append(mat("M_Roof", (0.15, 0.14, 0.13))); parts.append(r)
    # rocks
    m_rock = mat("M_Rock2", (0.22, 0.21, 0.20), rough=0.98)
    for i in range(25):
        ang = random.uniform(0, 2 * math.pi)
        rad = random.uniform(15, 68)
        x, y = rad * math.cos(ang), rad * math.sin(ang)
        s = random.uniform(0.8, 3.5)
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=2, radius=s,
                                              location=(x, y, terrain_h(x, y) + s * 0.3))
        o = bpy.context.active_object; o.name = f"Rock_{i:02d}"
        o.rotation_euler = (random.uniform(0, 3), random.uniform(0, 3), random.uniform(0, 3))
        o.data.materials.append(m_rock); parts.append(o)
    # pier: deck + posts, from shore toward sea at angle 40deg
    m_pier = mat("M_PierWood", (0.30, 0.22, 0.13), rough=0.9)
    ang = math.radians(40)
    for i in range(8):
        d = 58 + i * 2.4
        x, y = d * math.cos(ang), d * math.sin(ang)
        bpy.ops.mesh.primitive_cube_add(size=1, location=(x, y, 0.9))
        seg = bpy.context.active_object; seg.name = f"PierDeck_{i}"
        seg.scale = (2.6, 1.2, 0.08); seg.rotation_euler = (0, 0, ang)
        seg.data.materials.append(m_pier); parts.append(seg)
        if i % 2 == 0:
            for side in (-1, 1):
                px, py = x + side * math.sin(ang) * 1.1, y - side * math.cos(ang) * 1.1
                bpy.ops.mesh.primitive_cylinder_add(radius=0.09, depth=2.2, location=(px, py, 0.2))
                post = bpy.context.active_object; post.name = f"PierPost_{i}_{side}"
                post.data.materials.append(m_pier); parts.append(post)
    # wrecks (3 hulls)
    m_rust = mat("M_Rust", (0.30, 0.16, 0.08), rough=0.95, metal=0.4)
    for i, (wx, wy, wrot) in enumerate([(55, -25, 0.7), (-48, 30, 2.1), (-30, -52, 4.0)]):
        bpy.ops.mesh.primitive_cube_add(size=1, location=(wx, wy, 0.3))
        hull = bpy.context.active_object; hull.name = f"WreckHull_{i}"
        hull.scale = (5.0, 1.8, 1.0); hull.rotation_euler = (0.12, 0.05, wrot)
        hull.data.materials.append(m_rust); parts.append(hull)
        bpy.ops.mesh.primitive_cylinder_add(radius=0.08, depth=6.0,
                                            location=(wx, wy, 2.2),
                                            rotation=(math.radians(15), 0, wrot))
        mast = bpy.context.active_object; mast.name = f"WreckMast_{i}"
        mast.data.materials.append(m_pier); parts.append(mast)
    return parts

def export(path, objs):
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs:
        o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.export_scene.fbx(filepath=path, use_selection=True, apply_unit_scale=True,
                             apply_scale_options='FBX_SCALE_NONE', object_types={'MESH'},
                             add_leaf_bones=False, bake_anim=False, mesh_smooth_type='OFF')
    print("[SCAL] exported", path, os.path.getsize(path), "bytes")

clear_scene()
terrain = build_terrain()
ocean = build_ocean()
lh = build_lighthouse()
props = build_props()
export(os.path.join(OUT, "env.fbx"), [terrain, ocean])
export(os.path.join(OUT, "lighthouse.fbx"), lh)
export(os.path.join(OUT, "props.fbx"), props)
print("[SCAL] DONE")
