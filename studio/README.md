# MapleTapper studio (build tools backup)

The scripts that make the MapleTapper Instagram slides and Reels, kept here so a new Claude chat can pick up where the last one left off.

- `build.py`, `post0*.py`, `tree0*.py`, `bonus01.py`, `funfacts.py`: carousel slides (1080x1350), rendered with `render.js` (Playwright).
- `reels/build_reel.py`: Reels from Jim's video clips (maroon frame, captions, fact cards).
- `reels/photo_reel.py`: photo-montage Reels (full-bleed photos, color labels, lesson + call-to-action cards).
- `captions/`: final Instagram captions for every scheduled post.
- `tools/meta_audit.py`: checks that no photo or video carries hidden location/date data before posting.

House rules every post follows: facts checked against 2+ sources and rewritten in our own words; main house and license plates blurred, no location data; AI pictures carry no AI label of any kind: no tag on the slide, no caption note, no Instagram label (isAiGenerated false). Jim's call, Nov 4 2026: do only what Meta requires, and Meta only requires its label for photorealistic AI video or realistic AI audio (turn it on if we ever post those). Never call an AI picture a real photo; never AI people; brand colors maroon #7A1E1A, red #C8321F, gold #F4B63F, cream #FFF5DE; fonts Bricolage Grotesque + Special Elite.

Logo rule (Jim, Nov 7 2026): every carousel and Reel shows the MapleTapper logo (studio/assets/logo.png, the version with www.mapletapper.com) at least once, on the last slide / end card. The logo is dark brown on transparent, so place it on cream or gold, or on a cream badge over maroon. Never over a photo.

Call-to-action rule (Jim, Nov 8 2026): no "Next up" teaser boxes on slides, since they point nowhere. The box beside the logo on the last slide asks for a direct action tied to the post ("Your turn · comment below" + a short question, or share a photo / tag @mapletapper). Captions end with the comment question, then "🔔 Follow @mapletapper (Facebook: MapleTapper) so you don't miss tomorrow's post: ...".

Photo rule (Jim, Nov 8 2026): never show people boiling sap next to a propane tank (safety). Show maple tapping with the tubing-and-bucket setup instead (plenty in Drive: Clover's Maple Tapping Photos, e.g. maple-tapping-tube-through-lid, tube and tree). The kid's BUCKET kit is not sold; the Kid's Maple Tree Tapping Kit is the tubing version, so never use the kid's bucket kit product photo.

Guarantee (Jim, Nov 8 2026): all MapleTapper taps, tubing and equipment carry a lifetime guarantee. Jim: in years of selling, no tap or tube has deteriorated or been returned for failure. OK to say: lifetime guarantee; food-grade; made to last for years; in all our years selling, we've never had a tap or tube fail with regular use and good care. Do NOT name or describe other sellers' or overseas products (no claims about others without documented proof); keep it positive about ours. OK as a general buyer tip: not every tube or tap sold online is made for food (some tubing is made for oil, grease or industrial use), so check that tubing and taps are food-grade and made for maple sap. Ours are.
