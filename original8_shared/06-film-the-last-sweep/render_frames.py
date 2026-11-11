#!/usr/bin/env python3
"""FRAME ENGINE — 'The Last Sweep' (30s, 1280x720@30fps, 900 frames).
Every pixel from code: gradients, geometry, particle systems, noise fields.
Palette: ink #060a14 / cold blue #9fd4ff / warm gold #ffc46b (3 colors max).
Beats: B1 sweep 0-8 | B2 storm 8-16 | B3 dark 16-22.5 | B4 bloom 22.5-30.
Usage: python3 render_frames.py probe   -> renders 6 probe frames + stats
       python3 render_frames.py full    -> renders all 900 frames + stats.json
"""
import sys, os, math, json
sys.path.insert(0, 'C:/Users/agent/work/project/.venv/lib/python3.12/site-packages')
import numpy as np
from PIL import Image

W, H = 1280, 720
FPS = 30
DUR = 30.0
NF = int(round(DUR * FPS))  # 900
OUT = 'frames'
rng = np.random.default_rng(11)

INK  = np.array([6, 10, 20], np.float64)      # 1: ink night
BLUE = np.array([159, 212, 255], np.float64)  # 2: cold beam blue
GOLD = np.array([255, 196, 107], np.float64)  # 3: warm gold (B4 only)

HORIZON = 0.62 * H
LH_X = 0.78 * W
LAMP = np.array([LH_X, HORIZON - 0.30 * H])   # lamp point
BOAT0 = np.array([0.24 * W, 0.735 * H])

yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)

# ---------------- utils ----------------
def smooth01(x):
    x = np.clip(x, 0.0, 1.0)
    return x * x * (3 - 2 * x)

def seg(t, a, b):
    return smooth01((t - a) / max(1e-6, b - a))

def fnorm(t):
    """deterministic smoothed noise in [-1,1] from summed sines"""
    return (0.5 * math.sin(2.1 * t) + 0.3 * math.sin(3.7 * t + 1.3)
            + 0.2 * math.sin(5.3 * t + 2.1))

def angdiff(a, b):
    return np.abs(((a - b + math.pi) % (2 * math.pi)) - math.pi)

