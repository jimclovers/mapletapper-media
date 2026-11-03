"""Post 04 - Kids Corner: "A taphole is about the size of a pencil eraser" (4 slides). Photo: MapleTapper kids' book (drilling).
Facts checked against 2+ sources:
  - 5/16 in. taphole = 7.9 mm; a standard #2 pencil is about 7-7.6 mm across (Wikipedia via unsharpen.com; Bananas for Scale);
    "not much bigger than a pencil eraser" (MapleTapper kids' book)
  - about 1 1/2 in. deep (MapleTapper Guide; Post 2 sources), into the sapwood, the living wood under the bark that carries sap
    (USDA Forest Products Lab Wood Handbook; Northern Woodlands)
  - one taphole: about 10 gallons of sap a season (UMaine 7036: 5-15; MSU: 10-12; UNH: 8-10) -> about 1 quart of syrup (UMaine)
  - a good sap day: up to about a gallon per tap (MSU: a quart to a gallon per flow; UNH: about 1 gallon per run)
  - tapping takes about 10% or less of stored sugar; holes close in 1-3 years; new spot each year (Post 2 sources)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   dc_html, preview_html)
from post02 import with_images  # noqa: E402
from post03 import cover, stamp, check_svg, teaser  # noqa: E402
from funfacts import site_footer  # noqa: E402
from jugs import jug, SAP, SAP_EDGE, SYRUP  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"cover": "book/p4_drill.jpg"}
M, CR, RED, GOLD = C["maroon"], C["cream"], C["red"], C["gold"]
BARK, SAPW, INNER, HOLE = "#6B4A2E", "#EAD3A8", "#D7B57E", "#2B1A10"


def lbl(x, y, text, size=22, anchor="middle", color=M, font=TYPE):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="font-family: {font}; font-size: {size}px; letter-spacing: 0.04em; '
            f'fill: {color}">{text}</text>')


def pencil_vs_hole_svg():
    """Pencil end and taphole drawn at the same scale: 20 px per mm (pencil ~7.5 mm, hole 7.9 mm)."""
    w, h = 900, 350
    cy, r_p = 165, 75                # pencil body 150 px tall
    x0, x1, x2, x3, x4 = 20, 130, 420, 485, 545
    p = [
        f'<path d="M{x0} {cy} L{x1} {cy - r_p} V{cy + r_p} Z" fill="#E8C99B" stroke="{M}" style="stroke-width:4;stroke-linejoin:round"></path>',
        f'<path d="M{x0} {cy} L{x0 + 34} {cy - 23} V{cy + 23} Z" fill="#3A3A3A"></path>',
        f'<rect x="{x1}" y="{cy - r_p}" width="{x2 - x1}" height="50" fill="#F7CA63"></rect>',
        f'<rect x="{x1}" y="{cy - 25}" width="{x2 - x1}" height="50" fill="{GOLD}"></rect>',
        f'<rect x="{x1}" y="{cy + 25}" width="{x2 - x1}" height="50" fill="#D99A2B"></rect>',
        f'<rect x="{x1}" y="{cy - r_p}" width="{x2 - x1}" height="{2 * r_p}" fill="none" stroke="{M}" style="stroke-width:4"></rect>',
        f'<rect x="{x2}" y="{cy - r_p}" width="{x3 - x2}" height="{2 * r_p}" fill="#C9CDD2" stroke="{M}" style="stroke-width:4"></rect>',
        f'<path d="M{x2 + 16} {cy - r_p} V{cy + r_p} M{x2 + 32} {cy - r_p} V{cy + r_p} M{x2 + 48} {cy - r_p} V{cy + r_p}" stroke="#8E949B" style="stroke-width:3"></path>',
        f'<path d="M{x3} {cy - r_p + 4} H{x4 - 18} Q{x4} {cy - r_p + 4} {x4} {cy - r_p + 22} V{cy + r_p - 22} Q{x4} {cy + r_p - 4} {x4 - 18} {cy + r_p - 4} H{x3} Z" '
        f'fill="#F29C9C" stroke="{M}" style="stroke-width:4;stroke-linejoin:round"></path>',
    ]
    hx, r_h, r_b = 750, 79, 122       # hole r 79 = 7.9 mm
    p += [
        f'<circle cx="{hx}" cy="{cy}" r="{r_b}" fill="{BARK}"></circle>',
        f'<path d="M{hx - 112} {cy - 40} Q{hx - 88} {cy - 50} {hx - 94} {cy - 12} M{hx + 92} {cy + 30} Q{hx + 108} {cy + 58} {hx + 84} {cy + 72} '
        f'M{hx - 58} {cy + 100} Q{hx - 20} {cy + 92} {hx + 10} {cy + 110} M{hx + 20} {cy - 112} Q{hx + 50} {cy - 100} {hx + 78} {cy - 106}" '
        f'fill="none" stroke="#4E3420" style="stroke-width:6;stroke-linecap:round"></path>',
        f'<defs><radialGradient id="holeg" cx="0.45" cy="0.42" r="0.6"><stop offset="0" stop-color="#5A3A22"></stop>'
        f'<stop offset="1" stop-color="{HOLE}"></stop></radialGradient></defs>',
        f'<circle cx="{hx}" cy="{cy}" r="{r_h + 6}" fill="{SAPW}"></circle>',
        f'<circle cx="{hx}" cy="{cy}" r="{r_h}" fill="url(#holeg)"></circle>',
    ]
    bar = lambda x, ya, yb, col: (f'<path d="M{x} {ya} V{yb} M{x - 11} {ya} H{x + 11} M{x - 11} {yb} H{x + 11}" stroke="{col}" '
                                  f'style="stroke-width:5;stroke-linecap:round"></path>')
    p += [
        bar(x4 + 22, cy - r_p, cy + r_p, RED),
        bar(hx, cy - r_h, cy + r_h, GOLD),
        lbl(300, 330, "Pencil: about 7 mm wide", 28),
        lbl(hx, 330, "Taphole: about 8 mm", 28),
    ]
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block">{"".join(p)}</svg>'


def depth_svg():
    """Side view: bark + sapwood, the 1 1/2 in. hole, and a ruler. 180 px per inch."""
    w, h, ppi = 900, 262, 180
    top, bh = 50, 110
    bark_w = 54
    hole_len = int(1.5 * ppi)
    p = [
        f'<rect x="0" y="{top}" width="{bark_w}" height="{bh}" fill="{BARK}"></rect>',
        f'<rect x="{bark_w}" y="{top}" width="{w - bark_w - 160}" height="{bh}" fill="{SAPW}"></rect>',
        f'<rect x="{w - 160}" y="{top}" width="160" height="{bh}" fill="{INNER}"></rect>',
        f'<path d="M{bark_w + 40} {top + 18} H{w - 200} M{bark_w + 70} {top + 92} H{w - 230} M{w - 140} {top + 30} H{w - 20} M{w - 120} {top + 80} H{w - 30}" '
        f'stroke="#D2B582" style="stroke-width:3;stroke-linecap:round"></path>',
        f'<path d="M0 {top + 38} H{hole_len - 14} L{hole_len} {top + 55} L{hole_len - 14} {top + 72} H0 Z" fill="{HOLE}"></path>',
        f'<rect x="0" y="{top}" width="{w}" height="{bh}" fill="none" stroke="{M}" style="stroke-width:4"></rect>',
        lbl(0, top - 14, "Bark", 26, anchor="start"),
        lbl((bark_w + w - 160) / 2, top - 14, "Sapwood", 26),
        lbl(w - 80, top - 14, "Inner wood", 26),
    ]
    ry = top + bh + 22
    p.append(f'<rect x="0" y="{ry}" width="{int(2 * ppi) + 20}" height="54" rx="6" fill="{GOLD}" stroke="{M}" style="stroke-width:3"></rect>')
    for i in range(0, 9):
        x = int(i * ppi / 4)
        tall = 20 if i % 2 == 0 else 12
        p.append(f'<path d="M{x + 2} {ry} V{ry + tall}" stroke="{M}" style="stroke-width:3"></path>')
    for v, t in ((0, "0"), (0.5, "½"), (1, "1"), (1.5, "1½ in.")):
        x = int(v * ppi) + 2
        p.append(f'<text x="{x + (5 if v == 0 else 0)}" y="{ry + 47}" text-anchor="{"start" if v == 0 else "middle"}" '
                 f'style="font-family: {DISPLAY}; font-weight: 800; font-size: 25px; fill: {M}">{t}</text>')
    p.append(f'<path d="M{hole_len} {top + 72} V{ry}" stroke="{RED}" style="stroke-width:3;stroke-dasharray:6 5"></path>')
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block">{"".join(p)}</svg>'


def jar_svg(w=150, h=212):
    return (
        f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 120 170" style="display: block; flex: none">'
        f'<rect x="28" y="6" width="64" height="22" rx="4" fill="#C9CDD2" stroke="{M}" style="stroke-width:4"></rect>'
        f'<path d="M24 28 H96 Q108 28 108 44 V150 Q108 164 94 164 H26 Q12 164 12 150 V44 Q12 28 24 28 Z" fill="#FFFFFF" stroke="{M}" style="stroke-width:4"></path>'
        f'<path d="M16 64 H104 V150 Q104 160 94 160 H26 Q16 160 16 150 Z" fill="{SYRUP}"></path>'
        f'<path d="M30 76 V140" stroke="#F5C27A" style="stroke-width:8;stroke-linecap:round"></path></svg>'
    )


def sap_to_syrup():
    s, gap = 2.0, 16
    jw, jh = 40 * s, 50 * s
    cols, rows = 5, 2
    gw, gh = cols * jw + (cols - 1) * gap, rows * jh + (rows - 1) * gap
    jugs = "".join(jug(c * (jw + gap), r * (jh + gap), s, SAP, SAP_EDGE, CR, stroke_w=1.8) for r in range(rows) for c in range(cols))
    grid = f'<svg aria-hidden="true" width="{gw:.0f}" height="{gh:.0f}" viewBox="0 0 {gw:.0f} {gh:.0f}" style="display: block; flex: none">{jugs}</svg>'
    arrow = (f'<svg aria-hidden="true" width="70" height="40" viewBox="0 0 70 40" style="flex: none"><path d="M4 20 H60 M44 6 L62 20 L44 34" '
             f'fill="none" stroke="{M}" style="stroke-width:6;stroke-linecap:round;stroke-linejoin:round"></path></svg>')
    cap = lambda big, small: (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 2px; text-align: center">'
                              f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; line-height: 1.02; color: {M}">{big}</div>'
                              f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 28px; color: {M}">{small}</div></div>')
    return (
        f'<div data-chk="saptosyrup" style="background: {CR}; border-radius: 34px; padding: 34px 40px 30px; display: flex; flex-direction: column; gap: 22px">'
        f'<div style="display: flex; align-items: center; justify-content: space-between">{grid}{arrow}{jar_svg()}</div>'
        f'<div style="display: flex; justify-content: space-between; align-items: flex-start">'
        f'{cap("About 10 gallons", "of sap in one season")}{cap("About 1 quart", "of syrup")}</div></div>'
    )


def badge(kind, size=104):
    p = []
    if kind == "share":
        p = [f'<circle cx="40" cy="40" r="30" fill="{SAP}" stroke="{M}" style="stroke-width:4"></circle>',
             f'<path d="M40 40 L40 10 A30 30 0 0 1 57.6 15.7 Z" fill="{RED}" stroke="{M}" style="stroke-width:3;stroke-linejoin:round"></path>']
    elif kind == "heal":
        p = [f'<circle cx="40" cy="40" r="30" fill="{BARK}"></circle>', f'<circle cx="40" cy="40" r="18" fill="{SAPW}"></circle>',
             f'<circle cx="40" cy="40" r="8" fill="{HOLE}"></circle>',
             f'<path d="M24 40 A16 16 0 0 1 56 40" fill="none" stroke="#7FA36A" style="stroke-width:5;stroke-linecap:round"></path>']
    elif kind == "spot":
        p = [f'<rect x="14" y="8" width="52" height="64" rx="8" fill="{BARK}"></rect>',
             f'<circle cx="30" cy="54" r="7" fill="#8C6A4A" stroke="#4E3420" style="stroke-width:2"></circle>',
             f'<circle cx="50" cy="26" r="8" fill="{HOLE}" stroke="{GOLD}" style="stroke-width:3"></circle>',
             f'<path d="M34 48 Q40 36 45 32" fill="none" stroke="{GOLD}" style="stroke-width:3;stroke-linecap:round;stroke-dasharray:4 4"></path>']
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {CR}; display: flex; align-items: center; '
            f'justify-content: center; flex: none; box-shadow: inset 0 0 0 3px #EAD9B5"><svg aria-hidden="true" width="{size - 12}" '
            f'height="{size - 12}" viewBox="0 0 80 80">{"".join(p)}</svg></div>')


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover(
        "cover", "A drill bit boring a small taphole into a maple trunk, snow behind", "04",
        stamp("KIDS", "corner"),
        "A taphole is<br>about the size of<br>a pencil eraser.",
        "How one little hole gives a whole season of sap. Swipe!",
        title_size=86, obj_pos="35% 50%",
    )
    return root(M, inner, CR), "A taphole is about the size of a pencil eraser"


def slide2():
    inner = (
        kicker_row("Kids Corner · Up close", "2 / 4", M)
        + headline(f'Not much bigger than<br><span style="color: {RED}">a pencil eraser.</span>', 80, M)
        + '<div style="flex-grow: 1"></div>'
        + f'<div data-chk="pencil" style="display: flex; justify-content: center">{pencil_vs_hole_svg()}</div>'
        + f'<div data-chk="depth" style="display: flex; justify-content: center">{depth_svg()}</div>'
        + body("A grown-up drills it about 1½ inches deep, into the sapwood: the living wood just under the bark that carries sap.",
               32, M, "depthtext")
        + '<div style="flex-grow: 1"></div>'
        + f'<div data-chk="try" style="align-self: flex-start; background: {GOLD}; color: {M}; border-radius: 999px; padding: 14px 28px 12px; '
          f'font-family: {DISPLAY}; font-weight: 800; font-size: 30px">Try it: grab a pencil and a ruler!</div>'
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=26), M), "Not much bigger than a pencil eraser"


def slide3():
    drop = (f'<svg aria-hidden="true" width="64" height="64" viewBox="0 0 64 64" style="flex: none"><path d="M32 6 C32 6 12 32 12 42 '
            f'A20 20 0 0 0 52 42 C52 32 32 6 32 6 Z" fill="{SAP}" stroke="{CR}" style="stroke-width:4"></path></svg>')
    good_day = (
        f'<div data-chk="goodday" style="display: flex; gap: 22px; align-items: center">{drop}'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 34px; line-height: 1.2; color: {CR}">'
        f'On a really good sap day, one tap can drip <span style="color: {GOLD}; font-weight: 800">up to about a gallon.</span></div></div>'
    )
    inner = (
        kicker_row("Kids Corner · Sap math", "3 / 4", CR)
        + headline(f'One little hole,<br><span style="color: {GOLD}">a whole season<br>of sap.</span>', 96, CR)
        + '<div style="flex-grow: 1"></div>'
        + sap_to_syrup()
        + '<div style="flex-grow: 1"></div>'
        + good_day
        + '<div style="flex-grow: 1"></div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=28), CR), "One little hole, a whole season of sap"


def slide4():
    rows = [
        ("share", "Just a small share", "A maple stores plenty of sugar. One tap takes about 10% or less."),
        ("heal", "It grows over", "A healthy tree grows new wood over the hole in 1 to 3 years."),
        ("spot", "A fresh spot each year", "Next season’s hole goes in a new place on the trunk."),
    ]
    items = "".join(
        f'<div style="display: flex; gap: 26px; align-items: center">{badge(k)}<div style="display: flex; flex-direction: column; gap: 4px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.04; color: {M}">{t}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 33px; line-height: 1.22; color: {M}">{n}</div></div></div>'
        for k, t, n in rows
    )
    challenge = (
        f'<div data-chk="challenge" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 28px 34px; display: flex; flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Kid challenge</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.1">Find a pencil and look at the eraser end. '
        f'A taphole is just a little wider!</div></div>'
    )
    inner = (
        kicker_row("Kids Corner · Tree care", "4 / 4", M)
        + headline(f'And the tree<br><span style="color: {RED}">is just fine.</span>', 104, M)
        + '<div style="flex-grow: 1"></div>'
        + f'<div data-chk="rows" style="display: flex; flex-direction: column; gap: 30px">{items}</div>'
        + '<div style="flex-grow: 1"></div>'
        + challenge
        + '<div style="flex-grow: 1"></div>'
        + teaser("", "Tree ID: the black maple")
        + site_footer(M)
    )
    return root(CR, column(inner, gap=28), M), "And the tree is just fine"


SLIDES = [("Post04-1-Cover", slide1), ("Post04-2-UpClose", slide2), ("Post04-3-SapMath", slide3), ("Post04-4-TreeCare", slide4)]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_p4.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
