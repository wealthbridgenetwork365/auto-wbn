# Instagram Highlights: 3 topics x 3 story slides, doodle storytelling style, large bold type.
# Render with: python3 scripts/render_story.py content/highlights.py stories/
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import *  # noqa
from doodle import _p, _t, INK, RED, GREEN
from marks_story import lbl, divider, cap


def month(x, y, s, name):
    return coins(x, y, s, 3) + lbl(x, y + 52 * s, name, INK, int(34 * s / 0.7), 800)


POSTS = [
# ================================================================ 1 · CREATORS
dict(id="hl-creators", title="Creators", slides=[
 dict(tag="Creators · UGC", hook="Become a\n*creator.*", hs=170,
      kick="Chinese brands want *your content.* We get you *represented* in the Chinese market.", ks=54,
      scene=ground(40, 860, 620) + phone(170, 620, 0.95, "REC") + figure(400, 620, 1.2, "hold", "grin") + camera(600, 420, 0.8) + coins(760, 620, 0.9, 4), vh=640),
 dict(head="Who we\n*represent:*", hd=96,
      items=["Models", "Athletes", "Travel bloggers", "Fitness", "Fashion", "Cosmetics", "E-commerce", "Storytellers"], **{"is": 70},
      scene=ground(60, 840, 300) + camera(150, 300, 0.55) + ball(300, 300, 0.6) + plane(470, 200, 0.45) + dumbbell(640, 300, 0.6) + figure(800, 300, 0.6, "up", "grin", flip=True), vh=320),
 dict(head="How it *works:*", hd=96,
      items=["*DM us* to apply", "Send us your *media kit*", "We match you with *Chinese brands*", "You film, post and *get paid*"], **{"is": 72},
      scene=ground(60, 840, 420) + board(160, 420, 0.75, "KIT") + arrow(270, 270, 380, 270, -60) + handshake_hands(500, 330, 0.9) + arrow(610, 270, 700, 270, -60) + moneybag(790, 420, 0.8), vh=440),
]),
# ================================================================ 2 · AFFILIATE
dict(id="hl-affiliate", title="Affiliate", slides=[
 dict(tag="Affiliate program", hook="Become an\n*affiliate.*", hs=160,
      kick="Earn *recurring money* every month from the people you sign up.", ks=58,
      scene=ground(40, 860, 620) + figure(230, 620, 1.25, "point", "grin") + phone(500, 620, 1.0, "LINK") + moneybag(740, 620, 1.0), vh=640),
 dict(head="How it *works:*", hd=96,
      items=["Get your *personal link*", "Share it with your audience", "They sign up, *you earn*", "Paid *every month* they stay", "Plus a *discounted membership*"], **{"is": 70},
      scene=ground(60, 840, 360) + phone(170, 360, 0.75, "LINK") + arrow(280, 220, 380, 220, -60) + crowd(530, 360, 0.6, 4, "happy") + arrow(660, 220, 730, 220, -60) + coins(800, 360, 0.75, 4), vh=380),
 dict(hook="Share once.\n*Get paid*\n*monthly.*", hs=150,
      scene=lbl(450, 50, "YOUR MONTHS", INK, 40)
      + ground(40, 860, 420) + month(130, 360, 0.7, "JAN") + month(290, 360, 0.7, "FEB") + month(450, 360, 0.7, "MAR")
      + month(610, 360, 0.7, "APR") + month(770, 360, 0.7, "MAY") + arrow(150, 150, 750, 120, -80, GREEN, 12), vh=460,
      kick="*Tap the link in bio* to become an affiliate.", ks=60),
]),
# ================================================================ 3 · JOIN THE NETWORK
dict(id="hl-network", title="Join us", slides=[
 dict(tag="Wealth Bridge Network", hook="Join our\n*network.*", hs=170,
      kick="Your bridge to *China opportunities.*", ks=60,
      scene=ground(40, 860, 560) + figure(110, 560, 1.0, "wave", "grin") + bridge(450, 560, 1.0, 520) + skyline(780, 560, 0.7), vh=600),
 dict(head="Get access *to:*", hd=96,
      items=["*Brand deals*", "*Jobs* in China", "*Scholarships*", "*Manufacturing* & sourcing", "*Free mentorship*"], **{"is": 76},
      scene=ground(60, 840, 360) + phone(150, 360, 0.6, "DEAL") + board(330, 360, 0.55, "JOB") + cap(520, 330, 0.7) + factory(700, 360, 0.5), vh=380),
 dict(hook="Building\n*bridges.*\nCreating\n*access.*", hs=160,
      kick="*Tap the link in bio* to join today.", ks=64,
      scene=ground(60, 840, 520) + figure(230, 520, 1.15, "point", "grin") + follow_phone(600, 520, 1.1), vh=540),
]),
]
