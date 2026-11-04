"""Post 09 - Family game: "Maple scavenger hunt!" (4 slides). Photos: Jim's real maples (p6_12 cover).
Facts (all from earlier fact-checked posts, plus craft basics):
  - smooth leaf edges with U-shaped valleys: could be sugar maple; saw-tooth edges: red or silver maple (Tree ID 1-3;
    Every Color Reel sources: USDA NRCS, Morton Arboretum, VT Dendrology)
  - sugar maple seeds ripen and drop in fall; red and silver maples drop seeds in spring (Tree ID fun facts; USDA Silvics)
  - maples have opposite buds and branches (Tree ID posts; VT Dendrology)
  - 38 in. around = about 12 in. across (12 x 3.14 = 37.7); 12 in. minimum to tap (MapleTapper Guide; UNH Extension)
  - mark trees with ribbon while they still have leaves (Post 1; MapleTapper blog: marking maple trees)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from art import SUGAR, leaf_svg  # noqa: E402
from build import DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column  # noqa: E402
from funfacts import teaser, site_footer  # noqa: E402
from wk2 import M, CR, RED, GOLD, GREEN, BARK, SPACER, stamp, cover, build_preview  # noqa: E402

ASSETS = {"cover": "p6/p6_12_2e190651.jpg", "leaves": "/home/claude/mt/jimphotos/carpet1.jpg"}


def box(size=58):
    return (f'<div style="width: {size}px; height: {size}px; border: 5px solid {M}; border-radius: 12px; background: #FFFFFF; flex: none; '
            f'box-sizing: border-box"></div>')


def hunt_item(title, note):
    return (
        f'<div style="display: flex; gap: 22px; align-items: center">{box()}<div style="display: flex; flex-direction: column; gap: 2px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 38px; line-height: 1.05; color: {M}">{title}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 28px; line-height: 1.2; color: {M}">{note}</div></div></div>'
    )


def rubbing_svg():
    w, h = 470, 520
    hatch = (f'<defs><pattern id="hatch" width="10" height="10" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">'
             f'<rect width="10" height="10" fill="#FFFFFF"></rect><path d="M0 2 H10 M0 7 H10" stroke="{RED}" style="stroke-width:3.2;stroke-opacity:0.85"></path>'
             f'</pattern></defs>')
    paper = f'<rect x="40" y="30" width="390" height="460" rx="10" fill="#FFFFFF" stroke="#E6D3AE" style="stroke-width:4" transform="rotate(-4 235 260)"></rect>'
    leaf = leaf_svg(SUGAR, 150, 230, 340, "url(#hatch)", RED, rot=0, serrate=0, stem=True, vein_w=5, vein_op=0.9)
    crayon = (f'<g transform="rotate(38 380 120)"><rect x="330" y="96" width="150" height="40" rx="8" fill="{RED}"></rect>'
              f'<rect x="352" y="96" width="70" height="40" fill="#A82A1A"></rect>'
              f'<path d="M330 96 L300 116 L330 136 Z" fill="{RED}"></path></g>')
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block; flex: none">{hatch}{paper}{leaf}{crayon}</svg>'


def num(n):
    return (f'<div style="width: 64px; height: 64px; border-radius: 50%; background: {GOLD}; color: {M}; display: flex; align-items: center; '
            f'justify-content: center; flex: none; font-family: {DISPLAY}; font-weight: 800; font-size: 36px">{n}</div>')


def slide1():
    inner = cover(
        "cover", "A big maple in bright orange fall color in a park", "Sugarmaker’s Almanac · No. 09",
        stamp("FAMILY", "game"),
        "Maple<br>scavenger hunt!",
        "A family game for this weekend. Save it and go!",
        title_size=100, obj_pos="50% 42%",
    )
    return root(M, inner, CR), "Maple scavenger hunt!"


def slide2():
    items = "".join([
        hunt_item("A leaf with smooth edges", "Could be a sugar maple, the sweetest!"),
        hunt_item("A leaf with saw-tooth edges", "Red or silver maple"),
        hunt_item("A maple “helicopter” seed", "Sugar maples drop theirs in fall"),
        hunt_item("Twigs with buds in pairs", "Maple buds grow opposite each other"),
        hunt_item("A maple 38 inches around", "That’s 12 inches across: big enough to tap!"),
        hunt_item("The biggest maple on your street", "Measure it and tell us!"),
    ])
    inner = (
        kicker_row("Family game · The hunt", "2 / 4", M)
        + headline(f'Can you<br><span style="color: {RED}">find…</span>', 116, M)
        + SPACER
        + f'<div data-chk="items" style="display: flex; flex-direction: column; gap: 22px">{items}</div>'
        + SPACER
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=26), M), "Can you find…"


def slide3():
    steps = [
        ("Lay a leaf bumpy side up", "and put a sheet of paper on top."),
        ("Rub with a peeled crayon", "using the long side, not the tip."),
        ("Label it", "Which tree did it come from?"),
    ]
    rows = "".join(
        f'<div style="display: flex; gap: 18px; align-items: flex-start">{num(i + 1)}<div style="display: flex; flex-direction: column; gap: 2px; padding-top: 4px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 36px; line-height: 1.05; color: {CR}">{t}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 28px; line-height: 1.2; color: {CR}">{n}</div></div></div>'
        for i, (t, n) in enumerate(steps)
    )
    inner = (
        kicker_row("Family game · Bonus", "3 / 4", CR)
        + headline(f'Make a<br><span style="color: {GOLD}">leaf rubbing.</span>', 110, CR)
        + SPACER
        + f'<div data-chk="rub" style="display: flex; justify-content: center">{rubbing_svg()}</div>'
        + SPACER
        + f'<div data-chk="steps" style="display: flex; flex-direction: column; gap: 22px">{rows}</div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=24), CR), "Make a leaf rubbing"


def slide4():
    photo = (
        f'<div data-chk="photo" style="position: relative; height: 330px; border-radius: 30px; overflow: hidden; flex: none">'
        f'<img src="@@IMG_leaves@@" alt="A carpet of fallen red and pink maple leaves in a park" style="width: 100%; height: 100%; object-fit: cover; '
        f'object-position: 50% 60%; display: block"></div>'
    )
    share = (
        f'<div data-chk="share" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 24px 30px; display: flex; flex-direction: column; gap: 6px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase">Show us!</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 36px; line-height: 1.12">Share your finds and tag @mapletapper.</div></div>'
    )
    inner = (
        kicker_row("Family game · Last step", "4 / 4", M)
        + headline(f'Mark your<br><span style="color: {RED}">maples.</span>', 116, M)
        + body("Tie a ribbon around every maple you found. When the leaves are gone this winter, you’ll know which trees to tap.", 33, M, "why")
        + photo
        + share
        + SPACER
        + teaser("Sunday", "Bake with maple instead of sugar", M, CR)
        + site_footer(M)
    )
    return root(CR, column(inner, gap=24), M), "Mark your maples"


SLIDES = [("Post09-1-Cover", slide1), ("Post09-2-Hunt", slide2), ("Post09-3-Rubbing", slide3), ("Post09-4-Mark", slide4)]

if __name__ == "__main__":
    for p in build_preview(SLIDES, ASSETS):
        print(p)
