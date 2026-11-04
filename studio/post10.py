"""Post 10 - Swap guide: "Bake with maple instead of sugar" (4 slides). Illustrated cover (no baking photos on hand).
Facts checked against 2+ sources, Nov 4 2026:
  - use 3/4 cup maple syrup per 1 cup granulated sugar; cut other liquid by 2-4 Tbsp per cup of syrup; add 1/4-1/2 tsp
    baking soda unless the recipe has buttermilk, sour milk or sour cream; lower the oven 25 F because maple browns
    faster (University of Maine Extension "Make Mine Real Maple Syrup" 2022; Vermont Maple Sugar Makers' Association)
  - swap chart 2 c -> 1 1/2 c; 1 1/2 c -> 1 1/8 c; 1 c -> 3/4 c; 3/4 c -> 1/2 c + 1 Tbsp; 1/2 c -> 1/4 c + 2 Tbsp;
    1/4 c -> 3 Tbsp (UMaine Extension table; matches the 3/4 ratio)
  - darker grades taste stronger: Golden/Delicate, Amber/Rich, Dark/Robust, Very Dark/Strong (USDA AMS grade standards 2015)
  - holiday recipes in the MapleTapper Guide to Maple Tapping: maple mashed sweet potatoes, maple bacon Brussels sprouts,
    maple caramel sauce, maple granola
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column  # noqa: E402
from funfacts import site_footer  # noqa: E402
from wk2 import M, CR, RED, GOLD, GREEN, SPACER, stamp, cover_custom, build_preview  # noqa: E402

ASSETS = {}
SYRUP_C = "#B8651B"


def cup(x, fill_frac, kind):
    """A glass measuring cup at x; fill_frac of the 1-cup line filled with sugar or syrup."""
    top, bot, w = 90, 470, 300
    one_cup = 150                       # y of the 1-cup line
    p = []
    lvl = bot - (bot - one_cup) * fill_frac
    # contents (clip to cup body)
    p.append(f'<clipPath id="cup{kind}"><path d="M{x} {top} H{x + w} L{x + w - 26} {bot} Q{x + w - 30} {bot + 20} {x + w - 50} {bot + 20} '
             f'H{x + 50} Q{x + 30} {bot + 20} {x + 26} {bot} Z"></path></clipPath>')
    if kind == "sugar":
        dots = "".join(f'<circle cx="{x + 30 + (i * 37) % (w - 40)}" cy="{lvl + 14 + (i * 23) % int(bot - lvl)}" r="5" fill="#E9E1D2"></circle>'
                       for i in range(60))
        p.append(f'<g clip-path="url(#cup{kind})"><rect x="{x}" y="{lvl}" width="{w}" height="{bot - lvl + 30}" fill="#FFFFFF"></rect>{dots}'
                 f'<path d="M{x} {lvl + 6} Q{x + w / 2} {lvl - 14} {x + w} {lvl + 6}" fill="#FFFFFF"></path></g>')
    else:
        p.append(f'<g clip-path="url(#cup{kind})"><rect x="{x}" y="{lvl}" width="{w}" height="{bot - lvl + 30}" fill="{SYRUP_C}"></rect>'
                 f'<rect x="{x}" y="{lvl}" width="{w}" height="14" fill="#D9862E"></rect></g>')
    # glass outline + handle
    p.append(f'<path d="M{x} {top} H{x + w} L{x + w - 26} {bot} Q{x + w - 30} {bot + 20} {x + w - 50} {bot + 20} H{x + 50} '
             f'Q{x + 30} {bot + 20} {x + 26} {bot} Z" fill="#FFFFFF" fill-opacity="0.25" stroke="{M}" '
             f'style="stroke-width:8;stroke-linejoin:round"></path>')
    p.append(f'<path d="M{x + w - 8} {top + 70} Q{x + w + 80} {top + 80} {x + w + 66} {top + 190} Q{x + w + 58} {top + 250} {x + w - 22} {top + 260}" '
             f'fill="none" stroke="{M}" style="stroke-width:8;stroke-linecap:round"></path>')
    # measuring lines
    for frac, lab in [(1.0, "1 cup"), (0.75, "¾"), (0.5, "½"), (0.25, "¼")]:
        y = bot - (bot - one_cup) * frac
        p.append(f'<path d="M{x + 34} {y} H{x + 84}" stroke="{RED}" style="stroke-width:5;stroke-linecap:round"></path>'
                 f'<text x="{x + 94}" y="{y + 9}" style="font-family: {DISPLAY}; font-weight: 800; font-size: 26px; fill: {RED}">{lab}</text>')
    return "".join(p)


def cover_art():
    w, h = 1000, 600
    p = [cup(40, 1.0, "sugar"), cup(560, 0.75, "syrup")]
    p.append(f'<text x="478" y="330" text-anchor="middle" style="font-family: {DISPLAY}; font-weight: 800; font-size: 120px; fill: {M}">=</text>')
    lab = lambda x, t: f'<text x="{x}" y="560" text-anchor="middle" style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; fill: {M}">{t}</text>'
    p.append(lab(190, "1 cup sugar") + lab(710, "¾ cup maple syrup"))
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block; margin-top: 60px">{"".join(p)}</svg>'


def num(n, bg=RED, fg=CR, size=72):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; color: {fg}; display: flex; align-items: center; '
            f'justify-content: center; flex: none; font-family: {DISPLAY}; font-weight: 800; font-size: {int(size * 0.55)}px">{n}</div>')


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover_custom(
        cover_art(), "Sugarmaker’s Almanac · No. 10", stamp("SWAP", "guide"),
        "Bake with maple<br>instead of sugar",
        "The easy swap for holiday baking. Save it!",
        title_size=96,
    )
    return root(M, inner, CR), "Bake with maple instead of sugar"


def slide2():
    steps = [
        ("Use ¾ cup maple syrup", "for every 1 cup of white sugar."),
        ("Cut other liquids", "by 2 to 4 tablespoons for each cup of syrup."),
        ("Add a little baking soda", "¼ to ½ teaspoon, unless the recipe has buttermilk, sour milk or sour cream."),
        ("Lower the oven 25°F", "Maple browns faster at the edges."),
    ]
    rows = "".join(
        f'<div style="display: flex; gap: 22px; align-items: flex-start">{num(i + 1)}<div style="display: flex; flex-direction: column; gap: 4px; padding-top: 6px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; line-height: 1.04; color: {M}">{t}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 31px; line-height: 1.22; color: {M}">{n}</div></div></div>'
        for i, (t, n) in enumerate(steps)
    )
    inner = (
        kicker_row("Swap guide · How to", "2 / 4", M)
        + headline(f'The 4-step<br><span style="color: {RED}">maple swap.</span>', 108, M)
        + SPACER
        + f'<div data-chk="steps" style="display: flex; flex-direction: column; gap: 32px">{rows}</div>'
        + SPACER
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=28), M), "The 4-step maple swap"


def slide3():
    pairs = [("2 cups", "1½ cups"), ("1½ cups", "1⅛ cups"), ("1 cup", "¾ cup"), ("¾ cup", "½ cup + 1 Tbsp"),
             ("½ cup", "¼ cup + 2 Tbsp"), ("¼ cup", "3 Tbsp")]
    head = (f'<div style="display: flex; padding: 0 30px 6px; font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; '
            f'text-transform: uppercase; color: {GOLD}"><span style="flex: 1">Sugar</span><span style="flex: 1.3">Maple syrup</span></div>')
    rows = "".join(
        f'<div style="display: flex; align-items: center; padding: 18px 30px; border-radius: 22px; background: {CR if i % 2 == 0 else "#F6E7C4"}">'
        f'<span style="flex: 1; font-family: {DISPLAY}; font-weight: 700; font-size: 42px; color: {M}">{a}</span>'
        f'<span style="flex: 1.3; font-family: {DISPLAY}; font-weight: 800; font-size: 42px; color: {RED}">{b}</span></div>'
        for i, (a, b) in enumerate(pairs)
    )
    inner = (
        kicker_row("Swap guide · Quick chart", "3 / 4", CR)
        + headline(f'Swap<br><span style="color: {GOLD}">chart.</span>', 120, CR)
        + SPACER
        + f'<div data-chk="chart" style="display: flex; flex-direction: column; gap: 10px">{head}{rows}</div>'
        + SPACER
        + f'<div data-chk="src" style="font-family: {TYPE}; font-size: 22px; line-height: 1.35; color: {GOLD}">Sources: University of Maine '
          f'Extension; Vermont Maple Sugar Makers’ Association</div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=24), CR), "Swap chart"


def slide4():
    dishes = ["Maple mashed sweet potatoes", "Maple bacon Brussels sprouts", "Maple caramel sauce", "Maple granola"]
    from build import leaf_mark
    chips = "".join(f'<div style="display: flex; gap: 18px; align-items: center; background: #FFFFFF; border: 4px solid {M}; border-radius: 26px; '
                    f'padding: 16px 26px">{leaf_mark(RED, 44)}<span style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; '
                    f'line-height: 1.05; color: {M}">{d}</span></div>' for d in dishes)
    tip = (
        f'<div data-chk="tip" style="background: {M}; color: {CR}; border-radius: 30px; padding: 26px 32px; display: flex; flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase; color: {GOLD}">Flavor tip</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 37px; line-height: 1.14">Want more maple flavor? Use a darker syrup. '
        f'Dark and very dark grades taste the strongest.</div></div>'
    )
    save = (
        f'<div data-chk="save" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 24px 32px; font-family: {DISPLAY}; '
        f'font-weight: 800; font-size: 38px; line-height: 1.12">Save this post for holiday baking!</div>'
    )
    inner = (
        kicker_row("Swap guide · Holiday ideas", "4 / 4", M)
        + headline(f'Maple on the<br><span style="color: {RED}">holiday table.</span>', 96, M)
        + body("A few favorites from our Guide to Maple Tapping:", 33, M, "lead")
        + f'<div data-chk="dishes" style="display: flex; flex-direction: column; gap: 14px">{chips}</div>'
        + SPACER
        + tip
        + save
        + site_footer(M)
    )
    return root(CR, column(inner, gap=26), M), "Maple on the holiday table"


SLIDES = [("Post10-1-Cover", slide1), ("Post10-2-Steps", slide2), ("Post10-3-Chart", slide3), ("Post10-4-Holiday", slide4)]

if __name__ == "__main__":
    for p in build_preview(SLIDES, ASSETS):
        print(p)
