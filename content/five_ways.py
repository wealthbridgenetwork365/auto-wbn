# "5 ways to benefit from China" - 7-slide doodle carousel. Each topic slide is split into 4 sections (2x2 grid).
# Render: python3 scripts/render_doodle.py content/five_ways.py $PWD/posts/
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import *  # noqa
from doodle import _p, _t, INK
from china_stories import cta, G, NECIPS

TEACH = "Source: Migaku 2026 China teaching salary guide; ranges vary by employer"
CSC = "Source: CSC & Confucius Institute scholarship pages; check the official site for this cycle"
INV = "Not financial advice. Rules vary by city and change; check with a licensed adviser"


def cell(cx, y0, icon, title, lines):
    b = icon
    b += _t(cx, y0 + 250, title, 44, 800, G)
    for k, ln in enumerate(lines):
        b += _t(cx, y0 + 308 + 46 * k, ln, 36, 600)
    return b


def grid(cells):
    """cells: 4 x (icon_fn(cx, base_y), title, [lines]) laid out 2x2 with a cross divider."""
    b = _p("M450,20 L450,880", 7, color="#BBBBBB") + _p("M20,450 L880,450", 7, color="#BBBBBB")
    for k, (icon, title, lines) in enumerate(cells):
        cx, y0 = (225, 675)[k % 2], (0, 450)[k // 2]
        b += cell(cx, y0, icon(cx, y0 + 190), title, lines)
    return b


def topic(n, name, cells, src=""):
    return dict(head=f"{n}. *{name}*", hd=88, scene=grid(cells), vh=900, ah=960, src=src)


POSTS = [
dict(id="48-five-ways", pillar="Opportunities", title="4 ways to benefit from China",
 caption="Building Bridges | Creating Access",
 slides=[
 dict(hook="4 ways to\n*benefit*\nfrom China.", hs=150, swipe=True,
      kick="Jobs, sourcing, brand deals and language programs.",
      scene=ground(40, 860, 300) + board(150, 300, 0.45, "JOBS") + factory(360, 300, 0.4) + phone(560, 300, 0.55, "DEAL")
      + board(750, 300, 0.45, "中文"), vh=320),
 topic(1, "Jobs", [
   (lambda x, y: board(x, y, 0.5, "TEFL"), "Teaching", ["Up to 35K+ RMB/mo", "at top int'l schools"]),
   (lambda x, y: laptop(x, y, 0.55, "SALES"), "Trade & marketing", ["Foreign trade sales,", "e-commerce, ads"]),
   (lambda x, y: check(x, y - 30, 1.2, True), "What you need", ["Bachelor's degree;", "120-hr TEFL to teach"]),
   (lambda x, y: skyline(x, y, 0.38), "Top cities", ["Shanghai, Shenzhen,", "Guangzhou, Chengdu"]),
 ], TEACH),
 topic(2, "Sourcing", [
   (lambda x, y: factory(x, y, 0.45), "Where to find", ["Most common: 1688,", "Alibaba, Canton Fair"]),
   (lambda x, y: handshake_hands(x, y - 50, 0.75), "Meet in person", ["Build relationships", "and meet the direct", "manufacturer"]),
   (lambda x, y: box(x, y, 0.65), "Sample first", ["Approve a sample", "before bulk orders"]),
   (lambda x, y: coins(x, y, 0.8, 3), "Pay smart", ["Deposit first, balance", "after inspection"]),
 ]),
 topic(3, "Brand deals", [
   (lambda x, y: figure(x, y, 0.55, "up", "grin"), "Who", ["Creators & athletes", "with real audiences"]),
   (lambda x, y: tower(x, y, 0.36), "Brands", ["Hotels, cafés,", "fashion, sportswear"]),
   (lambda x, y: moneybag(x, y, 0.8), "You get", ["Paid deals, free", "stays & products"]),
   (lambda x, y: clock(x, y - 60, 0.9), "Timeline", ["Matched to paid", "in about 4 weeks"]),
 ]),
 topic(4, "Language", [
   (lambda x, y: board(x, y, 0.5, "中文"), "Scholarship", ["Confucius Institute:", "learn Chinese in China"]),
   (lambda x, y: door(x, y, 0.5), "Covers", ["Full tuition", "+ free dorm"]),
   (lambda x, y: coins(x, y, 0.8, 4), "Stipend", ["2,500-3,000", "RMB a month"]),
   (lambda x, y: phone(x, y, 0.55, "APPLY"), "Apply", ["Usually Jan-Apr", "via an institute"]),
 ], CSC),
 dict(hook="Join our\n*network.*", hs=170,
      kick="Tap the *link in bio* to join.",
      scene=ground(60, 840, 560) + figure(230, 560, 1.15, "point", "grin") + phone(600, 560, 1.4, "JOIN"), vh=580),
]),
]
