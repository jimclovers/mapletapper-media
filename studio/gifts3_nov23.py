"""Evening gift posts Nov 23-29 2026 (gift15-21): Thanksgiving / Black Friday / Small Business Saturday week.
No discounts or coupons (Jim). Every product photo shown whole (object-fit: contain). Prices from mapletapper.com/products.json (Nov 15).
Jim (Nov 15): Guide book orders placed this week can still go out before Thanksgiving.
Business facts: only Jim-confirmed ones (family run; three generations tapping our Michigan family farm; made in North America;
lifetime guarantee on taps, tubing and equipment)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import C, DISPLAY, TYPE, ROOT, headline, preview_html  # noqa: E402
from covers_v2 import PINE, SKY, NAVY, SNOW, logo_badge, tag, handle, rootdiv, data_uri  # noqa: E402
from closing import card  # noqa: E402
import gifts2_posts as g2  # noqa: E402

M, CR, G, R = C["maroon"], C["cream"], C["gold"], C["red"]
PR = lambda n: os.path.join(ROOT, "photos", "products", n)
J = lambda n: os.path.join(ROOT, "photos", "jim", "nov14", n)


def product_cover(bg, fg, tag_txt, tag_bg, tag_fg, title, photo, alt, title_size=104, right_tag="Order by Dec 21", photo_bg="#FFFFFF"):
    return rootdiv(bg, (
        f'<div style="position: absolute; left: 56px; top: 60px">{tag(tag_txt, tag_bg, tag_fg, 28)}</div>'
        + (f'<div style="position: absolute; right: 56px; top: 60px">{tag(right_tag, CR, M, 28)}</div>' if right_tag else "")
        + f'<div style="position: absolute; left: 56px; right: 56px; top: 150px; height: 600px; border-radius: 32px; background: {photo_bg}; '
          f'padding: 24px; box-sizing: border-box"><img src="{data_uri(photo)}" alt="{alt}" style="width: 100%; height: 100%; object-fit: contain; display: block"></div>'
        + f'<div style="position: absolute; left: 56px; right: 200px; top: 800px">' + headline(title, title_size, fg, chk="title") + '</div>'
        + handle(fg) + logo_badge(bg=CR, bottom=40, size=130)))


def photo_cover(photo, alt, small, title, pos="50% 50%"):
    return rootdiv("#222", (
        f'<img src="{data_uri(photo)}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: {pos}">'
        f'<div style="position: absolute; left: 0; right: 0; bottom: 0; height: 760px; background: linear-gradient(to top, rgba(15,10,5,.85), rgba(15,10,5,0))"></div>'
        f'<div style="position: absolute; left: 56px; right: 56px; bottom: 210px"><div style="margin-bottom: 18px">{tag(small, "rgba(255,255,255,.92)", M, 28)}</div>'
        + headline(title, 112, "#FFFFFF", chk="title", extra="; text-shadow: 0 3px 16px rgba(0,0,0,.45)") + '</div>'
        + handle("#FFFFFF") + logo_badge(bottom=40, size=130)))


POSTS = [
 dict(n=15, slug="kidstable", date="2026-11-23",
      cover=lambda: product_cover(SKY, NAVY, "Gift for the kids’ table", G, NAVY, "A book they’ll ask to read again", PR("kids_guide_cover_hi.jpg"),
                                  "The cover of A Kid's Guide to Maple Tapping", 96),
      kicker="For curious kids", head="Read it now, tap it later", photo=None,
      items=["A Kid’s Guide to Maple Tapping: $14.99", "Kid-friendly words and pictures, from tree to pancakes", "Pair it with the Kid’s Maple Tree Tapping Kit: $39.97",
             "Real taps, tubes and filters for one tree or a few"],
      price="Kid’s Guide · $14.99", q="What book is a hit at your kids’ table?", close="One good kids’ book is just the start."),
 dict(n=16, slug="ultimate", date="2026-11-24",
      cover=lambda: product_cover(PINE, CR, "For the DIYer", G, PINE, "A whole season in one box", PR("ultimate_flatlay.jpg"),
                                  "The Ultimate Maple Syrup Tapping Kit laid out: droplines, tubing, spiles, filters, thermometer, drill bit, leaf bottle and guidebook"),
      kicker="The big one", head="Everything from tap to bottle", photo=None,
      items=["Taps and droplines for up to 20 trees", "Tubing, connectors and filters", "A thermometer, drill bit and a maple-leaf glass bottle",
             "Our Guide to Maple Tapping", "Lifetime guarantee on the taps and tubing"],
      price="Ultimate Kit · $179.99", q="Who on your list loves a big project?", close="A whole season in one box is just the start."),
 dict(n=17, slug="hostlastcall", date="2026-11-25",
      cover=lambda: product_cover(NAVY, CR, "Still need a host gift?", G, NAVY, "It’s not too late", PR("guide_book.jpg"),
                                  "The Guide to Maple Tapping book", 112, right_tag="Order today"),
      kicker="Thanksgiving host gift", head="Order today, we’ll ship it this week", photo=None,
      items=["Our Guide to Maple Tapping: $12.99", "80 pages full of photos", "From finding a maple to bottling the syrup",
             "Running late? A MapleTapper gift card is the instant answer"],
      price="Guide to Maple Tapping · $12.99", q="Who’s hosting Thanksgiving this year?", close="One good book is just the start."),
 dict(n=18, slug="thankful", date="2026-11-26",
      cover=lambda: photo_cover(J("IMG_2834_gold_canopy_wide.jpg"), "A wide maple canopy in green and gold", "Happy Thanksgiving",
                                "Thankful for you"),
      kicker="From our family to yours", head="Happy Thanksgiving", photo=None,
      items=["Thank you for following along this fall", "Thank you to every family who tapped a tree with us", "Three generations tapping our Michigan family farm, and we love getting you started",
             "Enjoy the pie. We’ll be back tomorrow with our gift guide"],
      price="From all of us at MapleTapper", q="What are you thankful for this year?", close="A thankful heart is just the start.", no_deadline=True),
 dict(n=19, slug="blackfriday", date="2026-11-27",
      cover=lambda: product_cover(R, "#FFFFFF", "Black Friday gift guide", G, M, "Maple gifts for everyone on your list", PR("deluxe_flatlay.jpg"),
                                  "Deluxe maple tapping kit laid out: taps, blue tubes, filter, drill bit, recipe cards and guide book", 92),
      kicker="Who’s it for?", head="Pick by person", photo=None,
      items=["Kids and classrooms: Kid’s Kit, $39.97", "Grandparents: Kid’s Kit + Kid’s Guide, $39.97 + $14.99",
             "A neighbor with big maples: Deluxe Kit + Book, $69.96", "The DIYer: Ultimate Kit, $179.99", "Stockings: ten 5/16″ spiles, $19.97"],
      price="Gifts from $12.99", q="Who are you shopping for first?", close="The right gift is just the start."),
 dict(n=20, slug="shopsmall", date="2026-11-28",
      cover=lambda: photo_cover(PR("kids_kit_snow_jugs.jpg"), "Blue tubing running from maple taps into jugs in a snowy woods",
                                "Small Business Saturday", "Shop small, tap big", "50% 45%"),
      kicker="Who we are", head="A family business", photo=None,
      items=["Family run: three generations tapping our Michigan family farm", "Taps, tubing and gear made in North America",
             "Food-grade, with a lifetime guarantee", "In all our years selling, we’ve never had a tap or tube fail with regular use and good care"],
      price="Kits from $34.97", q="What small business are you supporting today?", close="Shopping small is just the start."),
 dict(n=21, slug="stocking", date="2026-11-29",
      cover=lambda: rootdiv(SNOW, (
          f'<div style="position: absolute; left: 56px; top: 60px">{tag("Stocking stuffers", R, "#FFFFFF", 28)}</div>'
          f'<div style="position: absolute; right: 56px; top: 60px">{tag("Order by Dec 21", PINE, "#FFFFFF", 28)}</div>'
          f'<div style="position: absolute; left: 56px; top: 150px; width: 470px; height: 620px; border-radius: 30px; background: #FFFFFF; padding: 20px; box-sizing: border-box">'
          f'<img src="{data_uri(PR("leaf_bottle_gold_cap.jpg"))}" alt="Glass maple-leaf syrup bottle with a gold cap" style="width: 100%; height: 100%; object-fit: contain"></div>'
          f'<div style="position: absolute; right: 56px; top: 150px; width: 470px; height: 620px; border-radius: 30px; background: #FFFFFF; padding: 20px; box-sizing: border-box">'
          f'<img src="{data_uri(PR("pink_spiles.jpg"))}" alt="Ten pink maple tapping spiles" style="width: 100%; height: 100%; object-fit: contain"></div>'
          f'<div style="position: absolute; left: 56px; right: 200px; top: 820px">' + headline("Stocking stuffers under $35", 104, R, chk="title") + '</div>'
          + handle(PINE) + logo_badge(bg=CR, bottom=40, size=130))),
      kicker="Small gifts, big fun", head="All under $35", photo=None,
      items=["Guide to Maple Tapping: $12.99", "A Kid’s Guide to Maple Tapping: $14.99", "Ten 5/16″ spiles, pink or white: $19.97",
             "Two reusable pre-filter cones: $19.99", "3 maple-leaf glass bottles with gold caps: $33.79"],
      price="Gift cards from $10", q="Which one fits in your stocking?", close="A stocking stuffer is just the start."),
]

if __name__ == "__main__":
    out = []
    for p in POSTS:
        n = p["n"]
        if p.get("no_deadline"):
            g2.DEADLINE = "Happy Thanksgiving"
        else:
            g2.DEADLINE = "Order by Dec 21 to have it by Christmas"
        for k, html in ((1, p["cover"]()), (2, g2.mid(p)), (3, card(p["close"], 1080, 1350))):
            f = os.path.join(ROOT, "preview", f"gift{n:02d}-{k}-{p['slug']}.html")
            open(f, "w").write(preview_html(f"Gift {n} slide {k}", html))
            out.append(f)
    print(" ".join(out))
