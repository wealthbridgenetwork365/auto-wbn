# "China, explained" storytelling series (doodle style). Drafts for approval.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from doodle import *  # noqa
from doodle import _p

SERIES = "China, explained · Part {}"
FOLLOW = "*Follow @wealthbridgenetwork* for more."
YIWU = "Source: People's Daily, Mar 2026"
TEACH = "Source: Migaku 2026 China teaching salary guide. USD at 6.67 RMB (Oct 26, 2026)"
CANTON = "Source: China Daily, Apr 2026 (139th Canton Fair, phase 1)"
CSC = "Source: CSC program pages (SUFE, 2026). Check the official site for this cycle"
PROPHET = "Source: Prophet, \"Chinese Brands Going Global\", May 2026"
DANYANG = "Source: China Daily, Jan 2022"
GDP = "Source: Xinhua via Henan Gov't, Feb 2026 (2025 GDP)"


def cta(part_next, scene_extra=""):
    return dict(
        text=["China is the biggest opportunity most people are ignoring.",
              f"We break it down, one topic at a time. {FOLLOW}"],
        scene=ground(60, 840, 540) + figure(200, 540, 1.05, "wave", "grin") + bridge(590, 540, 0.8, 520)
        + bubble(560, 250, 1.0, part_next, 500, "left", ACC_C) + scene_extra,
        vh=560)


ACC_C = "#139A52"

