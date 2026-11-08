"""Maple Kitchen recipe series (Jim, Nov 8 2026): watercolor / colored-pencil illustrated recipe carousels.
Distinct look from the Almanac: warm paper, Cormorant Garamond + Caveat, painted-look SVG illustrations (drawn in code,
watercolor effect via SVG filters). 4 slides: cover, ingredients, steps, free-cookbook CTA + logo.
Usage: python3 kitchen.py -> preview/Kitchen01-N.html
"""
import base64
import math
import os
import random

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = "/home/claude/node/node_modules/@fontsource"
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()
W, H = 1080, 1350
PAPER, INK, AMBER, RUST, SAGE, BERRY = "#F6EEDC", "#3B2A1E", "#C9822B", "#B5502A", "#6E8B5A", "#7A1E1A"
SERIF = "'Cormorant Garamond', Georgia, serif"
HAND = "'Caveat', 'Comic Sans MS', cursive"


def faces():
    out = []
    for fam, sub, wt, st in [("Cormorant Garamond", "cormorant-garamond", 500, "normal"), ("Cormorant Garamond", "cormorant-garamond", 600, "normal"),
                             ("Cormorant Garamond", "cormorant-garamond", 700, "normal"), ("Cormorant Garamond", "cormorant-garamond", 600, "italic"),
                             ("Caveat", "caveat", 600, "normal")]:
        out.append(f"@font-face{{font-family:'{fam}';font-style:{st};font-weight:{wt};src:url('file://{FONTS}/{sub}/files/{sub}-latin-{wt}-{st}.woff2') format('woff2')}}")
    return "".join(out)


DEFS = """
<filter id="wc" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="3" seed="4" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="14" xChannelSelector="R" yChannelSelector="G" result="d"/>
  <feGaussianBlur in="d" stdDeviation="0.8" result="b"/>
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="9" result="g"/>
  <feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.4 1.25" result="ga"/>
  <feComposite in="b" in2="ga" operator="in" result="grain"/>
  <feComposite in="grain" in2="b" operator="arithmetic" k2="0.55" k3="0.5"/>
</filter>
<filter id="edge" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="2" result="n"/>
  <feDisplacementMap in="SourceGraphic" in2="n" scale="9" xChannelSelector="R" yChannelSelector="G"/>
</filter>
<filter id="paper"><feTurbulence type="fractalNoise" baseFrequency="0.75" numOctaves="3" seed="5"/>
  <feColorMatrix type="matrix" values="0 0 0 0 0.45  0 0 0 0 0.36  0 0 0 0 0.25  0 0 0 0.10 0"/></filter>
"""


def wash(shape, fill, edge=None, op=0.85):
    """A watercolor wash: soft displaced fill plus a darker pigment edge."""
    edge = edge or fill
    return (f'<g filter="url(#wc)" opacity="{op}">{shape.replace("FILL", fill)}</g>'
            f'<g filter="url(#edge)" fill="none" stroke="{edge}" stroke-opacity=".55" style="stroke-width:3">{shape.replace("FILL", "none")}</g>')


