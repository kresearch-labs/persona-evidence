# THE KEEPER'S LEDGER — full game environment (Step 3)
# Island (5 regions per SPEC_LOCK 5), lighthouse ext+int, all props.
# Run: blender -b -P build_game_env.py
import bpy, math, os, random
from mathutils import noise, Vector

random.seed(20261020)
OUT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets_blender"))
os.makedirs(OUT, exist_ok=True)
REPORT = []

def note(m): REPORT.append(m); print("[ENV]", m)

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)
    for block in (bpy.data.meshes, bpy.data.materials, bpy.data.lights, bpy.data.cameras):
        for b in list(block):
            if b.users == 0: block.remove(b)

_mcache = {}
def mat(name, color, rough=0.9, metal=0.0, emit=0.0, emit_color=(1.0,0.75,0.4), glass=False):
    key = name
    if key in _mcache: return _mcache[key]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get("Principled BSDF")
    b.inputs["Base Color"].default_value = (*color, 1.0)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    if emit > 0:
        for k in ("Emission Color", "Emission"):
            if k in b.inputs: b.inputs[k].default_value = (*emit_color, 1.0); break
        if "Emission Strength" in b.inputs: b.inputs["Emission Strength"].default_value = emit
    if glass:
        for k in ("Transmission Weight", "Transmission"):
            if k in b.inputs: b.inputs[k].default_value = 1.0; break
        b.inputs["Roughness"].default_value = 0.05
    _mcache[key] = m
    return m

