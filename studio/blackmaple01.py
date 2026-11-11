"""Tree ID 04 - Black maple, sugar maple's twin (5 slides). Drawn leaves only (no real black maple photos yet).
Cover follows the Grid variety rule (Nov 11 2026): pine solid block, not a maroon band.

Facts (2+ sources each, rewritten):
- Stipules (small leafy flaps) at the base of the leaf stem; sugar maple has none; may drop late in season:
  Univ. of Illinois woody plants, Minnesota Wildflowers, Purdue Extension, UW-Green Bay herbarium.
- Leaf edges droop / look wilted: Univ. of Illinois, Purdue Extension, Ohio State F-36, UW-Green Bay.
- Fuzzy (velvety) underside: Univ. of Illinois, Minnesota Wildflowers, UW-Green Bay.
- Often treated as a subspecies of sugar maple; the two cross: Minnesota Wildflowers, UW-Green Bay, USDA FS Silvics (via MN Seasons).
- Grows on moist, rich sites incl. bottomlands: Purdue Extension, Minnesota Wildflowers.
- Most common in the Midwest: Discover Life (OH, IL, MI), UW-Green Bay (WI), Purdue (IN).
- Sap about as sweet as sugar maple: Ohio State F-36, Univ. of Missouri Center for Agroforestry; Britannica (preferred with sugar maple).
"""
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import (C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column,  # noqa: E402
                   preview_html, leaf_mark)
from post02 import pill  # noqa: E402
from art import leaf_path, leaf_svg, pol, f  # noqa: E402

PINE, SNOW = "#1F4A36", "#F7F4EE"
LEAF, LEAF_DK, VEIN = "#3E6B35", "#2B4D25", "#1E3A1A"
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()

# Black maple: 3 big lobes, small rounded basal lobes, few teeth.
BLACK = [
    (0, 1.00, "tip"), (9, 0.86, "tooth"), (13, 0.77, "notch"), (27, 0.50, "sU"), (41, 0.75, "notch"),
    (45, 0.85, "tooth"), (58, 0.99, "tip"), (71, 0.83, "tooth"), (76, 0.74, "notch"), (97, 0.44, "sU"),
    (112, 0.50, "tip"), (140, 0.34, "notch"), (163, 0.22, "notch"), (180, 0.17, "base"),
]


def stipules(s, cx, cy, fill, vein):
    """Two small leafy flaps where the leaf stem meets the twig (bottom end of the stem)."""
    bx, by = pol(0.42, 186, s, cx, cy)
    out = []
    for sign in (1, -1):
                out.append(f'<path d="M0 0 C{f(s*0.07)} {f(-s*0.05)} {f(s*0.07)} {f(-s*0.2)} 0 {f(-s*0.24)} C{f(-s*0.07)} {f(-s*0.2)} {f(-s*0.07)} {f(-s*0.05)} 0 0 Z" '
                   f'fill="{fill}" stroke="{vein}" style="stroke-width:{f(s * 0.012)}" '
                   f'transform="translate({f(bx + sign * s * 0.015)} {f(by - s * 0.02)}) rotate({52 * sign})"></path>')
    out.append(f'<rect x="{f(bx - s * 0.32)}" y="{f(by - s * 0.012)}" width="{f(s * 0.64)}" height="{f(s * 0.045)}" rx="{f(s * 0.02)}" fill="#6E5A4E"></rect>')
    return "".join(out), (bx, by)


def black_leaf(s, cx, cy, fill=LEAF, vein=VEIN, ring=None):
    st, (bx, by) = stipules(s, cx, cy, fill, vein)
    ringsvg = ""
    if ring:
        ringsvg = (f'<circle cx="{f(bx)}" cy="{f(by - s * 0.05)}" r="{f(s * 0.24)}" fill="none" stroke="{ring}" '
                   f'style="stroke-width:{f(s * 0.03)};stroke-dasharray:{f(s * 0.06)} {f(s * 0.04)}"></circle>')
    return st + leaf_svg(BLACK, s, cx, cy, fill, vein) + ringsvg, (bx, by)


