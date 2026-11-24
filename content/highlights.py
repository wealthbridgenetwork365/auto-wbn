# Instagram Highlights: 3 topics x 3 story slides, doodle storytelling style, large bold type.
# Render with: python3 scripts/render_story.py content/highlights.py stories/
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import *  # noqa
from doodle import _p, _t, INK, RED, GREEN
from marks_story import lbl, divider, cap


def link_card(x, y, w=720, title="CLICK THIS LINK"):
    """Soft green card with a dashed pill slot where the Instagram link sticker goes.
    (x, y) = top-centre of the card. Height 400."""
    l, h = x - w / 2, 400
    b = f'<rect x="{l+14}" y="{y+16}" width="{w}" height="{h}" rx="44" fill="{INK}"/>'                # hard shadow
    b += f'<rect x="{l}" y="{y}" width="{w}" height="{h}" rx="44" fill="#DFF7EA" stroke="{INK}" stroke-width="9"/>'
    b += (f'<rect x="{x-215}" y="{y+42}" width="430" height="84" rx="42" fill="#2FE08A" stroke="{INK}" stroke-width="7"/>'
          + _t(x, y + 99, title, 44, 800))
    b += _p(f"M{x},{y+142} L{x},{y+188} M{x-20},{y+168} L{x},{y+190} L{x+20},{y+168}", 8)                # little arrow
    b += (f'<rect x="{l+60}" y="{y+212}" width="{w-120}" height="150" rx="75" fill="#fff" stroke="{GREEN}" '
          f'stroke-width="7" stroke-dasharray="22 16"/>')
    for sx, sy in ((l + 40, y + 30), (l + w - 40, y + 370)):                                             # sparkles
        b += _p(f"M{sx},{sy-22} L{sx},{sy+22} M{sx-22},{sy} L{sx+22},{sy}", 7, color=GREEN)
    return b


def pills(names, y0=0, row=112, cols=(225, 675), w=420):
    """Two columns of rounded tags, alternating green/white."""
    b = ""
    for i, n in enumerate(names):
        cx, y = cols[i % 2], y0 + (i // 2) * row
        fill = "#2FE08A" if (i // 2 + i % 2) % 2 == 0 else "#fff"
        b += f'<rect x="{cx-w/2}" y="{y}" width="{w}" height="88" rx="44" fill="{fill}" stroke="{INK}" stroke-width="7"/>'
        b += _t(cx, y + 60, n, 42, 800)
    return b


CATS = ["Models", "Athletes", "Travel bloggers", "Fitness", "Fashion", "Beauty", "E-commerce", "Storytellers",
        "Food & lifestyle", "Tech & gadgets", "Gaming", "Podcasters", "Artists", "Photographers", "Comedians", "Family"]


def month(x, y, s, name):
    return coins(x, y, s, 3) + lbl(x, y + 70 * s, name, INK, int(34 * s / 0.7), 800)


POSTS = [
# ================================================================ 1 · CREATORS
dict(id="hl-creators", title="Creators", slides=[
 dict(tag="Creators · UGC", hook="Become a\n*creator.*", hs=170,
      kick="Chinese brands want *your content.* We get you *represented* in the Chinese market.", ks=54,
      scene=ground(40, 860, 620) + phone(170, 620, 0.95, "REC") + figure(400, 620, 1.2, "hold", "grin") + camera(600, 420, 0.8) + coins(760, 620, 0.9, 4), vh=640),
 dict(head="Who we\n*represent:*", hd=96,
      scene=pills(CATS) + _t(450, 8 * 112 + 60, "+ many more", 46, 800, GREEN), vh=8 * 112 + 90, ah=1100),
 dict(head="How it *works:*", hd=96,
      items=["Go to the *link in bio*", "Fill in the *application*", "Once approved, you'll get an *email from our team* with next steps"], **{"is": 64},
      scene=link_card(450, 20), vh=440),
]),
# ================================================================ 2 · AFFILIATE
dict(id="hl-affiliate", title="Affiliate", slides=[
 dict(tag="Affiliate program", hook="Become an\n*affiliate.*", hs=160,
      kick="Earn *recurring money* every month from the people you sign up. Plus a *discounted membership.*", ks=56,
      scene=ground(40, 860, 620) + figure(230, 620, 1.25, "point", "grin") + phone(500, 620, 1.0, "LINK") + moneybag(740, 620, 1.0), vh=640),
 dict(head="How it *works:*", hd=96,
      items=["Go to the *link in bio*", "Fill in the *affiliate application*", "Once approved, you'll get an *email from our team* with next steps", "Share your link and *earn every month*"], **{"is": 64},
      scene=ground(60, 840, 360) + phone(170, 360, 0.75, "LINK") + arrow(280, 220, 380, 220, -60) + crowd(530, 360, 0.6, 4, "happy") + arrow(660, 220, 730, 220, -60) + coins(800, 360, 0.75, 4), vh=380),
 dict(hook="Share once.\n*Get paid*\n*monthly.*", hs=130,
      scene=lbl(450, 30, "YOUR MONTHS", INK, 40) + arrow(150, 100, 750, 80, -60, GREEN, 12)
      + ground(40, 860, 270) + month(130, 200, 0.7, "JAN") + month(290, 200, 0.7, "FEB") + month(450, 200, 0.7, "MAR")
      + month(610, 200, 0.7, "APR") + month(770, 200, 0.7, "MAY")
      + link_card(450, 320), vh=740),
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
      kick="Join today. *Tap below.*", ks=64,
      scene=link_card(450, 20), vh=440),
]),
]