def carrots_dish(cx, cy, s=1.0, seed=3):
    r = random.Random(seed)
    o = []
    # dish shadow, dish body and rim
    o.append(wash(f'<ellipse cx="{cx+8*s}" cy="{cy+26*s}" rx="{330*s}" ry="{120*s}" fill="FILL"/>', "#8C7A66", op=.25))
    o.append(wash(f'<ellipse cx="{cx}" cy="{cy}" rx="{330*s}" ry="{125*s}" fill="FILL"/>', "#F9F6EF", "#7C93A8", op=1))
    o.append(wash(f'<ellipse cx="{cx}" cy="{cy}" rx="{330*s}" ry="{125*s}" fill="none" stroke="FILL" style="stroke-width:{14*s}"/>', "#5F86A6", op=.55))
    o.append(wash(f'<ellipse cx="{cx}" cy="{cy+6*s}" rx="{262*s}" ry="{88*s}" fill="FILL"/>', "#EFE6D6", "#B9A88F", op=.9))
    # glazed amber pool
    o.append(wash(f'<ellipse cx="{cx}" cy="{cy+10*s}" rx="{240*s}" ry="{74*s}" fill="FILL"/>', AMBER, op=.35))
    # carrot coins
    coins = []
    for _ in range(46):
        a, rr = r.uniform(0, 2 * math.pi), r.uniform(0, 1) ** 0.6
        x, y = cx + math.cos(a) * rr * 215 * s, cy + 8 * s + math.sin(a) * rr * 60 * s
        coins.append((y, x, r.uniform(24, 34) * s))
    for y, x, rad in sorted(coins):
        o.append(wash(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rad:.1f}" ry="{rad*.62:.1f}" fill="FILL"/>', "#E07A26", "#A9461A", op=.95))
        o.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{rad*.45:.1f}" ry="{rad*.27:.1f}" fill="#F2A14E" opacity=".75" filter="url(#wc)"/>')
        o.append(f'<path d="M{x-rad*.5:.1f} {y-rad*.25:.1f} q{rad*.3:.1f} {-rad*.18:.1f} {rad*.7:.1f} 0" fill="none" stroke="#FFF4DC" stroke-opacity=".8" style="stroke-width:{2.5*s}"/>')
    # thyme sprigs
    for k in range(5):
        x0, y0 = cx + r.uniform(-170, 170) * s, cy + r.uniform(-30, 40) * s
        ang = r.uniform(-0.6, 0.6)
        L = r.uniform(70, 110) * s
        x1, y1 = x0 + math.cos(ang) * L, y0 + math.sin(ang) * L * .4
        o.append(f'<path d="M{x0:.1f} {y0:.1f} L{x1:.1f} {y1:.1f}" stroke="#5B6E3E" style="stroke-width:{2.2*s}" filter="url(#edge)"/>')
        for t in [i / 7 for i in range(1, 7)]:
            lx, ly = x0 + (x1 - x0) * t, y0 + (y1 - y0) * t
            for side in (-1, 1):
                o.append(f'<ellipse cx="{lx:.1f}" cy="{ly + side*6*s:.1f}" rx="{5*s:.1f}" ry="{2.6*s:.1f}" fill="{SAGE}" opacity=".9" filter="url(#wc)"/>')
    return "".join(o)


def syrup_bottle(x, y, s=1.0):
    body = f'M{x} {y} q{-60*s} {10*s} {-62*s} {90*s} q{0} {80*s} {62*s} {86*s} q{62*s} {-6*s} {62*s} {-86*s} q{-2*s} {-80*s} {-62*s} {-90*s} z'
    o = [wash(f'<ellipse cx="{x+6*s}" cy="{y+178*s}" rx="{78*s}" ry="{16*s}" fill="FILL"/>', "#8C7A66", op=.25),
         wash(f'<path d="{body}" fill="FILL"/>', "#B8641C", "#7A3A10", op=.9),
         f'<path d="M{x-34*s} {y+40*s} q{-10*s} {40*s} {4*s} {80*s}" fill="none" stroke="#F7D49A" stroke-opacity=".8" style="stroke-width:{7*s}" filter="url(#edge)"/>',
         wash(f'<rect x="{x-14*s}" y="{y-58*s}" width="{28*s}" height="{62*s}" rx="{8*s}" fill="FILL"/>', "#C9822B", "#7A3A10", op=.8),
         wash(f'<rect x="{x-18*s}" y="{y-78*s}" width="{36*s}" height="{24*s}" rx="{6*s}" fill="FILL"/>', "#3B2A1E", op=.85),
         wash(f'<rect x="{x-44*s}" y="{y+70*s}" width="{88*s}" height="{44*s}" rx="{6*s}" fill="FILL"/>', "#F3E7CF", "#7A3A10", op=.95),
         f'<text x="{x}" y="{y+100*s}" text-anchor="middle" font-family="{HAND}" font-size="{26*s}" fill="{BERRY}">maple</text>']
    return "".join(o)


def leaf(x, y, s, col, rot=0):
    d = ("M0 -40 L8 -18 L24 -26 L18 -6 L38 -8 L26 6 L32 12 L10 12 L12 30 L0 22 L-12 30 L-10 12 L-32 12 L-26 6 L-38 -8 L-18 -6 L-24 -26 L-8 -18 Z")
    return f'<g transform="translate({x} {y}) rotate({rot}) scale({s})">{wash(f"<path d=\"{d}\" fill=\"FILL\"/>", col, op=.8)}</g>'


def svg(w, h, inner):
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" style="display:block">'
            f'<defs>{DEFS}</defs>{inner}</svg>')


