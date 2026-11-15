"""10am lessons Nov 23-29 2026 (Sugarmaker's Almanac No. 18-24), Thanksgiving / Black Friday week. 14 weeks to sap season.
Real photos only (Jim's photos + MapleTapper product photos). Reuses helpers from lessons_nov16.py.

Facts (2+ sources each, own words):
- Drill a 5/16" hole 1.5 to 2 in deep; straight in or tilted very slightly up; tap the spout in gently; keep 6 in to the side and
  2 ft above/below an old taphole: UMaine Ext. Bulletin 7036, Utah State Ext., Cornell (Warren County CCE), Smoky Lake beginner guide.
- One tap gives about 10 gallons of sap in a season, about 1 quart of syrup: UMaine 7036, Univ. of Minnesota Ext., NCAT.
- Sap averages about 2% sugar: Univ. of Minnesota Ext., UW Extension (umes).
- Canada makes more than 75% of the world's maple syrup; 90% of Canada's comes from Quebec: Agriculture and Agri-Food Canada 2025;
  Canadian Grocer (citing Statistics Canada). Vermont makes about half of US syrup (53%): USDA NASS; Vermont Business Magazine.
- Indigenous peoples of the Northeast/Great Lakes made maple sugar long before Europeans arrived: Farmers' Almanac; Frontiers 2025.
- When sap runs: nights below freezing, days in the 40s: Northern Woodlands; Farmers' Almanac; Mass. Maple Producers.
  Southern Michigan producers usually tap in late February (MSU Ext.); Iowa mid-Feb to early March (Iowa State Ext.);
  season about 4 to 6 weeks (MSU Ext. via Countrylines / Michigan Maple Syrup Assn).
- Keep sap cold (under 40 F) and boil within days; filter before boiling: UNH Ext.; Smoky Lake.
- Business facts: only the ones Jim confirmed (family run; three generations tapping our Michigan family farm; made in North America;
  lifetime guarantee; never had a tap or tube fail with regular use and good care).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import lessons_nov16 as ln  # noqa: E402
from lessons_nov16 import (M, CR, G, R, SP, J, img, photo_box, num, rows, your_turn, src_line, inner, full_photo_cover, pill,  # noqa: E402
                           top_pills)
from build import DISPLAY, TYPE, ROOT, headline, body, preview_html  # noqa: E402
from covers_v2 import PINE, SKY, NAVY, SNOW, logo_badge, tag, handle, rootdiv, data_uri  # noqa: E402
from closing import card  # noqa: E402

ln.WEEKS = 14
WEEKS = 14
P = lambda *a: os.path.join(ROOT, "photos", *a)
JIMP = lambda n: "file://" + P("jim", n)
PROD = lambda n: "file://" + P("products", n)

TAP_BUCKET = JIMP("bucket_tubing_tap.jpg")      # tap + blue tubing on a trunk, snow
JUG_BLUE = JIMP("milk_jug_tubing_blue.jpg")     # tubing into a milk jug at a big trunk, snow
SNOW_JUGS = PROD("kids_kit_snow_jugs.jpg")      # tubing into jugs in a snowy woods (from the Kid's Kit box)
LEAF_GRASS = J("IMG_2659_leaf_on_grass.jpg")
LEAF_BACK = J("IMG_2694_leaf_underside.jpg")
GOLD_UP = J("IMG_2623_fallen_leaves.jpg")       # gold canopy and a branch, looking up
LEAVES_SKY = J("IMG_2607_looking_up_trunks.jpg")  # gold/red leaves against blue sky
CANOPY_SKY = J("IMG_2837_canopy_sky.jpg")
TREE_TALL = ln.TREE_TALL


def contain_box(src, alt, h, bg="#FFFFFF"):
    return (f'<div data-chk="photo" style="flex: none; height: {h}px; border-radius: 30px; overflow: hidden; background: {bg}; padding: 14px; box-sizing: border-box">'
            f'{img(src, alt, fit="contain")}</div>')


# ================================================================ No. 18 How to tap a maple (Mon Nov 23)
def a18():
    s1 = full_photo_cover(18, TAP_BUCKET, "A maple tap in a trunk with blue tubing running down into the snow", "60% 40%",
                          "Save this for February", "How to tap a maple tree", 104, bottom_title=True)
    s2 = inner(CR, M, "The 5 steps", "2 / 5", [
        headline(f'Tapping day,<br><span style="color: {R}">step by step.</span>', 92, M),
        rows([("Pick a healthy maple", "At least 12 inches across, measured 4½ feet up."),
              ("Drill a 5/16″ hole", "1½ to 2 inches deep, straight in or tilted just slightly up."),
              ("Tap the spout in gently", "A few light taps until it’s snug. Don’t pound it."),
              ("Attach the tube", "Run it down into a clean, food-grade jug or container."),
              ("Check it every day", "Collect the sap and keep it cold.")], size=37, sub=30, gap=22),
        SP,
        src_line("University of Maine Extension; Utah State Extension; Cornell Cooperative Extension")])
    s3 = inner(G, M, "Good to know", "3 / 5", [
        photo_box(SNOW_JUGS, "Blue tubing running from maple taps into jugs in a snowy woods", 560, "50% 40%"),
        headline(f'Leave room for<br><span style="color: {R}">last year’s holes.</span>', 80, M),
        body("Drill at least 6 inches to the side of an old taphole, and 2 feet above or below it, so you hit fresh, healthy wood.",
             34, M, "p1", "; font-weight: 600"),
        SP])
    s4 = inner(CR, M, "When?", "4 / 5", [
        headline(f'Wait for the<br><span style="color: {R}">sap weather.</span>', 100, M),
        body("Tap when the forecast shows nights below freezing and days in the 40s. In much of the Midwest that’s late February "
             "or early March.", 38, M, "p1"),
        body("14 weeks to go. Plenty of time to mark your trees and gather your gear!", 38, R, "p2", "; font-weight: 700"),
        SP,
        your_turn("Have you ever tapped a tree? Yes, no, or this year!")])
    s5 = card("Tapping day is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5]


# ================================================================ No. 19 What's in a tapping kit (Tue Nov 24)
def a19():
    s1 = rootdiv(SNOW, (
        f'<div style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px">{tag("Kit profile", PINE, "#FFFFFF", 30)}'
        f'{pill(f"Almanac · No. 19 · {WEEKS} weeks to sap", G, M)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 150px">' + headline(f'What does each<br><span style="color: {R}">piece do?</span>', 112, PINE, chk="title") + '</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 440px; height: 720px; border-radius: 34px; background: #FFFFFF; '
        f'box-shadow: 0 12px 34px rgba(0,0,0,.15); padding: 24px; box-sizing: border-box">'
        + img(PROD("deluxe_flatlay.jpg"), "Deluxe maple tapping kit laid out: taps, blue tubes, filter, drill bit, recipe cards and guide book", fit="contain") + '</div>'
        + handle(PINE) + logo_badge(bg=CR, bottom=40, size=130)))
    s2 = inner(CR, M, "Piece by piece", "2 / 4", [
        headline(f'A tapping kit,<br><span style="color: {R}">explained.</span>', 92, M),
        rows([("Tree-saver taps (spiles)", "5/16″ spouts that go in the tree. Food-grade and reusable."),
              ("Drop-line tubes", "Carry sap from the tap down to your jug, so rain and bugs stay out."),
              ("Drill bit", "Makes a clean 5/16″ hole that fits the tap snugly."),
              ("Sap filter", "Strains out bark bits before you boil."),
              ("Our Guide to Maple Tapping", "Every step, from finding a tree to bottling.")],
             bullet=["🍁", "💧", "🔩", "🧺", "📖"], size=36, sub=29, gap=20),
        SP])
    s3 = inner(G, M, "Which kit?", "3 / 4", [
        headline("Match it to<br>your trees", 104, M),
        rows([("1 tree and a curious kid", "Kid’s Maple Tree Tapping Kit: 5 taps and tubes, kids’ book, filters"),
              ("A yard with a few maples", "Maple Syrup Tree Tapping Kit + Book: 10 taps and tubes"),
              ("Lots of maples", "Deluxe Kit + Book: 20 taps and tubes"),
              ("A whole season in one box", "Ultimate Kit: taps, tubing, filters, thermometer, bottle and guide")],
             bullet=["🧒", "🏡", "🌳", "🏆"], size=36, sub=29, gap=20),
        body("Every tap and tube has a lifetime guarantee.", 34, M, "p1", "; font-weight: 700"),
        SP,
        your_turn("How many maples could you tap?")])
    s4 = card("The right kit is just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


# ================================================================ No. 20 Kids: Thanksgiving leaf-rubbing placemats (Wed Nov 25)
def a20():
    s1 = rootdiv(G, (
        f'<div style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px">{tag("Kids’ table", R, "#FFFFFF", 32, "; font-weight: 700")}'
        f'{pill(f"Almanac · No. 20", CR, M)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 150px">' + headline("Thankful leaf placemats", 118, M, chk="title") + '</div>'
        f'<div data-chk="sub" style="position: absolute; left: 56px; top: 470px; width: 420px; font-family: {DISPLAY}; font-weight: 700; font-size: 42px; '
        f'line-height: 1.15; color: {M}">A crayon, a leaf and 10 minutes before dinner.</div>'
        f'<div style="position: absolute; right: 56px; top: 420px; width: 500px; height: 740px; border-radius: 40px; overflow: hidden; '
        f'border: 14px solid #FFFFFF; box-shadow: 0 14px 40px rgba(0,0,0,.2); transform: rotate(2deg)">'
        + img(LEAF_GRASS, "A big green maple leaf lying on the grass", "50% 55%") + '</div>'
        + handle(M) + logo_badge(bg=CR, bottom=40, size=130)))
    s2 = inner(CR, M, "How to make one", "2 / 4", [
        photo_box(LEAF_BACK, "The back of a maple leaf with raised veins", 470, "55% 50%", "The bumpy back side shows the most veins"),
        rows([("Grab a few leaves", "Flat, dry ones work best."),
              ("Bumpy side up", "Lay the leaves under a sheet of paper, back side facing up."),
              ("Rub with a crayon", "Peel it and use the long side. The veins pop right out!"),
              ("Write a thank-you", "On each leaf, write one thing you’re thankful for.")], size=36, sub=29, gap=18),
        SP])
    s3 = inner(G, M, "Make it a game", "3 / 4", [
        headline(f'Then ask the<br><span style="color: {R}">kids’ table:</span>', 100, M),
        rows([("Count the points", "How many lobes does each leaf have?"),
              ("Compare the edges", "Smooth or saw-toothed? Tomorrow’s tree detectives start here."),
              ("Guess the tree", "Which yard did each leaf come from?")], bullet=["🔢", "🔍", "🌳"], size=36, sub=29),
        body("Tip: slide finished placemats into clear sheet protectors so they survive the gravy.", 32, M, "p1", "; font-weight: 600"),
        SP,
        your_turn("What’s one thing your kids are thankful for?")])
    s4 = card("A thankful leaf is just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


# ================================================================ No. 21 Thanksgiving: 5 maple facts for the table (Thu Nov 26)
def a21():
    s1 = full_photo_cover(21, LEAVES_SKY, "Gold, orange and green maple leaves against a blue sky", "50% 40%",
                          "Happy Thanksgiving", "5 maple facts for the table", 116, bottom_title=True)
    facts = [("About 2% sugar", "Fresh maple sap is mostly water. It tastes only a little sweet."),
             ("40 to 1", "It takes about 40 gallons of sap to boil down 1 gallon of syrup."),
             ("1 tap ≈ 1 quart", "One tap gives about 10 gallons of sap in a season, about a quart of syrup."),
             ("Canada makes over ¾", "Of the world’s maple syrup, and 9 of every 10 Canadian gallons come from Quebec."),
             ("An old American tradition", "Indigenous peoples made maple sugar long before Europeans arrived.")]
    s2 = inner(CR, M, "Pass the syrup", "2 / 4", [
        headline(f'Fun facts to<br><span style="color: {R}">share tonight.</span>', 92, M),
        rows(facts, size=38, sub=30, gap=22),
        SP,
        src_line("Univ. of Minnesota Extension; Univ. of Maine Extension; Agriculture and Agri-Food Canada; USDA NASS")])
    s3 = inner(M, CR, "Bonus fact", "3 / 4", [
        photo_box(CANOPY_SKY, "A maple crown turning gold under a cloudy sky", 440, "50% 40%"),
        headline(f'Vermont makes<br><span style="color: {G}">about half.</span>', 100, CR),
        body("Of all the maple syrup made in the United States. The Midwest has plenty of maples too, including in your yard.", 36, CR, "p1"),
        SP,
        your_turn("Real maple syrup or pancake syrup at your table?", CR, M)])
    s4 = card("A thankful table is just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


# ================================================================ No. 22 Black Friday: how many taps do you need? (Fri Nov 27)
def a22():
    big = lambda n, l: (f'<div style="display: flex; flex-direction: column; align-items: center; gap: 4px; background: #FFFFFF; border-radius: 26px; '
                        f'padding: 22px 10px; flex: 1"><div style="font-family: {DISPLAY}; font-weight: 800; font-size: 76px; line-height: 1; color: {R}">{n}</div>'
                        f'<div style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; line-height: 1.1; color: {NAVY}; text-align: center">{l}</div></div>')
    s1 = rootdiv(SKY, (
        f'<div style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px">{tag("Maple math", NAVY, "#FFFFFF", 30)}'
        f'{pill(f"Almanac · No. 22 · {WEEKS} weeks to sap", "#FFFFFF", NAVY)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 150px">' + headline("How many taps do you need?", 118, NAVY, chk="title") + '</div>'
        f'<div data-chk="nums" style="position: absolute; left: 56px; right: 56px; top: 560px; display: flex; gap: 18px">'
        + big("1 tap", "about 10 gal of sap") + big("≈ 1 qt", "of syrup per season") + '</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 790px; height: 380px; border-radius: 30px; overflow: hidden; '
        f'border: 12px solid #FFFFFF">' + img(JUG_BLUE, "A maple tap with blue tubing running into a milk jug at the base of a big trunk", "50% 88%") + '</div>'
        + handle(NAVY) + logo_badge(bg="#FFFFFF", bottom=40, size=130)))
    rows_ = [("1 tap", "about 1 quart", "A taste for the family"), ("4 taps", "about 1 gallon", "Pancakes all spring"),
             ("10 taps", "about 2½ gallons", "Some to give away"), ("20 taps", "about 5 gallons", "Gifts for everyone")]
    cell = lambda t, b=False: f'<div style="font-family: {DISPLAY}; font-weight: {800 if b else 600}; font-size: 36px; line-height: 1.12; color: {M}">{t}</div>'
    table = (f'<div data-chk="table" style="background: #FFFFFF; border-radius: 30px; padding: 22px 30px">'
             + "".join(f'<div style="display: grid; grid-template-columns: 180px 260px 1fr; gap: 16px; align-items: center; padding: 18px 0; '
                       f'border-top: {"0" if i == 0 else "3px solid rgba(122,30,26,.15)"}">{cell(a, True)}{cell(b, True)}{cell(c)}</div>'
                       for i, (a, b, c) in enumerate(rows_)) + '</div>')
    s2 = inner(G, M, "A rough guide", "2 / 4", [
        headline(f'Taps in,<br><span style="color: {R}">syrup out.</span>', 104, M),
        table,
        body("Every year is different: weather, tree size and sugar content all change the total. Big, sunny yard trees often give more.",
             32, M, "p1", "; font-weight: 600"),
        SP,
        src_line("Univ. of Maine Extension; Univ. of Minnesota Extension; NCAT")])
    s3 = inner(CR, M, "Pick your kit", "3 / 4", [
        headline(f'One tap per tree<br><span style="color: {R}">12–18″ across.</span>', 86, M),
        rows([("Kid’s Kit", "5 taps and tubes, plus the kids’ book"), ("Maple Syrup Tree Tapping Kit + Book", "10 taps and tubes"),
              ("Deluxe Kit + Book", "20 taps and tubes, drill bit and filter"), ("Ultimate Kit", "Taps for up to 20 trees, plus the finishing gear")],
             bullet=["🧒", "🏡", "🌳", "🏆"], size=36, sub=29, gap=20),
        body("Order by Dec 21 to have it by Christmas.", 36, R, "p1", "; font-weight: 700"),
        SP,
        your_turn("How many taps would you start with?")])
    s4 = card("One tap is just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


# ================================================================ No. 23 Your plan from now to sap season (Sat Nov 28)
def a23():
    steps = [("Now", "Mark your maples", "Ribbon, a number, a photo of the leaf and bark."),
             ("December", "Gather your gear", "Taps, tubing, a filter and clean food-grade jugs."),
             ("January", "Watch the forecast", "Look for nights below freezing and days in the 40s."),
             ("Late Feb", "Tap!", "Southern Michigan usually starts in late February; farther north, March.")]
    line = "".join(
        f'<div style="display: flex; gap: 24px; align-items: flex-start"><div style="flex: none; width: 190px; font-family: {TYPE}; font-size: 30px; '
        f'letter-spacing: .04em; text-transform: uppercase; color: {R}; padding-top: 8px">{w}</div><div style="display: flex; flex-direction: column; gap: 2px">'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; line-height: 1.05; color: {PINE}">{t}</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 31px; line-height: 1.2; color: {PINE}">{n}</div></div></div>'
        for w, t, n in steps)
    s1 = rootdiv(SNOW, (
        f'<div style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px">{tag("Your countdown", R, "#FFFFFF", 30)}'
        f'{pill(f"Almanac · No. 23 · {WEEKS} weeks to sap", G, M)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 150px">' + headline(f'From turkey<br><span style="color: {R}">to tapping.</span>', 124, PINE, chk="title") + '</div>'
        f'<div data-chk="line" style="position: absolute; left: 56px; right: 56px; top: 470px; display: flex; flex-direction: column; gap: 34px; '
        f'border-left: 6px solid {G}; padding-left: 26px">{line}</div>'
        + handle(PINE) + logo_badge(bg=CR, bottom=40, size=130)))
    s2 = inner(CR, M, "Why wait?", "2 / 4", [
        photo_box(SNOW_JUGS, "Blue tubing from maple taps into jugs in a snowy woods", 540, "50% 40%"),
        headline(f'Sap runs on<br><span style="color: {R}">freeze and thaw.</span>', 90, M),
        body("Cold nights and warmer days build pressure in the tree, and the sap flows. The season usually lasts about 4 to 6 weeks.",
             34, M, "p1"),
        SP,
        src_line("Michigan State Univ. Extension; Iowa State Extension; Northern Woodlands")])
    s3 = inner(G, M, "This weekend", "3 / 4", [
        headline(f'Leftovers in the fridge?<br><span style="color: {R}">Go for a walk.</span>', 82, M),
        body("Bring the family, a tape measure and some ribbon. Mark the maples you want to tap while a few leaves still hang on.", 38, M, "p1"),
        SP,
        your_turn("Where are you in the countdown: marking, gearing up, or ready?")])
    s4 = card("A countdown plan is just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


# ================================================================ No. 24 No fancy gear needed: collecting sap (Sun Nov 29)
def a24():
    s1 = full_photo_cover(24, JUG_BLUE, "A maple tap with blue tubing running into a clean milk jug at the base of a big trunk", "50% 55%",
                          "Backyard sugaring", "No fancy gear needed", 100)
    s2 = inner(CR, M, "How it works", "2 / 4", [
        headline(f'Tap, tube,<br><span style="color: {R}">clean jug.</span>', 100, M),
        rows([("The tap goes in the tree", "A 5/16″ tree-saver spout."),
              ("The tube carries the sap", "Down into a jug, so rain, bugs and bark stay out."),
              ("Any clean, food-grade jug works", "Wash milk jugs well with hot water before you use them."),
              ("Empty it every day", "Sap is food. Treat it like milk.")], size=37, sub=30, gap=22),
        SP])
    s3 = inner(M, CR, "Keep it fresh", "3 / 4", [
        photo_box(TAP_BUCKET, "A tap and blue tubing on a maple trunk in the snow", 440, "60% 40%"),
        headline(f'Cold sap is<br><span style="color: {G}">good sap.</span>', 100, CR),
        body("Keep sap below 40°F and boil it within a few days. Strain it through a filter before it goes in the pot.", 36, CR, "p1"),
        SP,
        src_line("UNH Extension; Univ. of Maine Extension", CR),
        your_turn("Milk jugs or something else: what would you use?", CR, M)])
    s4 = card("A clean jug is just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


POSTS = [("almanac18", "Almanac18", a18), ("almanac19", "Almanac19", a19), ("almanac20", "Almanac20", a20), ("almanac21", "Almanac21", a21),
         ("almanac22", "Almanac22", a22), ("almanac23", "Almanac23", a23), ("almanac24", "Almanac24", a24)]

if __name__ == "__main__":
    out = []
    for folder, pre, fn in POSTS:
        for i, m in enumerate(fn()):
            p = os.path.join(ROOT, "preview", f"{pre}-{i + 1}.html")
            open(p, "w").write(preview_html(f"{pre}-{i + 1}", m))
            out.append(p)
    print(" ".join(out))
