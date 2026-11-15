"""Pins Nov 23-29 2026 (pin35-pin55), 1000x1500, 3 a day: 10am + 3pm product pins (UTM), 8pm lesson pin (blog article).
Products never cropped (contain). Facts as in lessons_nov23.py / pins_nov16.py."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import ROOT, font_faces_local  # noqa: E402
from pins_nov16 import pin, utm, SHOP, BLOG, PROD, BOARD, OUT, J, JJ, PR  # noqa: E402

PROD = dict(PROD, white="white-maple-tree-tapping-spiles-ten-5-16-maxflow-taps-bpa-free-food-grade-reusable",
            cones="2-maple-syrup-reusable-1-qt-pre-filter-cones-for-home-maple-sugaring-fits-all-cone-holder-sizes-collect-and-boil-sap-in-manageable-amounts-helps-prevent-spills-premium-synthetic-pre-filters-includes-instruction-card")

# (name, date, time, image, product?, pos, kicker, title, sub, link, board, alt, description)
PINS = [
    ("pin35-host-gift", "2026-11-23", "10:00", PR("guide_book.jpg"), True, "", "Thanksgiving host gift",
     "A Host Gift That Outlasts the Leftovers", "Our 80-page Guide to Maple Tapping",
     utm(SHOP + PROD["guide"], "pin35"), "backyard", "Guide to Maple Tapping book cover",
     "Bring a host gift that outlasts the leftovers: our 80-page Guide to Maple Tapping, from finding a maple to bottling the syrup. Order this week and we'll ship it out."),
    ("pin36-kids-book", "2026-11-23", "15:00", PR("kids_guide_cover_hi.jpg"), True, "", "Kids' table",
     "A Maple Tapping Book for Kids", "Read it at Thanksgiving, tap a tree in late winter",
     utm(SHOP + PROD["kidsbook"], "pin36"), "kids", "A Kid's Guide to Maple Tapping book cover",
     "A Kid's Guide to Maple Tapping: kid-friendly words and pictures, from finding a tree to pancakes. A screen-free gift for curious kids."),
    ("pin37-how-to-tap", "2026-11-23", "20:00", JJ("bucket_tubing_tap.jpg"), False, "60% 40%", "Save for February",
     "How to Tap a Maple Tree in 5 Steps", "Drill, tap, tube, collect, repeat",
     utm(BLOG + "how-to-tap-trees/", "pin37"), "tips", "A maple tap with blue tubing on a snowy trunk",
     "How to tap a maple tree: pick a healthy maple 12 inches across, drill a 5/16-inch hole 1½ to 2 inches deep, tap the spout in gently, run the tube to a clean food-grade jug, and collect every day."),
    ("pin38-ultimate", "2026-11-24", "10:00", PR("ultimate_flatlay.jpg"), True, "", "For the DIYer",
     "A Whole Maple Season in One Box", "Taps, tubing, filters, thermometer, bottle and guide",
     utm(SHOP + PROD["ultimate"], "pin38"), "backyard", "Ultimate maple tapping kit laid out",
     "Gift for the DIYer: the Ultimate Maple Syrup Tapping Kit has taps and droplines for up to 20 trees, filters, a thermometer, drill bit, maple-leaf bottle and our guide."),
    ("pin39-drill-depth", "2026-11-24", "15:00", PR("deluxe_flatlay.jpg"), True, "", "Tapping tip",
     "How Deep Do You Drill a Maple Tap Hole?", "5/16 inch wide, 1½ to 2 inches deep",
     utm(SHOP + PROD["deluxe"], "pin39"), "tips", "Deluxe maple tapping kit with taps, tubes, filter and drill bit",
     "How deep to drill a maple taphole: use a 5/16-inch bit and go 1½ to 2 inches deep, straight in or tilted slightly up. Our Deluxe Kit includes the drill bit."),
    ("pin40-kit-pieces", "2026-11-24", "20:00", PR("kids_kit_flatlay.jpg"), True, "", "Kit profile",
     "What's in a Maple Tapping Kit?", "What every piece does, explained",
     utm(BLOG + "maple-tapping-101/", "pin40"), "tips", "Kid's maple tree tapping kit laid out",
     "What's in a maple tapping kit and what each piece does: tree-saver taps, drop-line tubes, a drill bit, a sap filter and a step-by-step guide."),
    ("pin41-leaf-bottles", "2026-11-25", "10:00", PR("leaf_bottle_gold_cap.jpg"), True, "", "Gift idea",
     "Maple-Leaf Glass Bottles for Homemade Syrup", "Fill them in March, give them as gifts all year",
     utm(SHOP + PROD["bottles"], "pin41"), "backyard", "Glass maple-leaf syrup bottle with a gold cap",
     "Glass maple-leaf bottles with gold caps for your homemade maple syrup. Fill them in March and give them as gifts all year."),
    ("pin42-pink-spiles", "2026-11-25", "15:00", PR("pink_spiles.jpg"), True, "", "Stocking stuffer",
     "Pink Maple Taps: A Stocking Stuffer That Leads Outside", "Ten 5/16\" tree-saver spiles, food-grade",
     utm(SHOP + PROD["pink"], "pin42"), "backyard", "Ten pink 5/16 inch maple tapping spiles",
     "Ten bright pink 5/16-inch tree-saver maple taps. Food-grade, reusable, made in North America, with a lifetime guarantee. A stocking stuffer that leads outside."),
    ("pin43-leaf-placemats", "2026-11-25", "20:00", J("IMG_2659_leaf_on_grass.jpg"), False, "50% 55%", "Kids' table craft",
     "Thankful Leaf Placemats for Thanksgiving", "Leaf rubbings + a thank-you on every leaf",
     utm(BLOG + "maple-tapping-101/", "pin43"), "kids", "A big green maple leaf on the grass",
     "Easy Thanksgiving kids' table craft: make leaf-rubbing placemats with real maple leaves and a crayon, then write something you're thankful for on each leaf."),
    ("pin44-maple-facts", "2026-11-26", "10:00", J("IMG_2607_looking_up_trunks.jpg"), False, "50% 40%", "Happy Thanksgiving",
     "5 Maple Syrup Facts for the Thanksgiving Table", "Sap is only about 2% sugar!",
     utm(BLOG + "how-to-make-maple-syrup/", "pin44"), "tips", "Gold and orange maple leaves against a blue sky",
     "Maple facts to share at Thanksgiving: sap is about 2% sugar, it takes about 40 gallons to make 1 gallon of syrup, and one tap gives about a quart of syrup a season."),
    ("pin45-kids-kit", "2026-11-26", "15:00", PR("kids_kit_flatlay.jpg"), True, "", "Screen-free gift",
     "Tap a Real Maple with Your Kids This Winter", "5 taps and tubes, filters and a kids' book",
     utm(SHOP + PROD["kids"], "pin45"), "kids", "Kid's maple tree tapping kit laid out",
     "A screen-free family gift: the Kid's Maple Tree Tapping Kit with 5 taps and tubes, filters, and a picture book with an adult how-to."),
    ("pin46-tap-math", "2026-11-26", "20:00", JJ("milk_jug_tubing_blue.jpg"), False, "50% 70%", "Maple math",
     "How Many Taps Do You Need?", "1 tap ≈ 1 quart of syrup a season",
     utm(BLOG + "maple-tapping-preseason-checklist/", "pin46"), "tips", "A maple tap with blue tubing running into a milk jug",
     "How many maple taps do you need? One tap gives about 10 gallons of sap and about a quart of syrup a season, so about 4 taps make a gallon."),
    ("pin47-black-friday", "2026-11-27", "10:00", PR("deluxe_flatlay.jpg"), True, "", "Black Friday gift guide",
     "Maple Tapping Gifts for Everyone on Your List", "Kids, grandparents, neighbors and DIYers",
     utm(SHOP + PROD["deluxe"], "pin47"), "backyard", "Deluxe maple tapping kit laid out",
     "Black Friday gift guide: maple tapping kits for kids, grandparents, neighbors with big maples and DIYers. Order by Dec 21 to have it by Christmas."),
    ("pin48-one-tap", "2026-11-27", "15:00", JJ("milk_jug_tubing.jpg"), False, "50% 60%", "Backyard sugaring",
     "Start Small: 10 Taps Is Plenty", "About 2½ gallons of syrup in a good season",
     utm(SHOP + PROD["kit10"], "pin48"), "backyard", "A maple tap with tubing into a milk jug in the snow",
     "Start small: a 10-tap kit can make about 2½ gallons of maple syrup in a good season. Our Maple Syrup Tree Tapping Kit has 10 taps and tubes and a filter."),
    ("pin49-countdown", "2026-11-27", "20:00", PR("kids_kit_snow_jugs.jpg"), True, "", "Your countdown",
     "From Thanksgiving to Tapping Day", "Mark trees now, gather gear, tap in late winter",
     utm(BLOG + "when-to-tap-maple-trees/", "pin49"), "tips", "Blue tubing from maple taps into jugs in a snowy woods",
     "Your maple tapping countdown: mark your trees now, gather gear in December, watch the forecast in January, and tap when nights freeze and days reach the 40s."),
    ("pin50-shop-small", "2026-11-28", "10:00", PR("gift_card.jpg"), True, "", "Small Business Saturday",
     "Shop Small: A Family Maple Tapping Business", "Gift cards let them pick their kit",
     utm(SHOP + PROD["giftcard"], "pin50"), "backyard", "MapleTapper gift card",
     "Shop small this Saturday: MapleTapper is family run, with gear made in North America and a lifetime guarantee. A gift card lets them pick their kit."),
    ("pin51-old-holes", "2026-11-28", "15:00", JJ("bucket_tubing_tap.jpg"), False, "55% 35%", "Tapping tip",
     "Where to Tap: Skip Last Year's Holes", "6 inches to the side, 2 feet above or below",
     utm(SHOP + PROD["white"], "pin51"), "tips", "A maple tap and tubing on a trunk",
     "Where to drill your maple taphole: stay at least 6 inches to the side of an old hole and 2 feet above or below it, so you hit fresh, healthy wood."),
    ("pin52-plan", "2026-11-28", "20:00", J("IMG_2837_canopy_sky.jpg"), False, "50% 50%", "Get ready",
     "When Will Maple Sap Run Where You Live?", "Freezing nights and days in the 40s",
     utm(BLOG + "when-to-tap-maple-trees/", "pin52"), "tips", "A maple canopy turning gold",
     "When does maple sap run? When nights drop below freezing and days climb into the 40s. In southern Michigan that's usually late February; farther north, March."),
    ("pin53-stocking", "2026-11-29", "10:00", PR("kids_guide_cover.jpg"), True, "", "Stocking stuffers",
     "Maple Stocking Stuffers Under $35", "Books, spiles, filters and leaf bottles",
     utm(SHOP + PROD["kidsbook"], "pin53"), "kids", "A Kid's Guide to Maple Tapping book cover",
     "Maple stocking stuffers under $35: our tapping guides, ten 5/16-inch spiles, reusable pre-filter cones and maple-leaf glass bottles."),
    ("pin54-season-length", "2026-11-29", "15:00", PR("guide_book.jpg"), True, "", "Sap season",
     "How Long Does Maple Tapping Season Last?", "Usually about 4 to 6 weeks",
     utm(SHOP + PROD["guide"], "pin54"), "tips", "Guide to Maple Tapping book cover",
     "Maple tapping season usually lasts about 4 to 6 weeks, starting when nights freeze and days thaw. Learn every step in our Guide to Maple Tapping."),
    ("pin55-no-fancy-gear", "2026-11-29", "20:00", JJ("milk_jug_tubing_blue.jpg"), False, "50% 55%", "Backyard sugaring",
     "No Fancy Gear Needed to Tap a Maple", "A tap, a tube and a clean jug",
     utm(BLOG + "how-to-use-droplines/", "pin55"), "backyard", "A maple tap with blue tubing running into a milk jug",
     "Backyard maple tapping without fancy gear: a 5/16-inch tap, a drop-line tube and a clean food-grade jug. Empty it daily and keep the sap cold."),
]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    out = []
    for name, d, t, photo, product, pos, kicker, title, sub, link, board, alt, desc in PINS:
        html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
                f'<style>{font_faces_local()} body{{margin:0}}</style></head><body>{pin(photo, product, pos, kicker, title, sub, alt)}</body></html>')
        p = os.path.join(OUT, name + ".html")
        open(p, "w").write(html)
        out.append(p)
    print(" ".join(out))