def page(inner, bg=PAPER):
    grain = svg(W, H, f'<rect width="{W}" height="{H}" filter="url(#paper)"/>')
    return (f'<!doctype html><html><head><meta charset="utf-8"><style>{faces()} body{{margin:0}}</style></head><body>'
            f'<div data-root style="position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{bg};font-family:{SERIF};color:{INK}">'
            f'<div style="position:absolute;inset:0;pointer-events:none">{grain}</div>'
            f'<div style="position:absolute;inset:34px;border:2px solid {INK}22;border-radius:6px;pointer-events:none"></div>'
            f'<div style="position:relative;z-index:1;width:{W}px;height:{H}px;box-sizing:border-box;padding:76px 84px 64px;display:flex;flex-direction:column">{inner}</div>'
            f'</div></body></html>')


def masthead(no, right):
    return (f'<div data-chk="mast" style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:2px solid {INK};padding-bottom:12px">'
            f'<span style="font-weight:700;font-size:34px;letter-spacing:.18em;text-transform:uppercase">Maple Kitchen</span>'
            f'<span style="font-style:italic;font-weight:600;font-size:30px;color:{RUST}">{no} · {right}</span></div>')


def footer():
    return (f'<div data-chk="foot" style="display:flex;justify-content:space-between;align-items:center;font-size:28px;font-style:italic;font-weight:600;color:{INK}99">'
            f'<span>@mapletapper</span><span>Swipe for the recipe →</span></div>')


R = dict(
    no="No. 01", art="k01_carrots.jpg", title="Maple-Glazed Carrots", kicker="A weeknight side dish", time="20 minutes", serves="Serves 4",
    blurb="Sweet, glossy and done in one pan. Real maple syrup gives carrots a buttery glaze that kids actually eat.",
    ingredients=[("1 lb", "carrots, peeled and sliced into coins"), ("1 tbsp", "butter"), ("2 tbsp", "pure maple syrup"),
                 ("¼ tsp", "salt, plus a pinch for the water"), ("", "black pepper, to taste"), ("", "fresh thyme or parsley (optional)")],
    steps=["Simmer the carrot coins in lightly salted water until just tender, 6 to 8 minutes. Drain.",
           "In the same pan, melt the butter over medium heat. Stir in the maple syrup and salt.",
           "Add the carrots and stir for 2 to 3 minutes, until the glaze turns thick and glossy.",
           "Season with pepper, scatter on the herbs, and serve warm."],
    tip="Darker syrup grades taste more mapley, perfect for glazes.",
    cta_q="What should we cook with maple next?",
)


def slide1(r):
    art = (f'<img src="file://{ROOT}/photos/ai/{r["art"]}" alt="" style="width:1000px;height:563px;object-fit:cover;display:block;'
           f'-webkit-mask-image:radial-gradient(ellipse 72% 70% at 50% 50%, #000 62%, transparent 100%);mask-image:radial-gradient(ellipse 72% 70% at 50% 50%, #000 62%, transparent 100%)">')
    inner = (masthead(r["no"], r["kicker"])
             + f'<div style="margin:24px -44px 0">{art}</div>'
             + f'<h1 data-chk="title" style="margin:6px 0 0;font-weight:700;font-size:112px;line-height:.92;letter-spacing:-.01em;color:{BERRY}">{r["title"]}</h1>'
             + f'<div style="display:flex;gap:28px;margin-top:20px;font-family:{HAND};font-size:44px;color:{RUST}"><span>⏱ {r["time"]}</span><span>·</span><span>{r["serves"]}</span></div>'
             + f'<p style="margin:16px 0 0;font-size:38px;line-height:1.25;font-weight:500">{r["blurb"]}</p>'
             + '<div style="flex:1"></div>' + footer())
    return page(inner)


def slide2(r):
    rows = "".join(
        f'<div style="display:flex;gap:26px;align-items:baseline;padding:16px 0;border-bottom:1px dashed {INK}55">'
        f'<span style="width:150px;flex:none;font-family:{HAND};font-size:48px;color:{RUST}">{q}</span>'
        f'<span style="font-size:42px;font-weight:600;line-height:1.15">{t}</span></div>' for q, t in r["ingredients"])
    art = svg(912, 300, carrots_dish(300, 150, .55, seed=7) + syrup_bottle(700, 90, .62) + leaf(820, 230, .9, "#C8321F", 30))
    inner = (masthead(r["no"], "Ingredients") + f'<h2 style="margin:26px 0 8px;font-size:72px;font-weight:700;color:{BERRY}">You’ll need</h2>'
             + rows + '<div style="flex:1"></div>' + f'<div style="margin:0 -20px 14px">{art}</div>' + footer())
    return page(inner)