def svg(w, h, inner, extra=""):
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block; flex: none{extra}">{inner}</svg>'


def logo_badge(right=48, bottom=48, size=150, bg=C["cream"]):
    return (f'<div data-chk="logo" style="position: absolute; right: {right}px; bottom: {bottom}px; width: {size}px; height: {size}px; '
            f'border-radius: 50%; background: {bg}; display: flex; align-items: center; justify-content: center; z-index: 5; '
            f'box-shadow: 0 6px 18px rgba(0,0,0,.25)"><img src="{LOGO}" alt="MapleTapper logo" style="width: {int(size * .78)}px"></div>')


def badge(inner_svg, bg=C["cream"], size=96):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; flex: none; display: flex; '
            f'align-items: center; justify-content: center; box-shadow: inset 0 0 0 3px #EAD9B5">{inner_svg}</div>')


def clue(b, main, note, color=C["maroon"]):
    return (f'<div style="display: flex; gap: 26px; align-items: center">{b}'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 42px; line-height: 1.1; color: {color}">{main}'
            f'<div style="font-weight: 500; font-size: 31px; line-height: 1.25; margin-top: 4px">{note}</div></div></div>')


# ---------------------------------------------------------------- slides

def slide1():
    leaf, (bx, by) = black_leaf(390, 540, 560, fill=C["gold"], vein="#8A5A12", ring=SNOW)
    art = svg(1080, 1350, leaf, "; position: absolute; left: 0; top: 270px")
    label = (f'<div data-chk="label" style="position: absolute; left: {int(bx) + 130}px; top: {int(by) + 270 + 40}px; font-family: {TYPE}; '
             f'font-size: 30px; letter-spacing: .05em; text-transform: uppercase; color: {SNOW}; line-height: 1.2">'
             f'↖ Look for the<br>tiny “ears”</div>')
    inner = (
        f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 56px; display: flex; justify-content: space-between; z-index: 2">'
        f'{pill("Tree ID · 4 of 9", C["gold"], PINE, 26)}{pill("15 weeks to sap season", SNOW, PINE, 26)}</div>'
        f'<div style="position: absolute; left: 56px; top: 140px; width: 900px; z-index: 2">'
        + headline("Black maple:<br>sugar maple’s twin", 116, SNOW, chk="title") + '</div>'
        + art + label
        + f'<div data-chk="handle" style="position: absolute; left: 56px; bottom: 64px; display: flex; align-items: center; gap: 10px; '
          f'font-family: {TYPE}; font-size: 28px; color: {SNOW}">{leaf_mark(SNOW, 32)}@mapletapper</div>'
        + logo_badge()
    )
    return (f'<div data-root style="position: relative; width: {W}px; height: {H}px; overflow: hidden; background: {PINE}; '
            f'font-family: {DISPLAY}">{inner}</div>'), "Tree ID 4: black maple"