# ---------------- static scenery ----------------
def build_static():
    s = {}
    # sky gradient: darker top, slight lift toward horizon (ink family only)
    sky_s = 0.72 + 0.55 * smooth01(yy / HORIZON)
    sky = INK[None, None, :] * sky_s[..., None]
    # sea base: lighter near horizon, darker at bottom
    depth = smooth01((yy - HORIZON) / (H - HORIZON))
    sea_s = 0.92 - 0.45 * depth
    s['base'] = np.where((yy >= HORIZON)[..., None], INK[None, None, :] * sea_s[..., None], sky).astype(np.float32)
    # noise texture for sea (smoothed)
    tex = rng.random((H // 2 + 160, W // 2 + 160)).astype(np.float32)
    for _ in range(2):
        p = np.pad(tex, 1, mode='edge')
        tex = (p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
               p[1:-1, :-2] + p[1:-1, 1:-1] + p[1:-1, 2:] +
               p[2:, :-2] + p[2:, 1:-1] + p[2:, 2:]) / 9.0
    s['tex'] = tex
    # stars
    n = 70
    sx = rng.uniform(0, W, n); sy = rng.uniform(0, 0.52 * H, n)
    ph = rng.uniform(0, 2 * math.pi, n); sp = rng.uniform(0.4, 1.3, n)
    s['stars'] = (sx.astype(int), sy.astype(int), ph, sp)
    # rain drops
    n = 340
    rx = rng.uniform(0, W, n); ry = rng.uniform(0, H, n)
    rv = rng.uniform(380, 640, n); rl = rng.uniform(9, 16, n)
    s['rain'] = (rx, ry, rv, rl)
    return s

S = build_static()

# ---------------- lighthouse geometry ----------------
def lighthouse_mask():
    """dark silhouette mask + lamp room box"""
    m = np.zeros((H, W), bool)
    x0, x1 = int(LH_X - 40), int(LH_X + 40)
    y0, y1 = int(LAMP[1] - 14), int(HORIZON + 3)
    ys, xs = np.mgrid[y0:y1, x0:x1]
    # tower trapezoid: half-width 17 at base -> 9 at top
    hw = 17 + (ys - (HORIZON + 3)) / (LAMP[1] - 14 - (HORIZON + 3)) * (9 - 17)
    tower = np.abs(xs - LH_X) <= hw
    # lamp room: rect half-width 8, from LAMP[1]-12 to LAMP[1]+10
    lamp_room = (np.abs(xs - LH_X) <= 8) & (ys >= LAMP[1] - 12) & (ys <= LAMP[1] + 10)
    # cap: triangle above lamp room
    cap = (np.abs(xs - LH_X) <= (LAMP[1] - 2 - ys) * 0.9) & (ys < LAMP[1] - 2) & (ys > LAMP[1] - 14)
    m[y0:y1, x0:x1] = tower | lamp_room | cap
    return m

LH_MASK = lighthouse_mask()

# ---------------- boat geometry ----------------
def boat_mask(cx, cy, s=1.0):
    """hull triangle + mast; returns bool mask in small bbox"""
    pts = np.array([(-27, 9), (27, 9), (0, -11)], np.float32) * s
    m = np.zeros((H, W), bool)
    x0, x1 = int(cx - 30 * s), int(cx + 30 * s)
    y0, y1 = int(cy - 30 * s), int(cy + 12 * s)
    if x1 <= x0 or y1 <= y0:
        return m, (x0, x1, y0, y1)
    ys, xs = np.mgrid[y0:y1, x0:x1]
    px = xs - cx; py = ys - cy
    # barycentric of triangle pts
    (ax, ay), (bx, by), (cxx, cyy) = pts
    d = (by - cyy) * (ax - cx_) if False else None
    v0 = np.array([bx - ax, by - ay]); v1 = np.array([cx_ - ax, cyy - ay]) if False else None
    # simpler: half-plane tests (triangle convex, CCW)
    def hp(p, q, r):
        return (q[0] - p[0]) * (r[..., 1] - p[1]) - (q[1] - p[1]) * (r[..., 0] - p[0])
    P, Q, R = pts[0], pts[1], pts[2]
    pr = np.stack([px, py], axis=-1)
    d1 = hp(P, Q, pr); d2 = hp(Q, R, pr); d3 = hp(R, P, pr)
    neg = (d1 <= 0) & (d2 <= 0) & (d3 <= 0)
    pos = (d1 >= 0) & (d2 >= 0) & (d3 >= 0)
    hull = neg | pos
    # mast: thin vertical line from (0,-11) to (0,-26)
    mast = (np.abs(px) <= 1.2) & (py >= -26 * s) & (py <= -11 * s)
    m[y0:y1, x0:x1] = hull | mast
    return m, (x0, x1, y0, y1)

cx_ = None  # placeholder to avoid NameError in dead branch

def hull_edge_mask(cx, cy, s=1.0):
    """outline pixels of the hull for rim light"""
    m, _ = boat_mask(cx, cy, s)
    inner, _ = boat_mask(cx, cy, s * 0.78)
    return m & ~inner

# ---------------- per-frame render ----------------
def lamp_gain(t):
    alive = 1 - seg(t, 16.2, 17.4)
    storm, _, _, _ = envs(t)
    flick = 1 - 0.38 * max(0.0, fnorm(t * 2.3)) * storm
    # dying flickers 16.2-17.4
    if 16.0 < t < 17.6:
        u = (t - 16.0) / 1.6
        flick *= max(0.0, 0.35 + 0.65 * abs(math.sin(u * math.pi * 3)) * (1 - u))
    return alive * flick

def envs(t):
    storm = seg(t, 8, 11.5) * (1 - seg(t, 21, 24.5))
    bloom = seg(t, 22.5, 25.2)
    boat_beam = seg(t, 24.6, 26.4)
    still = seg(t, 18.8, 20.0) * (1 - seg(t, 22.5, 23.6))
    return storm, bloom, boat_beam, still

def lamp_angle(t):
    base = math.radians(187)
    sweep = math.radians(24) * math.sin(2 * math.pi * t / 6.0)
    storm, _, _, _ = envs(t)
    sweep += math.radians(11) * fnorm(t * 1.6) * storm
    return base + sweep

def boat_pos(t):
    storm, bloom, _, still = envs(t)
    drift = 0.045 * W * ease_full(t / DUR)
    bobA = (3.0 + 4.5 * storm) * (1 - 0.72 * still)
    x = BOAT0[0] + drift
    y = BOAT0[1] + bobA * math.sin(2 * math.pi * 0.45 * t) + 0.012 * H * ease_full(t / DUR)
    return x, y

def ease_full(u):
    u = min(max(u, 0.0), 1.0)
    return u * u * (3 - 2 * u)

def wedge(srcx, srcy, theta, width_rad, gain, dist_fall=950.0):
    dx = xx - srcx; dy = yy - srcy
    dist = np.hypot(dx, dy)
    ang = np.arctan2(dy, dx)
    d = angdiff(ang, theta)
    core = smooth01(1 - d / width_rad)
    fall = np.exp(-dist / dist_fall) * smooth01(dist / 30.0)
    return gain * core * fall

def render_frame(i):
    t = i / FPS
    storm, bloom, boat_beam, still = envs(t)
    lg = lamp_gain(t)
    canvas = S['base'].copy()

    # ---- stars ----
    star_g = (1 - 0.85 * storm) * (1 - 0.35 * bloom)
    sx, sy, ph, sp = S['stars']
    tw = 0.5 + 0.5 * np.sin(ph + t * sp * 2 * math.pi * 0.2)
    a = (0.10 + 0.22 * tw) * star_g
    canvas[sy.astype(int), sx.astype(int)] += BLUE[None, :] * a[:, None]

    # ---- lamp glow + beam (B1-B3) ----
    if lg > 0.003:
        dxl = xx - LAMP[0]; dyl = yy - LAMP[1]
        distl = np.hypot(dxl, dyl)
        glow = np.exp(-distl / 26.0) * 1.5 + np.exp(-distl / 90.0) * 0.35
        canvas += BLUE[None, None, :] * (glow * lg)[..., None]
        th = lamp_angle(t)
        beam = wedge(LAMP[0], LAMP[1], th, math.radians(7.5), 0.85 * lg)
        canvas += BLUE[None, None, :] * beam[..., None]
        # sea glint alignment under beam
        # boat glimmer when beam points at it
        bx, by = boat_pos(t)
        ang_to_boat = math.atan2(by - LAMP[1], bx - LAMP[0])
        align = math.exp(-((angdiff(np.array(ang_to_boat), th) ** 2)) / (math.radians(6) ** 2))
        rim_g = align * lg

    # ---- lighthouse silhouette ----
    canvas[LH_MASK] *= 0.30
    # faint cold rim on tower seaward edge (left side) while lamp alive
    if lg > 0.003:
        rim = LH_MASK & (np.abs(xx - (LH_X - 17)) < 2.2) & (yy > LAMP[1] + 8) & (yy < HORIZON)
        canvas[rim] += BLUE[None, :] * (0.25 * lg)

    # ---- sea: noise glints ----
    tex = S['tex']
    scroll = int((t * 14) % 64)
    amp = (0.35 + 1.5 * storm + 0.25 * bloom) * (1 - 0.6 * still)
    ty = ((yy - HORIZON) * 0.5 + 40 + scroll * 0.4).astype(int) % (tex.shape[0] - 1)
    txf = (xx * 0.5 + t * 11.0)
    txi = txf.astype(int) % (tex.shape[1] - 1)
    fr = (txf - np.floor(txf))[..., None] if False else (txf - np.floor(txf))
    n = tex[ty, txi] * (1 - fr) + tex[ty, np.minimum(txi + 1, tex.shape[1] - 1)] * fr
    glint = smooth01(n - (0.86 - 0.10 * storm)) * amp
    rowfall = smooth01(1 - (yy - HORIZON) / (H - HORIZON) * 1.15)
    sea_light = np.clip(glint * rowfall, 0, 1) * (0.16 + 0.10 * storm)
    sea_mask = yy >= HORIZON
    canvas[sea_mask] += BLUE[None, :] * sea_light[..., None][sea_mask]

    # ---- reflection streak under active light ----
    if lg > 0.003:
        lsx = LAMP[0]
        ref = np.exp(-((xx - lsx) ** 2) / (2 * 11 ** 2)) * smooth01((yy - HORIZON) / 30) \
              * (1 - smooth01((yy - HORIZON - 150) / 120))
        ref *= lg * (0.5 + 0.3 * np.sin(2.1 * (t * 3.1 + yy * 0.02)))
        canvas[sea_mask] += BLUE[None, :] * (ref * 0.5)[..., None][sea_mask]

    # ---- rain ----
    rain_g = storm * (1 - seg(t, 22.0, 25.0)) * (1 - 0.85 * seg(t, 18.5, 20.5))
    if rain_g > 0.01:
        rx, ry, rv, rl = S['rain']
        layer = np.zeros((H, W), np.float32)
        pyy = (ry + rv * t) % (H + 20) - 10
        pxx = (rx - 26 * t) % W
        for k in range(len(rx)):
            x0 = int(pxx[k]); y0 = int(pyy[k]); L = int(rl[k])
            if 0 <= x0 < W - 2 and 0 <= y0 < H - L:
                layer[y0:y0 + L, x0] += 0.16
                layer[y0:y0 + L, x0 + 1] += 0.08
        canvas += BLUE[None, None, :] * (layer * rain_g)[..., None]

    # ---- boat ----
    bx, by = boat_pos(t)
    bm, bbox = boat_mask(bx, by, 1.0)
    # hull silhouette
    canvas[bm] *= 0.34
    # rim light from lamp beam (glimmer) in B1/B2
    if lg > 0.003:
        em = hull_edge_mask(bx, by, 1.0)
        canvas[em] += BLUE[None, :] * (0.55 * rim_g)
    # B4: warm bloom from within the hull
    if bloom > 0.001:
        dxb = xx - bx; dyb = yy - by
        distb = np.hypot(dxb, dyb)
        rad = 16 + 95 * bloom
        g = np.exp(-distb / rad) * (0.55 + 1.5 * bloom)
        canvas += GOLD[None, None, :] * g[..., None]
        # hull interior glows brightest
        canvas[bm] += GOLD[None, :] * (1.15 * bloom)
        # reflection under boat, warm
        if by < HORIZON + 60:
            refb = np.exp(-((xx - bx) ** 2) / (2 * 9 ** 2)) * smooth01((yy - by + 6) / 24) \
                   * (1 - smooth01((yy - by - 90) / 80))
            canvas[sea_mask] += GOLD[None, :] * (refb * 0.8 * bloom)[..., None][sea_mask]
    # B4: boat beam (same wedge geometry as the lamp, warm)
    if boat_beam > 0.001:
        th_b = math.radians(335 + 20 * math.sin(2 * math.pi * (t - 24.6) / 6.0))
        beam_b = wedge(bx, by, th_b, math.radians(7.5), 0.8 * boat_beam, dist_fall=1050)
        canvas += GOLD[None, None, :] * beam_b[..., None]
        # warm rim on old lighthouse when beam sweeps it (memory touch)
        ang_to_lh = math.atan2(LAMP[1] - by, LAMP[0] - bx)
        al = math.exp(-((angdiff(np.array(ang_to_lh), th_b) ** 2)) / (math.radians(6) ** 2))
        rim2 = LH_MASK & (np.abs(xx - (LH_X - 17)) < 2.2) & (yy > LAMP[1] + 8) & (yy < HORIZON + 2)
        canvas[rim2] += GOLD[None, :] * (0.5 * al * boat_beam)

    # ---- second tiny boat on horizon (B4 end) ----
    if t > 26.2:
        u = ease_full((t - 26.2) / 3.8)
        sx2 = 0.62 * W - u * (0.10 * W)
        sy2 = HORIZON - 2
        bm2, bb2 = boat_mask(sx2, sy2, 0.42)
        canvas[bm2] *= 0.30
        if boat_beam > 0.001:
            em2 = hull_edge_mask(sx2, sy2, 0.42)
            canvas[em2] += GOLD[None, :] * (0.7 * boat_beam)

    # ---- vignette ----
    dxv = (xx - W / 2) / (W / 2); dyv = (yy - H / 2) / (H / 2)
    r2 = dxv * dxv + dyv * dyv
    canvas *= (1 - 0.22 * smooth01((r2 - 0.35) / 0.65))[..., None]

    # ---- tonemap (canvas is 0-255 scale) ----
    out = 1 - np.exp(-2.2 * canvas / 255.0)
    out = np.clip(out, 0, 1)
    return (out * 255).astype(np.uint8)

# ---------------- stats ----------------
def frame_stats(img, prev_lum):
    f = img.astype(np.float32)
    lum = f.mean(axis=2)
    warm = ((f[..., 0] > f[..., 2] * 1.12) & (f[..., 0] > 55)).mean()
    beamzone = lum[:int(HORIZON), :].mean()
    sea = lum[int(HORIZON):, :].mean()
    motion = float(np.abs(lum[::4, ::4] - prev_lum).mean()) if prev_lum is not None else 0.0
    return dict(lum=float(lum.mean()), warm=float(warm), sky=float(beamzone),
                sea=float(sea), motion=motion), lum[::4, ::4]

def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'probe'
    os.makedirs(OUT, exist_ok=True)
    probes = [30, 270, 300, 495, 540, 630, 660, 705, 750, 795, 840, 870]
    stats = []
    prev = None
    rng_frames = probes if mode == 'probe' else range(NF)
    for i in rng_frames:
        img = render_frame(i)
        st, prev = frame_stats(img, prev)
        st['frame'] = i; st['t'] = round(i / FPS, 2)
        stats.append(st)
        Image.fromarray(img).save(f'{OUT}/f{i:05d}.png', compress_level=1)
        if mode == 'full' and i % 150 == 0:
            print(f'frame {i}/{NF}', flush=True)
    with open('frames_stats.json', 'w') as fh:
        json.dump(stats, fh)
    for st in stats:
        print(st)

if __name__ == '__main__':
    main()
