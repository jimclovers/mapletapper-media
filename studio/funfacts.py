"""Slide 5 'Fun fact' for Tree IDs 1-3. Graphic-only (no photos). Facts verified Oct 29 against 2+ sources each:
- Silver: saccharinum = "sugary" (Morton Arboretum/SEINet, DePauw, Stanford); saccharum = "sugar" (Wiktionary);
  silver ~1.5% < red 1.5-2% < sugar 2-2.5% (Michigan DNR, Indiana Woodland Steward, USDA, OSU).
- Red: red flowers before leaves, red twigs/buds, scarlet fall leaves (USDA NRCS, USU, VT Dendrology, Natural Lands);
  red leaf stems (UDel, UF); maple sap is colorless (Shepherd Maple Fest, J. Chem. Ed.).
- Sugar: Comfort Maple, Pelham ON, Canada's oldest known sugar maple, est. 400-500 yrs in 1975 (NPCA, Ontario Forestry
  Assn.), growing since about 1500 (Atlas Obscura, Wikipedia); repaired with bricks, concrete and guy wires (Wikipedia,
  PA Urban Forestry); far beyond a typical sugar maple's lifespan (National Observer); farms tap trees 100+ years.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, kicker_row, footer_row, headline, body, root, column  # noqa: E402
from post02 import pill  # noqa: E402
from art import SOFT, leaf_path  # noqa: E402

SPACER = '<div style="flex-grow: 1"></div>'


def teaser(when, what, bg, fg):
    return (
        f'<div data-chk="teaser" style="background: {bg}; color: {fg}; border-radius: 32px; padding: 28px 36px; display: flex; '
        f'flex-direction: column; gap: 10px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Next up{" · " + when if when else ""}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; line-height: 1.04; letter-spacing: -0.01em">{what}</div></div>'
    )


def site_footer(color):
    return footer_row(color, f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; letter-spacing: 0; color: {color}">mapletapper.com</span>')


# ---------------------------------------------------------------- silver maple: the name trap
def silver_fun():
    m, red = C["maroon"], C["red"]

    def name_card(chk, common, latin_html, meaning, pct, hi):
        ring = f"box-shadow: inset 0 0 0 6px {m};" if hi else ""
        return (
            f'<div data-chk="{chk}" style="background: {C["cream"]}; border-radius: 30px; padding: 24px 34px 26px; display: flex; '
            f'flex-direction: column; gap: 8px; {ring}">'
            f'<div style="display: flex; justify-content: space-between; align-items: center; gap: 16px">'
            f'<span style="font-family: {DISPLAY}; font-weight: 800; font-size: 38px; color: {m}">{common}</span>'
            f'{pill(pct, C["gold"], m, 24)}</div>'
            f'<div style="font-family: {TYPE}; font-size: 62px; line-height: 1.08; color: {m}">{latin_html}</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 32px; color: {m}">{meaning}</div></div>'
        )

    hl_in = (f'<span style="color: {red}; text-decoration: underline; text-decoration-thickness: 5px; '
             f'text-underline-offset: 10px">in</span>')
    cards = (
        f'<div data-chk="cards" style="display: flex; flex-direction: column; gap: 20px">'
        + name_card("card1", "Silver maple", f"Acer sacchar{hl_in}um", "Latin for “sugary”", "About 1.5% sugar", True)
        + name_card("card2", "Sugar maple", "Acer saccharum", "Latin for “sugar”", "2–2.5% sugar", False)
        + "</div>"
    )
    punch = body("Just two letters apart, yet silver maple is the least sweet of the three common tapping maples.",
                 38, m, "punch", "; font-weight: 700")
    inner = (
        kicker_row("Fun fact", "5 / 5", m)
        + headline("Its name says<br>“sugary.”", 100, m)
        + cards
        + punch
        + SPACER
        + teaser("", "Myth or fact: does tapping hurt the tree?", C["cream"], m)
        + site_footer(m)
    )
    return root(C["sky"], column(inner, gap=30), m), "Fun fact: the name trap"


# ---------------------------------------------------------------- red maple: red in every season
def _icon(svg_inner):
    return (
        f'<div style="width: 76px; height: 76px; border-radius: 50%; background: {C["cream"]}; display: flex; align-items: center; '
        f'justify-content: center; flex: none; box-shadow: inset 0 0 0 3px #EAD9B5">'
        f'<svg aria-hidden="true" width="64" height="64" viewBox="0 0 80 80">{svg_inner}</svg></div>'
    )


TWIG = "#6B3A2A"


def flower_icon():
    twig = f'<path d="M12 66 L66 16" fill="none" stroke="{TWIG}" style="stroke-width:4;stroke-linecap:round"></path>'
    dots = ""
    for (x, y) in [(26, 53), (40, 40), (54, 27)]:
        for dx, dy in [(-7, -8), (0, -11), (7, -8), (-9, -1), (9, -1)]:
            dots += (f'<path d="M{x} {y} L{x + dx * 0.7:.1f} {y + dy * 0.7:.1f}" stroke="{C["red"]}" style="stroke-width:1.6"></path>'
                     f'<circle cx="{x + dx}" cy="{y + dy}" r="3.6" fill="{C["red"]}"></circle>')
    return _icon(twig + dots)


def stem_icon():
    leaf = f'<path d="{leaf_path(SOFT, 22, 40, 44, serrate=1)}" fill="#4E7A3A"></path>'
    stem = f'<path d="M40 44 L40 70" fill="none" stroke="{C["red"]}" style="stroke-width:6;stroke-linecap:round"></path>'
    return _icon(leaf + stem)


def fall_icon():
    leaf = f'<path d="{leaf_path(SOFT, 24, 40, 48, serrate=1)}" fill="#D8352A"></path>'
    stem = f'<path d="M40 48 L40 68" fill="none" stroke="#D8352A" style="stroke-width:3.5;stroke-linecap:round"></path>'
    return _icon(leaf + stem)


def twig_icon():
    twig = (f'<path d="M18 70 L44 34 L44 14 M44 34 L64 22" fill="none" stroke="{TWIG}" '
            f'style="stroke-width:5;stroke-linecap:round;stroke-linejoin:round"></path>')
    buds = "".join(
        f'<ellipse cx="{x}" cy="{y}" rx="5" ry="7.5" fill="{C["red"]}" transform="rotate({r} {x} {y})"></ellipse>'
        for (x, y, r) in [(44, 9, 0), (67, 19, 58), (31, 52, -38)]
    )
    return _icon(twig + buds)


def red_fun():
    m, red = C["maroon"], C["red"]
    tiles = [
        ("Late winter", "Red flowers on bare branches", flower_icon()),
        ("Summer", "Red leaf stems", stem_icon()),
        ("Fall", "Scarlet leaves (usually)", fall_icon()),
        ("Winter", "Red twigs and buds", twig_icon()),
    ]

    def tile(i, season, text, icon):
        return (
            f'<div data-chk="tile{i}" style="background: #FFFFFF; border-radius: 28px; padding: 22px 24px 24px; display: flex; '
            f'flex-direction: column; gap: 12px; box-shadow: inset 0 0 0 3px #EAD9B5">'
            f'{icon}'
            f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {red}">{season}</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 36px; line-height: 1.08; color: {m}">{text}</div></div>'
        )

    grid = (f'<div data-chk="grid" style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px">'
            + "".join(tile(i, *t) for i, t in enumerate(tiles)) + "</div>")
    punch = body("Its sap? Clear as water, like every maple’s.", 40, m, "punch", "; font-weight: 700")
    inner = (
        kicker_row("Fun fact", "5 / 5", m)
        + headline(f'<span style="color: {red}">Red</span> in<br>every season.', 100, m)
        + grid
        + punch
        + SPACER
        + teaser("", "Why tapping is the perfect family project", m, C["cream"])
        + site_footer(m)
    )
    return root(C["cream"], column(inner, gap=30), m), "Fun fact: red in every season"


# ---------------------------------------------------------------- sugar maple: older than the Pilgrims
def sugar_fun():
    cr, g, m = C["cream"], C["gold"], C["maroon"]
    stops = [
        ("About 1500", "A seedling sprouts (estimated)"),
        ("1620", "The Pilgrims land"),
        ("1867", "Canada becomes a country"),
        ("Today", "Still standing, patched with bricks and held up by cables"),
    ]
    rows = "".join(
        f'<div style="position: relative; display: flex; gap: 30px; align-items: flex-start">'
        f'<div style="flex: none; width: 26px; height: 26px; margin-top: 4px; border-radius: 50%; background: {g if i < 3 else cr}; '
        f'box-shadow: 0 0 0 5px {C["red"]}"></div>'
        f'<div style="display: flex; flex-direction: column; gap: 4px">'
        f'<div style="font-family: {TYPE}; font-size: 28px; letter-spacing: 0.04em; color: {g}">{year}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 36px; line-height: 1.1; color: {cr}">{text}</div></div></div>'
        for i, (year, text) in enumerate(stops)
    )
    timeline = (
        f'<div data-chk="timeline" style="position: relative; display: flex; flex-direction: column; gap: 22px">'
        f'<div aria-hidden="true" style="position: absolute; left: 11px; top: 20px; bottom: 40px; width: 4px; border-radius: 2px; '
        f'background: {g}; opacity: 0.55"></div>'
        + rows + "</div>"
    )
    sub = body("Canada’s oldest known sugar maple, the Comfort Maple in Pelham, Ontario, is estimated at 400 to 500 years old.",
               34, g, "sub", "; font-weight: 600")
    punch = body("Care for your tree, and it can give sap for generations.", 36, cr, "punch", "; font-weight: 700")
    inner = (
        kicker_row("Fun fact", "5 / 5", cr)
        + headline("Older than<br>the Pilgrims.", 100, cr)
        + sub
        + timeline
        + punch
        + SPACER
        + teaser("", "Kids Corner: how big is a taphole?", cr, m)
        + site_footer(cr)
    )
    return root(C["red"], column(inner, gap=28), cr), "Fun fact: older than the Pilgrims"
