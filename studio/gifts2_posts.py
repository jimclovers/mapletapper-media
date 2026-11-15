"""Gift guide week 2 (evenings Nov 16-22 2026): slide 2 (details + Your turn) and slide 3 (standard closing) for each post.
Covers come from gifts2_covers.py. Rule: never crop products (object-fit: contain)."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, root, column, preview_html
from covers_v2 import data_uri, PINE, SNOW
from closing import card
import gifts2_covers as gc

M, CR, G, R = C["maroon"], C["cream"], C["gold"], C["red"]
PR = gc.PR
DEADLINE = "Order by Dec 21 to have it by Christmas"

POSTS = [
 dict(n=8, slug="deluxe", cover=gc.g1, kicker="What’s in the box", head="Everything for 20 taps", photo=None,
      items=["20 tree-saver taps and 20 three-foot tubes", "A sap filter, a drill bit and recipe cards", "Our 80-page Guide to Maple Tapping", "Lifetime guarantee on the taps and tubes"],
      price="Deluxe Kit + Book · $69.96", q="How many maples could you tap on your street?", close="A yard full of maples is just the start."),
 dict(n=9, slug="classroom", cover=gc.g2, kicker="For teachers and scout leaders", head="A science unit in a box", photo="kids_kit_flatlay.jpg",
      items=["Five taps and tubes, for one tree or a few", "A full-color kids’ book, plus a how-to for the grown-up", "Measure the tree, track the sap, watch it become syrup"],
      price="Kid’s Kit · $39.97", q="Teachers: what would your class measure first?", close="One schoolyard maple is just the start."),
 dict(n=10, slug="budget", cover=gc.g3, kicker="How to pick", head="Match the gift to the yard", photo=None,
      items=["One tree and a curious kid: Kid’s Kit, $39.97", "A yard with several maples: Deluxe Kit + Book, $69.96", "A whole season in one box: Ultimate Kit, $179.99", "Can’t decide? A gift card, $10 to $200"],
      price="Gifts from $12.99", q="Which one’s going on your list?", close="The right kit is just the start."),
 dict(n=11, slug="bottles", cover=gc.g4, kicker="For someone who already taps", head="Finish strong", photo=None,
      items=["Syrup filters, three-piece quart set: $29.97", "Reusable. Clear syrup with no gritty “sugar sand”", "3 glass maple-leaf bottles with 6 gold caps: $33.79", "Fill them in March, give them as gifts all year"],
      price="Filters + leaf bottles", q="Who would you give your first bottle to?", close="The first bottle is just the start."),
 dict(n=12, slug="grandparents", cover=gc.g5, kicker="A gift you open twice", head="Christmas, then late winter", photo=None,
      items=["Unwrap it at Christmas, tap together when the sap runs", "Kid’s Maple Tree Tapping Kit, with real taps and tubes: $39.97", "A Kid’s Guide to Maple Tapping, in kid-friendly words: $14.99", "Then everyone gets pancakes"],
      price="Kid’s Kit + Kid’s Guide", q="Who taught you something outdoors as a kid?", close="One afternoon with the grandkids is just the start."),
 dict(n=13, slug="pinkspiles", cover=gc.g6, kicker="Stocking stuffer", head="Small, bright, built to last", photo=None,
      items=["Ten 5/16″ tree-saver spiles", "Easy to spot on the tree, and in the snow", "BPA-free, food-grade, made in North America", "Reusable for years, with a lifetime guarantee", "Also in white"],
      price="Ten spiles · $19.97", q="Pink or white? Vote below.", close="Pink taps are just the start."),
 dict(n=14, slug="hostgift", cover=gc.g7, kicker="Thanksgiving host gift", head="Outlasts the leftovers", photo=None,
      items=["Our Guide to Maple Tapping, 80 pages full of photos", "From finding a maple to bottling the syrup", "Read it in fall, tap in late winter"],
      price="Guide to Maple Tapping · $12.99", q="What are you bringing this year?", close="One good book is just the start."),
]


def mid(p):
    pic = ""
    if p["photo"]:
        pic = (f'<div data-chk="pic" style="height: 350px; border-radius: 28px; background: #fff; flex: none; overflow: hidden">'
               f'<img src="{data_uri(PR(p["photo"]))}" alt="" style="width: 100%; height: 100%; object-fit: contain; display: block"></div>')
    fs = 38 if p["photo"] else 46
    items = "".join(
        f'<div style="display: flex; gap: 20px; align-items: flex-start"><span style="flex: none; width: 46px; height: 46px; border-radius: 50%; background: {R}; '
        f'color: #fff; font-family: {DISPLAY}; font-weight: 800; font-size: 28px; display: flex; align-items: center; justify-content: center; margin-top: 2px">✓</span>'
        f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: {fs}px; line-height: 1.18; color: {M}">{t}</span></div>' for t in p["items"])
    price = (f'<div data-chk="price" style="background: #fff; border: 4px solid {G}; border-radius: 26px; padding: 22px 30px">'
             f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; line-height: 1.1; color: {M}">{p["price"]}</div>'
             f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 30px; color: {M}; margin-top: 6px">{DEADLINE} · mapletapper.com</div></div>')
    cta = (f'<div data-chk="cta" style="background: {PINE}; color: {SNOW}; border-radius: 28px; padding: 22px 30px">'
           f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: .06em; text-transform: uppercase; color: {G}">Your turn · comment below</div>'
           f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 38px; line-height: 1.1; margin-top: 6px">{p["q"]}</div></div>')
    inner = (kicker_row(p["kicker"], "2 / 3", M) + headline(p["head"], 88, M) + pic
             + f'<div data-chk="items" style="display: flex; flex-direction: column; gap: {20 if p['photo'] else 30}px">{items}</div>'
             + '<div style="flex-grow: 1"></div>' + price + cta + footer_row(M, swipe(M)))
    return root(CR, column(inner, gap=26), M)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview")
    for p in POSTS:
        n = p["n"]
        for k, html in ((1, p["cover"]()), (2, mid(p)), (3, card(p["close"], 1080, 1350))):
            open(os.path.join(out, f"gift{n:02d}-{k}-{p['slug']}.html"), "w").write(preview_html(f"Gift {n} slide {k}", html))
    print("built")
