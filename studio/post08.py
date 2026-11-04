"""Post 08 - Label check: "Is that really maple syrup?" (4 slides). Photos: MapleTapper book (pancakes, jar on a branch).
Facts checked against 2+ sources, Nov 4 2026:
  - US standard of identity: maple syrup is made by concentrating and heating maple sap; at least 66% soluble solids by
    weight from the sap; only salt, preservatives or defoaming agents may be added (21 CFR 168.140 via Cornell LII and
    GPO; USDA AMS grade standards quote the 66% Brix minimum)
  - typical pancake syrup labels: corn syrup and/or high fructose corn syrup, water, cellulose gum, caramel color, salt,
    natural and artificial flavor, preservatives (Pearl Milling Company Original via Walmart; Mrs. Butterworth's
    Original; Kroger Buttered Pancake Syrup) - shown generically, no brand names
  - grade names on real syrup: Grade A + color and taste, e.g. Amber Color and Rich Taste (USDA AMS standards, 2015)
  - about 40 gallons of sap per gallon of syrup (MSU Extension; Ontario Maple; earlier posts)
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from build import DISPLAY, TYPE, kicker_row, footer_row, swipe, headline, body, root, column  # noqa: E402
from funfacts import teaser, site_footer  # noqa: E402
from wk2 import M, CR, RED, GOLD, GREEN, SPACER, stamp, cover, circle_badge, check_mark, x_mark, build_preview  # noqa: E402

ASSETS = {"cover": "book/p1_pancakes.jpg", "jar": "book/p1_cover_jar.jpg"}


def panel(ok, name, ingredients, note):
    col = GREEN if ok else RED
    badge = circle_badge(check_mark(CR) if ok else x_mark(CR), col, size=88, ring=col)
    return (
        f'<div style="flex: 1; display: flex; flex-direction: column; gap: 14px">'
        f'<div style="display: flex; align-items: center; gap: 14px">{badge}<div style="font-family: {DISPLAY}; font-weight: 800; '
        f'font-size: 44px; line-height: 1.02; color: {M}">{name}</div></div>'
        f'<div style="background: #FFFFFF; border: 4px solid {M}; border-radius: 16px; padding: 20px 22px; display: flex; flex-direction: column; gap: 8px">'
        f'<div style="font-family: Arial, Helvetica, sans-serif; font-weight: 900; font-size: 30px; letter-spacing: 0.02em; color: #111">INGREDIENTS:</div>'
        f'<div style="font-family: Arial, Helvetica, sans-serif; font-weight: 600; font-size: 31px; line-height: 1.3; color: #111">{ingredients}</div></div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 600; font-size: 31px; line-height: 1.2; color: {M}">{note}</div></div>'
    )


def chip(text, bg, fg):
    return (f'<span style="display: inline-block; background: {bg}; color: {fg}; border-radius: 999px; padding: 10px 22px 9px; '
            f'font-family: {DISPLAY}; font-weight: 800; font-size: 30px; line-height: 1.1">{text}</span>')


# ---------------------------------------------------------------- slides
def slide1():
    inner = cover(
        "cover", "Maple syrup pouring onto a stack of pancakes with butter", "Sugarmaker’s Almanac · No. 08",
        stamp("LABEL", "check"),
        "Is that really<br>maple syrup?",
        "Most pancake syrup isn’t. Flip the bottle. Swipe!",
        title_size=100, obj_pos="50% 40%",
    )
    return root(M, inner, CR), "Is that really maple syrup?"


def slide2():
    inner = (
        kicker_row("Label check · Flip the bottle", "2 / 4", M)
        + headline(f'Read the<br><span style="color: {RED}">ingredients.</span>', 104, M)
        + body("Flip the bottle over. The ingredient list tells you what’s really inside.", 34, M, "lead")
        + SPACER
        + f'<div data-chk="panels" style="display: flex; gap: 30px; align-items: flex-start">'
        + panel(True, "Pure maple<br>syrup", "Pure maple syrup.", "One ingredient: maple sap, boiled down.")
        + panel(False, "Pancake<br>syrup", "Corn syrup, high fructose corn syrup, water, cellulose gum, caramel color, salt, "
                "natural and artificial flavor, preservatives.", "A typical store label. Maple isn’t on the list.")
        + "</div>"
        + SPACER
        + footer_row(M, swipe(M))
    )
    return root(CR, column(inner, gap=28), M), "Read the ingredients"


def slide3():
    real = " ".join(chip(t, GREEN, CR) for t in ["Pure maple syrup", "100% pure maple", "Grade A + a color and taste"])
    fake = " ".join(chip(t, CR, M) for t in ["Pancake syrup", "Table syrup", "Breakfast syrup", "Maple-flavored", "Artificially flavored"])
    group = lambda label, chips, chk: (
        f'<div data-chk="{chk}" style="display: flex; flex-direction: column; gap: 16px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase; color: {GOLD}">{label}</div>'
        f'<div style="display: flex; flex-wrap: wrap; gap: 14px">{chips}</div></div>'
    )
    law = (
        f'<div data-chk="law" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 26px 32px; display: flex; flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 25px; letter-spacing: 0.06em; text-transform: uppercase">The rule</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 37px; line-height: 1.14">In the US, maple syrup must be made from maple sap '
        f'and be at least 66% sugar. Nothing sweet can be added.</div></div>'
    )
    inner = (
        kicker_row("Label check · Words to know", "3 / 4", CR)
        + headline(f'Words on<br><span style="color: {GOLD}">the front.</span>', 108, CR)
        + SPACER
        + group("Real maple syrup says", real, "real")
        + group("Not pure maple syrup", fake, "fake")
        + SPACER
        + law
        + f'<div data-chk="src" style="font-family: {TYPE}; font-size: 22px; color: {GOLD}">Source: FDA standard for maple syrup, 21 CFR 168.140</div>'
        + footer_row(CR, swipe(CR))
    )
    return root(M, column(inner, gap=26), CR), "Words on the front"


def slide4():
    photo = (
        f'<div data-chk="photo" style="position: relative; height: 360px; border-radius: 30px; overflow: hidden; flex: none">'
        f'<img src="@@IMG_jar@@" alt="A jar of maple syrup sitting on a maple branch" style="width: 100%; height: 100%; object-fit: cover; '
        f'object-position: 50% 45%; display: block">'
        f'<div style="position: absolute; left: 24px; bottom: 22px; background: {CR}; color: {M}; border-radius: 999px; padding: 10px 24px 9px; '
        f'font-family: {DISPLAY}; font-weight: 800; font-size: 28px">About 40 gallons of sap in every gallon</div></div>'
    )
    challenge = (
        f'<div data-chk="challenge" style="background: {GOLD}; color: {M}; border-radius: 30px; padding: 26px 32px; display: flex; flex-direction: column; gap: 8px">'
        f'<div style="font-family: {TYPE}; font-size: 26px; letter-spacing: 0.06em; text-transform: uppercase">Family taste test</div>'
        f'<div style="font-family: {DISPLAY}; font-weight: 800; font-size: 38px; line-height: 1.12">Pour a spoonful of each. '
        f'Can you taste the difference? Which one does your family like best?</div></div>'
    )
    inner = (
        kicker_row("Label check · Try it", "4 / 4", M)
        + headline(f'Why real syrup<br><span style="color: {RED}">costs more.</span>', 96, M)
        + body("Real maple syrup is sap boiled down for hours, in a short season each spring. Pancake syrup starts with corn syrup.", 33, M, "why")
        + photo
        + challenge
        + SPACER
        + teaser("Saturday", "Maple scavenger hunt!", M, CR)
        + site_footer(M)
    )
    return root(CR, column(inner, gap=24), M), "Why real syrup costs more"


SLIDES = [("Post08-1-Cover", slide1), ("Post08-2-Ingredients", slide2), ("Post08-3-Words", slide3), ("Post08-4-TasteTest", slide4)]

if __name__ == "__main__":
    for p in build_preview(SLIDES, ASSETS):
        print(p)
