# "China tips" storytelling series: 7 topics x 5 slides, doodle style. Drafts for approval.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from doodle import *  # noqa
from doodle import _p

G = "#139A52"
YIWU = "Source: People's Daily, Mar 2026"
TEACH = "Source: Migaku 2026 China teaching salary guide. USD at 6.67 RMB (Oct 26, 2026)"
CANTON = "Source: China Daily, Apr 2026 (139th Canton Fair, phase 1)"
CSC = "CSC program pages (SUFE, 2026); check the official site for this cycle"
PROPHET = "Source: Prophet, \"Chinese Brands Going Global\", May 2026"
DANYANG = "Source: China Daily, Jan 2022"
GDP = "Source: Xinhua via Henan Gov't, Feb 2026 (2025 GDP)"
ALIPAY = "Source: WanderInChina Alipay guide, 2026. Fees and rules can change, check in-app"

TAGS = "#china #explore #chinatravel #Guangzhou"
SIGN = "Building Bridges | Creating Access"


def caption(hook, body, extra_tags=""):
    return f"{hook}\n\n{body}\n\nFollow @wealthbridgenetwork for more China tips.\n\n{SIGN}\n\n{TAGS}{(' ' + extra_tags) if extra_tags else ''}"


def cta(line="Want more China tips like this?"):
    return dict(hook=line, hs=96,
                kick="*Follow @wealthbridgenetwork* for more tips every week. Save this post and send it to a friend.",
                scene=ground(60, 840, 560) + figure(230, 560, 1.15, "point", "grin") + follow_phone(600, 560, 1.15), vh=580)


