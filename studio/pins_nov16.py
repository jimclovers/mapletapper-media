"""Pins Nov 16-22 2026 (pin14-pin34), 1000x1500. 3 a day (Nov 17 gets 3 new + the existing 8pm pin).
Lesson pins (8pm; Nov 17 at 5pm) match the 10am Almanac post and link to a matching blog article.
Stand-alone pins (10am, 3pm) teach one thing and link to a product page with UTM tags.
Products are never cropped (object-fit: contain on a light panel). Jim's scenery photos may be cropped.

Extra facts for stand-alone pins (2+ sources each):
- 5/16" hole is ~50% smaller in area than 7/16" and closes sooner: UVM Proctor (Wilmot et al. 2007); CDL; equipment makers.
- Sap runs on nights below freezing (20s F) and days above (40s F): Northern Woodlands; Mass. Maple Producers; Farmers' Almanac.
- Filter sap before boiling to remove bark bits and bugs: UNH Extension; UMaine Bulletin 7038.
- Syrup is done at 7 F above water's boiling point (~219 F); boiling point shifts with weather: MSU Ext.; UMN Ext.; Ohio State.
- Bottle hot, at least 180 F (185-190 F best): Cornell; UMN Ext.; UW-Madison Ext.; MSU Ext.
- Keep sap cold (under 40 F), it spoils like milk; boil within days: UNH Extension; Smoky Lake Maple beginner guide.
- Season ends when buds swell and sap turns off-flavor: Mass. Maple Producers; Farmers' Almanac; our blog.
- ~40 gal sap -> 1 gal syrup (sugar maple), 12 in / 4.5 ft, 1 tap 12-18 in: already-posted rules.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from art import C  # noqa: E402
from build import DISPLAY, TYPE, ROOT, font_faces_local, leaf_mark  # noqa: E402

PW, PH, PHOTO_H = 1000, 1500, 960
OUT = os.path.join(ROOT, "pins", "preview")
J = lambda n: os.path.join(ROOT, "photos", "jim", "nov14", n)
JJ = lambda n: os.path.join(ROOT, "photos", "jim", n)
PR = lambda n: os.path.join(ROOT, "photos", "products", n)
SHOP = "https://mapletapper.com/products/"
BLOG = "https://blog.mapletapper.com/"
PROD = {
    "pink": "pink-maple-tree-tapping-spiles-ten-5-16-tree-saver-taps-bpa-free-food-grade-reusable",
    "deluxe": "deluxe-maple-syrup-tree-tapping-kit-20-taps-20-3-foot-drop-line-tubes-8-quart-sap-filter-dark-blue-premium-food-grade-tubing-recipe-cards-drill-bit-80-page-guide-to-maple-tapping-book",
    "kids": "kids-maple-tree-tapping-kit-taps-tubes",
    "guide": "guide-to-maple-tapping",
    "ultimate": "ultimate-maple-tapping-kit-tap-20-trees-taps-tubes",
    "bottles": "glass-maple-syrup-bottles-3-maple-leaf-design-250-ml-bottles-6-self-sealing-caps-food-grade-canning-bottles-for-sugarmaking",
    "giftcard": "maple-tapper-gift-card",
    "kidsbook": "a-kids-guide-to-maple-tapping",
    "kit10": "maple-syrup-tree-tapping-kit-10-taps-10-3-foot-drop-line-tubes-1-quart-maple-sap-filter-dark-blue-premium-food-grade-tubing-instructions-recipe-cards",
}
BOARD = {"backyard": "374291487720159160", "tips": "374291487720168172", "kids": "374291487720159204",
         "treeid": "374291487721076640"}


def utm(url, slug):
    return f"{url}?utm_source=pinterest&utm_medium=social&utm_campaign=holiday2026&utm_content={slug}"


# (name, date, time, image, product?, pos, kicker, title, sub, link, board, alt)
PINS = [
    ("pin14-small-taps", "2026-11-16", "10:00", PR("pink_spiles.jpg"), True, "", "Tree-friendly tapping",
     "Why Small 5/16\" Maple Taps Are Better for Trees", "The hole is about half the size of an old 7/16\" tap, so it closes sooner",
     utm(SHOP + PROD["pink"], "pin14"), "tips", "Ten pink 5/16 inch tree-saver maple taps"),
    ("pin15-food-grade", "2026-11-16", "15:00", PR("deluxe_flatlay.jpg"), True, "", "Buyer tip",
     "Is Your Maple Tubing Food-Grade?", "Sap is food. Use taps and tubing made for it.",
     utm(SHOP + PROD["deluxe"], "pin15"), "tips", "Deluxe maple tapping kit with taps, blue tubing, filter and guide book"),
    ("pin16-mark-maples", "2026-11-16", "20:00", J("IMG_2638_tree_tall.jpg"), False, "50% 50%", "Do it this fall",
     "Mark Your Maple Trees Before the Leaves Drop", "4 easy ways to find them again in late winter",
     utm(BLOG + "marking-maple-trees-for-easy-identification/", "pin16"), "treeid", "A big round maple alone on a lawn in fall"),
    ("pin17-kids-kit", "2026-11-17", "10:00", PR("kids_kit_flatlay.jpg"), True, "", "Screen-free gift",
     "Kids Can Tap a Real Maple Tree", "5 taps and tubes, filters, and a picture book with an adult how-to",
     utm(SHOP + PROD["kids"], "pin17"), "kids", "Kid's maple tree tapping kit laid out"),
    ("pin18-tree-size", "2026-11-17", "15:00", J("IMG_2621_canopy_trunks.jpg"), False, "50% 60%", "Tree check",
     "Is Your Maple Big Enough to Tap?", "12 inches across at 4½ feet up, about 38 inches around",
     utm(SHOP + PROD["guide"], "pin18"), "backyard", "A big maple trunk in a park"),
    ("pin19-read-bark", "2026-11-17", "17:00", J("IMG_2630_canopy_branch.jpg"), False, "50% 50%", "Winter tree ID",
     "How to Read Maple Bark", "3 bark patterns that help you name a maple without leaves",
     utm(BLOG + "maple-tapping-101/", "pin19"), "treeid", "Maple bark with thick plates lifting at the edges"),
    ("pin20-sap-weather", "2026-11-18", "10:00", PR("kids_kit_snow_jugs.jpg"), True, "", "Sap season",
     "When Does Maple Sap Run?", "Nights below freezing, days in the 40s",
     utm(SHOP + PROD["guide"], "pin20"), "tips", "Blue tubing running from maple taps into jugs in the snow"),
    ("pin21-filter-sap", "2026-11-18", "15:00", PR("ultimate_flatlay.jpg"), True, "", "Sugarmaking step",
     "Filter Maple Sap Before You Boil", "Strain out bark bits and bugs first for cleaner syrup",
     utm(SHOP + PROD["ultimate"], "pin21"), "tips", "Ultimate maple tapping kit with taps, tubing, filters and bottle"),
    ("pin22-measure-leaf", "2026-11-18", "20:00", J("IMG_2691_leaf_tape_vertical.jpg"), False, "50% 45%", "Kids corner",
     "Measure a Maple Leaf: Easy Tree ID for Kids", "Wider than it is long? Do the snap test!",
     utm(BLOG + "maple-tapping-101/", "pin22"), "kids", "A maple leaf next to a tape measure"),
    ("pin23-40-to-1", "2026-11-19", "10:00", PR("deluxe_flatlay.jpg"), True, "", "Maple math",
     "40 Gallons of Sap Make 1 Gallon of Syrup", "That's from sugar maples. Here's why real syrup is special.",
     utm(SHOP + PROD["deluxe"], "pin23"), "tips", "Deluxe maple tapping kit laid out"),
    ("pin24-when-done", "2026-11-19", "15:00", PR("guide_book.jpg"), True, "", "Boiling tip",
     "When Is Maple Syrup Done?", "7°F above water's boiling point, about 219°F",
     utm(SHOP + PROD["guide"], "pin24"), "tips", "Guide to Maple Tapping book cover"),
    ("pin25-stored-sugar", "2026-11-19", "20:00", J("IMG_2843_gold_crown.jpg"), False, "50% 40%", "Surprising fact",
     "Where Does the Sugar in Maple Sap Come From?", "Summer leaves make it. The tree stores it for spring.",
     utm(BLOG + "when-to-tap-maple-trees/", "pin25"), "tips", "A tall maple crown turning gold"),
    ("pin26-bottle-hot", "2026-11-20", "10:00", PR("leaf_bottle_gold_cap.jpg"), True, "", "Bottling tip",
     "How to Bottle Maple Syrup", "Pour it hot: at least 180°F, 185 to 190°F is best",
     utm(SHOP + PROD["bottles"], "pin26"), "backyard", "Glass maple leaf syrup bottle with a gold cap"),
    ("pin27-gift-timeline", "2026-11-20", "15:00", PR("gift_card.jpg"), True, "", "Holiday gift idea",
     "Learn This Fall, Unwrap at Christmas, Tap in Late Winter", "A gift card lets them pick the kit that fits their trees",
     utm(SHOP + PROD["giftcard"], "pin27"), "backyard", "MapleTapper gift card"),
    ("pin28-big-crowns", "2026-11-20", "20:00", J("IMG_2635_tree_wide.jpg"), False, "50% 50%", "Tapping tip",
     "Pick Maples with Big Crowns for Sweeter Sap", "What research says about choosing your best trees",
     utm(BLOG + "advanced-sugarmaking-how-to-increase-your-syrup-production/", "pin28"), "tips", "A big maple with a wide crown in a field"),
    ("pin29-sweetest-tree", "2026-11-21", "10:00", PR("kids_guide_cover_hi.jpg"), True, "", "Kids corner",
     "Which Maple Has the Sweetest Sap?", "Sugar maple: about 40 gallons of sap for 1 gallon of syrup",
     utm(SHOP + PROD["kidsbook"], "pin29"), "kids", "A Kid's Guide to Maple Tapping book cover"),
    ("pin30-sap-cold", "2026-11-21", "15:00", JJ("milk_jug_tubing_blue.jpg"), False, "50% 50%", "Sap care",
     "Treat Maple Sap Like Milk", "Keep it cold, under 40°F, and boil it within a few days",
     utm(SHOP + PROD["kit10"], "pin30"), "backyard", "Blue tubing from a maple tap into a jug"),
    ("pin31-leaf-color", "2026-11-21", "20:00", J("IMG_2844_leaves_closer.jpg"), False, "50% 45%", "Leaf science",
     "Why Maple Leaves Turn Gold and Red", "Easy fall science for kids",
     utm(BLOG + "maple-tapping-101/", "pin31"), "kids", "Green maple leaves turning gold"),
    ("pin32-one-tap", "2026-11-22", "10:00", PR("ultimate_flatlay.jpg"), True, "", "Tree-friendly tapping",
     "How Many Taps Can One Maple Take?", "Trees 12 to 18 inches across get one tap",
     utm(SHOP + PROD["ultimate"], "pin32"), "tips", "Ultimate maple tapping kit laid out"),
    ("pin33-season-end", "2026-11-22", "15:00", J("IMG_2643_branches_sky.jpg"), False, "50% 50%", "Sap season",
     "When Does Maple Tapping Season End?", "When buds swell, the sap turns off-flavor. Pull your taps.",
     utm(SHOP + PROD["guide"], "pin33"), "tips", "Maple branches against the sky"),
    ("pin34-maple-walk", "2026-11-22", "20:00", J("IMG_2834_gold_canopy_wide.jpg"), False, "50% 50%", "Family walk",
     "A Fall Maple Walk: 4 Things to Look For", "Find, read, measure and mark your syrup trees",
     utm(BLOG + "maple-tapping-preseason-checklist/", "pin34"), "backyard", "A wide maple canopy in green and gold"),
]


def pin(photo, product, pos, kicker, title, sub, alt):
    src = "file://" + photo
    if product:
        top = (f'<div style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PHOTO_H}px; background: #F7F4EE; '
               f'box-sizing: border-box; padding: 110px 50px 40px"><img src="{src}" alt="{alt}" style="width: 100%; height: 100%; '
               f'object-fit: contain; display: block"></div>')
    else:
        top = (f'<img src="{src}" alt="{alt}" style="position: absolute; left: 0; top: 0; width: {PW}px; height: {PHOTO_H}px; '
               f'object-fit: cover; object-position: {pos}; display: block">')
    return (
        f'<div data-root style="position: relative; width: {PW}px; height: {PH}px; overflow: hidden; background: {C["maroon"]}; '
        f'font-family: {DISPLAY}; color: {C["cream"]}">' + top
        + f'<span data-chk="kicker" style="position: absolute; left: 48px; top: 40px; background: {C["gold"] if product else C["cream"]}; color: {C["maroon"]}; '
        f'border-radius: 999px; padding: 12px 26px 10px; font-family: {TYPE}; font-size: 30px; letter-spacing: 0.06em; '
        f'text-transform: uppercase">{kicker}</span>'
        f'<div style="position: absolute; left: 0; top: {PHOTO_H}px; width: {PW}px; height: {PH - PHOTO_H}px; box-sizing: border-box; '
        f'padding: 50px 64px 46px; display: flex; flex-direction: column; gap: 18px">'
        f'<h1 data-chk="title" style="margin: 0; font-weight: 800; font-size: {84 if len(title) < 44 else 72}px; line-height: 0.96; letter-spacing: -0.025em; text-wrap: balance">{title}</h1>'
        f'<p data-chk="sub" style="margin: 0; font-weight: 700; font-size: 38px; line-height: 1.2; text-wrap: balance; color: {C["gold"]}">{sub}</p>'
        f'<div style="flex-grow: 1"></div>'
        f'<div data-chk="footer" style="display: flex; align-items: center; gap: 14px; font-family: {TYPE}; font-size: 32px; '
        f'letter-spacing: 0.04em">{leaf_mark(C["gold"], 38)}mapletapper.com</div>'
        f'</div></div>'
    )


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    out = []
    for name, d, t, photo, product, pos, kicker, title, sub, link, board, alt in PINS:
        html = (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>{title}</title>'
                f'<style>{font_faces_local()} body{{margin:0}}</style></head><body>{pin(photo, product, pos, kicker, title, sub, alt)}</body></html>')
        p = os.path.join(OUT, name + ".html")
        open(p, "w").write(html)
        out.append(p)
    print(" ".join(out))
