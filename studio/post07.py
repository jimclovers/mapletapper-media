"""Post 07 - Kids Corner: "Is your tree big enough to tap?" (4 slides). Photo: Jim's real maple trunk (jimphotos/trunk.jpg).
Facts checked against 2+ sources, Nov 4 2026:
  - measure at 4.5 ft ("breast height"); wrap a tape or string around, divide the distance around by 3.14 (pi) to get
    the distance across (Michigan State University Extension E-2915; Portland Parks & Recreation; Tucker, GA DBH sheet)
  - bump or branch at 4.5 ft: measure just above or below it (Tucker, GA; City of Milwaukie, OR)
  - tap only trees 12 in. across or more; 12-18 in. = 1 tap; bigger trees can take more than one (MapleTapper Guide to
    Maple Tapping: 12-18 in. 1 tap, 18-32 in. up to 3; UNH Good Forestry 8.3: 12-18 in. 1 tap, over 18 in. 2 taps)
  - 12 x 3.14 = 37.7 (about 38 in. around); 18 x 3.14 = 56.5 (about 57 in. around)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column  # noqa: E402
from funfacts import teaser, site_footer  # noqa: E402
from wk2 import M, CR, RED, GOLD, GREEN, BARK, SPACER, stamp, cover, build_preview  # noqa: E402

ASSETS = {"cover": "/home/claude/mt/jimphotos/trunk.jpg"}


def trunk_svg():
    w, h = 300, 660
    g, ft = 630, 112          # ground y, px per foot
    top4 = g - 4.5 * ft
    p = [f'<path d="M0 {g} H{w}" stroke="{M}" style="stroke-width:4;stroke-linecap:round"></path>']
    # back half of the string (behind the trunk)
    p.append(f'<path d="M96 {top4} A66 16 0 0 1 228 {top4}" fill="none" stroke="{GOLD}" style="stroke-width:5;stroke-opacity:0.55"></path>')
    # trunk with a little flare
    p.append(f'<defs><linearGradient id="tfade" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{BARK}" stop-opacity="0"></stop>'
             f'<stop offset="0.12" stop-color="{BARK}" stop-opacity="1"></stop></linearGradient></defs>')
    p.append(f'<path d="M100 0 H224 L226 {g - 60} Q232 {g - 10} 252 {g} H72 Q92 {g - 10} 98 {g - 60} Z" fill="url(#tfade)"></path>')
    p.append(f'<path d="M222 120 Q252 96 286 70 L292 80 Q258 108 224 142 Z" fill="{BARK}"></path>')
    for x, y0, y1 in [(122, 40, 220), (140, 260, 470), (160, 60, 300), (182, 330, 560), (204, 120, 400), (130, 500, 600), (196, 470, 610)]:
        p.append(f'<path d="M{x} {y0} Q{x + 6} {(y0 + y1) / 2} {x - 2} {y1}" fill="none" stroke="#8C6A4A" style="stroke-width:6;stroke-linecap:round"></path>')
    # front half of the string
    p.append(f'<path d="M96 {top4} A66 16 0 0 0 228 {top4}" fill="none" stroke="{GOLD}" style="stroke-width:7;stroke-linecap:round"></path>')
    # ruler on the left
    rx = 30
    p.append(f'<rect x="{rx - 16}" y="{top4 - 10}" width="32" height="{g - top4 + 10}" rx="6" fill="#F7CA63" stroke="{M}" style="stroke-width:3"></rect>')
    for i in range(5):
        y = g - i * ft
        p.append(f'<path d="M{rx - 16} {y} H{rx + 4}" stroke="{M}" style="stroke-width:3"></path>')
    p.append(f'<path d="M{rx - 16} {top4} H{rx + 16}" stroke="{RED}" style="stroke-width:5"></path>')
    p.append(f'<path d="M{rx + 20} {top4} H92" stroke="{RED}" style="stroke-width:4;stroke-dasharray:8 6"></path>')
    p.append(f'<rect x="{rx + 22}" y="{top4 - 64}" width="96" height="44" rx="22" fill="{RED}"></rect>'
             f'<text x="{rx + 70}" y="{top4 - 33}" text-anchor="middle" style="font-family: {DISPLAY}; font-weight: 800; font-size: 26px; fill: {CR}">4½ ft</text>')
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block; flex: none">{"".join(p)}</svg>'


def num(n, bg=RED, fg=CR, size=70):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; color: {fg}; display: flex; align-items: center; '
            f'justify-content: center; flex: none; font-family: {DISPLAY}; font-weight: 800; font-size: {int(size * 0.55)}px">{n}</div>')


def step(n, title, note):
    return (
        f'<div style="display: flex; gap: 20px; align-items: flex-start">{num(n)}<div style="display: flex; flex-direction: column; gap: 4px; padding-top: 6px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.04; color: {M}">{title}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 29px; line-height: 1.22; color: {M}">{note}</div></div></div>'
    )


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover(
        "cover", "A big maple trunk standing on a carpet of red fall leaves in a park", "Sugarmaker’s Almanac · No. 07",
        stamp("KIDS", "corner"),
        "Is your tree big<br>enough to tap?",
        "All you need is a string and a ruler. Swipe!",
        title_size=96, obj_pos="50% 62%",
    )
    return root(M, inner, CR), "Is your tree big enough to tap?"


def slide2():
    steps = (
        f'<div data-chk="steps" style="flex: 1; display: flex; flex-direction: column; gap: 30px">'
        + step(1, "Find 4½ feet up", "That’s “breast height,” about a grown-up’s chest.")
        + step(2, "Wrap a string around", "Keep it level and snug. Pinch where the ends meet.")
        + step(3, "Lay it on a ruler", "Now you know how far around the tree is.")
        + "</div>"
    )
    tip = (f'<div data-chk="tip" style="background: {GOLD}; color: {M}; border-radius: 26px; padding: 20px 28px; font-family: {DISPLAY}; '
           f'font-weight: 700; font-size: 30px; line-height: 1.2">Bump or branch in the way? Measure just above or below it.</div>')
    inner = (
        kicker_row("Kids Corner · Measure it", "2 / 4", M)
        + headline(f'Measure like<br><span style="color: {RED}">a forester.</span>', 100, M)
        + SPACER
        + f'<div style="display: flex; gap: 26px; align-items: flex-end">{steps}{trunk_svg()}</div>'
        + SPACER
        + tip
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=26), M), "Measure like a forester"


def slide3():
    formula = (
        f'<div data-chk="formula" style="background: {CR}; border-radius: 30px; padding: 26px 30px; display: flex; flex-direction: column; gap: 8px; '
        f'align-items: center">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 54px; line-height: 1.05; color: {M}">Around ÷ 3.14 = across</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 31px; color: {M}">Example: 38 inches around ÷ 3.14 ≈ 12 inches across</div></div>'
    )

    def size_row(around, across, verdict, bg, fg):
        return (
            f'<div style="display: flex; align-items: center; gap: 22px; background: rgba(255,245,222,0.08); border-radius: 26px; padding: 18px 22px">'
            f'<div style="width: 300px; flex: none; display: flex; flex-direction: column; gap: 2px">'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1; color: {CR}">{across}</div>'
            f'<div style="font-family: {TYPE}; font-size: 22px; letter-spacing: 0.04em; color: {GOLD}">{around}</div></div>'
            f'<div style="flex: 1; background: {bg}; color: {fg}; border-radius: 999px; padding: 14px 24px 12px; font-family: {DISPLAY}; '
            f'font-weight: 800; font-size: 31px; line-height: 1.1; text-align: center">{verdict}</div></div>'
        )
    rows = (
        f'<div data-chk="sizes" style="display: flex; flex-direction: column; gap: 16px">'
        + size_row("UNDER 38 IN. AROUND", "Under 12 in.", "Too small. Let it grow!", RED, CR)
        + size_row("38 TO 57 IN. AROUND", "12 to 18 in.", "Big enough for 1 tap", GREEN, CR)
        + size_row("OVER 57 IN. AROUND", "Over 18 in.", "Big tree: more than 1 tap", GOLD, M)
        + "</div>"
    )
    inner = (
        kicker_row("Kids Corner · Do the math", "3 / 4", CR)
        + headline(f'Now do<br><span style="color: {GOLD}">the math!</span>', 112, CR)
        + SPACER
        + formula
        + f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase; color: {GOLD}">How far across?</div>'
        + rows
        + SPACER
        + f'<div data-chk="src" style="font-family: {TYPE}; font-size: 22px; line-height: 1.35; color: {GOLD}">Size guide: MapleTapper Guide to Maple '
          f'Tapping; University of New Hampshire Extension</div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=24), CR), "Now do the math!"


def slide4():
    circle = (
        f'<svg aria-hidden="true" width="260" height="300" viewBox="0 0 260 300" style="flex: none">'
        f'<text x="130" y="30" text-anchor="middle" style="font-family: {DISPLAY}; font-weight: 800; font-size: 28px; fill: {RED}">around</text>'
        f'<circle cx="130" cy="170" r="110" fill="#C99A63"></circle>'
        f'<circle cx="130" cy="170" r="82" fill="none" stroke="#A97B48" style="stroke-width:5"></circle>'
        f'<circle cx="130" cy="170" r="54" fill="none" stroke="#A97B48" style="stroke-width:5"></circle>'
        f'<circle cx="130" cy="170" r="110" fill="none" stroke="{RED}" style="stroke-width:12"></circle>'
        f'<path d="M24 170 H236" stroke="{M}" style="stroke-width:7;stroke-linecap:round"></path>'
        f'<circle cx="24" cy="170" r="10" fill="{M}"></circle><circle cx="236" cy="170" r="10" fill="{M}"></circle>'
        f'<rect x="72" y="182" width="116" height="40" rx="20" fill="{M}"></rect>'
        f'<text x="130" y="210" text-anchor="middle" style="font-family: {DISPLAY}; font-weight: 800; font-size: 26px; fill: {CR}">across</text></svg>'
    )
    pi_text = (
        f'<div style="display: flex; flex-direction: column; gap: 10px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 46px; line-height: 1.05; color: {M}">It’s called pi (π).</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 31px; line-height: 1.25; color: {M}">Every circle is a little more than '
        f'3 times as far around as it is across. A tree trunk is close to a circle, so pi works!</div></div>'
    )
    challenge = (
        f'<div data-chk="challenge" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 26px 32px; display: flex; flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Kid challenge</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.1">Measure 3 trees. Which is biggest? '
        f'Which ones are big enough to tap?</div></div>'
    )
    inner = (
        kicker_row("Kids Corner · Fun fact", "4 / 4", M)
        + headline(f'Why<br><span style="color: {RED}">3.14?</span>', 130, M)
        + SPACER
        + f'<div data-chk="pi" style="display: flex; gap: 30px; align-items: center">{circle}{pi_text}</div>'
        + SPACER
        + challenge
        + teaser("Friday", "Real maple syrup vs pancake syrup", M, CR)
        + site_footer(M)
    )
    return root(CR, column(inner, gap=26), M), "Why 3.14?"


SLIDES = [("Post07-1-Cover", slide1), ("Post07-2-Measure", slide2), ("Post07-3-Math", slide3), ("Post07-4-Pi", slide4)]

if __name__ == "__main__":
    for p in build_preview(SLIDES, ASSETS):
        print(p)