POSTS = [
# ================================================================ 1 · SOURCING
dict(id="31-how-to-source", pillar="Sourcing", title="Stop buying from China like this",
 caption=caption("Most people lose money on their first China order. Here's why.",
                 "3 steps to source from China without getting burned: where to look, why samples matter, and when to pay. Save this before you place your next order.",
                 "#sourcing #alibaba #yiwu #ecommerce"),
 slides=[
 dict(hook="Stop buying\nfrom China\n*like this.*", swipe=True,
      scene=ground(60, 840, 470) + figure(250, 470, 1.0, "shrug", "sad", confused=True) + box(480, 470, 0.9, q=True) + box(640, 470, 0.75, q=True) + check(560, 230, 1.3, False), vh=490),
 dict(text=["Most people message three suppliers and pay the first one that replies.", "Six weeks later: *wrong color, wrong size, no refund.*"],
      scene=ground(60, 840, 460) + laptop(250, 460, 0.95, "PAY NOW") + arrow(410, 330, 520, 330, -60) + box(640, 460, 0.95, q=True), vh=480),
 dict(head="Step 1: Know where to look.", items=["**Alibaba.com**: built for overseas buyers", "**1688.com**: China's domestic site, often cheaper", "**Canton Fair**: Guangzhou, every spring & autumn", "**Yiwu**: nearly *80,000* market booths"], **{"is": 44},
      scene=laptop(115, 280, 0.66, "Alibaba") + laptop(345, 280, 0.66, "1688") + stall(585, 280, 0.6) + pin(800, 280, 1.0), vh=290, src=YIWU),
 dict(head="Step 2: Sample. Step 3: Inspect.", items=["Order samples from *3* suppliers, compare side by side", "Pay a deposit, not the full amount", "Have a third-party inspector check goods before you pay the balance", "Get price, MOQ, lead time and shipping terms *in writing*"], **{"is": 42},
      scene=ground(60, 840, 300) + box(150, 300, 0.75) + check(150, 95, 1.0, False) + box(340, 300, 0.75) + check(340, 95, 1.0, True) + magnifier(560, 300, 0.85) + ship(780, 300, 0.42), vh=310),
 cta(),
]),
# ================================================================ 2 · MAKE MONEY
dict(id="32-make-money", pillar="Make money", title="7 ways to make money in China",
 caption=caption("7 ways foreigners are making money in China right now.",
                 "Teaching, brand deals, sourcing, reselling, trade-fair content, free study and jobs with Chinese brands going global. Which one are you trying first?",
                 "#makemoneyonline #ugccreator #teachabroad #sidehustle"),
 slides=[
 dict(hook="7 ways to\nmake money\nin *China.*", swipe=True, kick="Most people only know one.",
      scene=ground(60, 840, 420) + figure(270, 420, 0.95, "up", "grin") + moneybag(520, 420, 1.0) + coins(700, 420, 0.8, 5), vh=440),
 dict(head="1. Teach English  ·  2. Brand deals", text=["Public schools pay about *$1,800-$3,000* a month. Top international schools pay *$5,250+.*",
                                                       "Chinese brands pay creators and athletes to make content: hotels, cafés, sportswear."], fs=46,
      scene=ground(60, 840, 380) + board(210, 380, 0.75, "ABC") + figure(420, 380, 0.75, "point", "happy", tie=True, flip=True) + figure(610, 380, 0.75, "hold", "grin") + camera(730, 260, 0.55), vh=400, src=TEACH),
 dict(head="3, 4 and 5:", items=["**Sourcing agent**: find and check factories for businesses back home", "**Import & resell**: buy from the factory, sell online at home", "**Trade-fair content**: film supplier tours at the Canton Fair (*167K* overseas buyers in one phase)"], **{"is": 42},
      scene=ground(40, 860, 300) + factory(150, 300, 0.55) + arrow(260, 210, 330, 210, -50) + ship(460, 300, 0.36) + arrow(560, 210, 630, 210, -50) + laptop(760, 300, 0.55, "$$$"), vh=320, src=CANTON),
 dict(head="6 and 7:", items=["**Study for free**: CSC scholarships cover tuition, a dorm and a monthly stipend", "**Work for a Chinese brand going global**: they need English speakers for marketing and sales"], **{"is": 44},
      text=[], scene=ground(60, 840, 420) + board(230, 420, 0.8, "CSC") + figure(430, 420, 0.8, "wave", "happy") + tower(700, 420, 0.62), vh=440, src="Source: " + CSC),
 cta(),
]),
# ================================================================ 3 · STRUGGLES
dict(id="33-company-struggles", pillar="Brand deals", title="What Chinese companies can't do",
 caption=caption("Chinese companies can make almost anything. Except this.",
                 "The 4 things Chinese brands struggle with when they go global, and why every one of them is an opportunity for creators and athletes.",
                 "#branding #ugccreator #athletes #marketing"),
 slides=[
 dict(hook="China can\nmake anything.\n*Except this.*", swipe=True,
      scene=ground(60, 840, 450) + factory(300, 450, 0.95) + figure(630, 450, 1.0, "shrug", "flat", confused=True), vh=470),
 dict(head="1. Nobody knows the brand.  2. Price wars.", text=["Sell through big marketplaces and shoppers remember *the store*, not the brand.", "Lead with specs and price and you're *one of a thousand* listings."], fs=46,
      scene=ground(40, 860, 330) + laptop(170, 330, 0.7, "STORE") + "".join(tag(400 + i*120, 330, 0.68, "$9") for i in range(4)), vh=350, src=PROPHET),
 dict(head="3. The culture.  4. Real voices.", text=["Translating words is easy. Knowing what makes people *trust and buy* is not.", "Ads don't build trust. *People do.* They need creators and athletes people believe."], fs=46,
      scene=ground(60, 840, 400) + figure(170, 400, 0.8, "phone", "happy") + bubble(360, 120, 0.9, "Buy now!!!", 300, "left") + figure(560, 400, 0.8, "hold", "grin") + camera(680, 280, 0.5) + ball(800, 400, 0.5), vh=420),
 dict(text=["Their problem is *your opportunity.*", "Every struggle is a job for someone who understands both sides. *Creators & athletes:* DM us."], fs=56,
      scene=ground(40, 860, 440) + figure(150, 440, 0.85, "wave", "happy") + arrow(300, 300, 600, 300, -90, G) + arrow(600, 340, 300, 340, 90) + figure(750, 440, 0.85, "wave", "happy", flip=True), vh=460),
 cta(),
]),
# ================================================================ 4 · CITIES
dict(id="34-china-cities", pillar="Best cities", title="Every city in China has a job",
 caption=caption("Picking a city in China? Don't guess.",
                 "Shanghai, Shenzhen, Guangzhou, Hangzhou, Yiwu and Chengdu each have a different job. Here's who each city is for.",
                 "#shanghai #shenzhen #chengdu #hangzhou"),
 slides=[
 dict(hook="Pick the\n*right city*\nin China.", swipe=True, kick="Every city has a different job.",
      scene=ground(60, 840, 400) + pin(140, 270, 0.75) + pin(320, 190, 0.75, G) + pin(500, 290, 0.75) + pin(680, 210, 0.75)
      + _p("M140,290 Q230,380 320,210 Q410,380 500,310 Q590,230 680,230", 7) + figure(830, 400, 0.6, "think", "happy", flip=True), vh=420),
 dict(head="Shanghai & Shenzhen", items=["**Shanghai**: finance, head offices, global brands. *Best for business.*", "**Shenzhen**: hardware and electronics, next to Hong Kong. *Best for tech.*"], **{"is": 46},
      scene=ground(60, 840, 420) + skyline(250, 420, 0.95) + chip(680, 400, 0.9), vh=440),
 dict(head="Guangzhou & Hangzhou", items=["**Guangzhou**: home of the Canton Fair. *Best for sourcing & wholesale.*", "**Hangzhou**: Alibaba's hometown, a *2.3 trillion yuan* economy. *Best for e-commerce.*"], **{"is": 46},
      scene=ground(60, 840, 400) + stall(260, 400, 0.85) + phone(600, 400, 0.85, "LIVE") + moneybag(760, 400, 0.6), vh=420, src=GDP),
 dict(head="Yiwu & Chengdu", items=["**Yiwu**: nearly *80,000* booths of small goods. *Best for bulk sourcing.*", "**Chengdu**: food, pandas, lower living costs than Shanghai. *Best for creators & teachers.*"], **{"is": 46},
      scene=ground(60, 840, 400) + stall(230, 400, 0.8) + noodles(520, 400, 0.75) + panda(740, 400, 0.85), vh=420, src=YIWU),
 cta(),
]),
# ================================================================ 5 · PRODUCTS
dict(id="35-product-hometowns", pillar="Sourcing", title="Every product has a hometown",
 caption=caption("Nearly half the world's eyeglass lenses come from ONE town in China.",
                 "In China, whole towns specialize in a single product. Know the town and you know where the best factories are.",
                 "#sourcing #madeinchina #ecommerce #smallbusiness"),
 slides=[
 dict(hook="One town\nmakes *45%*\nof the world's\nlenses.", hs=118, swipe=True,
      scene=ground(60, 840, 360) + glasses(330, 300, 0.95) + figure(680, 360, 0.75, "point", "wow", flip=True), vh=380, src=DANYANG + " (Danyang, Jiangsu)"),
 dict(text=["China doesn't make things everywhere.", "Whole towns specialize in *one product.* Find the town, and you find the best factories."], fs=54,
      scene=ground(60, 840, 470) + pin(200, 470, 0.9) + glasses(200, 245, 0.55) + pin(450, 470, 0.9, G) + sofa(450, 255, 0.5) + pin(700, 470, 0.9) + kite(700, 265, 0.48), vh=490),
 dict(head="Product hometowns:", items=["**Danyang**: glasses", "**Shenzhen**: electronics", "**Foshan**: furniture", "**Weifang**: kites (about *75%* of the world market)", "**Dingzhou**: fitness gear"], **{"is": 46},
      scene=glasses(120, 250, 0.5) + chip(300, 250, 0.6) + sofa(490, 250, 0.6) + kite(660, 250, 0.62) + dumbbell(820, 250, 0.6), vh=260, src=DANYANG + " (Danyang, Weifang, Dingzhou)"),
 dict(text=["*Go to the town, not just the website.*", "When dozens of factories sit on the same street, they compete on price and quality for you."], fs=54,
      scene=ground(40, 860, 440) + factory(150, 440, 0.6) + factory(380, 440, 0.6) + factory(610, 440, 0.6) + figure(810, 440, 0.85, "point", "grin", flip=True), vh=460),
 cta(),
]),
# ================================================================ 6 · TRAVEL / PAYMENTS
dict(id="36-first-trip-apps", pillar="Travel", title="Don't land in China without this",
 caption=caption("Cash is basically gone in China. Here's how visitors pay.",
                 "Set up Alipay with your own Visa or Mastercard before you fly, know the 200 RMB fee rule, and keep a backup. Save this for your trip.",
                 "#chinatravel #alipay #traveltips #visitchina"),
 slides=[
 dict(hook="Don't land\nin China\n*without this.*", swipe=True,
      scene=ground(60, 840, 440) + plane(270, 330, 0.85) + figure(620, 440, 0.95, "phone", "wow"), vh=460),
 dict(text=["In China, almost everyone pays by *scanning a QR code* with their phone.", "Street food, taxis, the metro. Cash still works, but locals rarely use it."], fs=52,
      scene=ground(60, 840, 430) + stall(250, 430, 0.8) + figure(560, 430, 0.9, "phone", "happy") + figure(760, 430, 0.9, "shrug", "flat", flip=True, confused=True), vh=450),
 dict(head="Set up Alipay before you fly:", items=["Download Alipay (the international version works)", "Verify with your passport and a face scan", "Link your *Visa or Mastercard*", "Scan to pay: shops, taxis, metro, food"], **{"is": 44},
      scene=ground(60, 840, 300) + phone(200, 300, 0.75, "Alipay") + arrow(310, 180, 400, 180, -50) + figure(520, 300, 0.75, "hold", "grin") + coins(740, 300, 0.7), vh=320, src=ALIPAY),
 dict(head="The 200 RMB rule:", items=["Under *200 RMB* (about $30): no 3% fee", "Over 200 RMB: a *3% fee* per payment", "Add WeChat Pay as a backup", "Keep a little cash for emergencies"], **{"is": 46},
      scene=ground(60, 840, 300) + tag(230, 300, 1.0, "200") + check(380, 160, 1.0, True) + coins(600, 300, 0.85) + figure(790, 300, 0.7, "point", "happy", flip=True), vh=320, src=ALIPAY),
 cta(),
]),
# ================================================================ 7 · BRAND DEALS
dict(id="37-brand-deals", pillar="Brand deals", title="Chinese brands want foreign creators",
 caption=caption("Chinese brands are looking for foreign creators and athletes.",
                 "How a China brand deal works, what brands look for, and how to get deal-ready. Creators & athletes: DM us your media kit.",
                 "#ugccreator #branddeals #athletes #contentcreator"),
 slides=[
 dict(hook="Chinese brands\nwant *your*\ncontent.", swipe=True, kick="Creators & athletes, this one's for you.",
      scene=ground(60, 840, 400) + figure(220, 400, 0.85, "hold", "grin") + camera(360, 270, 0.6) + figure(560, 400, 0.85, "up", "happy") + ball(720, 400, 0.6), vh=420),
 dict(head="How a deal works:", items=["**You**: creator or athlete with a real audience", "**Wealth Bridge**: matches you and manages the deal", "**The brand**: hotel, café, fashion, sportswear", "**You film, post and get paid**"], **{"is": 44},
      scene=ground(40, 860, 300) + figure(110, 300, 0.6, "wave", "happy") + arrow(190, 190, 280, 190, -50) + phone(410, 300, 0.6, "WBN") + arrow(540, 190, 620, 190, -50) + tower(730, 300, 0.42), vh=320),
 dict(head="What brands look for:", items=["A clear niche: travel, food, fitness, fashion", "Engaged followers, not just big numbers", "Clean, well-lit vertical video with captions", "A one-page *media kit* with rates and past work"], **{"is": 44},
      scene=ground(60, 840, 300) + phone(170, 300, 0.75, "REC") + figure(400, 300, 0.75, "point", "happy") + board(680, 300, 0.62, "KIT"), vh=320),
 dict(text=["You don't need millions of followers.", "UGC creators get paid *per video*, not per follower. Start with 3 sample videos and a media kit."], fs=52,
      scene=ground(60, 840, 430) + phone(200, 430, 0.8, "1") + phone(380, 430, 0.8, "2") + phone(560, 430, 0.8, "3") + figure(760, 430, 0.9, "up", "grin", flip=True), vh=450),
 cta("Want a brand deal in China?"),
]),
]