def slide3(r):
    steps = "".join(
        f'<div style="display:flex;gap:26px;align-items:flex-start;margin-top:26px">'
        f'<span style="flex:none;width:74px;height:74px;border-radius:50%;border:3px solid {RUST};display:flex;align-items:center;justify-content:center;'
        f'font-family:{HAND};font-size:50px;color:{RUST}">{i}</span>'
        f'<span style="font-size:41px;font-weight:600;line-height:1.22">{t}</span></div>' for i, t in enumerate(r["steps"], 1))
    tip = (f'<div data-chk="tip" style="margin-top:34px;padding:22px 30px;background:#EAD9B8aa;border-radius:10px;border-left:8px solid {AMBER}">'
           f'<span style="font-family:{HAND};font-size:44px;color:{RUST}">Cook’s note: </span><span style="font-size:38px;font-style:italic;font-weight:600">{r["tip"]}</span></div>')
    art = svg(912, 260, leaf(110, 120, 1.1, "#C8321F", -25) + carrots_dish(470, 130, .5, seed=21) + leaf(820, 110, .9, AMBER, 20))
    inner = (masthead(r["no"], "Method") + f'<h2 style="margin:26px 0 0;font-size:72px;font-weight:700;color:{BERRY}">Let’s cook</h2>' + steps + tip
             + '<div style="flex:1"></div>' + f'<div style="margin:0 -20px 10px">{art}</div>' + footer())
    return page(inner)


def slide4(r):
    book = svg(912, 470, f'<g transform="translate(250 30) rotate(-4)">'
                         + wash('<rect x="0" y="0" width="420" height="400" rx="10" fill="FILL"/>', BERRY, "#4A0F0C", op=.92)
                         + wash('<rect x="28" y="28" width="364" height="344" rx="6" fill="none" stroke="FILL" style="stroke-width:4"/>', "#F4B63F", op=.8)
                         + f'<text x="210" y="120" text-anchor="middle" font-family="{SERIF}" font-weight="700" font-size="52" fill="#F6EEDC" letter-spacing="4">MAPLE</text>'
                         + f'<text x="210" y="178" text-anchor="middle" font-family="{SERIF}" font-weight="700" font-size="52" fill="#F6EEDC" letter-spacing="4">KITCHEN</text>'
                         + f'<text x="210" y="232" text-anchor="middle" font-family="{HAND}" font-size="38" fill="#F4B63F">all our recipes</text>'
                         + '</g>' + leaf(250, 380, 1.4, "#C8321F", -20) + leaf(700, 70, 1.0, AMBER, 15) + carrots_dish(700, 390, .3, seed=11))
    box = (f'<div data-chk="cta" style="flex:1 1 0;background:{BERRY};color:{PAPER};border-radius:14px;padding:24px 30px">'
           f'<div style="font-family:{HAND};font-size:40px;color:#F4B63F">Your turn · comment below</div>'
           f'<div style="font-size:44px;font-weight:700;line-height:1.08">{r["cta_q"]}</div></div>')
    inner = (masthead(r["no"], "Free cookbook")
             + f'<h2 style="margin:26px 0 0;font-size:84px;line-height:.95;font-weight:700;color:{BERRY}">Get every recipe, free.</h2>'
             + f'<p style="margin:14px 0 0;font-size:40px;font-weight:600;line-height:1.22">Save them all in our <i>Maple Kitchen</i> cookbook. Print it for the kitchen or keep it on your phone.</p>'
             + f'<div style="margin:10px -20px 0">{book}</div>'
             + f'<div style="font-family:{HAND};font-size:52px;color:{RUST};text-align:center;margin-top:-6px">Download it free at mapletapper.com</div>'
             + '<div style="flex:1"></div>'
             + f'<div style="display:flex;gap:26px;align-items:center">{box}<img data-chk="logo" src="{LOGO}" alt="MapleTapper logo, www.mapletapper.com" style="width:200px;flex:none"></div>')
    return page(inner)


if __name__ == "__main__":
    for i, fn in enumerate((slide1, slide2, slide3, slide4), 1):
        open(os.path.join(ROOT, "preview", f"Kitchen01-{i}.html"), "w").write(fn(R))
    print("built")
