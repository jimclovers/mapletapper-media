"""Evening gift posts, Nov 9-15 2026 (Holiday Gift Guide, 3 slides each).
Usage: python3 gifts.py  -> preview/Gift0N-K.html  (render with render.js, save to posts/giftNN/)
Prices from the MapleTapper Shopify store, Nov 7 2026. No discounts. Order by Dec 21 for Christmas.
"""
import base64
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, W, H, ROOT, kicker_row, footer_row, headline, body, root, column, preview_html  # noqa: E402

SRC = "/home/claude/src"
LOGO = "data:image/png;base64," + base64.b64encode(open(os.path.join(ROOT, "assets", "logo.png"), "rb").read()).decode()
M, R, G, CR = C["maroon"], C["red"], C["gold"], C["cream"]


def img(name):
    return "file://" + os.path.join(SRC, name)


def pill(text, bg, fg, size=24):
    return (f'<span style="display: inline-flex; align-items: center; background: {bg}; color: {fg}; border-radius: 999px; '
            f'padding: 10px 20px 8px; font-family: {TYPE}; font-size: {size}px; letter-spacing: 0.06em; text-transform: uppercase">{text}</span>')


def price_tag(price, bg=G, fg=M):
    return (f'<span data-chk="price" style="display: inline-flex; align-items: baseline; gap: 10px; background: {bg}; color: {fg}; border-radius: 18px; '
            f'padding: 12px 24px; font-family: {DISPLAY}; font-weight: 800; font-size: 48px; line-height: 1">{price}</span>')