POSTS = [
# =============================================================== 1 · SOURCING
dict(id="31-how-to-source", pillar="Sourcing", title="How to source products from China", slides=[
 dict(tag=SERIES.format(1), text=["How to source products from China.", "*(Without getting burned.)*"], fs=72,
      scene=ground(40, 860, 580) + figure(250, 580, 1.15, "hold", "happy") + magnifier(400, 470, 0.9) + factory(650, 580, 1.15), vh=600),
 dict(text=["Most people find a supplier online, message three factories and pay the first one that replies.",
            "Six weeks later the boxes arrive. *Wrong color. Wrong size. No refund.*"],
      scene=ground(80, 820, 520) + figure(300, 520, 1.0, "shrug", "sad", confused=True) + box(560, 520, 0.95, q=True) + box(700, 520, 0.7, q=True)),
 dict(head="Step 1: Know where to look.", items=["**Alibaba.com**: built for overseas buyers", "**1688.com**: China's domestic wholesale site, often cheaper, in Chinese",
            "**Trade fairs**: the Canton Fair in Guangzhou, every spring and autumn", "**Wholesale markets**: Yiwu, the \"world's supermarket\""], **{"is": 42},
      scene=laptop(115, 300, 0.7, "Alibaba") + laptop(345, 300, 0.7, "1688") + stall(585, 300, 0.62) + pin(800, 300, 1.05), vh=310),
 dict(text=["Yiwu has nearly *80,000 booths* selling over *2.1 million* types of products.", "You can walk it for a week and not see it all."],
      scene=ground(40, 860, 520) + stall(210, 520, 0.9) + stall(560, 520, 0.9) + figure(780, 520, 0.95, "point", "wow", flip=True), src=YIWU),
 dict(head="Step 2: Never skip the sample.", text=["Order samples from *three* suppliers. Put them side by side.", "The cheapest one is rarely the one you want."], fs=50,
      scene=ground(60, 840, 500) + box(170, 500, 0.85) + check(170, 270, 1.2, False) + box(400, 500, 0.85) + check(400, 270, 1.2, False)
      + box(630, 500, 0.85) + check(630, 270, 1.2, True) + figure(790, 500, 0.9, "point", "happy", flip=True), vh=520),
 dict(head="Step 3: Check before you pay in full.", text=["Pay a deposit. Have a *third-party inspector* check the goods at the factory. Then pay the balance and ship."], fs=48,
      scene=coins(110, 330, 1.0) + arrow(200, 230, 300, 230, -60) + magnifier(410, 330, 1.0) + arrow(530, 230, 620, 230, -60)
      + ship(750, 330, 0.55) + ground(30, 870, 330), vh=360),
 dict(head="The Big Four (get them in writing):", items=["Price per unit", "Minimum order quantity (MOQ)", "Production lead time", "Shipping terms (FOB, DDP...)"], **{"is": 50},
      scene=tag(130, 300, 1.0, "$") + box(360, 300, 0.95, "MOQ") + clock(570, 300, 1.05) + ship(790, 300, 0.5), vh=320),
 cta("Part 2: Making money"),
]),
# =============================================================== 2 · MAKE MONEY
dict(id="32-make-money", pillar="Make money", title="7 ways to make money in China", slides=[
 dict(tag=SERIES.format(2), text=["7 ways to make money in China.", "*Most people only know one.*"], fs=74,
      scene=ground(60, 840, 580) + figure(300, 580, 1.2, "up", "grin") + moneybag(560, 580, 1.2) + coins(730, 580, 0.9, 5), vh=600),
 dict(text=["People think China is closed to foreigners.", "Meanwhile, foreigners there are *teaching, filming, sourcing* and *signing brand deals.*"],
      scene=ground(60, 840, 520) + door(220, 520, 0.95, lock=True) + check(220, 160, 1.0, False) + door(560, 520, 0.95, open_=True) + figure(720, 520, 0.95, "point", "happy", flip=True)),
 dict(head="1. Teach English", text=["Public schools pay about *$1,800-$3,000* a month.", "Top international schools pay *$5,250+.*"], fs=50,
      scene=ground(60, 840, 480) + board(330, 480, 0.95, "ABC") + figure(640, 480, 0.95, "point", "happy", tie=True, flip=True), src=TEACH, vh=500),
 dict(head="2. Brand deals (creators & athletes)", text=["Chinese brands want foreign faces to make content: hotels, cafés, sportswear, travel.", "*You film. They pay.*"], fs=50,
      scene=ground(60, 840, 500) + figure(220, 500, 0.95, "hold", "grin") + camera(390, 340, 0.7) + figure(620, 500, 0.95, "up", "happy") + ball(760, 500, 0.7), vh=520),
 dict(head="3. Sourcing agent  ·  4. Import & resell", text=["Help businesses back home find and check factories, for a fee.", "Or buy from the factory yourself and sell online at home."], fs=48,
      scene=ground(40, 860, 440) + factory(150, 440, 0.6) + arrow(260, 340, 340, 340, -50) + ship(470, 440, 0.38) + arrow(580, 340, 650, 340, -50) + laptop(770, 440, 0.6, "$$$"), vh=460),
 dict(head="5, 6 and 7:", items=["**Trade-fair content**: film supplier tours at the Canton Fair (*167K* overseas buyers in one phase)",
            "**Study for free**: CSC scholarships cover tuition, a dorm and a monthly stipend",
            "**Work for a Chinese brand going global**: they need English speakers for marketing and sales"], **{"is": 40},
      scene=ground(60, 840, 290) + stall(170, 290, 0.6) + board(450, 290, 0.6, "CSC") + tower(730, 290, 0.48), vh=300, src=CANTON + "; " + CSC),
 dict(text=["Pick *one.* Go deep.", "Most people try all seven and finish none."], fs=64,
      scene=ground(60, 840, 560) + signpost(330, 560, 1.15, ("ONE", "ALL 7")) + figure(640, 560, 1.05, "think", "flat", flip=True), vh=580),
 cta("Part 3: Their struggles"),
]),
# =============================================================== 3 · STRUGGLES
dict(id="33-company-struggles", pillar="Brand deals", title="What Chinese companies struggle with", slides=[
 dict(tag=SERIES.format(3), text=["Chinese companies can make almost anything.", "*Here's what they can't do.*"], fs=70,
      scene=ground(60, 840, 560) + factory(300, 560, 1.1) + figure(640, 560, 1.1, "shrug", "flat", confused=True), vh=580),
 dict(text=["They can build a great product for a fraction of the cost.", "Then they try to sell it in America... and *nobody knows who they are.*"],
      scene=ground(60, 840, 500) + figure(190, 500, 0.95, "hold", "happy") + box(330, 380, 0.6) + crowd(620, 500, 1.1, 5), vh=520),
 dict(head="Struggle #1: Nobody knows the brand.", text=["Many sell through big marketplaces. Shoppers remember *the store*, not the brand."], fs=50,
      scene=ground(60, 840, 500) + laptop(300, 500, 1.0, "STORE") + box(620, 500, 1.0, q=True), src=PROPHET),
 dict(head="Struggle #2: Competing on price.", text=["Lead with specs and price, and you become *one of a thousand* identical listings."], fs=50,
      scene=ground(40, 860, 500) + "".join(tag(110 + i*170, 500, 0.9, "$9") for i in range(5)) + squiggle(250, 760, 230), src=PROPHET),
 dict(head="Struggle #3: Speaking the culture.", text=["Translating words is easy.", "Knowing what makes people *trust, laugh and buy* is not."], fs=50,
      scene=ground(60, 840, 520) + figure(170, 520, 0.95, "phone", "happy") + bubble(390, 150, 1.0, "Buy now!!!", 300, "left")
      + figure(690, 520, 0.95, "down", "flat", flip=True, confused=True)),
 dict(head="Struggle #4: Finding real voices.", text=["They need creators and athletes people actually *believe.*", "Ads don't build trust. People do."], fs=50,
      scene=ground(60, 840, 500) + figure(260, 500, 0.95, "hold", "grin") + phone(400, 340, 0.55, "REC") + figure(620, 500, 0.95, "up", "happy") + ball(760, 500, 0.65), vh=520),
 dict(text=["Their problem is *your opportunity.*", "Every struggle above is a job for someone who understands both sides."], fs=58,
      scene=ground(40, 860, 520) + figure(110, 520, 0.85, "wave", "happy") + bridge(450, 520, 0.95, 560) + figure(800, 520, 0.85, "wave", "happy", flip=True), vh=540),
 dict(text=["*Creators & athletes:* we connect you with Chinese brands that need your voice.", FOLLOW + " DM us your media kit."], fs=50,
      scene=ground(60, 840, 500) + figure(250, 500, 1.0, "wave", "grin") + bridge(580, 500, 0.8, 520) + bubble(560, 220, 1.0, "Part 4: The cities", 480, "left", ACC_C), vh=520),
]),
# =============================================================== 4 · CITIES
dict(id="34-china-cities", pillar="Best cities", title="Every city in China has a job", slides=[
 dict(tag=SERIES.format(4), text=["China isn't one place.", "*Every city has a different job.*"], fs=74,
      scene=ground(60, 840, 580) + pin(120, 400, 0.9) + pin(300, 300, 0.9, ACC_C) + pin(480, 440, 0.9) + pin(660, 330, 0.9)
      + _p("M120,420 Q220,520 300,320 Q390,520 480,460 Q570,360 660,350", 7) + figure(840, 580, 0.75, "think", "happy", flip=True), vh=600),
 dict(head="Shanghai: money & global brands", text=["China's finance capital. Head offices, big brands, the most international city.", "*Best for:* business, finance, brand meetings."], fs=48,
      scene=ground(60, 840, 500) + skyline(380, 500, 1.15) + figure(720, 500, 0.85, "hips", "happy", tie=True), vh=520),
 dict(head="Shenzhen: hardware & electronics", text=["The tech city next to Hong Kong. If it has a circuit board, a supplier is nearby.", "*Best for:* tech, gadgets, startups."], fs=48,
      scene=ground(60, 840, 500) + chip(300, 470, 1.15) + phone(570, 500, 0.8) + figure(760, 500, 0.85, "point", "wow", flip=True)),
 dict(head="Guangzhou: trade", text=["Home of the Canton Fair, China's giant trade show, every spring and autumn.", "*Best for:* sourcing, apparel, wholesale."], fs=48,
      scene=ground(60, 840, 500) + stall(300, 500, 1.0) + figure(600, 500, 0.9, "hold", "happy") + box(730, 410, 0.5)),
 dict(head="Hangzhou: e-commerce", text=["Alibaba's hometown, and a *2.3 trillion yuan* economy.", "*Best for:* selling online, livestream shopping."], fs=48,
      scene=ground(60, 840, 500) + phone(280, 500, 1.1, "LIVE") + figure(520, 500, 0.95, "phone", "grin") + moneybag(730, 500, 0.75), src=GDP),
 dict(head="Yiwu: small goods", text=["Nearly *80,000 booths*: toys, jewelry, gifts, packaging, decor.", "*Best for:* sourcing small products in bulk."], fs=48,
      scene=ground(60, 840, 500) + stall(260, 500, 0.9) + stall(560, 500, 0.75) + figure(780, 500, 0.85, "shrug", "wow", flip=True), src=YIWU),
 dict(head="Chengdu: food & lifestyle", text=["Spicy food, pandas and a slower pace, with a lower cost of living than Shanghai.", "*Best for:* creators, teachers, saving money."], fs=48,
      scene=ground(60, 840, 500) + noodles(300, 500, 1.0) + panda(600, 500, 1.1)),
 cta("Part 5: The products"),
]),
# =============================================================== 5 · PRODUCTS
dict(id="35-product-hometowns", pillar="Sourcing", title="Every product has a hometown", slides=[
 dict(tag=SERIES.format(5), text=["Almost everything you own has a *hometown* in China."], fs=76,
      scene=ground(60, 840, 580) + figure(260, 580, 1.15, "hold", "wink") + glasses(470, 400, 0.55) + kite(700, 580, 0.95), vh=600),
 dict(text=["China doesn't make things everywhere.", "Whole towns specialize in *one product.* Find the town and you find the best factories."], fs=52,
      scene=ground(60, 840, 500) + pin(200, 500, 0.9) + glasses(200, 270, 0.6) + pin(450, 500, 0.9, ACC_C) + sofa(450, 280, 0.55) + pin(700, 500, 0.9) + kite(700, 290, 0.5), vh=520),
 dict(head="Danyang: glasses", text=["One city in Jiangsu makes about *45% of the world's* eyeglass lenses."], fs=54,
      scene=ground(60, 840, 500) + glasses(380, 360, 1.1) + figure(720, 500, 0.95, "point", "wow", flip=True), src=DANYANG),
 dict(head="Shenzhen: electronics", text=["Phones, chargers, earbuds, drones. Parts, factories and engineers, all in one city."], fs=52,
      scene=ground(60, 840, 500) + phone(220, 500, 0.9) + chip(470, 470, 0.9) + figure(720, 500, 0.95, "hold", "happy", flip=True)),
 dict(head="More hometowns:", items=["**Foshan**: furniture", "**Weifang**: kites (about *75%* of the world market)", "**Dingzhou**: fitness gear", "**Qingxian**: makeup brushes"], **{"is": 48},
      scene=sofa(140, 300, 0.75) + kite(370, 300, 0.75) + dumbbell(600, 300, 0.8) + brush(800, 300, 0.85), vh=320, src=DANYANG + " (Weifang, Dingzhou, Qingxian)"),
 dict(text=["*Go to the town, not just the website.*", "When dozens of factories sit on the same street, they compete on price and quality for you."], fs=52,
      scene=ground(40, 860, 500) + factory(150, 500, 0.6) + factory(380, 500, 0.6) + factory(610, 500, 0.6) + figure(810, 500, 0.85, "point", "grin", flip=True)),
 cta("Save this one!"),
]),
]