def slide2():
    # simple icons
    ears = svg(80, 80, f'<rect x="8" y="58" width="64" height="6" rx="3" fill="#6E5A4E"></rect>'
                       f'<path d="M40 10 L40 60" stroke="{VEIN}" style="stroke-width:4;stroke-linecap:round"></path>'
                       f'<ellipse cx="0" cy="0" rx="9" ry="16" fill="{LEAF}" transform="translate(27 48) rotate(-62)"></ellipse>'
                       f'<ellipse cx="0" cy="0" rx="9" ry="16" fill="{LEAF}" transform="translate(53 48) rotate(62)"></ellipse>')
    droop = svg(80, 80, f'<path d="M8 58 Q16 26 40 24 Q64 26 72 58 Q60 40 40 38 Q20 40 8 58 Z" fill="{LEAF}"></path>'
                        f'<path d="M40 38 L40 66" stroke="{VEIN}" style="stroke-width:4;stroke-linecap:round"></path>')
    fuzz = "".join(f'<path d="M{x} {y} l3 -6" stroke="{LEAF_DK}" style="stroke-width:2;stroke-linecap:round"></path>'
                   for x, y in [(22, 36), (32, 30), (44, 28), (54, 32), (26, 48), (38, 44), (50, 44), (60, 46), (32, 58), (46, 56)])
    fuzzy = svg(80, 80, f'<ellipse cx="40" cy="44" rx="32" ry="24" fill="#B7CFA4"></ellipse>{fuzz}')
    big, _ = black_leaf(250, 330, 250, ring=C["red"])
    pic = (f'<div data-chk="pic" style="position: relative; overflow: hidden; height: 520px; border-radius: 30px; background: {SNOW}; flex: none">'
           + svg(1000, 520, big, "; position: absolute; left: -30px; top: -10px")
           + f'<div style="position: absolute; left: 470px; top: 330px; width: 420px; font-family: {DISPLAY}; font-weight: 700; font-size: 34px; '
             f'line-height: 1.2; color: {C["maroon"]}"><span style="color: {C["red"]}">←</span> Stipules: small leafy flaps where the leaf stem meets the twig</div>'
           + f'<span style="position: absolute; right: 22px; top: 20px; background: {C["cream"]}; color: {C["maroon"]}; border-radius: 999px; '
             f'padding: 9px 18px 7px; font-family: {TYPE}; font-size: 22px; letter-spacing: 0.05em; text-transform: uppercase">Drawing</span></div>')
    clues = (f'<div data-chk="clues" style="display: flex; flex-direction: column; gap: 26px">'
             + clue(badge(ears), "Tiny “ears” on the stem", "Sugar maple never has them")
             + clue(badge(droop), "Droopy leaf edges", "The leaf looks a little wilted")
             + clue(badge(fuzzy), "Fuzzy underside", "Soft, velvety hairs all over the back")
             + "</div>")
    inner = (kicker_row("How to spot it", "2 / 5", C["maroon"])
             + headline("3 clues it’s<br>a black maple", 92, C["maroon"])
             + pic + clues + '<div style="flex-grow: 1"></div>' + footer_row(C["maroon"], swipe(C["maroon"])))
    return root(C["cream"], column(inner, gap=28), C["maroon"]), "How to spot a black maple"


def slide3():
    rows = [("Base of leaf stem", "Bare", "Tiny leafy “ears”"),
            ("Leaf edges", "Flat", "Droop down"),
            ("Back of leaf", "Hairs mostly on the veins", "Fuzzy all over"),
            ("Where it grows", "Well-drained hills", "Also moist, low ground")]
    cell = lambda t, b=False: (f'<div style="font-family: {DISPLAY}; font-weight: {800 if b else 600}; font-size: 33px; line-height: 1.15; '
                               f'color: {C["maroon"]}">{t}</div>')
    head = (f'<div style="display: grid; grid-template-columns: 300px 1fr 1fr; gap: 18px; font-family: {TYPE}; font-size: 26px; '
            f'letter-spacing: .05em; text-transform: uppercase; color: {C["maroon"]}"><span></span><span>Sugar maple</span><span>Black maple</span></div>')
    body_rows = "".join(
        f'<div style="display: grid; grid-template-columns: 300px 1fr 1fr; gap: 18px; align-items: center; padding: 22px 0; '
        f'border-top: 3px solid rgba(122,30,26,.25)">{cell(a, True)}{cell(b)}{cell(c, True)}</div>' for a, b, c in rows)
    table = f'<div data-chk="table" style="background: {C["cream"]}; border-radius: 30px; padding: 30px 34px 10px">{head}{body_rows}</div>'
    note = body("So close that many botanists call black maple a kind of sugar maple, and the two often cross. "
                "The ears can fall off by late summer, so check a few leaves.", 34, C["maroon"], "note", "; font-weight: 600")
    inner = (kicker_row("Side by side", "3 / 5", C["maroon"])
             + headline("Twins, with<br>a few tells", 104, C["maroon"])
             + table + note + '<div style="flex-grow: 1"></div>' + footer_row(C["maroon"], swipe(C["maroon"])))
    return root(C["gold"], column(inner, gap=30), C["maroon"]), "Sugar maple vs black maple"