def cover(n, photo, alt, head, sub, fit="cover", photo_bg="#FFFFFF", tag=None):
    ph = (f'<div style="position: absolute; left: 0; top: 0; width: {W}px; height: 760px; background: {photo_bg}">'
          f'<img src="{photo}" alt="{alt}" style="width: 100%; height: 100%; object-fit: {fit}; display: block"></div>')
    top = (f'<div data-chk="pills" style="position: absolute; left: 56px; right: 56px; top: 52px; display: flex; justify-content: space-between; z-index: 2">'
           f'{pill(f"Holiday Gift Guide · {n} of 7", CR, M)}{pill("Order by Dec 21", G, M)}</div>')
    tg = f'<div style="position: absolute; right: 56px; top: 690px; z-index: 3; transform: rotate(3deg)">{price_tag(tag)}</div>' if tag else ""
    bottom = (f'<div style="position: absolute; left: 0; top: 760px; width: {W}px; height: {H - 760}px; box-sizing: border-box; '
              f'padding: 84px 72px 60px; display: flex; flex-direction: column; gap: 22px; background: {M}">'
              + headline(head, 84, CR) + body(sub, 36, G, "sub", "; font-weight: 700")
              + '<div style="flex-grow: 1"></div>'
              + footer_row(CR, f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; color: {CR}">Swipe →</span>') + "</div>")
    return root(M, ph + top + tg + bottom, CR)


def check(main, note=""):
    return (f'<div style="display: flex; gap: 22px; align-items: flex-start">'
            f'<div style="flex: none; width: 54px; height: 54px; border-radius: 50%; background: {R}; color: {CR}; display: flex; align-items: center; '
            f'justify-content: center; font-family: {DISPLAY}; font-weight: 800; font-size: 32px">✓</div>'
            f'<div style="display: flex; flex-direction: column; gap: 4px"><div style="font-family: {DISPLAY}; font-weight: 800; font-size: 40px; line-height: 1.08; color: {M}">{main}</div>'
            + (f'<div style="font-family: {DISPLAY}; font-weight: 500; font-size: 29px; line-height: 1.25; color: {M}; opacity: .85">{note}</div>' if note else "")
            + "</div></div>")


def middle(n, kicker, head, items, photo=None, alt="", photo_h=380):
    ph = (f'<div style="border-radius: 28px; overflow: hidden; height: {photo_h}px; flex: none; background: #fff">'
          f'<img src="{photo}" alt="{alt}" style="width: 100%; height: 100%; object-fit: cover; display: block"></div>') if photo else ""
    inner = (kicker_row(kicker, f"{n} / 3", R) + headline(head, 76, M) + ph
             + '<div style="display: flex; flex-direction: column; gap: 22px">' + "".join(check(*i) for i in items) + "</div>"
             + '<div style="flex-grow: 1"></div>' + footer_row(M, f'<span style="font-family: {DISPLAY}; font-weight: 700; font-size: 30px; color: {M}">Swipe →</span>'))
    return root(CR, column(inner, gap=30), M)


def last(head, lines, cta_label, cta_q, price_line, photo=None, alt="", photo_h=330):
    box = (f'<div data-chk="cta" style="flex: 1 1 0; background: {M}; color: {CR}; border-radius: 32px; padding: 26px 34px; display: flex; flex-direction: column; gap: 8px">'
           f'<div style="font-family: {TYPE}; font-size: 24px; letter-spacing: 0.06em; text-transform: uppercase; color: {G}">{cta_label}</div>'
           f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 42px; line-height: 1.05">{cta_q}</div></div>')
    logo = f'<img data-chk="logo" src="{LOGO}" alt="MapleTapper logo, www.mapletapper.com" style="width: 210px; flex: none; display: block">'
    ship = (f'<div data-chk="ship" style="background: #fff; border: 4px solid {G}; border-radius: 28px; padding: 26px 32px; display: flex; flex-direction: column; gap: 8px">'
            f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: .06em; text-transform: uppercase; color: {R}">Christmas delivery</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 44px; line-height: 1.08; color: {M}">{price_line}</div>'
            f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 32px; color: {M}">Order by Dec 21 at mapletapper.com</div></div>')
    inner = (kicker_row("Holiday Gift Guide", "3 / 3", R) + headline(head, 80, M)
             + "".join(body(l, 36, M, f"l{i}") for i, l in enumerate(lines))
             + (f'<div style="border-radius: 28px; overflow: hidden; height: {photo_h}px; flex: none"><img src="{photo}" alt="{alt}" style="width: 100%; height: 100%; object-fit: cover; display: block"></div>' if photo else "")
             + ship
             + '<div style="flex-grow: 1"></div>'
             + f'<div style="display: flex; align-items: center; gap: 28px">{box}{logo}</div>'
             + footer_row(M, "<span></span>"))
    return root(CR, column(inner, gap=30), M)


POSTS = {
    1: dict(
        slug="kidskit",
        cover=dict(photo=img("kids_kit.jpg"), alt="The Kid's Maple Tree Tapping Kit: buckets, lids, spouts, filter and the kid's guide book",
                   head="A gift they'll use outside, not on a screen.", sub="The Kid's Maple Tree Tapping Kit", fit="contain", tag="$39.97"),
        mid=dict(kicker="Why kids love it", head="Real trees.<br>Real syrup.", photo=img("boy_spile.jpg"), alt="A child's hand on a spout in a maple trunk",
                 items=[("They tap a real backyard maple", "Kid-size buckets and real spouts"),
                        ("A guide book written just for them", "A Kid's Guide to Maple Tapping is in the box"),
                        ("A science lesson they can taste", "Watch sap drip, then boil it into syrup")]),
        last=dict(head="Open it at Christmas. Tap it in late winter.", lines=["Sap runs when nights freeze and days thaw, so the fun starts right after the holidays."],
                  cta_label="Your turn · tag a friend", cta_q="Know a kid who'd love this? Tag their grown-up!", price_line="Kid's Kit · $39.97", photo=img("syrup_jars.jpg"), alt="Jars of homemade maple syrup"),
    ),
    2: dict(
        slug="kidsbook",
        cover=dict(photo=img("boy_spile.jpg"), alt="A child's hand on a spout in a maple trunk, snow behind",
                   head="A stocking stuffer that leads outside.", sub="A Kid's Guide to Maple Tapping", tag="$14.99"),
        mid=dict(kicker="Inside the book", head="Made for young sugarmakers", photo=img("dripping_sap.jpg"), alt="Sap dripping into a blue bucket in the woods",
                 items=[("How sap turns into syrup", "Explained in kid-friendly words"),
                        ("How to find and tap a maple", "With a grown-up, of course"),
                        ("Pairs with any tapping kit", "Or read it first and plan for spring")]),
        last=dict(head="Small gift. Big backyard adventure.", lines=["Tuck it in a stocking now, then head outside together when the sap starts running."],
                  cta_label="Your turn · comment below", cta_q="Who read with you as a kid? Tell us!", price_line="Kid's Guide · $14.99", photo=img("big_maple.jpg"), alt="A big maple trunk in snow"),
    ),
    3: dict(
        slug="starter",
        cover=dict(photo=img("tubes_bucket.jpg"), alt="A spout and blue drop line running into a white bucket at the base of a maple",
                   head="First time tapping? Start here.", sub="Starter 10-Tap Kit + Book", tag="$39.97"),
        mid=dict(kicker="What you get", head="Everything for a first season", photo=img("big_maple.jpg"), alt="A big maple trunk with snow at its base", photo_h=300,
                 items=[("10 taps", "Enough for up to 10 trees, one tap each"),
                        ("Our Guide to Maple Tapping book", "Step by step, from finding trees to bottling"),
                        ("Made for backyards", "No sugar shack needed. A kitchen stove or a porch burner works.")]),
        last=dict(head="The perfect gift for the curious one.", lines=["Know someone who's always asking “could I make my own syrup”? This is their answer."],
                  cta_label="Your turn · comment below", cta_q="How many maples are in your yard?", price_line="Starter Kit + Book · $39.97", photo=img("boil_outside.jpg"), alt="Sap boiling outside"),
    ),
    4: dict(
        slug="ultimate",
        cover=dict(photo=img("ultimate.png"), alt="Everything in the Ultimate Kit laid out: spouts, droplines, tubing, filters, thermometer, drill bit, bottle and book",
                   head="The gift for the DIYer who has everything.", sub="The Ultimate Maple Tapping Kit", fit="contain", photo_bg="#000000", tag="$179.99"),
        mid=dict(kicker="What's in the box", head="Tap, collect, filter, bottle", photo=img("tubes_bucket.jpg"), alt="A spout and drop line running into a bucket", photo_h=260,
                 items=[("20 tree-saver spouts + 20 droplines", "Plus 50 feet of tubing and 10 connectors"),
                        ("3-piece filter kit + candy thermometer", "For clear syrup boiled to just the right point"),
                        ("5/16\" drill bit + maple leaf glass bottle", "Drill clean holes, then show off the syrup"),
                        ("Our 80-page Guide + recipe cards", "Lifetime guarantee on the taps and tubes")]),
        last=dict(head="Everything from tree to table.", lines=["One box covers a whole season, from the first drip to the first bottle."],
                  cta_label="Your turn · comment below", cta_q="Who's the DIYer on your list?", price_line="Ultimate Kit · $179.99", photo=img("filter_pour.jpg"), alt="Syrup pouring through a filter"),
    ),
    5: dict(
        slug="stuffers",
        cover=dict(photo=img("bottles_primary.png"), alt="Three maple leaf glass bottles with caps and recipe cards",
                   head="Stocking stuffers for syrup lovers.", sub="Five gifts, all $35 or less", fit="contain"),
        mid=dict(kicker="Under $35", head="Pick a stocking stuffer", photo=img("filter_pour.jpg"), alt="Syrup pouring through a filter", photo_h=240,
                 items=[("Guide to Maple Tapping book · $12.99", "Our step-by-step guide"),
                        ("A Kid's Guide to Maple Tapping · $14.99", "For young sugarmakers"),
                        ("Tree-saver spiles · $19.97", "In black, pink or white"),
                        ("Syrup filters · from $19.99", "For clear, grit-free syrup"),
                        ("3 maple leaf glass bottles · $33.79", "For gifting homemade syrup")]),
        last=dict(head="Little gifts, sweet results.", lines=["Easy to wrap, easy to ship, and every one gets used in sap season."],
                  cta_label="Your turn · comment below", cta_q="Which one goes in your stocking?", price_line="Stocking stuffers from $12.99", photo=img("dripping_sap.jpg"), alt="Sap dripping into a bucket"),
    ),
    6: dict(
        slug="timeline",
        cover=dict(photo=img("boil_outside.jpg"), alt="Sap boiling in a pot over a propane burner outside, steam rising",
                   head="Give it in December. Boil syrup by March.", sub="How a tapping kit gift plays out"),
        mid=dict(kicker="The gift timeline", head="From wrapping paper to pancakes", photo=img("dripping_sap.jpg"), alt="Sap dripping into a bucket", photo_h=300,
                 items=[("December: open the kit", "Read the guide over the holidays"),
                        ("January: pick your trees", "Maples at least 12 inches across"),
                        ("Late winter: tap", "When nights are in the 20s and days in the 40s"),
                        ("Spring: boil and bottle", "About 40 gallons of sugar maple sap make 1 gallon of syrup")]),
        last=dict(head="A gift that lasts all season.", lines=["Most gifts are opened once. This one keeps going every freeze-and-thaw day until spring."],
                  cta_label="Your turn · comment below", cta_q="When does sap run where you live?", price_line="Tapping kits from $34.97", photo=img("syrup_jars.jpg"), alt="Jars of homemade maple syrup"),
    ),
    7: dict(
        slug="giftcard",
        cover=dict(photo=img("syrup_jars.jpg"), alt="Jars of homemade maple syrup stacked in a sunny window",
                   head="Not sure which kit? Let them pick.", sub="MapleTapper gift cards"),
        mid=dict(kicker="Why a gift card", head="The no-guess gift", photo=img("boil_outside.jpg"), alt="Sap boiling outside", photo_h=340,
                 items=[("Any amount from $10 to $200", "Fits every budget"),
                        ("Good for anything in the shop", "Kits, books, spiles, filters and bottles"),
                        ("A last-minute lifesaver", "Perfect when you're short on time")]),
        last=dict(head="Let them choose their own adventure.", lines=["Starter kit, Ultimate kit or a stocking full of supplies: it's their call."],
                  cta_label="Your turn · comment below", cta_q="What's the best gift you ever got?", price_line="Gift cards $10 to $200", photo=img("tubes_bucket.jpg"), alt="A spout and drop line running into a bucket"),
    ),
}


if __name__ == "__main__":
    out = os.path.join(ROOT, "preview")
    for n, p in POSTS.items():
        for k, html in ((1, cover(n, **p["cover"])), (2, middle(2, **p["mid"])), (3, last(**p["last"]))):
            open(os.path.join(out, f"Gift0{n}-{k}.html"), "w").write(preview_html(f"Gift {n} slide {k}", html))
    print("built")
