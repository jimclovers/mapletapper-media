"""Post 05 - Tree check: "Which maples should you skip?" (5 slides). Clears up Post 1's "no broken branches" line.
Photos: Jim's real maple photos (jim2 p07 trunk, p17 full crown). Facts checked against 2+ sources, Nov 4 2026:
  - healthy tap trees: free of fungi; few or no wounds incl. broken-off branches, large bark seams, bark sloughing off;
    full crown (UW-Madison Extension Forestry 2013); free of large dead limbs and trunk decay, avoid cavities and hollow
    branch stubs, drilling them may increase decay (South Dakota DANR 2014); risk signs incl. poor crown, prior
    defoliation, weather damage, fungus, insects, drought (Vermont FPR tapping guidelines 2019)
  - storm crown loss: under 10% tap as normal, 11-25% tap lightly (fewer, smaller holes), 26-75% don't tap
    (UNH Cooperative Extension via Northern Woodlands 2009); over 25% tap lightly or not, wait several years
    (Michigan State University Extension, ask.extension.org 2026)
  - healthy trees wall off the wound and close a taphole in 1-3 years; tap only clean white wood; 12 in. minimum
    (UNH Good Forestry in the Granite State 8.3); tapping takes sugar the tree would use for new growth (UW-Madison);
    tapping a limb-loss-stressed maple likely hinders recovery (Northern Woodlands)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column  # noqa: E402
from funfacts import teaser, site_footer  # noqa: E402
from wk2 import (M, CR, RED, GOLD, GREEN, BARK, SPACER, stamp, cover, circle_badge, check_mark, x_mark, row,  # noqa: E402
                 build_preview)

ASSETS = {"cover": "/home/claude/mt/jim2/p07_d43e50b6.jpg", "full": "/home/claude/mt/jim2/p17_b5d463a4.jpg"}


# ---------------------------------------------------------------- drawings
CANOPY = {"c": (100, 92, 58), "l": (55, 104, 40), "r": (145, 104, 40), "ul": (72, 58, 37), "ur": (128, 58, 37), "t": (100, 40, 34)}


def tree_svg(lost, notch=False, w=230):
    h = int(w * 215 / 200)
    p = [f'<path d="M91 205 L94 120 H106 L109 205 Z" fill="{BARK}"></path>']
    dash = f'fill="none" stroke="{M}" style="stroke-width:3;stroke-dasharray:7 6"'
    for k in lost:
        x, y, r = CANOPY[k]
        p.append(f'<circle cx="{x}" cy="{y}" r="{r}" {dash}></circle>')
    if notch:
        p.append(f'<circle cx="171" cy="70" r="14" {dash}></circle>')
    for k, (x, y, r) in CANOPY.items():
        if k not in lost:
            p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{GREEN}"></circle>')
    return (f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 200 215" style="display: block">{"".join(p)}</svg>')


def flag_icon(kind):
    s = f'stroke="{CR}" fill="none" style="stroke-width:5;stroke-linecap:round;stroke-linejoin:round"'
    if kind == "limb":
        return (f'<path d="M12 62 L46 31" stroke="{CR}" style="stroke-width:9;stroke-linecap:round"></path>'
                f'<path d="M41 27 L52 21 L50 29 L60 27 L52 37 Z" fill="{CR}"></path>'
                f'<path d="M28 48 L22 34" {s}></path>')
    if kind == "rot":
        return (f'<path d="M27 8 V72 M53 8 V72" {s}></path>'
                f'<ellipse cx="40" cy="42" rx="9" ry="14" fill="{M}" stroke="{CR}" style="stroke-width:4"></ellipse>')
    if kind == "fungus":
        return (f'<path d="M15 42 Q40 8 65 42 Z" fill="{CR}"></path>'
                f'<rect x="33" y="42" width="14" height="22" rx="4" fill="{CR}"></rect>'
                f'<path d="M14 66 H66" {s}></path>')
    if kind == "crack":
        return (f'<path d="M24 8 V72 M56 8 V72" {s}></path>'
                f'<path d="M40 10 L35 25 L44 38 L36 52 L41 70" {s}></path>')
    if kind == "thin":
        return (f'<circle cx="40" cy="32" r="24" fill="none" stroke="{CR}" style="stroke-width:3;stroke-dasharray:5 5"></circle>'
                f'<path d="M40 74 V44 M40 54 L27 41 M40 48 L53 36" {s}></path>'
                f'<circle cx="27" cy="39" r="5" fill="{CR}"></circle><circle cx="54" cy="34" r="5" fill="{CR}"></circle>')
    return ""


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover(
        "cover", "Close-up of a big maple trunk with deeply furrowed bark, fall leaves on the ground", "Sugarmaker’s Almanac · No. 05",
        stamp("TREE", "check"),
        "Which maples<br>should you skip?",
        "A missing twig is fine. Here’s what isn’t. Swipe!",
        title_size=96, obj_pos="50% 44%",
    )
    return root(M, inner, CR), "Which maples should you skip?"


def slide2():
    photo = (
        f'<div data-chk="photo" style="position: relative; height: 400px; border-radius: 30px; overflow: hidden; flex: none">'
        f'<img src="@@IMG_full@@" alt="A maple with a full, healthy crown in fall color" style="width: 100%; height: 100%; object-fit: cover; '
        f'object-position: 50% 30%; display: block">'
        f'<div style="position: absolute; left: 24px; bottom: 22px; background: {CR}; color: {M}; border-radius: 999px; padding: 10px 24px 9px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 28px">A full, healthy crown: tap-ready</div></div>'
    )
    ok = circle_badge(check_mark(CR), GREEN, size=96, ring="#4E7A40")
    rows = "".join([
        row(ok, "A few lost twigs or small branches", "Normal wear for a big tree.", M, 40, 30),
        row(ok, "Rough, deeply furrowed bark", "Normal on older maples.", M, 40, 30),
        row(ok, "An old scar that has grown over", "Just tap clean wood away from it.", M, 40, 30),
    ])
    inner = (
        kicker_row("Tree check · Still tap-ready", "2 / 5", M)
        + headline(f'A missing twig?<br><span style="color: {RED}">Tap away.</span>', 96, M)
        + photo
        + f'<div data-chk="rows" style="display: flex; flex-direction: column; gap: 24px">{rows}</div>'
        + SPACER
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=28), M), "A missing twig? Tap away."


def slide3():
    def card(lost, notch, pct, verdict, vcol, vtext, small):
        return (
            f'<div style="flex: 1; background: {CR}; border-radius: 28px; padding: 22px 16px 24px; display: flex; flex-direction: column; '
            f'align-items: center; gap: 10px">{tree_svg(lost, notch, 250)}'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 42px; line-height: 1; color: {M}; text-align: center">{pct}</div>'
            f'<div style="font-family: {TYPE}; font-size: 22px; letter-spacing: 0.05em; text-transform: uppercase; color: {M}">of the crown lost</div>'
            f'<div style="background: {vcol}; color: {vtext}; border-radius: 999px; padding: 9px 20px 8px; font-family: {DISPLAY}; font-weight: 800; '
            f'font-size: 29px; white-space: nowrap">{verdict}</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 25px; line-height: 1.15; color: {M}; text-align: center">{small}</div></div>'
        )
    cards = (
        f'<div data-chk="cards" style="display: flex; gap: 22px">'
        + card([], True, "Under 10%", "Tap as usual", GREEN, CR, "A few lost branches")
        + card(["ur"], False, "10 to 25%", "Tap lightly", GOLD, M, "One small tap")
        + card(["ur", "r", "t"], False, "Over 25%", "Skip it", RED, CR, "Give it a few years")
        + "</div>"
    )
    inner = (
        kicker_row("Tree check · Storm damage", "3 / 5", CR)
        + headline(f'Storm took<br><span style="color: {GOLD}">some branches?</span>', 92, CR)
        + body("Look up at the crown, the leafy top of the tree. About how much is gone?", 34, CR, "lead")
        + SPACER
        + cards
        + SPACER
        + f'<div data-chk="src" style="font-family: {TYPE}; font-size: 23px; line-height: 1.35; color: {GOLD}">Guidelines: University of New Hampshire '
          f'and Michigan State University Extension</div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=26), CR), "Storm took some branches?"


def slide4():
    flags = [
        ("limb", "Big dead limbs", "Large dead branches still on the trunk."),
        ("rot", "Rot", "Cavities, soft wood, hollow branch stubs."),
        ("fungus", "Mushrooms or fungus", "Growing on the trunk or roots."),
        ("crack", "Long cracks or peeling bark", "Deep seams, or bark falling away."),
        ("thin", "A thin, struggling crown", "Or leaves stripped by insects or drought last summer."),
    ]
    rows = "".join(row(circle_badge(flag_icon(k), RED, size=100, ring="#A82A1A"), t, n, M, 42, 30) for k, t, n in flags)
    inner = (
        kicker_row("Tree check · Red flags", "4 / 5", M)
        + headline(f'Skip trees<br><span style="color: {RED}">with these.</span>', 104, M)
        + SPACER
        + f'<div data-chk="rows" style="display: flex; flex-direction: column; gap: 22px">{rows}</div>'
        + SPACER
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=28), M), "Skip trees with these"


def slide5():
    item = lambda t: (f'<div style="display: flex; gap: 12px; align-items: center"><svg aria-hidden="true" width="40" height="40" viewBox="0 0 80 80" '
                      f'style="flex: none">{check_mark(GREEN, 9)}</svg><span style="font-family: {DISPLAY}; font-weight: 700; font-size: 31px; '
                      f'line-height: 1.1; color: {M}">{t}</span></div>')
    checklist = (
        f'<div data-chk="checklist" style="background: {CR}; border-radius: 30px; padding: 26px 32px 30px; display: flex; flex-direction: column; gap: 16px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase; color: {M}">Tap-ready checklist</div>'
        f'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px 20px">'
        + item("12+ inches across") + item("Full, leafy crown") + item("Solid trunk, no rot") + item("Clean wood, away from old holes")
        + "</div></div>"
    )
    inner = (
        kicker_row("Tree check · Why it matters", "5 / 5", CR)
        + headline(f'Why skip<br><span style="color: {GOLD}">a hurt tree?</span>', 96, CR)
        + body("A taphole is a small wound. A healthy maple walls it off and grows over it in 1 to 3 years. "
               "A hurt tree needs its stored sugar to heal, and drilling near rot can make it worse.", 33, CR, "why")
        + SPACER
        + checklist
        + SPACER
        + teaser("Wednesday", "Myth or fact: too warm for Midwest sugar maples?", GOLD, M)
        + site_footer(CR)
    )
    return root(M, column(inner, gap=26), CR), "Why skip a hurt tree?"


SLIDES = [("Post05-1-Cover", slide1), ("Post05-2-StillOK", slide2), ("Post05-3-Storm", slide3), ("Post05-4-RedFlags", slide4),
          ("Post05-5-Why", slide5)]

if __name__ == "__main__":
    for p in build_preview(SLIDES, ASSETS):
        print(p)