def slide4():
    yes = (f'<div data-chk="yes" style="display: inline-block; align-self: flex-start; background: {C["gold"]}; color: {C["maroon"]}; '
           f'border-radius: 26px; padding: 14px 40px 16px; font-family: {DISPLAY}; font-weight: 800; font-size: 120px; line-height: 1; '
           f'transform: rotate(-3deg)">Yes!</div>')
    p = lambda t, chk: body(t, 40, C["cream"], chk, "; font-weight: 600")
    rules = (f'<div data-chk="rules" style="background: {C["cream"]}; border-radius: 30px; padding: 30px 36px; display: flex; flex-direction: column; gap: 14px">'
             f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: .06em; text-transform: uppercase; color: {C["maroon"]}">Same rules as sugar maple</div>'
             + "".join(f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 36px; line-height: 1.2; color: {C["maroon"]}">🍁 {t}</div>'
                       for t in ["At least 12 inches across, 4½ feet up", "A 5/16″ tree-saver spout", "Food-grade taps, tubing and buckets"])
             + "</div>")
    inner = (kicker_row("Can you tap it?", "4 / 5", C["cream"])
             + yes
             + p("Black maple sap is about as sweet as sugar maple sap, say Ohio State and University of Missouri tree experts.", "p1")
             + p("That’s why sugarmakers tap the two side by side, often without knowing which is which.", "p2")
             + '<div style="flex-grow: 1"></div>' + rules + '<div style="flex-grow: 1"></div>'
             + footer_row(C["cream"], swipe(C["cream"])))
    return root(C["maroon"], column(inner, gap=34), C["cream"]), "Can you tap a black maple?"


def slide5():
    leaf, _ = black_leaf(150, 120, 120)
    facts = (f'<div data-chk="facts" style="display: flex; flex-direction: column; gap: 24px">'
             + body("<b>A Midwest tree.</b> It’s most common from Ohio and Michigan west to Iowa and Minnesota.", 38, C["maroon"], "f1")
             + body("<b>Loves rich, moist soil,</b> even along rivers, where sugar maple sticks to higher ground.", 38, C["maroon"], "f2")
             + body("<b>Best time to check:</b> spring and summer, while the leaves (and their ears) are still on.", 38, C["maroon"], "f3")
             + "</div>")
    cta = (f'<div data-chk="cta" style="flex: 1 1 0; background: {PINE}; color: {SNOW}; border-radius: 32px; padding: 26px 34px; display: flex; '
           f'flex-direction: column; gap: 8px"><div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; '
           f'color: {C["gold"]}">Your turn · comment below</div><div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.06">'
           f'Sugar or black? What do you think you have?</div></div>')
    inner = (kicker_row("Good to know", "5 / 5", C["maroon"])
             + f'<div style="display: flex; align-items: center; gap: 24px">{svg(240, 240, leaf)}'
               + headline("Tap it right<br>beside your<br>sugar maples", 84, C["maroon"]) + "</div>"
             + facts + '<div style="flex-grow: 1"></div>'
             + f'<div style="display: flex; align-items: center; gap: 28px">{cta}'
               f'<img data-chk="logo" src="{LOGO}" alt="MapleTapper logo, www.mapletapper.com" style="width: 210px; flex: none; display: block"></div>'
             + footer_row(C["maroon"], "<span></span>"))
    return root(C["cream"], column(inner, gap=30), C["maroon"]), "Good to know: black maple"


SLIDES = [("BlackMaple01-1-Cover", slide1), ("BlackMaple01-2-Spot", slide2), ("BlackMaple01-3-Twins", slide3),
          ("BlackMaple01-4-Tap", slide4), ("BlackMaple01-5-Know", slide5)]

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    for name, fn in SLIDES:
        markup, title = fn()
        open(os.path.join(ROOT, "preview", name + ".html"), "w").write(preview_html(title, markup))
    print("preview built")
