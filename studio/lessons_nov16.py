"""10am lessons Nov 16-22 2026 (Sugarmaker's Almanac No. 11-17), built from Jim's REAL photos (photos/jim/nov14). No drawn leaves.
15 weeks to sap season. Grid variety covers; Your-turn box on the slide before the standard closing card.
NOTE: several nov14 file names don't match their picture (e.g. IMG_2620_tree_sun = fallen leaves). Files are picked by what they show.
We never name the species of Jim's own trees (his measured leaf and IMG_2644 bark look like Norway maple; unconfirmed).

Facts (2+ sources each, own words):
- Mark trees in fall; easier than winter ID: UMaine Ext. Bulletin 7036; UW-Madison Ext. ("ID those trees now"); Utah State Ext.
- 12 in across at 4.5 ft (~38 in around = 12 x 3.14), 1 tap for 12-18 in: our posted rule; UMaine 7036, USU (circumference / 3.14).
- Young maples smooth gray; old sugar maple long thick plates lifting at edges; Norway shallow connecting ridges; silver long thin strips
  loose at ends; red thin scaly plates; bark varies: UMass Ext. (sugar maple), NC State Ext. (Norway "finely furrowed"), Gardenguides
  citing Ohio State/UMD Ext., Timberland Investor.
- Norway leaves often wider than long; milky sap from snapped leaf stem, native maples clear; milk can fade late in the year:
  Purdue Ext., Univ. of Minnesota Ext., UConn Ext., Utah State Ext.
- Leaves make sugar in summer, stored as starch in wood/roots; enzymes (amylase) turn it back to sugar in late winter -> sweet sap:
  Cornell Maple Program (Wightman), Penn State Ext., UVM Ext. Maple Minute.
- Bigger trees / bigger sunny crowns -> more sap and sweeter sap: UVM Proctor (Perkins et al. 2018), Univ. of Kentucky (crown classes),
  MSU thesis (crown diameter), Northern Woodlands (yard maple vs woods tree).
- Fall color: chlorophyll fades, yellow/orange carotenoids were there all summer; reds (anthocyanins) made in fall from sugars in the
  leaf, helped by bright days and cool nights; timing set mainly by night length: USDA Forest Service (2 articles), Clemson HGIC.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, swipe, headline, body, root, column, preview_html  # noqa: E402
from covers_v2 import PINE, SKY, NAVY, SNOW, logo_badge, tag, handle, rootdiv  # noqa: E402
from closing import card  # noqa: E402

M, CR, G, R = C["maroon"], C["cream"], C["gold"], C["red"]
WEEKS = 15
SP = '<div style="flex-grow: 1"></div>'
J = lambda n: "file://" + os.path.join(ROOT, "photos", "jim", "nov14", n)

# what each file actually shows
TREE_TALL = J("IMG_2638_tree_tall.jpg")         # lone round maple on lawn, portrait
TREE_WIDE = J("IMG_2635_tree_wide.jpg")         # same tree, landscape
TREE_CLOSE = J("IMG_2637_tree_close.jpg")       # same tree, landscape, closer
LEAF_RING = J("IMG_2620_tree_sun.jpg")          # fallen leaves ringing a trunk
PLATES = J("IMG_2630_canopy_branch.jpg")        # bark: long plates lifting at edges
CRISS = J("IMG_2644_bark.jpg")                  # bark: tight crisscross ridges
TRUNK = J("IMG_2621_canopy_trunks.jpg")         # trunk + sun, park path
CROWDED = J("IMG_2618_bark_close.jpg")          # looking up crowded trunks
LEN = J("IMG_2691_leaf_tape_vertical.jpg")
WID = J("IMG_2687_leaf_tape_horizontal.jpg")
GOLD_CROWN = J("IMG_2843_gold_crown.jpg")
GREEN_LEAVES = J("IMG_2845_leaves_close.jpg")
GREEN_GOLD = J("IMG_2844_leaves_closer.jpg")
TWO_TONE = J("IMG_2842_green_and_gold_canopy.jpg")
ORANGE_TREE = J("IMG_2633_leaves_sky.jpg")      # orange maple by a path
CANOPY = J("IMG_2834_gold_canopy_wide.jpg")


def pill(text, bg, fg, size=26):
    return (f'<span style="display: inline-block; background: {bg}; color: {fg}; font-family: {TYPE}; font-size: {size}px; '
            f'letter-spacing: .05em; text-transform: uppercase; padding: 9px 20px 7px; border-radius: 999px">{text}</span>')


def top_pills(no, color_bg=CR, color_fg=M):
    return (f'<div data-chk="pills" style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px; z-index: 4">'
            f'{pill(f"Sugarmaker’s Almanac · No. {no}", color_bg, color_fg)}{pill(f"{WEEKS} weeks to sap season", G, M)}</div>')


def img(src, alt, pos="50% 50%", fit="cover", extra=""):
    return (f'<img src="{src}" alt="{alt}" style="width: 100%; height: 100%; object-fit: {fit}; object-position: {pos}; '
            f'display: block{extra}">')


def photo_box(src, alt, h, pos="50% 50%", label=None, fit="cover", bg="#000"):
    lab = (f'<span style="position: absolute; left: 18px; bottom: 18px; background: rgba(255,245,222,.94); color: {M}; '
           f'border-radius: 999px; padding: 9px 20px 7px; font-family: {TYPE}; font-size: 24px; letter-spacing: .04em">{label}</span>'
           if label else "")
    return (f'<div data-chk="photo" style="position: relative; flex: none; height: {h}px; border-radius: 30px; overflow: hidden; background: {bg}">'
            f'{img(src, alt, pos, fit)}{lab}</div>')


def num(n, bg=R, fg=CR, size=64):
    return (f'<div style="width: {size}px; height: {size}px; border-radius: 50%; background: {bg}; color: {fg}; display: flex; '
            f'align-items: center; justify-content: center; flex: none; font-family: {DISPLAY}; font-weight: 800; '
            f'font-size: {int(size * .55)}px">{n}</div>')


def rows(items, color=M, size=38, sub=30, bullet=None, gap=26, chk="rows"):
    out = []
    for i, it in enumerate(items):
        t, n = it if isinstance(it, tuple) else (it, "")
        b = num(i + 1) if bullet is None else f'<div style="font-size: 46px; line-height: 1; flex: none">{bullet[i]}</div>'
        out.append(f'<div style="display: flex; gap: 22px; align-items: flex-start">{b}<div style="display: flex; flex-direction: column; '
                   f'gap: 4px; padding-top: 6px"><div style="font-family: {DISPLAY}; font-weight: 800; font-size: {size}px; line-height: 1.06; '
                   f'color: {color}">{t}</div>' + (f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: {sub}px; '
                   f'line-height: 1.24; color: {color}">{n}</div>' if n else "") + '</div></div>')
    return f'<div data-chk="{chk}" style="display: flex; flex-direction: column; gap: {gap}px">{"".join(out)}</div>'


def your_turn(q, bg=PINE, fg=SNOW):
    return (f'<div data-chk="cta" style="background: {bg}; color: {fg}; border-radius: 30px; padding: 24px 32px; display: flex; '
            f'flex-direction: column; gap: 6px"><div style="font-family: {TYPE}; font-size: 24px; letter-spacing: .06em; '
            f'text-transform: uppercase; color: {G}">Your turn · comment below</div><div style="font-family: {DISPLAY}; '
            f'font-weight: 800; font-size: 40px; line-height: 1.08">{q}</div></div>')


def src_line(t, color=M):
    return (f'<div data-chk="src" style="font-family: {TYPE}; font-size: 21px; line-height: 1.35; color: {color}; opacity: .85">'
            f'Sources: {t}</div>')


def inner(bg, fg, kicker, page, parts, gap=28):
    return root(bg, column(kicker_row(kicker, page, fg) + "".join(parts) + footer_row(fg, swipe(fg)), gap=gap), fg)


def full_photo_cover(no, src, alt, pos, label_small, title, title_size=96, bottom_title=False):
    """Style 1: full-bleed real photo, small cream title tag (or big white words for style 2)."""
    shade = ('<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 760px; '
             'background: linear-gradient(to top, rgba(15,10,5,.85), rgba(15,10,5,0))"></div>')
    if bottom_title:
        words = (f'<div style="position: absolute; left: 56px; right: 56px; bottom: 210px">'
                 f'<div style="margin-bottom: 18px">{tag(label_small, "rgba(255,255,255,.92)", M, 28)}</div>'
                 + headline(title, title_size, "#FFFFFF", chk="title", extra="; text-shadow: 0 3px 16px rgba(0,0,0,.45)") + '</div>')
    else:
        shade = ('<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 260px; '
                 'background: linear-gradient(to top, rgba(0,0,0,.5), rgba(0,0,0,0))"></div>')
        words = (f'<div data-chk="title" style="position: absolute; left: 56px; top: 150px; max-width: 760px; background: {CR}; '
                 f'border-radius: 26px; padding: 24px 34px 30px; box-shadow: 0 8px 24px rgba(0,0,0,.25); transform: rotate(-1.5deg)">'
                 f'<div style="font-family: {TYPE}; font-size: 28px; letter-spacing: .06em; text-transform: uppercase; color: {R}">{label_small}</div>'
                 f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: {title_size}px; line-height: .95; letter-spacing: -.02em; '
                 f'color: {M}">{title}</div></div>')
    return rootdiv("#222", f'<div style="position: absolute; inset: 0">{img(src, alt, pos)}</div>' + shade + top_pills(no) + words
                   + handle("#FFFFFF") + logo_badge(bottom=40, size=130))


# ================================================================ No. 11 Mark your maples (Mon Nov 16)
def a11():
    s1 = full_photo_cover(11, TREE_TALL, "A big, round maple standing alone on a green lawn in fall color", "50% 55%",
                          "Do it this week", "Mark your maples before the leaves drop", 92)
    s2 = inner(CR, M, "Why now?", "2 / 5", [
        photo_box(LEAF_RING, "Fallen maple leaves in a ring around a tree trunk", 560, "50% 40%", "The leaves under a tree are a clue"),
        headline(f'Leaves are the<br><span style="color: {R}">name tag.</span>', 96, M),
        body("Once the leaves are gone, most maples look a lot alike. Tree experts say marking your trees in fall is much easier "
             "than trying to identify them in winter. If a few leaves still hang on, or lie under the tree, go now.", 34, M, "p1"),
        SP])
    s3 = inner(G, M, "How to mark them", "3 / 5", [
        headline("4 easy ways to<br>mark a tree", 100, M),
        rows([("Tie on bright ribbon", "Flagging tape or ribbon around the trunk, at eye level."),
              ("Give it a number", "Write it on the ribbon. Tree #1, #2, #3…"),
              ("Snap 2 photos", "One of a leaf and one of the bark, to check later."),
              ("Drop a pin on your phone", "Saves the spot on your map, even under snow.")]),
        SP,
        src_line("University of Maine Extension; University of Wisconsin–Madison Extension")])
    s4 = inner(CR, M, "While you’re there", "4 / 5", [
        photo_box(TRUNK, "The trunk of a big maple in a park, sun shining through the branches", 440, "50% 60%"),
        headline(f'Is it big<br><span style="color: {R}">enough?</span>', 100, M),
        rows([("12 inches across, 4½ feet up", "Wrap a tape around the trunk. About 38 inches around = 12 inches across."),
              ("One tap per tree", "Trees 12 to 18 inches across get one tap.")], size=36, sub=30, gap=20),
        SP,
        your_turn("How many maples did you find and mark?")])
    s5 = card("Marking your maples is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5]


# ================================================================ No. 12 Read the bark (Tue Nov 17)
def a12():
    s1 = full_photo_cover(12, PLATES, "Close-up of thick gray maple bark with long plates lifting at the edges", "50% 50%",
                          "Winter tree ID", "Read the bark", 150, bottom_title=True)
    s2 = inner(M, CR, "Start here", "2 / 5", [
        photo_box(TRUNK, "Gray bark on a park maple trunk", 520, "50% 55%"),
        headline(f'Young maples<br><span style="color: {G}">all look smooth.</span>', 92, CR),
        body("Every kind of maple starts with smooth, gray bark. The clues show up as the tree gets older and bigger, "
             "which is the size you want to tap anyway.", 36, CR, "p1"),
        SP])

    def pair(src, alt, title, note, pos):
        return (f'<div style="display: flex; gap: 26px; align-items: center"><div style="width: 300px; height: 300px; flex: none; '
                f'border-radius: 26px; overflow: hidden">{img(src, alt, pos)}</div><div style="display: flex; flex-direction: column; gap: 8px">'
                f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.04; color: {M}">{title}</div>'
                f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 31px; line-height: 1.2; color: {R}">{note}</div></div></div>')
    s3 = inner(CR, M, "3 patterns on older trees", "3 / 5", [
        headline("What do<br>you see?", 104, M),
        f'<div data-chk="pairs" style="display: flex; flex-direction: column; gap: 24px">'
        + pair(PLATES, "Bark with long, thick plates lifting at the edges", "Long, thick plates that lift at the edges",
               "A sugar maple clue", "50% 50%")
        + pair(CRISS, "Bark with tight, shallow crisscross ridges", "Tight, shallow ridges that crisscross and don’t peel",
               "A Norway maple clue", "50% 50%")
        + '</div>',
        rows([("Long, thin strips loose at both ends", "Shaggy, like a bad hair day: a silver maple clue.")],
             bullet=["🌳"], size=36, sub=30),
        SP])
    s4 = inner(G, M, "Good to know", "4 / 5", [
        headline(f'Bark is a clue,<br><span style="color: {R}">not proof.</span>', 98, M),
        body("Bark changes a lot from tree to tree, even in one kind of maple. So use it with other clues:", 36, M, "p1"),
        rows([("Check a leaf while you still can", ""), ("Snap a green leaf stem", "A milky drop means Norway maple."),
              ("Mark the tree", "Then you’ll know it in February.")], size=36, sub=30, gap=18),
        SP,
        src_line("UMass Extension; NC State Extension; Purdue Extension"),
        your_turn("Share a bark photo. Can you guess the tree?")])
    s5 = card("Reading bark is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5]


# ================================================================ No. 13 Kids corner: measure a leaf (Wed Nov 18)
def a13():
    ruler = "".join(f'<rect x="{i * 40}" y="0" width="4" height="{40 if i % 3 == 0 else 22}" fill="{NAVY}"></rect>' for i in range(24))
    s1 = rootdiv(SKY, (
        f'<div style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px">{tag("Kids corner", G, NAVY, 32, "; font-weight: 700")}'
        f'{pill(f"{WEEKS} weeks to sap season", "#FFFFFF", NAVY)}</div>'
        f'<div style="position: absolute; left: 56px; top: 150px; width: 960px">' + headline("Measure a<br>maple leaf", 118, NAVY, chk="title") + '</div>'
        f'<svg aria-hidden="true" style="position: absolute; left: 56px; top: 560px" width="300" height="40" viewBox="0 0 960 40">{ruler}</svg>'
        f'<div data-chk="sub" style="position: absolute; left: 56px; top: 630px; width: 400px; font-family: {DISPLAY}; font-weight: 700; '
        f'font-size: 42px; line-height: 1.15; color: {NAVY}">Grab a tape measure and a leaf!</div>'
        f'<div style="position: absolute; right: 56px; top: 400px; width: 480px; height: 740px; border-radius: 40px; overflow: hidden; '
        f'border: 14px solid #FFFFFF; box-shadow: 0 14px 40px rgba(0,0,0,.25); background: #8a8a88">'
        + img(LEN, "A green maple leaf next to a yellow tape measure", "50% 40%") + '</div>'
        + handle(NAVY) + logo_badge(bg="#FFFFFF", bottom=40, size=130)))
    s2 = inner(CR, M, "Step 1 · Length", "2 / 5", [
        f'<div style="display: flex; gap: 30px; align-items: stretch; height: 760px"><div style="width: 520px; flex: none; border-radius: 30px; '
        f'overflow: hidden">{img(LEN, "A maple leaf laid next to a tape measure, from tip to stem", "50% 45%")}</div>'
        f'<div style="display: flex; flex-direction: column; gap: 22px; justify-content: center">'
        + headline(f'How <span style="color: {R}">long?</span>', 96, M)
        + body("Measure from the tip of the middle point down to where the stem starts.", 36, M, "p1")
        + body("<b>Don’t count the stem!</b>", 36, R, "p2") + '</div></div>',
        SP,
        body("Write it down: “Length = __ inches.”", 38, M, "p3", "; font-weight: 700")])
    s3 = inner(CR, M, "Step 2 · Width", "3 / 5", [
        photo_box(WID, "A maple leaf under a tape measure laid across its widest points", 640, "50% 30%", bg="#8a8a88"),
        headline(f'How <span style="color: {R}">wide?</span>', 100, M),
        body("Measure straight across the widest part, from one side point to the other.", 38, M, "p1"),
        SP,
        body("Write it down: “Width = __ inches.”", 38, M, "p3", "; font-weight: 700")])
    s4 = inner(G, M, "What it tells you", "4 / 5", [
        headline(f'Wider than<br><span style="color: {R}">it is long?</span>', 98, M),
        body("Then it might be a <b>Norway maple</b>, a look-alike tree from Europe. Their leaves are often wider than they are long.", 36, M, "p1"),
        rows([("Do the snap test", "Snap a fresh, green leaf stem. A milky white drop = Norway maple. Clear = a native maple."),
              ("Best in summer", "The milk can fade late in the year, so test again next summer.")], size=36, sub=30, gap=18),
        SP,
        src_line("Purdue Extension; University of Minnesota Extension; Utah State Extension"),
        your_turn("What did your leaf measure? Length × width!", NAVY)])
    s5 = card("Measuring leaves is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5]


# ================================================================ No. 14 Surprising fact: stored sugar (Thu Nov 19)
def a14():
    s1 = full_photo_cover(14, GOLD_CROWN, "A tall maple crown turning gold against a cloudy sky", "50% 40%",
                          "Surprising fact", "Next spring’s syrup is already in this tree", 104, bottom_title=True)
    s2 = inner(CR, M, "All summer long", "2 / 5", [
        photo_box(GREEN_LEAVES, "Green and yellow maple leaves on a branch", 560, "50% 45%"),
        headline(f'Leaves make<br><span style="color: {R}">sugar.</span>', 104, M),
        body("Maple leaves use sunlight to make sugar. The tree packs the extra away as <b>starch</b> in its wood and roots, "
             "like a pantry for winter.", 36, M, "p1"),
        SP])
    s3 = inner(M, CR, "Late winter", "3 / 5", [
        headline(f'Starch turns back<br><span style="color: {G}">into sugar.</span>', 96, CR),
        rows([("The tree wakes up its enzymes", "Including amylase, the same helper in your spit that breaks down starch."),
              ("Starch becomes sugar", "The sugar mixes into the sap. That’s why late-winter sap tastes sweet."),
              ("Freezing nights, warm days", "That back-and-forth pushes the sweet sap out of your tap.")], color=CR, bullet=None),
        SP,
        src_line("Cornell Maple Program; Penn State Extension; UVM Extension", CR)])
    s4 = inner(G, M, "Why it matters", "4 / 5", [
        photo_box(TREE_CLOSE, "A big, round maple with a full crown in a field", 480, "50% 45%"),
        headline(f'Healthy leaves now,<br><span style="color: {R}">sweet sap later.</span>', 82, M),
        body("Big, healthy trees with lots of sunny leaves store the most. So protect your maples, and mark the best ones now.", 34, M, "p1"),
        SP,
        your_turn("Did you know trees save sugar for winter? Yes or no?")])
    s5 = card("Stored-up sugar is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5]


# ================================================================ No. 15 Big crown, sweeter sap (Fri Nov 20)
def a15():
    s1 = rootdiv(SNOW, (
        f'<div style="position: absolute; left: 56px; top: 60px; display: flex; gap: 12px">{tag("Tapping tip", R, "#FFFFFF", 30)}'
        f'{pill(f"Almanac · No. 15 · {WEEKS} weeks to sap", G, M)}</div>'
        f'<div style="position: absolute; left: 56px; right: 56px; top: 150px">' + headline(f'Big crown,<br><span style="color: {R}">sweeter sap.</span>', 124, PINE, chk="title") + '</div>'
        f'<div style="position: absolute; left: 56px; top: 470px; width: 560px; height: 720px; border-radius: 34px; overflow: hidden; '
        f'border: 12px solid #FFFFFF; box-shadow: 0 12px 34px rgba(0,0,0,.22); transform: rotate(-2deg)">'
        + img(TREE_TALL, "A lone maple with a wide, full crown on a lawn", "50% 50%") + '</div>'
        f'<div style="position: absolute; right: 56px; top: 560px; width: 380px; height: 520px; border-radius: 30px; overflow: hidden; '
        f'border: 12px solid #FFFFFF; box-shadow: 0 12px 34px rgba(0,0,0,.22); transform: rotate(3deg)">'
        + img(CROWDED, "Looking up at crowded trunks with small crowns", "50% 50%") + '</div>'
        + handle(PINE) + logo_badge(bg=CR, bottom=40, size=130)))
    s2 = inner(CR, M, "Why the crown matters", "2 / 4", [
        photo_box(TREE_WIDE, "A big maple with a wide crown standing in an open field", 520, "50% 50%"),
        headline(f'More sunny leaves,<br><span style="color: {R}">more sugar.</span>', 86, M),
        body("Researchers at the University of Vermont and in Kentucky found that bigger maples with big crowns in full sun give "
             "more sap, and sweeter sap, than small, shaded trees.", 34, M, "p1"),
        SP,
        src_line("UVM Proctor Maple Research Center; University of Kentucky; Northern Woodlands")])
    s3 = inner(G, M, "Pick your best trees", "3 / 4", [
        headline("Look for:", 112, M),
        rows([("A wide, full crown", "Lots of leaves in the sun, not squeezed by other trees."),
              ("A trunk 12 inches across or more", "Measured 4½ feet up. Bigger is better."),
              ("No big dead limbs", "Healthy trees store the most sugar.")], bullet=["🌳", "📏", "✅"]),
        body("Good news: that big yard or roadside maple often beats a skinny tree in the woods.", 36, M, "p1", "; font-weight: 700"),
        SP,
        your_turn("Yard tree or woods tree: which will you tap?")])
    s4 = card("Big, sunny maples are just the start.", 1080, 1350)
    return [s1, s2, s3, s4]


# ================================================================ No. 16 Leaf color science (Sat Nov 21)
def a16():
    s1 = full_photo_cover(16, GREEN_GOLD, "Green maple leaves with a few turning yellow and orange", "50% 45%",
                          "Leaf science for kids", "Where does the gold come from?", 112, bottom_title=True)
    s2 = inner(CR, M, "Surprise!", "2 / 5", [
        photo_box(TWO_TONE, "A maple crown, half green and half gold", 600, "50% 35%"),
        headline(f'The gold was there<br><span style="color: {R}">all summer.</span>', 86, M),
        body("Leaves hold green chlorophyll <i>and</i> yellow-orange colors called carotenoids. In fall the tree stops making "
             "green, so the hidden gold finally shows.", 34, M, "p1"),
        SP])
    s3 = inner(M, CR, "And the reds?", "3 / 5", [
        photo_box(ORANGE_TREE, "A maple in orange fall color beside a path", 560, "50% 40%"),
        headline(f'Reds are<br><span style="color: {G}">brand new.</span>', 100, CR),
        body("Red colors (anthocyanins) are made in fall, from sugar trapped in the leaf. Bright days and cool nights help. "
             "Longer nights tell the tree when to start.", 34, CR, "p1"),
        SP,
        src_line("USDA Forest Service; Clemson Extension", CR)])
    s4 = inner(G, M, "Try it", "4 / 5", [
        headline("Leaf color<br>line-up", 110, M),
        rows([("Collect 3 leaves", "One green, one gold, one red or orange."),
              ("Line them up", "From the most green to the least green."),
              ("Ask why", "Which one lost its green first? Which made the most red?")]),
        SP,
        your_turn("What color are the maples near you right now?")])
    s5 = card("Fall color is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5]


# ================================================================ No. 17 Sunday maple walk (Sun Nov 22)
def a17():
    s1 = full_photo_cover(17, CANOPY, "A wide maple canopy in green and gold", "50% 50%", "Sunday maple walk",
                          "4 things to notice on a fall walk", 84)

    def walk(src, alt, pos, n, title, text, page, extra=""):
        band = (f'<div data-chk="band" style="position: absolute; left: 40px; right: 40px; bottom: 40px; background: {CR}; border-radius: 30px; '
                f'padding: 28px 34px; display: flex; flex-direction: column; gap: 10px">'
                f'<div style="display: flex; gap: 18px; align-items: center">{num(n)}<div style="font-family: {DISPLAY}; font-weight: 800; '
                f'font-size: 52px; line-height: 1; color: {M}">{title}</div></div>'
                f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 34px; line-height: 1.24; color: {M}">{text}</div>{extra}</div>')
        return rootdiv("#222", f'<div style="position: absolute; inset: 0">{img(src, alt, pos)}</div>'
                       f'<div style="position: absolute; left: 56px; top: 56px">{tag(page, "rgba(255,245,222,.92)", M, 24)}</div>' + band)
    s2 = walk(TREE_TALL, "A lone maple with a big round crown", "50% 45%", 1, "Find the tree",
              "Maples growing in the open get big, round crowns, and big crowns mean sweeter sap.", "2 / 6")
    s3 = walk(PLATES, "Maple bark with plates lifting at the edges", "50% 50%", 2, "Read the bark",
              "Thick plates that lift at the edges are a sugar maple clue.", "3 / 6")
    s4 = walk(WID, "A maple leaf under a tape measure", "50% 30%", 3, "Measure a leaf",
              "Wider than it is long? Do the snap test for Norway maple.", "4 / 6")
    s5 = walk(LEAF_RING, "Fallen maple leaves around a tree trunk", "50% 35%", 4, "Mark it",
              "Tie on a ribbon before the last leaves blow away.", "5 / 6",
              f'<div style="margin-top: 8px">{your_turn("Which of the 4 did you try this week?")}</div>')
    s6 = card("A Sunday maple walk is just the start.", 1080, 1350)
    return [s1, s2, s3, s4, s5, s6]


POSTS = [("almanac11", "Almanac11", a11), ("almanac12", "Almanac12", a12), ("almanac13", "Almanac13", a13),
         ("almanac14", "Almanac14", a14), ("almanac15", "Almanac15", a15), ("almanac16", "Almanac16", a16),
         ("almanac17", "Almanac17", a17)]

if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "preview"), exist_ok=True)
    out = []
    for folder, pre, fn in POSTS:
        for i, m in enumerate(fn()):
            p = os.path.join(ROOT, "preview", f"{pre}-{i + 1}.html")
            open(p, "w").write(preview_html(f"{pre}-{i + 1}", m))
            out.append(p)
    print(" ".join(out))
