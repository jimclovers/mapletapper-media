"""Vector illustration helpers for the MapleTapper Instagram series.

All shapes are emitted as SVG markup that is safe for the Design canvas:
every element is explicitly closed, attributes are quoted, and any
hyphenated presentation property goes in a style attribute.
"""
import math
import random

# MapleTapper palette (pulled from the brand's own artwork: logo, pins, kit infographics)
C = {
    "maroon": "#7A1E1A",
    "maroon_dk": "#5A1411",
    "red": "#C8321F",
    "red_dk": "#9E2416",
    "orange": "#E8622C",
    "amber": "#F08A24",
    "gold": "#F4B63F",
    "gold_lt": "#FFD47E",
    "cream": "#FFF5DE",
    "sky": "#9BD1F0",
    "sky_dk": "#6FB6E3",
    "bark": "#6E5A4E",
    "bark_dk": "#4E3E35",
    "bark_lt": "#8C7768",
    "gray": "#8F8E89",
    "gray_dk": "#55534F",
    "gray_lt": "#B9B7B0",
    "tan": "#D9A55B",
    "tan_dk": "#A8743A",
}


def f(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")


def pol(r, deg, s, cx, cy):
    a = math.radians(deg)
    return (cx + r * s * math.sin(a), cy - r * s * math.cos(a))


def _norm(v):
    l = math.hypot(*v)
    return (v[0] / l, v[1] / l) if l else (0.0, 0.0)


# Leaf specs: right half, from the top tip (theta 0) down to the base (theta 180).
# kind: tip | tooth | sU (rounded U sinus) | sV (sharp V sinus) | base
SUGAR = [
    (0, 1.00, "tip"),
    (9, 0.86, "tooth"),
    (13, 0.77, "notch"),
    (27, 0.50, "sU"),
    (41, 0.75, "notch"),
    (45, 0.85, "tooth"),
    (58, 0.99, "tip"),
    (71, 0.83, "tooth"),
    (76, 0.74, "notch"),
    (95, 0.46, "sU"),
    (108, 0.60, "tooth"),
    (118, 0.69, "tip"),
    (138, 0.42, "notch"),
    (163, 0.24, "notch"),
    (180, 0.17, "base"),
]

SOFT = [
    (0, 1.00, "tip"),
    (5, 0.88, "tooth"),
    (8, 0.80, "notch"),
    (11, 0.71, "tooth"),
    (28, 0.30, "sV"),
    (42, 0.62, "tooth"),
    (46, 0.72, "notch"),
    (50, 0.86, "tooth"),
    (60, 0.98, "tip"),
    (68, 0.84, "tooth"),
    (72, 0.74, "notch"),
    (80, 0.62, "tooth"),
    (98, 0.32, "sV"),
    (110, 0.50, "tooth"),
    (122, 0.64, "tip"),
    (136, 0.46, "tooth"),
    (160, 0.24, "notch"),
    (180, 0.12, "base"),
]


def _outline(spec):
    right = [p for p in spec if p[0] not in (0, 180)]
    tip = [p for p in spec if p[0] == 0][0]
    base = [p for p in spec if p[0] == 180][0]
    left = [(-t, r, k) for (t, r, k) in reversed(right)]
    return [base] + left + [tip] + right


def leaf_path(spec, s, cx, cy, rot=0.0, serrate=0, bulge=0.06, fillet=0.075):
    """Return an SVG path 'd' for a maple leaf whose petiole joins at (cx, cy)."""
    pts = [(pol(r, t + rot, s, cx, cy), k) for (t, r, k) in _outline(spec)]
    n = len(pts)
    d = []
    cur = None

    def edge_to(a, b):
        # gentle outward bulge (away from the leaf base) via a quadratic curve
        mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
        ox, oy = _norm((mx - cx, my - cy))
        seg = math.hypot(b[0] - a[0], b[1] - a[1])
        if serrate:
            # small saw teeth pointing toward the lobe tip
            out = []
            for j in range(1, serrate + 1):
                t0 = (j - 0.45) / serrate
                px = a[0] + (b[0] - a[0]) * t0 + ox * seg * 0.035
                py = a[1] + (b[1] - a[1]) * t0 + oy * seg * 0.035
                t1 = j / serrate
                qx = a[0] + (b[0] - a[0]) * t1
                qy = a[1] + (b[1] - a[1]) * t1
                out.append(f"L{f(px)} {f(py)} L{f(qx)} {f(qy)}")
            return " ".join(out)
        cx2 = mx + ox * seg * bulge
        cy2 = my + oy * seg * bulge
        return f"Q{f(cx2)} {f(cy2)} {f(b[0])} {f(b[1])}"

    # Pre-compute fillet tangent points for U sinuses
    fil = {}
    for i, (p, k) in enumerate(pts):
        if k != "sU":
            continue
        prev = pts[i - 1][0]
        nxt = pts[(i + 1) % n][0]
        u1 = _norm((prev[0] - p[0], prev[1] - p[1]))
        u2 = _norm((nxt[0] - p[0], nxt[1] - p[1]))
        cosang = max(-1.0, min(1.0, u1[0] * u2[0] + u1[1] * u2[1]))
        half = math.acos(cosang) / 2
        rho = fillet * s
        dist = rho / math.tan(half)
        t1 = (p[0] + u1[0] * dist, p[1] + u1[1] * dist)
        t2 = (p[0] + u2[0] * dist, p[1] + u2[1] * dist)
        bis = _norm((u1[0] + u2[0], u1[1] + u2[1]))
        ctr = (p[0] + bis[0] * rho / math.sin(half), p[1] + bis[1] * rho / math.sin(half))
        cross = (t1[0] - ctr[0]) * (t2[1] - ctr[1]) - (t1[1] - ctr[1]) * (t2[0] - ctr[0])
        sweep = 1 if cross > 0 else 0
        fil[i] = (t1, t2, rho, sweep)

    def entry(i):
        return fil[i][0] if i in fil else pts[i][0]

    def exitp(i):
        return fil[i][1] if i in fil else pts[i][0]

    start = exitp(0)
    d.append(f"M{f(start[0])} {f(start[1])}")
    cur = start
    for i in range(1, n + 1):
        idx = i % n
        target = entry(idx)
        d.append(edge_to(cur, target))
        if idx in fil:
            t1, t2, rho, sweep = fil[idx]
            d.append(f"A{f(rho)} {f(rho)} 0 0 {sweep} {f(t2[0])} {f(t2[1])}")
            cur = t2
        else:
            cur = target
        if idx == 0:
            break
    d.append("Z")
    return " ".join(d)


def leaf_svg(spec, s, cx, cy, fill, vein, rot=0.0, serrate=0, stem=True, vein_w=None, vein_op=0.55):
    """A complete leaf group: blade, veins and stem."""
    out = []
    if stem:
        a = pol(0.0, 0, s, cx, cy)
        b = pol(0.42, 180 + rot + 6, s, cx, cy)
        c = pol(0.22, 180 + rot - 2, s, cx, cy)
        out.append(
            f'<path d="M{f(a[0])} {f(a[1])} Q{f(c[0])} {f(c[1])} {f(b[0])} {f(b[1])}" fill="none" stroke="{vein}" '
            f'style="stroke-width:{f(s * 0.035)};stroke-linecap:round"></path>'
        )
    out.append(f'<path d="{leaf_path(spec, s, cx, cy, rot, serrate)}" fill="{fill}"></path>')
    vw = vein_w if vein_w is not None else s * 0.02
    for (t, r, k) in spec:
        if k != "tip":
            continue
        for sign in ([1] if t == 0 else [1, -1]):
            tt = t * sign
            tip = pol(r * 0.86, tt + rot, s, cx, cy)
            mid = pol(r * 0.45, tt + rot - 4 * sign, s, cx, cy)
            out.append(
                f'<path d="M{f(cx)} {f(cy)} Q{f(mid[0])} {f(mid[1])} {f(tip[0])} {f(tip[1])}" fill="none" stroke="{vein}" '
                f'style="stroke-width:{f(vw)};stroke-linecap:round;opacity:{vein_op}"></path>'
            )
    return "".join(out)


def mini_leaf(s, cx, cy, fill, rot=0.0, vein=None):
    """Small decorative leaf: blade (+ faint veins if vein colour given)."""
    if vein:
        return leaf_svg(SUGAR, s, cx, cy, fill, vein, rot=rot, stem=True, vein_w=max(1.5, s * 0.03), vein_op=0.5)
    return f'<path d="{leaf_path(SUGAR, s, cx, cy, rot)}" fill="{fill}"></path>'
