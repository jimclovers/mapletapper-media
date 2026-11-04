# MapleTapper studio (build tools backup)

The scripts that make the MapleTapper Instagram slides and Reels, kept here so a new Claude chat can pick up where the last one left off.

- `build.py`, `post0*.py`, `tree0*.py`, `bonus01.py`, `funfacts.py`: carousel slides (1080x1350), rendered with `render.js` (Playwright).
- `reels/build_reel.py`: Reels from Jim's video clips (maroon frame, captions, fact cards).
- `reels/photo_reel.py`: photo-montage Reels (full-bleed photos, color labels, lesson + call-to-action cards).
- `captions/`: final Instagram captions for every scheduled post.
- `tools/meta_audit.py`: checks that no photo or video carries hidden location/date data before posting.

House rules every post follows: facts checked against 2+ sources and rewritten in our own words; main house and license plates blurred, no location data; AI pictures get a small "AI illustration" tag on the slide, on the picture itself, and never Instagram's AI label at the top of the post (isAiGenerated stays false; Jim's call, Nov 4 2026; Meta only requires its label for photorealistic AI video or realistic AI audio, which we don't post); never AI people; brand colors maroon #7A1E1A, red #C8321F, gold #F4B63F, cream #FFF5DE; fonts Bricolage Grotesque + Special Elite.
