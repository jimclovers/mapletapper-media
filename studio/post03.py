"""Post 03 - Family Tradition: "The perfect family project" (4 slides).
Photos: MapleTapper book photos (sap drip, a child setting a spile, the boiling pot). Facts checked against 2+ sources:
  - kids can help with every step except handling the boiling sap (MapleTapper Guide; MSU Extension; DIY.org)
  - few, simple tools (MSU Extension; MapleTapper Guide)
  - boil outdoors: ~39 gal of water steams off per gallon of syrup (40:1 ratio; MSU Extension; Ontario Maple)
  - syrup is done 7 F above water's boiling point (MSU Extension; Virginia Tech FST-311)
  - maple cream +22-24 F (Syrupfest; Cornell; Mass Maple), hard candy +28-30 F (Ohio State F-46; MapleTapper books),
    granulated sugar +40-45 F (Ohio State F-46; Syrupfest; MapleTapper books)
  - syrup that is too heavy can be thinned with sap (CDL hydrometer guide; Bascom Maple)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   dc_html, preview_html)
from post02 import pill, with_images  # noqa: E402
from funfacts import site_footer  # noqa: E402
from jugs import jug, SAP, SAP_EDGE  # noqa: E402

PHOTO_DIR = os.path.join(ROOT, "photos")
ASSETS = {"cover": "book/p3_sap_drip.jpg", "kid": "book/p3_kid_spile.jpg", "pot": "book/p3_boil_pot.jpg"}
M, CR, RED, GOLD = C["maroon"], C["cream"], C["red"], C["gold"]
PHOTO_H = 780


def stamp(big1, small, big2="", top=PHOTO_H - 68):
    return (
        f'<div data-chk="stamp" style="position: absolute; left: 60px; top: {top}px; z-index: 3; transform: rotate(-3deg); background: {GOLD}; '
        f'border: 6px solid {CR}; border-radius: 22px; padding: 10px 30px 12px; display: flex; align-items: baseline; gap: 16px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 72px; letter-spacing: -0.02em; line-height: 1; color: {M}">'
        f'{big1}<span style="font-family: {TYPE}; font-weight: 400; font-size: 40px; letter-spacing: 0">{small}</span>{big2}</div>'
    )


def cover(img_key, alt, almanac_no, stamp_html, title_html, sub, title_size=98, obj_pos="50% 50%"):
    photo = (
        f'<img src="@@IMG_{img_key}@@" alt="{alt}" '
        f'style="position: absolute; left: 0; top: 0; width: {W}px; height: {PHOTO_H}px; object-fit: cover; object-position: {obj_pos}; display: block">'
    )
    top = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill(f"Sugarmaker’s Almanac · No. {almanac_no}", CR, M)}{pill("17 weeks to sap season", GOLD, M)}</div>'
    )
    bottom = (
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {W}px; height: {H - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 100px 72px 60px; display: flex; flex-direction: column; gap: 20px; background: {M}">'
        + headline(title_html, title_size, CR, chk="title")
        + body(sub, 36, GOLD, "sub", "; font-weight: 700")
        + '<div style="flex-grow: 1"></div>'
        + footer_row(CR, swipe(CR))
        + "</div>"
    )
    return photo + top + stamp_html + bottom


# ---------------------------------------------------------------- small drawings
def check_svg(color, size=34):
    return (
        f'<svg aria-hidden="true" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="{color}" '
        f'style="stroke-width:3;stroke-linecap:round;stroke-linejoin:round;flex: none"><path d="M4 12.5 L9.5 18 L20 6.5"></path></svg>'
    )


def icon_svg(kind, size=96):
    s = f'stroke="{M}" style="stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round"'
    parts = []
    if kind == "drill":
        parts = [
            f'<rect x="12" y="28" width="44" height="22" rx="7" fill="{RED}" {s}></rect>',
            f'<path d="M28 50 L26 74 H44 L42 50" fill="{RED}" {s}></path>',
            f'<rect x="20" y="72" width="30" height="12" rx="3" fill="{M}" {s}></rect>',
            f'<rect x="56" y="32" width="12" height="14" rx="2" fill="#B9B4AC" {s}></rect>',
            f'<path d="M68 39 H90" fill="none" stroke="{M}" style="stroke-width:3.6;stroke-linecap:round"></path>',
            f'<path d="M73 36 L77 42 M79 36 L83 42" fill="none" stroke="{M}" style="stroke-width:1.6"></path>',
        ]
    elif kind == "spile":
        parts = [
            f'<rect x="6" y="18" width="18" height="44" rx="4" fill="#8A5A2B" {s}></rect>',
            f'<path d="M24 34 H54 Q60 34 60 40 V48" fill="none" stroke="{M}" style="stroke-width:9;stroke-linecap:round"></path>',
            f'<path d="M24 34 H54 Q60 34 60 40 V48" fill="none" stroke="#2F2A28" style="stroke-width:5;stroke-linecap:round"></path>',
            f'<path d="M60 48 Q60 70 74 76 Q86 82 88 92" fill="none" stroke="{SAP_EDGE}" style="stroke-width:6;stroke-linecap:round"></path>',
            f'<circle cx="60" cy="58" r="3.2" fill="{SAP}" stroke="{SAP_EDGE}" style="stroke-width:1.4"></circle>',
        ]
    elif kind == "jug":
        parts = [jug(18, 12, 1.5, SAP, SAP_EDGE, CR, stroke_w=2.4)]
    elif kind == "pot":
        parts = [
            f'<path d="M30 10 Q24 18 30 26 M48 8 Q42 17 48 26 M66 10 Q60 18 66 26" fill="none" stroke="#9BB3C4" style="stroke-width:3;stroke-linecap:round"></path>',
            f'<path d="M16 38 H80 V74 Q80 86 68 86 H28 Q16 86 16 74 Z" fill="#C9CDD2" {s}></path>',
            f'<path d="M12 38 H84" fill="none" {s}></path>',
            f'<path d="M16 48 H6 M80 48 H90" fill="none" {s}></path>',
            f'<path d="M22 52 H74" fill="none" stroke="#E0902A" style="stroke-width:5;stroke-linecap:round"></path>',
        ]
    elif kind == "thermo":
        parts = [
            f'<circle cx="48" cy="24" r="16" fill="{CR}" {s}></circle>',
            f'<path d="M48 24 L57 17" fill="none" stroke="{RED}" style="stroke-width:3;stroke-linecap:round"></path>',
            f'<path d="M38 15 L40 17 M58 31 L56 29 M48 9 V12" fill="none" stroke="{M}" style="stroke-width:2"></path>',
            f'<path d="M48 40 V90" fill="none" stroke="{M}" style="stroke-width:5;stroke-linecap:round"></path>',
            f'<rect x="54" y="44" width="10" height="16" rx="3" fill="#B9B4AC" {s}></rect>',
        ]
    elif kind == "filter":
        parts = [
            f'<path d="M14 18 H82 L54 72 H42 Z" fill="#EFE3CF" {s}></path>',
            f'<path d="M14 18 H82" fill="none" {s}></path>',
            f'<path d="M24 30 H72 M30 42 H66 M36 54 H60" fill="none" stroke="#C9B48F" style="stroke-width:2;stroke-dasharray:4 4"></path>',
            f'<path d="M48 76 Q43 84 48 88 Q53 84 48 76 Z" fill="#E0902A" stroke="#B5701C" style="stroke-width:1.6"></path>',
        ]
    return (
        f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {CR}; display: flex; align-items: center; '
        f'justify-content: center; flex: none; box-shadow: inset 0 0 0 3px #EAD9B5">'
        f'<svg aria-hidden="true" width="{size - 14}" height="{size - 14}" viewBox="0 0 96 96">{"".join(parts)}</svg></div>'
    )


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover(
        "cover", "A drop of maple sap falling from a spile into a collection bag", "03",
        stamp("FAMILY", "tradition"),
        "The perfect<br>family project.",
        "3 reasons tapping works for every age. Swipe!",
        obj_pos="50% 45%",
    )
    return root(M, inner, CR), "The perfect family project"


def slide2():
    photo = (
        f'<div data-chk="photo" style="display: flex; gap: 34px; align-items: center">'
        f'<div style="position: relative; flex: none; width: 480px; height: 320px; border-radius: 28px; overflow: hidden; box-shadow: 0 0 0 8px {GOLD}">'
        f'<img src="@@IMG_kid@@" alt="A child’s gloved hand pushing a spile into a fresh taphole" '
        f'style="width: 100%; height: 100%; object-fit: cover; display: block"></div>'
        f'<div style="display: flex; flex-direction: column; gap: 14px">'
        f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {RED}">From our guide</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 40px; line-height: 1.16; color: {M}">'
        f'Except for moving the boiling sap, kids can help with every step.</div></div></div>'
    )

    def col(title, items, bg, fg, mark, grow=1):
        rows = "".join(
            f'<div style="display: flex; gap: 14px; align-items: center; font-family: {DISPLAY}; font-weight: 600; font-size: 31px; '
            f'line-height: 1.12; color: {fg}">{check_svg(mark, 32)}<span>{t}</span></div>' for t in items)
        return (
            f'<div style="flex: {grow} 1 0; background: {bg}; border-radius: 30px; padding: 28px 30px 30px; display: flex; flex-direction: column; gap: 18px">'
            f'<div style="font-family: {TYPE}; font-size: 28px; letter-spacing: 0.06em; text-transform: uppercase; color: {fg}">{title}</div>'
            f'{rows}</div>'
        )

    cols = (
        f'<div data-chk="cols" style="display: flex; gap: 22px; align-items: stretch">'
        + col("Kids", ["Pick and mark the tree", "Set the spile, with help", "Check the jugs daily", "Measure the sap"], GOLD, M, M, grow=1.25)
        + col("Grown-ups", ["Drill the taphole", "Run the boil", "Pour the hot syrup"], M, CR, GOLD)
        + "</div>"
    )
    inner = (
        kicker_row("Reason 1 · Every age helps", "2 / 4", M)
        + headline(f'There’s a job<br>for <span style="color: {RED}">every age.</span>', 100, M)
        + '<div style="flex-grow: 1"></div>'
        + photo
        + '<div style="flex-grow: 1"></div>'
        + cols
        + '<div style="flex-grow: 1"></div>'
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=30), M), "A job for every age"


def slide3():
    tools = [
        ("drill", "Drill + 5/16″ bit", "Mark the bit at 1½ in."),
        ("spile", "Spiles + tubing", "One for each taphole"),
        ("jug", "Clean jugs", "Or buckets with lids"),
        ("pot", "A big pot", "Stainless steel is best"),
        ("thermo", "Thermometer", "Marked every degree"),
        ("filter", "Felt filter", "Catches the gritty bits"),
    ]
    tiles = "".join(
        f'<div style="background: {CR}; border-radius: 28px; padding: 22px 22px; display: flex; gap: 18px; align-items: center">'
        f'{icon_svg(k, 112)}<div style="display: flex; flex-direction: column; gap: 4px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 37px; line-height: 1.04; color: {M}">{t}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 27px; line-height: 1.2; color: {M}">{n}</div></div></div>'
        for k, t, n in tools
    )
    grid = f'<div data-chk="tools" style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px">{tiles}</div>'
    note = (
        f'<div data-chk="note" style="background: {GOLD}; color: {M}; border-radius: 28px; padding: 24px 30px; display: flex; gap: 22px; align-items: center">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 64px; line-height: 1; letter-spacing: -0.02em; flex: none">39</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 31px; line-height: 1.2">'
        f'<b style="font-weight: 800">Boil outdoors.</b> Each gallon of syrup sends about 39 gallons of water up as steam.</div></div>'
    )
    inner = (
        kicker_row("Reason 2 · Simple gear", "3 / 4", CR)
        + headline(f'No farm needed.<br><span style="color: {GOLD}">Just a few tools.</span>', 92, CR)
        + '<div style="flex-grow: 1"></div>'
        + grid
        + '<div style="flex-grow: 1"></div>'
        + note
        + '<div style="flex-grow: 1"></div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=30), CR), "Just a few tools"


def teaser(when, what, bg=M, fg=CR, title_size=44):
    return (
        f'<div data-chk="teaser" style="background: {bg}; color: {fg}; border-radius: 30px; padding: 26px 34px; display: flex; '
        f'flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase">Next up{" · " + when if when else ""}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: {title_size}px; line-height: 1.04; letter-spacing: -0.01em">{what}</div></div>'
    )


def ladder_svg(w=150, h=500):
    """A tall candy thermometer with four evenly spaced marks (not to scale)."""
    top, bot, cx = 24, h - 70, w // 2
    marks = [top + 40 + i * ((bot - top - 80) / 3) for i in range(4)]
    p = [
        f'<rect x="{cx - 22}" y="{top}" width="44" height="{bot - top + 20}" rx="22" fill="{CR}" stroke="{M}" style="stroke-width:5"></rect>',
        f'<circle cx="{cx}" cy="{bot + 24}" r="40" fill="{RED}" stroke="{M}" style="stroke-width:5"></circle>',
        f'<rect x="{cx - 10}" y="{marks[0] - 6}" width="20" height="{bot - marks[0] + 30}" rx="10" fill="{RED}"></rect>',
    ]
    for y in marks:
        p.append(f'<path d="M{cx + 24} {y:.0f} H{w - 2}" stroke="{M}" style="stroke-width:5;stroke-linecap:round"></path>')
    return marks, f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="flex: none; display: block">{"".join(p)}</svg>'


def slide4():
    H_L = 410
    marks, therm = ladder_svg(130, H_L)
    rows = [
        ("+40–45°F", "Maple sugar", False),
        ("+28–30°F", "Hard maple candy", False),
        ("+22–24°F", "Maple cream", False),
        ("+7°F", "Maple syrup: done!", True),
    ]
    labels = "".join(
        f'<div style="position: absolute; left: 0; top: {y - 34:.0f}px; display: flex; align-items: baseline; gap: 16px; white-space: nowrap">'
        f'<span style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; letter-spacing: -0.02em; color: {RED if hi else M}">{t}</span>'
        f'<span style="font-family: {DISPLAY}; font-weight: {800 if hi else 600}; font-size: 32px; color: {RED if hi else M}">{n}</span></div>'
        for y, (t, n, hi) in zip(marks, rows)
    )
    pot = (
        f'<div style="position: absolute; right: 0; top: 56px; display: flex; flex-direction: column; align-items: center; gap: 12px">'
        f'<img src="@@IMG_pot@@" alt="Sap boiling in a big stainless pot with a dial thermometer clipped on" '
        f'style="width: 230px; height: 230px; border-radius: 50%; object-fit: cover; border: 10px solid {GOLD}; display: block"></div>'
    )
    ladder = (
        f'<div data-chk="ladder" style="display: flex; gap: 22px; align-items: flex-start">{therm}'
        f'<div style="position: relative; flex: 1 1 0; height: {H_L}px">{labels}{pot}'
        f'<div style="position: absolute; left: 0; bottom: 6px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.04em; color: {M}">'
        f'°F above the boiling point of water · recipes vary a little</div></div></div>'
    )
    tip = (
        f'<div data-chk="tip" style="background: {GOLD}; color: {M}; border-radius: 26px; padding: 22px 28px; font-family: {DISPLAY}; '
        f'font-weight: 600; font-size: 31px; line-height: 1.2"><b style="font-weight: 800">Syrup a bit too thick?</b> '
        f'Stir in a splash of sap.</div>'
    )
    inner = (
        kicker_row("Reason 3 · Room for error", "4 / 4", M)
        + headline(f'Hard to<br><span style="color: {RED}">mess up.</span>', 96, M)
        + body("Syrup is done at 7°F above the boiling point of water. Keep boiling and the same syrup can become a treat:", 32, M, "sub")
        + ladder
        + tip
        + body("Grown-ups run the boil and stay with the pot: candy and sugar get far hotter than boiling water.", 27, M, "safety",
               "; font-weight: 600")
        + '<div style="flex-grow: 1"></div>'
        + teaser("", "Tree ID: the sugar maple")
        + site_footer(M)
    )
    return root(CR, column(inner, gap=24), M), "Hard to mess up"


SLIDES = [("Post03-1-Cover", slide1), ("Post03-2-EveryAge", slide2), ("Post03-3-Tools", slide3), ("Post03-4-HardToMessUp", slide4)]

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
    if mode == "preview":
        local = {k: "file://" + os.path.join(PHOTO_DIR, v) for k, v in ASSETS.items()}
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, with_images(markup, local)))
        print("preview built")
    else:
        urls = json.load(open(os.path.join(ROOT, "assets_p3.json")))
        for name, fn in SLIDES:
            markup, title = fn()
            open(os.path.join(ROOT, "canvas", "project", name + ".dc.html"), "w").write(dc_html(title, with_images(markup, urls)))
        print("canvas built")
