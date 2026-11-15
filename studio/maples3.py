"""Sugar maple, black maple, or in between? (5 slides, Jim's idea Nov 14 2026). Our own drawings.
Facts (2+ sources, own words): sugar maple usually 5 lobes with rounded U notches; black maple usually 3 lobes,
shallow notches, drooping edges, fuzzy underside, stipules at the stem base; the two cross where their ranges
overlap and the offspring mix traits (Minnesota Wildflowers, UW-Green Bay herbarium, USDA FS Silvics, Univ. of Illinois);
sap about equally sweet (Ohio State F-36, Univ. of Missouri)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column, preview_html, W, H
from covers_v2 import PINE, SNOW, SKY, NAVY, handle, logo_badge, tag, rootdiv
from art import f
from closing import card
from blackmaple01 import HALF as BLACK, YS

M, CR, G, R = C["maroon"], C["cream"], C["gold"], C["red"]
# Sugar maple: 5 separate pointed lobes, deep rounded U notches, a few pointed teeth, nearly flat base.
SUGAR = [("Q", 0.10, 0.04, 0.22, 0.02), ("Q", 0.44, 0.00, 0.68, 0.10), ("Q", 0.46, 0.00, 0.40, -0.16),
         ("Q", 0.56, -0.20, 0.80, -0.16), ("Q", 0.80, -0.28, 0.84, -0.34), ("Q", 0.96, -0.36, 1.14, -0.56),
         ("Q", 0.98, -0.58, 0.88, -0.66), ("Q", 0.90, -0.72, 0.84, -0.84), ("Q", 0.62, -0.62, 0.42, -0.46),
         ("Q", 0.24, -0.40, 0.24, -0.74), ("Q", 0.24, -0.90, 0.40, -1.00), ("Q", 0.30, -1.00, 0.26, -1.06),
         ("Q", 0.14, -1.12, 0.0, -1.34)]
VT = {id(SUGAR): ((1.14, -0.56), (0.68, 0.10)), id(BLACK): ((1.06, -0.72), (0.76, -0.02))}
GREENS = {"sugar": "#63A63F", "black": "#2F5A2B"}
VEIN = "#1E3A1A"


def leaf(half, u, ox, oy, fill, ears=False, stem=0.75):
    pt = lambda x, y: (ox + x * u, oy + y * u * YS)
    P = lambda x, y: "%s %s" % (f(pt(x, y)[0]), f(pt(x, y)[1]))
    d = ["M" + P(0, 0)] + ["Q%s %s" % (P(c[1], c[2]), P(c[3], c[4])) for c in half]
    ends = [(0.0, 0.0)] + [(c[3], c[4]) for c in half]
    for i in range(len(half) - 1, -1, -1):
        c = half[i]; ex, ey = ends[i]
        d.append("Q%s %s" % (P(-c[1], c[2]), P(-ex, ey)))
    blade = f'<path d="{" ".join(d)} Z" fill="{fill}" stroke="{VEIN}" style="stroke-width:{f(u * 0.014)};stroke-linejoin:round"></path>'
    ln = lambda a, b, w: f'<path d="M{P(*a)} L{P(*b)}" stroke="{VEIN}" fill="none" style="stroke-width:{f(u * w)};stroke-linecap:round"></path>'
    tip = half[-1]; lat, bas = VT[id(half)]
    veins = ln((0, 0), (0, tip[4] * 0.92), 0.02)
    for sg in (1, -1):
        veins += ln((0, 0), (sg * lat[0] * 0.92, lat[1] * 0.92), 0.017) + ln((0, 0), (sg * bas[0] * 0.82, bas[1] * 0.7), 0.013)
    by = oy + stem * u
    stm = f'<path d="M{f(ox)} {f(oy)} L{f(ox)} {f(by)}" stroke="{VEIN}" fill="none" style="stroke-width:{f(u * 0.03)};stroke-linecap:round"></path>'
    ear = ""
    if ears:
        ear = "".join(f'<path d="M0 0 C{f(u*0.08)} {f(-u*0.05)} {f(u*0.08)} {f(-u*0.2)} 0 {f(-u*0.25)} C{f(-u*0.08)} {f(-u*0.2)} {f(-u*0.08)} {f(-u*0.05)} 0 0 Z" '
                      f'fill="{fill}" stroke="{VEIN}" style="stroke-width:{f(u * 0.014)}" transform="translate({f(ox + sg * u * 0.015)} {f(by)}) rotate({50 * sg})"></path>' for sg in (1, -1))
    return stm + ear + blade + veins


def svg(w, h, inner, extra=""):
    return f'<svg aria-hidden="true" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display: block; flex: none{extra}">{inner}</svg>'


def slide1():
    row = leaf(SUGAR, 205, 285, 400, GREENS["sugar"]) + leaf(BLACK, 205, 795, 400, GREENS["black"], ears=True)
    def lab(x, name, l1, l2):
        return (f'<div style="position: absolute; left: {x - 240}px; top: 1010px; width: 480px; text-align: center; color: {NAVY}">'
                f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 50px; line-height: 1">{name}</div>'
                f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 34px; line-height: 1.2; margin-top: 8px">{l1}<br>{l2}</div></div>')
    inner = (f'<div style="position: absolute; left: 56px; top: 60px">{tag("Leaf detective", NAVY, G, 30)}</div>'
             f'<div style="position: absolute; left: 56px; top: 140px; width: 960px">' + headline("Sugar maple or<br>black maple?", 112, NAVY, chk="title") + "</div>"
             + svg(1080, 620, row, "; position: absolute; left: 0; top: 400px")
             + lab(285, "Sugar", "5 pointed lobes", "deep notches") + lab(795, "Black", "3 broad lobes", "shallow notches")
             + handle(NAVY) + logo_badge(bg="#FFFFFF", size=120, bottom=36))
    return rootdiv(SKY, inner), "Sugar maple or black maple?"


def profile(n, kick, head, half, fill, ears, items, bg, note=None):
    pic = (f'<div data-chk="pic" style="height: 470px; border-radius: 30px; background: {SNOW}; flex: none; position: relative; overflow: hidden">'
           + svg(1000, 470, leaf(half, 175, 500, 312, fill, ears=ears, stem=0.6))
           + f'<span style="position: absolute; right: 22px; top: 20px; background: {CR}; color: {M}; border-radius: 999px; padding: 9px 18px 7px; '
             f'font-family: {TYPE}; font-size: 22px; letter-spacing: .05em; text-transform: uppercase">Drawing</span></div>')
    li = "".join(f'<div style="display: flex; gap: 20px; align-items: flex-start"><span style="flex: none; width: 44px; height: 44px; border-radius: 50%; background: {R}; color: #fff; '
                 f'font-family: {DISPLAY}; font-weight: 800; font-size: 26px; display: flex; align-items: center; justify-content: center; margin-top: 2px">{i}</span>'
                 f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 48px; line-height: 1.14; color: {M}">{t}</span></div>' for i, t in enumerate(items, 1))
    inner = (kicker_row(kick, f"{n} / 5", M) + headline(head, 92, M) + pic
             + f'<div data-chk="items" style="display: flex; flex-direction: column; gap: 32px">{li}</div>'
             + (body(note, 32, M, "note", "; font-weight: 600") if note else "") + '<div style="flex-grow: 1"></div>' + footer_row(M, swipe(M)))
    return root(bg, column(inner, gap=26), M)


def slide2():
    return profile(2, "The classic", "Sugar maple", SUGAR, GREENS["sugar"], False,
                   ["5 pointed lobes", "Deep, rounded U-shaped notches", "Leaf lies flat", "Stem base is bare: no “ears”"], CR), "Sugar maple leaf"


def slide3():
    return profile(3, "The twin", "Black maple", BLACK, GREENS["black"], True,
                   ["Usually 3 broad lobes", "Shallow notches, edges that droop", "Fuzzy underside and leaf stem", "Tiny leafy “ears” where the stem meets the twig"], G), "Black maple leaf"


def slide4():
    pic = (f'<div data-chk="pic" style="height: 330px; border-radius: 30px; background: {SNOW}; flex: none; position: relative; overflow: hidden">'
           + svg(1000, 330, leaf(SUGAR, 105, 300, 205, GREENS["sugar"], stem=0.6) + leaf(BLACK, 105, 700, 205, GREENS["black"], ears=True, stem=0.6)
                 + f'<text x="500" y="200" text-anchor="middle" style="font-family: {DISPLAY}; font-weight: 800; font-size: 90px; fill: {M}">+</text>') + "</div>")
    cta = (f'<div data-chk="cta" style="background: {PINE}; color: {SNOW}; border-radius: 28px; padding: 22px 30px">'
           f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: .06em; text-transform: uppercase; color: {G}">Your turn · comment below</div>'
           f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 38px; line-height: 1.1; margin-top: 6px">Sugar, black or in between: which leaf is on your tree?</div></div>')
    inner = (kicker_row("The mix", "4 / 5", M) + headline("The in-between tree", 92, M) + pic
             + body("Where both trees grow, mostly in the Midwest, they cross. The young trees mix the clues: maybe 5 lobes but droopy, or 3 lobes but no ears.", 42, M, "p1", "; font-weight: 600")
             + body("<b>Good news:</b> you don’t have to pick. Sugar, black and in-between maples all tap the same way, and the sap is about as sweet.", 42, M, "p2")
             + '<div style="flex-grow: 1"></div>' + cta + footer_row(M, swipe(M)))
    return root(CR, column(inner, gap=24), M), "The in-between maple"


def slide5():
    return card("Telling maples apart is just the start.", 1080, 1350), "Closing"


SLIDES = [("maples3-1-cover", slide1), ("maples3-2-sugar", slide2), ("maples3-3-black", slide3), ("maples3-4-between", slide4), ("maples3-5-closing", slide5)]
if __name__ == "__main__":
    for name, fn in SLIDES:
        m, t = fn()
        open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview", name + ".html"), "w").write(preview_html(t, m))
    print("built")