def cyl(name, r, depth, loc, material, verts=24, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name; o.data.materials.append(material)
    return o

def cone(name, r1, r2, depth, loc, material, verts=24, rot=(0,0,0)):
    bpy.ops.mesh.primitive_cone_add(vertices=verts, radius1=r1, radius2=r2, depth=depth, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name; o.data.materials.append(material)
    return o

def cube(name, size, loc, material, scale=(1,1,1), rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(size=size, location=loc, rotation=rot)
    o = bpy.context.active_object; o.name = name; o.scale = scale
    o.data.materials.append(material)
    return o

def sphere(name, r, loc, material, subdiv=2):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=subdiv, radius=r, location=loc)
    o = bpy.context.active_object; o.name = name; o.data.materials.append(material)
    return o

# ============ TERRAIN: 5 regions (SPEC_LOCK 5) ============
# Lighthouse Point center-south high; Cottage Row east; Wreck Shore west;
# Old Landing north (pier+chart house); Back Hills south.
def terrain_h(x, y):
    r = math.hypot(x, y)
    base = max(0.0, 1.0 - (r / 110.0)) ** 1.4
    n  = noise.noise(Vector((x*0.045, y*0.045, 0.0)))
    n2 = noise.noise(Vector((x*0.14,  y*0.14,  7.3)))
    n3 = noise.noise(Vector((x*0.30,  y*0.30,  13.1)))
    h = base * (7.0 + 4.5*n + 1.6*n2 + 0.5*n3) - 1.4
    # Lighthouse Point: hill at (0,-20) up to 8m
    d = math.hypot(x-0, y+20)
    h += max(0.0, 1.0 - d/26.0)**2 * 6.0
    if d < 7.0: h = 8.0  # tower pad
    # Back Hills: rolling south
    d2 = math.hypot(x-10, y+55)
    h += max(0.0, 1.0 - d2/40.0)**1.5 * 3.5
    # Cottage Row: gentle shelf east
    d3 = math.hypot(x-38, y-8)
    h = max(h, (max(0.0, 1.0-d3/22.0)**1.2 * 3.2) + 0.4)
    # Wreck Shore: low west beach
    d4 = math.hypot(x+45, y-5)
    h -= max(0.0, 1.0-d4/30.0)**1.3 * 2.2
    # Old Landing: flat north pier area
    d5 = math.hypot(x-5, y-52)
    h = max(h, (max(0.0, 1.0-d5/20.0)**1.1 * 2.2) + 0.2)
    # path smoothing along main route (lighthouse->landing->cottage->shore)
    for (px,py,pr) in [(0,-12,3.5),(0,0,3.5),(2,18,3.5),(4,36,3.5),(5,50,3.5),
                       (14,-6,3.0),(28,-7,3.0),(38,-8,3.0),
                       (-16,-8,3.0),(-32,-6,3.0),(-45,-5,3.0),
                       (6,-34,2.8),(9,-46,2.8)]:
        dp = math.hypot(x-px, y-py)
        if dp < pr:
            t = dp/pr
            h = h*(t) + (h+0.15)*(1-t)  # slightly raised, smoothed
    return h

def build_terrain():
    bpy.ops.mesh.primitive_grid_add(x_subdivisions=220, y_subdivisions=220, size=300)
    o = bpy.context.active_object; o.name = "IslandTerrain"
    for v in o.data.vertices:
        v.co.z = terrain_h(v.co.x, v.co.y)
    o.data.materials.append(mat("M_Ground", (0.23,0.24,0.18), rough=0.95))
    bpy.ops.object.shade_smooth()
    note("terrain done")
    return o

def build_ocean():
    o = cube("Ocean", 1, (0,0,-0.9), mat("M_Ocean", (0.02,0.06,0.09), rough=0.2), scale=(700,700,0.5))
    return o

# ============ LIGHTHOUSE (ext + int) ============
def build_lighthouse():
    parts = []
    m_white = mat("M_TowerWhite", (0.72,0.70,0.66), rough=0.65)
    m_dark  = mat("M_TowerDark", (0.09,0.09,0.10), rough=0.6)
    m_glass = mat("M_LampGlass", (0.75,0.82,0.88), glass=True)
    m_lamp  = mat("M_LampCore", (1.0,0.82,0.5), emit=10.0)
    m_brass = mat("M_Brass", (0.65,0.5,0.25), rough=0.35, metal=0.8)
    m_wood  = mat("M_Wood", (0.32,0.22,0.13), rough=0.85)
    m_stone = mat("M_Stone", (0.30,0.29,0.27), rough=0.95)
    # exterior
    parts.append(cyl("LH_Base", 3.4, 0.8, (0,-20,8.4), m_stone))
    parts.append(cone("LH_Tower", 2.7, 2.0, 15.0, (0,-20,16.3), m_white))
    parts.append(cyl("LH_Gallery", 2.9, 0.35, (0,-20,24.0), m_dark))
    for i in range(14):  # gallery railing
        a = i/14.0*2*math.pi
        parts.append(cyl(f"LH_Rail_{i}", 0.045, 1.0, (2.75*math.cos(a), -20+2.75*math.sin(a), 24.7), m_dark, verts=8))
    parts.append(cyl("LH_LampRoom", 1.8, 2.4, (0,-20,25.4), m_glass, verts=32))
    for i in range(8):  # glazing bars
        a = i/8.0*2*math.pi
        parts.append(cyl(f"LH_Bar_{i}", 0.05, 2.4, (1.75*math.cos(a), -20+1.75*math.sin(a), 25.4), m_dark, verts=8))
    parts.append(cyl("LH_LampCore", 0.55, 1.3, (0,-20,25.3), m_lamp, verts=16))
    parts.append(cone("LH_Roof", 1.95, 0.06, 1.5, (0,-20,27.3), m_dark))
    # door
    parts.append(cube("LH_Door", 1, (0,-17.35,9.3), m_wood, scale=(1.1,0.15,2.2)))
    # interior: spiral stair + landings (inside tower, y=-20)
    z = 9.0
    step_i = 0
    while z < 23.6:
        a = step_i * 0.42
        r_in = 0.9
        x = r_in*math.cos(a); y = -20 + r_in*math.sin(a)
        s = cube(f"LH_Step_{step_i}", 1, (x,y,z), m_wood, scale=(0.85,0.32,0.06), rot=(0,0,a))
        parts.append(s)
        z += 0.31; step_i += 1
    note("stair steps=%d" % step_i)
    # landings at 3 heights (keeper room, mid, lamp)
    parts.append(cyl("LH_Floor_Keeper", 2.4, 0.25, (0,-20,12.6), m_wood, verts=32))
    parts.append(cyl("LH_Floor_Mid", 2.3, 0.22, (0,-20,18.4), m_wood, verts=32))
    parts.append(cyl("LH_Floor_Lamp", 1.9, 0.3, (0,-20,24.2), m_wood, verts=32))
    # keeper room furniture (on 12.6 floor)
    parts.append(cube("LH_LogDesk", 1, (1.2,-21.6,13.35), m_wood, scale=(1.5,0.8,0.1)))
    for dx in (-0.9,0.9):
        parts.append(cyl(f"LH_DeskLeg_{dx}", 0.06, 0.75, (1.2+dx,-21.6,12.97), m_wood, verts=8))
    parts.append(cube("LH_Bed", 1, (-1.3,-18.8,13.15), m_wood, scale=(1.1,2.2,0.35)))
    parts.append(cube("LH_BedMattress", 1, (-1.3,-18.8,13.45), mat("M_Cloth",(0.45,0.42,0.36)), scale=(1.0,2.0,0.22)))
    parts.append(cyl("LH_OilTank", 0.75, 1.5, (1.6,-18.6,13.6), m_brass, verts=20))
    parts.append(cyl("LH_TankGauge", 0.09, 0.06, (1.6,-17.82,13.9), mat("M_Gauge",(0.85,0.83,0.75),emit=0.4), verts=12, rot=(math.pi/2,0,0)))
    # lens assembly (lamp floor 24.2): pedestal + lens drum
    parts.append(cyl("LH_LensPedestal", 0.5, 0.9, (0,-20,24.8), m_brass, verts=16))
    parts.append(cyl("LH_LensDrum", 0.95, 1.5, (0,-20,25.7), m_glass, verts=32))
    parts.append(cyl("LH_LensCore", 0.4, 1.1, (0,-20,25.7), m_lamp, verts=16))
    parts.append(cyl("LH_LensRing_Top", 1.0, 0.08, (0,-20,26.5), m_brass, verts=32))
    parts.append(cyl("LH_LensRing_Bot", 1.0, 0.08, (0,-20,24.95), m_brass, verts=32))
    # wick mechanism + clockwork (visible wear target)
    parts.append(cyl("LH_Clockwork", 0.35, 0.5, (0.8,-20.9,24.75), m_brass, verts=16))
    parts.append(cyl("LH_WickFeed", 0.12, 0.8, (0.45,-20.45,25.2), m_brass, verts=10, rot=(0,math.pi/2.6,0)))
    note("lighthouse done (%d parts)" % len(parts))
    return parts

# ============ BUILDINGS ============
def build_buildings():
    parts = []
    m_wood  = mat("M_Wood", (0.32,0.22,0.13), rough=0.85)
    m_wood2 = mat("M_WoodDark", (0.22,0.15,0.09), rough=0.9)
    m_roof  = mat("M_Roof", (0.14,0.13,0.12), rough=0.8)
    m_stone = mat("M_Stone", (0.30,0.29,0.27), rough=0.95)
    # Cottage (Cottage Row east, at ~(38,-8), terrain ~3.2)
    cx, cy = 38, -8
    cz = terrain_h(cx, cy)
    parts.append(cube("Cottage_Body", 1, (cx,cy,cz+1.5), m_wood, scale=(4.2,3.0,1.5)))
    parts.append(cone("Cottage_Roof", 3.6, 0.1, 1.6, (cx,cy,cz+3.05), m_roof, verts=4, rot=(0,0,math.pi/4)))
    parts.append(cube("Cottage_Door", 1, (cx,cy-3.02,cz+1.1), m_wood2, scale=(0.9,0.1,2.0)))
    parts.append(cube("Cottage_Window", 1, (cx-2.0,cy-3.02,cz+1.6), mat("M_WindowGlass",(0.6,0.7,0.75),emit=0.8), scale=(1.0,0.08,0.9)))
    parts.append(cyl("Cottage_Chimney", 0.35, 1.8, (cx+1.4,cy+0.8,cz+3.6), m_stone, verts=12))
    # Supply shed
    sx, sy = 33, -2
    sz = terrain_h(sx,sy)
    parts.append(cube("Shed_Body", 1, (sx,sy,sz+1.0), m_wood2, scale=(2.2,1.8,1.0)))
    parts.append(cone("Shed_Roof", 1.9, 0.08, 0.7, (sx,sy,sz+1.85), m_roof, verts=4, rot=(0,0,math.pi/4)))
    parts.append(cube("Shed_Door", 1, (sx,sy-1.82,sz+0.8), m_wood, scale=(0.8,0.08,1.5)))
    # Chart house (Old Landing north, ~(8,48))
    hx, hy = 8, 48
    hz = terrain_h(hx,hy)
    parts.append(cube("ChartHouse_Body", 1, (hx,hy,hz+1.4), m_wood, scale=(3.2,2.4,1.4)))
    parts.append(cone("ChartHouse_Roof", 2.8, 0.1, 1.2, (hx,hy,hz+2.7), m_roof, verts=4, rot=(0,0,math.pi/4)))
    parts.append(cube("ChartHouse_Door", 1, (hx,hy-2.42,hz+1.0), m_wood2, scale=(0.9,0.1,1.9)))
    parts.append(cube("ChartHouse_Window", 1, (hx+1.6,hy-2.42,hz+1.5), mat("M_WindowGlass",(0.6,0.7,0.75),emit=0.8), scale=(0.9,0.08,0.8)))
    # chart table inside (visible through door)
    parts.append(cube("ChartHouse_Table", 1, (hx,hy+0.3,hz+0.85), m_wood2, scale=(1.8,0.9,0.08)))
    # Signal post (cottage row)
    px, py = 36, -14
    pz = terrain_h(px,py)
    parts.append(cyl("SignalPost", 0.09, 4.5, (px,py,pz+2.25), m_wood2, verts=10))
    parts.append(cube("SignalYard", 1, (px,py,pz+4.2), m_wood2, scale=(1.4,0.08,0.08)))
    # Salvage bench (Wreck Shore west)
    bx, by = -42, -3
    bz = terrain_h(bx,by)
    parts.append(cube("SalvageBench_Top", 1, (bx,by,bz+0.85), m_wood, scale=(2.0,0.9,0.09)))
    for dx in (-0.8,0.8):
        parts.append(cyl(f"SalvageBench_Leg_{dx}", 0.07, 0.8, (bx+dx,by,bz+0.42), m_wood2, verts=8))
    parts.append(cube("SalvageBench_Vise", 1, (bx+0.7,by,bz+1.0), mat("M_Iron",(0.2,0.2,0.22),rough=0.5,metal=0.7), scale=(0.25,0.3,0.3)))
    note("buildings done (%d parts)" % len(parts))
    return parts

# ============ PIER (Old Landing) ============
def build_pier():
    parts = []
    m_pier = mat("M_PierWood", (0.28,0.20,0.12), rough=0.9)
    ang = math.radians(188)  # pointing north-ish into sea from landing
    x0, y0 = 5, 56
    for i in range(14):
        d = i * 2.2
        x = x0 + d*math.cos(ang); y = y0 + d*math.sin(ang)
        z = 1.1 if i < 10 else 1.1
        parts.append(cube(f"Pier_Deck_{i}", 1, (x,y,z), m_pier, scale=(2.4,2.3,0.09), rot=(0,0,ang)))
        if i % 2 == 0:
            for side in (-1,1):
                ox = side*math.sin(ang)*1.05; oy = -side*math.cos(ang)*1.05
                parts.append(cyl(f"Pier_Post_{i}_{side}", 0.09, 2.4, (x+ox,y+oy,z-1.1), m_pier, verts=8))
    # boat moored at pier end
    bx = x0 + 30*math.cos(ang); by = y0 + 30*math.sin(ang)
    parts.append(cube("MooringPost", 1, (x0+28*math.cos(ang), y0+28*math.sin(ang), 1.5), mat("M_Iron",(0.2,0.2,0.22),metal=0.7), scale=(0.15,0.15,0.8)))
    note("pier done (%d parts)" % len(parts))
    return parts, (bx, by)

# ============ ROCKS / CLIFFS / DRIFTWOOD ============
def build_nature():
    parts = []
    m_rock = mat("M_Rock", (0.21,0.20,0.19), rough=0.98)
    m_rock2 = mat("M_RockWet", (0.16,0.16,0.16), rough=0.75)
    m_wood = mat("M_Driftwood", (0.35,0.28,0.20), rough=0.95)
    # cliff ring rocks + scattered
    for i in range(60):
        a = random.uniform(0, 2*math.pi)
        rad = random.uniform(20, 95)
        x, y = rad*math.cos(a), rad*math.sin(a)
        if terrain_h(x,y) < -0.5:  # only in water/shore
            s = random.uniform(1.0, 4.5)
            parts.append(sphere(f"Rock_{i:02d}", s, (x,y,terrain_h(x,y)+s*0.25), m_rock2 if terrain_h(x,y)<0 else m_rock))
    for i in range(30):
        a = random.uniform(0, 2*math.pi)
        rad = random.uniform(14, 80)
        x, y = rad*math.cos(a), rad*math.sin(a)
        h = terrain_h(x,y)
        if h > 0.2:
            s = random.uniform(0.5, 2.2)
            parts.append(sphere(f"RockIn_{i:02d}", s, (x,y,h+s*0.3), m_rock))
    # driftwood on wreck shore
    for i in range(12):
        x = random.uniform(-52,-34); y = random.uniform(-16,10)
        h = terrain_h(x,y)
        if h > 0.1:
            parts.append(cube(f"Driftwood_{i:02d}", 1, (x,y,h+0.12), m_wood, scale=(random.uniform(1.5,3.5),0.18,0.14), rot=(0,random.uniform(-0.1,0.1),random.uniform(0,3.1))))
    note("nature done (%d parts)" % len(parts))
    return parts

# ============ WRECKS (3 initial hulls, Wreck Shore) ============
def build_wrecks():
    parts = []
    m_rust = mat("M_Rust", (0.28,0.15,0.07), rough=0.95, metal=0.4)
    m_wood = mat("M_WoodWet", (0.24,0.17,0.10), rough=0.9)
    for i,(wx,wy,wrot) in enumerate([(-48,-14,0.7),(-44,4,2.4),(-52,-2,4.1)]):
        h = terrain_h(wx,wy)
        parts.append(cube(f"Wreck_Hull_{i}", 1, (wx,wy,h+0.5), m_wood if i%2 else m_rust, scale=(4.5,1.7,0.9), rot=(0.10,0.04,wrot)))
        parts.append(cube(f"Wreck_Rib_{i}_a", 1, (wx-1.2,wy,h+1.1), m_wood, scale=(0.15,1.5,0.7), rot=(0,0,wrot)))
        parts.append(cube(f"Wreck_Rib_{i}_b", 1, (wx+1.2,wy,h+1.0), m_wood, scale=(0.15,1.4,0.5), rot=(0,0,wrot)))
        parts.append(cyl(f"Wreck_Mast_{i}", 0.09, 5.5, (wx,wy,h+2.4), m_wood, verts=8, rot=(math.radians(18),0,wrot)))
    note("wrecks done (%d parts)" % len(parts))
    return parts

# ============ BACK HILLS TRACE SITES (5 markers, subtle) ============
def build_trace_sites():
    parts = []
    m_rust = mat("M_RustOld", (0.30,0.18,0.09), rough=0.95, metal=0.3)
    m_cloth = mat("M_ClothOld", (0.4,0.36,0.30), rough=0.95)
    sites = [(14,-38,"Trace_Lantern"), (2,-52,"Trace_Ledger"), (22,-50,"Trace_Note"),
             (-6,-44,"Trace_Lantern2"), (10,-60,"Trace_Boots")]
    for i,(x,y,nm) in enumerate(sites):
        h = terrain_h(x,y)
        if nm.endswith("Lantern") or nm.endswith("Lantern2"):
            parts.append(cyl(nm, 0.16, 0.42, (x,y,h+0.21), m_rust, verts=10))
            parts.append(cyl(nm+"_Glass", 0.11, 0.22, (x,y,h+0.30), mat("M_LanternGlass",(0.8,0.7,0.45),emit=0.25), verts=10))
        elif nm == "Trace_Ledger":
            parts.append(cube(nm, 1, (x,y,h+0.06), m_cloth, scale=(0.42,0.30,0.09), rot=(0,0,0.4)))
        elif nm == "Trace_Note":
            parts.append(cube(nm, 1, (x,y,h+0.02), mat("M_Paper",(0.75,0.72,0.62)), scale=(0.30,0.22,0.015), rot=(0,0,1.2)))
        else:
            for dx in (-0.12,0.12):
                parts.append(cube(nm+f"_{dx}", 1, (x+dx,y,h+0.10), m_cloth, scale=(0.14,0.30,0.18)))
    note("trace sites done (%d parts)" % len(parts))
    return parts

# ============ PATH MARKERS (erosion system anchors, subtle stones) ============
def build_pathstones():
    parts = []
    m_stone = mat("M_PathStone", (0.34,0.33,0.30), rough=0.95)
    route = [(0,-12),(0,0),(2,18),(4,36),(5,50),(14,-6),(28,-7),(38,-8),(-16,-8),(-32,-6),(-45,-5),(6,-34),(9,-46)]
    for i,(x,y) in enumerate(route):
        h = terrain_h(x,y)
        for j in range(3):
            ox, oy = random.uniform(-2,2), random.uniform(-2,2)
            parts.append(sphere(f"PathStone_{i}_{j}", random.uniform(0.15,0.3), (x+ox,y+oy,terrain_h(x+ox,y+oy)+0.08), m_stone, subdiv=1))
    note("pathstones done (%d parts)" % len(parts))
    return parts

def export(path, objs):
    objs = [o for o in objs if o and o.name in bpy.data.objects]
    bpy.ops.object.select_all(action='DESELECT')
    for o in objs: o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.export_scene.fbx(filepath=path, use_selection=True, apply_unit_scale=True,
                             apply_scale_options='FBX_SCALE_NONE', object_types={'MESH'},
                             add_leaf_bones=False, bake_anim=False, mesh_smooth_type='OFF')
    note("exported %s (%d objs, %d bytes)" % (os.path.basename(path), len(objs), os.path.getsize(path)))

clear_scene()
terrain = build_terrain()
ocean = build_ocean()
lh = build_lighthouse()
bld = build_buildings()
pier, boat_pos = build_pier()
nat = build_nature()
wrk = build_wrecks()
trc = build_trace_sites()
pst = build_pathstones()

export(os.path.join(OUT, "game_env.fbx"), [terrain, ocean])
export(os.path.join(OUT, "game_lighthouse.fbx"), lh)
export(os.path.join(OUT, "game_buildings.fbx"), bld)
export(os.path.join(OUT, "game_pier.fbx"), pier)
export(os.path.join(OUT, "game_nature.fbx"), nat)
export(os.path.join(OUT, "game_wrecks.fbx"), wrk)
export(os.path.join(OUT, "game_traces.fbx"), trc)
export(os.path.join(OUT, "game_pathstones.fbx"), pst)

with open(os.path.join(OUT, "env_report.txt"), "w") as f:
    f.write("\n".join(REPORT) + "\n")
print("[ENV] ALL DONE")
