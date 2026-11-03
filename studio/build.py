"""Build Post 01 (5-slide carousel) for the MapleTapper Instagram series.

Outputs, for every slide:
  preview/<name>.html      local preview with bundled fonts (for PNG export + checking)
  canvas/project/<name>.dc.html   the Design-canvas artboard (Google Fonts link)
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.dirname(__file__))
from art import C, SUGAR, SOFT, leaf_svg, leaf_path, mini_leaf, pol, f  # noqa: E402

ROOT = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(ROOT, "fonts", "node_modules")
W, H = 1080, 1350

DISPLAY = "'Bricolage Grotesque', 'Helvetica Neue', Arial, sans-serif"
TYPE = "'Special Elite', 'Courier New', monospace"

# ---------------------------------------------------------------- text bits

def kicker_row(left, right, color, chk="kicker"):
    return (
        f'<div data-chk="{chk}" style="display: flex; justify-content: space-between; align-items: center; '
        f'font-family: {TYPE}; font-size: 28px; letter-spacing: 0.06em; text-transform: uppercase; color: {color}">'
        f"<span>{left}</span><span>{right}</span></div>"
    )


def arrow_svg(color, size=34):
    return (
        f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
        f'style="stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;flex: none">'
        f'<path d="M4 12 H19"></path><path d="M13 6 L19 12 L13 18"></path></svg>'
    )


def leaf_mark(color, size=30):
    d = leaf_path(SUGAR, 10.5, 12, 15.5)
    return (
        f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" style="flex: none">'
        f'<path d="{d}" fill="{color}"></path></svg>'
    )


def footer_row(left_color, right_html, chk="footer"):
    return (
        f'<div data-chk="{chk}" style="display: flex; justify-content: space-between; align-items: center; '
        f'font-family: {TYPE}; font-size: 28px; letter-spacing: 0.04em; color: {left_color}">'
        f'<span style="display: flex; align-items: center; gap: 10px">{leaf_mark(left_color, 34)}@mapletapper</span>'
        f"{right_html}</div>"
    )


def swipe(color, label="Swipe"):
    return (
        f'<span style="display: flex; align-items: center; gap: 10px; font-family: {DISPLAY}; font-weight: 700; '
        f'font-size: 30px; letter-spacing: 0; color: {color}">{label}{arrow_svg(color, 32)}</span>'
    )


def headline(html, size, color, chk="headline", extra=""):
    return (
        f'<h1 data-chk="{chk}" style="margin: 0; font-family: {DISPLAY}; font-weight: 800; font-size: {size}px; '
        f'line-height: 0.92; letter-spacing: -0.025em; color: {color}{extra}">{html}</h1>'
    )


def body(html, size, color, chk, extra=""):
    return (
        f'<p data-chk="{chk}" style="margin: 0; font-family: {DISPLAY}; font-weight: 500; font-size: {size}px; '
        f'line-height: 1.28; color: {color}{extra}">{html}</p>'
    )


def svg_open(w, h, extra_style=""):
    return (
        f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'style="display: block; flex: none{extra_style}">'
    )


# ---------------------------------------------------------------- illustrations

def ribbon(tx, y, half, outline):
    """Cream flagging-tape ribbon with a bow, tied around a trunk centred at tx."""
    cr = C["cream"]
    st = f'stroke="{outline}" style="stroke-width:3;stroke-linejoin:round"'
    p = []
    # band around the trunk (slight curve)
    p.append(
        f'<path d="M{f(tx - half - 4)} {f(y - 12)} Q{f(tx)} {f(y - 4)} {f(tx + half + 4)} {f(y - 12)} '
        f'L{f(tx + half + 4)} {f(y + 12)} Q{f(tx)} {f(y + 20)} {f(tx - half - 4)} {f(y + 12)} Z" fill="{cr}" {st}></path>'
    )
    kx, ky = tx + half * 0.25, y + 4
    # tails fluttering to the right
    p.append(
        f'<path d="M{f(kx)} {f(ky)} C{f(kx + 30)} {f(ky + 30)}, {f(kx + 70)} {f(ky + 20)}, {f(kx + 104)} {f(ky + 62)} '
        f'L{f(kx + 88)} {f(ky + 70)} L{f(kx + 96)} {f(ky + 86)} C{f(kx + 60)} {f(ky + 44)}, {f(kx + 26)} {f(ky + 50)}, {f(kx - 4)} {f(ky + 12)} Z" '
        f'fill="{cr}" {st}></path>'
    )
    p.append(
        f'<path d="M{f(kx)} {f(ky)} C{f(kx + 10)} {f(ky + 40)}, {f(kx + 40)} {f(ky + 60)}, {f(kx + 40)} {f(ky + 104)} '
        f'L{f(kx + 26)} {f(ky + 96)} L{f(kx + 18)} {f(ky + 112)} C{f(kx + 20)} {f(ky + 70)}, {f(kx - 8)} {f(ky + 44)}, {f(kx - 8)} {f(ky + 10)} Z" '
        f'fill="{cr}" {st}></path>'
    )
    # bow loops
    for sgn in (-1, 1):
        p.append(
            f'<path d="M{f(kx)} {f(ky)} C{f(kx + sgn * 20)} {f(ky - 46)}, {f(kx + sgn * 62)} {f(ky - 30)}, {f(kx + sgn * 50)} {f(ky - 4)} '
            f'C{f(kx + sgn * 40)} {f(ky + 16)}, {f(kx + sgn * 16)} {f(ky + 8)}, {f(kx)} {f(ky)} Z" fill="{cr}" {st}></path>'
        )
    p.append(f'<circle cx="{f(kx)}" cy="{f(ky)}" r="11" fill="{cr}" {st}></circle>')
    return "".join(p)


def cover_art():
    random.seed(11)
    p = []
    # distant falling leaves (behind tree)
    for (x, y, s, col, rot) in [
        (128, 812, 46, C["red"], -25), (420, 800, 34, C["amber"], 30), (228, 956, 40, C["maroon"], 55),
        (440, 900, 30, C["gold"], -50), (120, 1072, 36, C["orange"], 15), (372, 1060, 44, C["red_dk"], -10),
        (520, 1010, 28, C["amber"], 80), (996, 486, 30, C["red"], 20),
    ]:
        p.append(mini_leaf(s, x, y, col, rot))
    # tree
    tx, ground, top = 800, 1180, 890
    p.append(
        f'<path d="M{tx - 54} {ground + 8} C{tx - 34} {ground - 70}, {tx - 26} {top + 90}, {tx - 22} {top} '
        f'L{tx + 22} {top} C{tx + 26} {top + 90}, {tx + 36} {ground - 70}, {tx + 58} {ground + 8} Z" fill="{C["bark"]}"></path>'
    )
    for (x1, y1, x2, y2, w) in [(tx - 6, top + 30, tx - 150, top - 110, 20), (tx + 8, top + 10, tx + 150, top - 130, 18), (tx, top + 6, tx - 8, top - 210, 22)]:
        p.append(
            f'<path d="M{x1} {y1} Q{(x1 + x2) / 2} {y1 - 20} {x2} {y2}" fill="none" stroke="{C["bark"]}" '
            f'style="stroke-width:{w};stroke-linecap:round"></path>'
        )
    cx, cy, k = 800, 786, 0.86
    layers = [
        (C["red_dk"], [(-150, 40, 150), (150, 30, 150), (0, -110, 170), (-60, 120, 140), (80, 120, 140)]),
        (C["red"], [(-125, -40, 130), (125, -50, 130), (0, 20, 170), (-195, 90, 100), (190, 92, 100)]),
        (C["orange"], [(-62, -122, 110), (92, -112, 105), (-140, 36, 95), (142, 40, 95), (0, 118, 112)]),
        (C["amber"], [(-84, -158, 58), (64, -176, 52), (-178, -22, 48), (176, -14, 52), (40, 30, 60)]),
    ]
    for col, circles in layers:
        for (dx, dy, r) in circles:
            p.append(f'<circle cx="{f(cx + dx * k)}" cy="{f(cy + dy * k)}" r="{f(r * k)}" fill="{col}"></circle>')
    # leaf texture along the crown edge
    for i in range(44):
        ang = random.uniform(-150, 150)
        rad = random.uniform(195, 262) * k
        x = cx + rad * math.sin(math.radians(ang))
        y = cy - rad * math.cos(math.radians(ang)) + 30 * k
        col = random.choice([C["gold"], C["amber"], C["red"], C["maroon"], C["orange"]])
        p.append(mini_leaf(random.uniform(26, 36), x, y, col, random.uniform(-60, 60)))
    for i in range(30):
        x = cx + random.uniform(-180, 180) * k
        y = cy + random.uniform(-170, 130) * k
        p.append(mini_leaf(random.uniform(20, 28), x, y, random.choice([C["gold_lt"], C["gold"], C["maroon"]]), random.uniform(-80, 80)))
    # ribbon on the trunk
    p.append(ribbon(tx, 1066, 30, C["maroon_dk"]))
    # ground
    p.append(
        f'<path d="M0 1196 C220 1158, 520 1168, 700 1180 C860 1190, 980 1174, 1080 1156 L1080 1350 L0 1350 Z" fill="{C["maroon"]}"></path>'
    )
    for (x, y, s, col, rot) in [(610, 1186, 26, C["orange"], 70), (690, 1192, 22, C["gold"], -40), (960, 1176, 26, C["amber"], 20),
                                (1030, 1168, 22, C["red"], -70), (900, 1194, 20, C["gold"], 45)]:
        p.append(mini_leaf(s, x, y, col, rot))
    return f'<svg aria-hidden="true" width="{W}" height="{H}" viewBox="0 0 {W} {H}" style="position: absolute; left: 0; top: 0; display: block">{"".join(p)}</svg>'


def notch_callout(x, y, r, color, letter):
    return (
        f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(r)}" fill="none" stroke="{color}" style="stroke-width:5;stroke-dasharray:10 7"></circle>'
    )


def leaf_card_svg(kind):
    w, h = 400, 292
    s, cx, cy = 150, 200, 214
    if kind == "hard":
        leaf = leaf_svg(SUGAR, s, cx, cy, C["orange"], C["red_dk"])
        # upper-right sinus position (theta 27, r .5) -> callout
        sx, sy = pol(0.47, 27, s, cx, cy)
        badge_col = C["maroon"]
    else:
        leaf = leaf_svg(SOFT, s, cx, cy, C["gold"], C["tan_dk"], serrate=2)
        sx, sy = pol(0.31, 28, s, cx, cy)
        badge_col = C["maroon"]
    ring = notch_callout(sx, sy, 26, badge_col, "")
    return svg_open(w, h) + leaf + ring + "</svg>"


def bark_svg(kind, R=118, ring_col=None, bg=None):
    random.seed(3 if kind == "hard" else 5)
    S = 2 * R + 16
    c = S / 2
    p = []
    if kind == "hard":
        p.append(f'<rect x="0" y="0" width="{S}" height="{S}" fill="{C["gray_dk"]}"></rect>')
        x = c - R - 10
        while x < c + R + 10:
            wdt = random.uniform(16, 26)
            y = c - R - 20 - random.uniform(0, 140)
            while y < c + R + 20:
                seg = random.uniform(120, 260)
                wob = random.uniform(-4, 4)
                col = random.choice([C["gray"], C["gray"], C["gray_lt"], "#A3A19B"])
                p.append(
                    f'<path d="M{f(x)} {f(y)} Q{f(x + wob)} {f(y + seg / 2)} {f(x)} {f(y + seg)} L{f(x + wdt)} {f(y + seg)} '
                    f'Q{f(x + wdt + wob)} {f(y + seg / 2)} {f(x + wdt)} {f(y)} Z" fill="{col}"></path>'
                )
                y += seg + random.uniform(4, 9)
            x += wdt + random.uniform(5, 8)
    else:
        p.append(f'<rect x="0" y="0" width="{S}" height="{S}" fill="{C["bark_dk"]}"></rect>')
        row = 0
        y = c - R - 30
        while y < c + R + 30:
            x = c - R - 40 - (row % 2) * 30
            while x < c + R + 40:
                wdt = random.uniform(44, 70)
                hgt = random.uniform(34, 46)
                col = random.choice(["#9C8E82", "#A99B8E", "#8E7F73", "#B3A598"])
                p.append(
                    f'<path d="M{f(x)} {f(y + 6)} L{f(x + wdt * 0.5)} {f(y)} L{f(x + wdt)} {f(y + 4)} L{f(x + wdt - 4)} {f(y + hgt)} '
                    f'L{f(x + 6)} {f(y + hgt + 4)} Z" fill="{col}"></path>'
                )
                # light flaking edge
                p.append(
                    f'<path d="M{f(x + 4)} {f(y + 7)} Q{f(x + wdt * 0.5)} {f(y - 4)} {f(x + wdt - 2)} {f(y + 5)}" fill="none" stroke="#D6CBBE" '
                    f'style="stroke-width:3;stroke-linecap:round"></path>'
                )
                x += wdt - 6
            y += hgt - 8
            row += 1
    # circular mask via a thick ring in the background colour, then a cream border
    mask_w = R
    p.append(f'<circle cx="{f(c)}" cy="{f(c)}" r="{f(R + mask_w / 2)}" fill="none" stroke="{bg}" style="stroke-width:{f(mask_w)}"></circle>')
    p.append(f'<circle cx="{f(c)}" cy="{f(c)}" r="{f(R)}" fill="none" stroke="{ring_col}" style="stroke-width:6"></circle>')
    return svg_open(S, S) + "".join(p) + "</svg>"


def samara_svg():
    w, h = 300, 250
    p = []
    # one wing pointing up from its seed at the origin
    wing = "M-8 -6 C-16 -60, -22 -120, -14 -178 C-10 -204, 14 -210, 26 -190 C40 -160, 40 -96, 22 -40 C16 -22, 10 -10, 6 -4 Z"
    veins = ["M-2 -14 C-8 -70, -10 -130, -6 -186", "M2 -16 C6 -70, 12 -130, 16 -182", "M4 -14 C12 -60, 22 -110, 28 -160"]
    bx, by = 150, 214
    p.append(f'<path d="M{bx} {by + 4} Q{bx + 4} {by + 22} {bx - 2} {by + 34}" fill="none" stroke="{C["tan_dk"]}" style="stroke-width:5;stroke-linecap:round"></path>')
    for (ox, ang) in [(-13, -24), (13, 24)]:
        flip = -1 if ang < 0 else 1
        p.append(f'<g transform="translate({bx + ox} {by}) rotate({ang}) scale({flip} 1)">')
        p.append(f'<path d="{wing}" fill="{C["tan"]}"></path>')
        for i, v in enumerate(veins):
            p.append(f'<path d="{v}" fill="none" stroke="{C["tan_dk"]}" style="stroke-width:{3 if i == 0 else 2};stroke-linecap:round;opacity:0.6"></path>')
        p.append(f'<ellipse cx="0" cy="-4" rx="15" ry="19" fill="{C["tan_dk"]}"></ellipse>')
        p.append("</g>")
    return svg_open(w, h) + "".join(p) + "</svg>"


def trunk_art():
    w, h = 380, 620
    p = [f'<rect x="0" y="0" width="{w}" height="{h}" fill="{C["sky"]}"></rect>']
    tx, half = 190, 100
    p.append(f'<path d="M{tx - half} -10 L{tx + half} -10 L{tx + half + 6} {h - 96} C{tx + half + 30} {h - 60}, {tx + half + 54} {h - 52}, {tx + half + 80} {h - 40} '
             f'L{tx - half - 80} {h - 40} C{tx - half - 54} {h - 52}, {tx - half - 30} {h - 60}, {tx - half - 6} {h - 96} Z" fill="{C["bark"]}"></path>')
    random.seed(9)
    for i in range(9):
        x = tx - half + 14 + i * 22 + random.uniform(-4, 4)
        y = random.uniform(-10, 60)
        while y < h - 120:
            seg = random.uniform(80, 170)
            p.append(f'<path d="M{f(x)} {f(y)} q{f(random.uniform(-6, 6))} {f(seg / 2)} 0 {f(seg)}" fill="none" stroke="{C["bark_dk"]}" style="stroke-width:{f(random.uniform(4, 7))};stroke-linecap:round;opacity:0.8"></path>')
            y += seg + random.uniform(16, 40)
    p.append(f'<path d="M0 {h - 52} C90 {h - 66}, 280 {h - 64}, {w} {h - 50} L{w} {h} L0 {h} Z" fill="{C["maroon"]}"></path>')
    for (x, y, s, col, rot) in [(46, h - 50, 28, C["orange"], 60), (112, h - 40, 24, C["gold"], -30), (290, h - 46, 28, C["amber"], 15), (346, h - 36, 22, C["red"], -60), (220, h - 30, 20, C["gold"], 80)]:
        p.append(mini_leaf(s, x, y, col, rot))
    p.append(ribbon(tx, 170, half, C["maroon_dk"]))
    ay = 392
    p.append(f'<path d="M{tx - half + 12} {ay} H{tx + half - 12}" fill="none" stroke="{C["cream"]}" style="stroke-width:5;stroke-linecap:round;stroke-dasharray:14 10"></path>')
    for sgn in (-1, 1):
        ex = tx + sgn * (half - 12)
        p.append(f'<path d="M{ex - sgn * 16} {ay - 14} L{ex} {ay} L{ex - sgn * 16} {ay + 14}" fill="none" stroke="{C["cream"]}" style="stroke-width:5;stroke-linecap:round;stroke-linejoin:round"></path>')
    return svg_open(w, h) + "".join(p) + "</svg>"


def icon(kind, col):
    s = 'fill="none" stroke="%s" style="stroke-width:5.5;stroke-linecap:round;stroke-linejoin:round"' % col
    if kind == "leaf":
        return f'<path d="{leaf_path(SUGAR, 25, 40, 50)}" fill="{col}"></path><path d="M40 50 L40 64" fill="none" stroke="{col}" style="stroke-width:4;stroke-linecap:round"></path>'
    if kind == "snow":
        out = []
        for a in (0, 60, 120):
            out.append(f'<g transform="rotate({a} 40 40)"><path d="M40 16 V64" {s}></path><path d="M33 21 L40 28 L47 21" {s}></path><path d="M33 59 L40 52 L47 59" {s}></path></g>')
        return "".join(out)
    if kind == "tap":
        return (f'<path d="M15 12 H27 V68 H15 Z" fill="{col}"></path>'
                f'<path d="M27 32 L53 36" fill="none" stroke="{col}" style="stroke-width:8;stroke-linecap:round"></path>'
                f'<path d="M51 36 L58 43" fill="none" stroke="{col}" style="stroke-width:5;stroke-linecap:round"></path>'
                f'<path d="M59 49 C55 55, 53 58, 53 61 A6 6 0 0 0 65 61 C65 58, 63 55, 59 49 Z" fill="{col}"></path>')
    if kind == "jar":
        return (f'<path d="M26 24 H54" {s}></path><path d="M28 30 C22 34, 22 38, 22 44 V62 C22 66, 25 68, 29 68 H51 C55 68, 58 66, 58 62 V44 C58 38, 58 34, 52 30" {s}></path>'
                f'<path d="M30 16 H50 V24 H30 Z" {s}></path><path d="M24 48 H56 V62 C56 64, 54 66, 52 66 H28 C26 66, 24 64, 24 62 Z" fill="{col}"></path>')
    return ""


def icon_badge(kind, size=80):
    return (
        f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {C["cream"]}; display: flex; '
        f'align-items: center; justify-content: center; flex: none">'
        f'<svg aria-hidden="true" width="{size - 10}" height="{size - 10}" viewBox="0 0 80 80">{icon(kind, C["red"])}</svg></div>'
    )


def check_badge():
    return (
        f'<div style="width: 46px; height: 46px; border-radius: 50%; background: {C["maroon"]}; display: flex; align-items: center; '
        f'justify-content: center; flex: none; margin-top: 2px">'
        f'<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{C["cream"]}" '
        f'style="stroke-width:3.4;stroke-linecap:round;stroke-linejoin:round"><path d="M5 12.5 L10 17 L19 7"></path></svg></div>'
    )


# ---------------------------------------------------------------- slides

def root(bg, inner, color):
    return (
        f'<div data-root style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: {bg}; '
        f'box-sizing: border-box; font-family: {DISPLAY}; color: {color}">{inner}</div>'
    )


def column(inner, pad="72px 72px 64px", gap=28):
    return (
        f'<div style="position: relative; z-index: 1; box-sizing: border-box; width: {W}px; height: {H}px; padding: {pad}; '
        f'display: flex; flex-direction: column; gap: {gap}px">{inner}</div>'
    )


def slide1():
    red = C["red"]
    inner = (
        kicker_row("Sugarmaker’s Almanac · No.&nbsp;01", "@mapletapper", C["maroon"])
        + headline(f'Find your<br><span style="color: {red}">syrup trees</span><br>this fall.', 150, C["maroon"], extra="; margin-top: 6px")
        + body("Before the leaves drop, maples are easy to spot. Here’s how to find (and mark) yours.", 38, C["maroon"], "sub", "; max-width: 470px")
        + '<div style="flex-grow: 1"></div>'
        + f'<div data-chk="pill" style="align-self: flex-start; display: flex; align-items: center; gap: 14px; background: {C["cream"]}; '
        f'color: {C["maroon"]}; border-radius: 999px; padding: 20px 30px 20px 34px; font-family: {DISPLAY}; font-weight: 700; font-size: 34px; '
        f'margin-bottom: 4px">Swipe for 3 easy clues{arrow_svg(C["maroon"], 34)}</div>'
    )
    return root(C["sky"], cover_art() + column(inner, pad="64px 72px 60px", gap=26), C["maroon"]), "Find your syrup trees this fall"


def leaf_card(kind):
    if kind == "hard":
        tag, big, small = "Hard maple", "U-shaped<br>valleys", "Sugar, black &amp; rock maples. The sweetest sap!"
    else:
        tag, big, small = "Soft maple", "V-shaped<br>valleys", "Red &amp; silver maples. Tappable, just a longer boil."
    return (
        f'<div data-chk="card-{kind}" style="flex: 1 1 0; min-width: 0; background: {C["sky"]}; border-radius: 36px; padding: 26px 28px 30px; '
        f'display: flex; flex-direction: column; align-items: center; gap: 6px">'
        f'<div style="align-self: flex-start; font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase; '
        f'color: {C["cream"]}; background: {C["maroon"]}; border-radius: 10px; padding: 7px 14px 5px">{tag}</div>'
        f"{leaf_card_svg(kind)}"
        f'<div style="align-self: stretch; font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 0.98; letter-spacing: -0.02em; color: {C["maroon"]}">{big}</div>'
        f'<div style="align-self: stretch; font-family: {DISPLAY}; font-weight: 500; font-size: 29px; line-height: 1.22; color: {C["maroon"]}; margin-top: 6px">{small}</div>'
        f"</div>"
    )


def slide2():
    inner = (
        kicker_row("Clue 1 · The leaf", "2 / 5", C["maroon"])
        + headline("Check the<br>notches", 128, C["maroon"])
        + body("Most maple leaves have 5 lobes. The valleys between them tell you which kind you’ve found.", 38, C["maroon"], "sub", "; max-width: 900px")
        + f'<div data-chk="cards" style="display: flex; gap: 28px">{leaf_card("hard")}{leaf_card("soft")}</div>'
        + f'<div data-chk="tip" style="display: flex; align-items: center; gap: 20px; background: {C["maroon"]}; color: {C["cream"]}; border-radius: 28px; '
        f'padding: 22px 30px; font-family: {DISPLAY}; font-weight: 600; font-size: 31px; line-height: 1.25">'
        f'{leaf_mark(C["gold"], 44)}<span>Bonus clue: sugar maples usually have the most colorful fall leaves.</span></div>'
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["cream"], column(inner, gap=26), C["maroon"]), "Clue 1: check the notches"


def bark_item(kind, title, note):
    return (
        f'<div data-chk="bark-{kind}" style="flex: 1 1 0; display: flex; flex-direction: column; align-items: center; gap: 14px; text-align: center">'
        f'{bark_svg(kind, 116, C["cream"], C["maroon"])}'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["gold"]}">{title}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 33px; line-height: 1.18; color: {C["cream"]}; max-width: 400px">{note}</div>'
        f"</div>"
    )


def slide3():
    sub = f'font-family: {DISPLAY}; font-weight: 800; font-size: 50px; letter-spacing: -0.02em; line-height: 1; color: {C["gold"]}; margin: 0'
    inner = (
        kicker_row("Clues 2 &amp; 3 · Bark + seeds", "3 / 5", C["cream"])
        + headline("Bark &amp;<br>helicopters", 128, C["cream"])
        + f'<h2 data-chk="h-bark" style="{sub}; margin-top: 10px">Read the bark</h2>'
        + f'<div data-chk="bark-row" style="display: flex; gap: 36px">'
        + bark_item("hard", "Hard maple", "Gray, with narrow, deep furrows")
        + bark_item("soft", "Soft maple", "Layered and flaky")
        + "</div>"
        + f'<h2 data-chk="h-seeds" style="{sub}; margin-top: 14px">Look for “helicopters”</h2>'
        + f'<div data-chk="seed-row" style="display: flex; align-items: center; gap: 26px">{samara_svg()}'
        + body("All maples grow two-winged seeds. <b style=\"font-weight: 800\">Hard maples drop theirs in late summer &amp; early fall.</b> Soft maples drop theirs in spring.", 34, C["cream"], "seed-text", "; flex: 1 1 0")
        + "</div>"
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], swipe(C["cream"]))
    )
    return root(C["maroon"], column(inner, gap=22), C["cream"]), "Clues 2 & 3: bark and helicopters"


def check_item(main, note=""):
    extra = f'<div style="font-weight: 500; font-size: 27px; margin-top: 4px; opacity: 0.85">{note}</div>' if note else ""
    return (
        f'<div style="display: flex; gap: 18px; align-items: flex-start">{check_badge()}'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 33px; line-height: 1.16; color: {C["maroon"]}">{main}{extra}</div></div>'
    )


def slide4():
    card = (
        f'<div data-chk="checklist" style="flex: 1 1 0; min-width: 0; background: {C["cream"]}; border-radius: 36px; padding: 38px 36px; '
        f'display: flex; flex-direction: column; justify-content: center; gap: 28px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; letter-spacing: -0.02em; line-height: 1; color: {C["maroon"]}">Is it tap-ready?</div>'
        + check_item("At least 12 in. across", "(about 38 in. around)")
        + check_item("A full, healthy crown of branches")
        + check_item("No lawn pesticides or herbicides")
        + check_item("Yard maples count. No forest needed!")
        + "</div>"
    )
    art = (
        f'<div data-chk="trunk" style="position: relative; width: 380px; height: 620px; flex: none; border-radius: 36px; overflow: hidden">{trunk_art()}'
        f'<div style="position: absolute; left: 124px; top: 414px; background: {C["cream"]}; color: {C["maroon"]}; border-radius: 12px; '
        f'padding: 8px 14px 6px; font-family: {TYPE}; font-size: 28px; letter-spacing: 0.04em">12 in.+</div></div>'
    )
    inner = (
        kicker_row("Found one?", "4 / 5", C["maroon"])
        + headline("Tie a ribbon<br>on it!", 136, C["maroon"])
        + body("In February, bare maples all look alike. Weather-resistant tape helps you find yours again.", 38, C["maroon"], "sub", "; max-width: 900px")
        + f'<div data-chk="row" style="display: flex; gap: 28px; align-items: stretch; margin-top: 6px">{art}{card}</div>'
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["maroon"], swipe(C["maroon"]))
    )
    return root(C["gold"], column(inner, gap=26), C["maroon"]), "Found one? Tie a ribbon on it"


def step(kind, label, main, here=False):
    badge = (
        f'<span style="display: inline-block; vertical-align: middle; margin-left: 12px; background: {C["gold"]}; color: {C["maroon"]}; '
        f'border-radius: 999px; padding: 5px 14px 3px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.04em">You are here</span>'
        if here else ""
    )
    return (
        f'<div style="display: flex; gap: 26px; align-items: center; position: relative; z-index: 1">{icon_badge(kind)}'
        f'<div style="display: flex; flex-direction: column; gap: 4px; min-width: 0">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase; color: {C["cream"]}">{label}{badge}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 36px; line-height: 1.14; color: {C["cream"]}">{main}</div></div></div>'
    )


def pancakes_svg():
    w, h = 300, 236
    p = []
    p.append(f'<ellipse cx="150" cy="206" rx="140" ry="24" fill="{C["cream"]}"></ellipse>')
    p.append(f'<ellipse cx="150" cy="200" rx="112" ry="14" fill="#F3E3C0"></ellipse>')
    for i, y in enumerate([180, 150, 120, 90]):
        p.append(f'<rect x="{46 + i * 3}" y="{y - 22}" width="{208 - i * 6}" height="38" rx="19" fill="#C8842F"></rect>')
        p.append(f'<rect x="{46 + i * 3}" y="{y - 26}" width="{208 - i * 6}" height="32" rx="16" fill="#F2B45A"></rect>')
    syrup = "#A8521A"
    p.append(f'<path d="M66 70 C70 58, 230 58, 234 70 C236 80, 222 82, 220 92 C218 104, 214 118, 208 118 C202 118, 202 100, 196 94 '
             f'C188 88, 176 98, 170 96 C160 92, 150 112, 142 112 C134 112, 134 94, 124 92 C112 90, 104 104, 96 102 C88 100, 92 86, 84 82 '
             f'C74 78, 64 80, 66 70 Z" fill="{syrup}"></path>')
    p.append(f'<path d="M214 100 C214 120, 216 136, 210 146 C204 154, 198 144, 202 132 C206 122, 208 112, 214 100 Z" fill="{syrup}"></path>')
    p.append(f'<path d="M92 66 C120 60, 170 60, 206 66" fill="none" stroke="#E3954A" style="stroke-width:5;stroke-linecap:round;opacity:0.9"></path>')
    p.append(f'<rect x="128" y="40" width="44" height="26" rx="6" fill="#FFE7A3"></rect>')
    p.append(f'<rect x="128" y="40" width="44" height="9" rx="4" fill="#FFF3CC"></rect>')
    return svg_open(w, h) + "".join(p) + "</svg>"


def slide5():
    timeline = (
        f'<div data-chk="timeline" style="position: relative; display: flex; flex-direction: column; gap: 16px">'
        f'<div style="position: absolute; left: 38px; top: 40px; bottom: 40px; border-left: 5px dashed {C["cream"]}; opacity: 0.55"></div>'
        + step("leaf", "Now · Fall", "Find &amp; mark your maples", here=True)
        + step("snow", "Winter", "Gather your gear &amp; watch the forecast")
        + step("tap", "Late winter", "Tap when nights freeze &amp; days hit the 40s °F")
        + step("jar", "Sap season", "Collect, boil &amp; pour your own syrup")
        + "</div>"
    )
    stat = (
        f'<div data-chk="stat" style="background: {C["cream"]}; color: {C["maroon"]}; border-radius: 32px; padding: 28px 34px; display: flex; '
        f'flex-direction: column; gap: 8px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 52px; letter-spacing: -0.02em; line-height: 1">4 taps ≈ 1 gallon of syrup</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 28px; line-height: 1.25">Each tap gives about 10–12 gallons of sap a season. That boils down to roughly a quart of syrup.</div></div>'
    )
    inner = (
        kicker_row("Your sweet-season roadmap", "5 / 5", C["cream"])
        + headline("From tree<br>to pancakes", 122, C["cream"])
        + timeline
        + stat
        + f'<div data-chk="cta" style="display: flex; align-items: center; gap: 24px">'
        + body("Save this post &amp; follow along. We’ll walk you through every step, all the way to your first batch.", 34, C["cream"], "cta-text", "; flex: 1 1 0; font-weight: 600")
        + pancakes_svg() + "</div>"
        + '<div style="flex-grow: 1"></div>'
        + footer_row(C["cream"], f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; letter-spacing: 0; color: {C["cream"]}">Free guide: mapletapper.com</span>')
    )
    return root(C["red"], column(inner, gap=24), C["cream"]), "From tree to pancakes"


SLIDES = [("Main", slide1), ("Post01-2-Notches", slide2), ("Post01-3-Bark", slide3), ("Post01-4-Ribbon", slide4), ("Post01-5-Roadmap", slide5)]


def font_faces_local():
    b = os.path.join(FONT_DIR, "@fontsource-variable/bricolage-grotesque/files/bricolage-grotesque-latin-standard-normal.woff2")
    s = os.path.join(FONT_DIR, "@fontsource/special-elite/files/special-elite-latin-400-normal.woff2")
    return (
        "@font-face{font-family:'Bricolage Grotesque';src:url('file://%s') format('woff2');font-weight:200 800;font-stretch:75%% 100%%;}"
        "@font-face{font-family:'Special Elite';src:url('file://%s') format('woff2');font-weight:400;}" % (b, s)
    )


GF = "https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800&amp;family=Special+Elite&amp;display=swap"


def dc_clean(markup):
    import re as _re
    markup = markup.replace(" data-root", "")
    markup = _re.sub(r' data-chk="[^"]*"', "", markup)
    return markup.replace("&nbsp;", "\u00a0")


def dc_html(title, markup):
    markup = dc_clean(markup)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous">
<link href="{GF}" rel="stylesheet">
<style>
body{{margin:0}}
a{{color:#7A1E1A}}a:hover{{color:#5A1411}}
</style>
</helmet>
{markup}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{H}}}}}'>
class Component extends DCLogic {{
  renderVals() {{
    return {{}};
  }}
}}
</script>
</body>
</html>
"""


def preview_html(title, markup):
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{font_faces_local()} body{{margin:0}}</style></head><body>{markup}</body></html>"""


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    os.makedirs(os.path.join(ROOT, "canvas", "project"), exist_ok=True)
    for name, fn in SLIDES:
        markup, title = fn()
        open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, markup))
        open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, markup))
    print("built", len(SLIDES))
