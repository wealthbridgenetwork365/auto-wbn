# "China stories" series (Nov 18-24, 2026): 7 storytelling carousels x 5 slides, doodle style.
# Recurring illustrative character "Sam" (a stick figure, not a real person).
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from doodle import *  # noqa
from doodle import _p, _t

G = "#139A52"
TAGS = "#china #explore #chinatravel #Guangzhou"
SIGN = "Building Bridges | Creating Access"

VF30 = "Source: Beijing Municipal Gov't, Nov 2025. Rules change; check your embassy before booking"
TWT = "Source: Shanghai Int'l Services Portal, Aug 2026. Rules change; check your embassy before booking"
ALI11 = "Source: AFP via Phys.org, Feb 2011"
YICAI = "Source: Yicai, May 2025 city ranking"
NECIPS = "Source: gsxt.gov.cn (National Enterprise Credit Information Publicity System)"
CNY = "Sources: China Survival Kit, Nov 2026; DHL post-CNY guide, 2026"
STUDY = "Source: Beijing Municipal Gov't, residence permit rules (Exit-Entry Regulations, Art. 22)"


def caption(hook, body, extra_tags=""):
    return f"{hook}\n\n{body}\n\nFollow @wealthbridgenetwork for more China tips.\n\n{SIGN}\n\n{TAGS}{(' ' + extra_tags) if extra_tags else ''}"


def cta(line="Want more China tips like this?"):
    return dict(hook=line, hs=96,
                kick="*Follow @wealthbridgenetwork* for more tips every week. Save this post and send it to a friend.",
                scene=ground(60, 840, 560) + figure(230, 560, 1.15, "point", "grin") + follow_phone(600, 560, 1.15), vh=580)


POSTS = [
# ================================================================ 1 · SUPPLIER STRUGGLES
dict(id="38-supplier-struggles", pillar="Sourcing", title="Why your China supplier keeps failing you",
 caption=caption("Why do so many people get burned by Chinese suppliers?",
                 "It's usually not the factory. It's middlemen, vague specs, paying 100% upfront and 'quality fade'. Here's what goes wrong and how to fix it. Save this before your next order.",
                 "#sourcing #madeinchina #ecommerce #smallbusiness"),
 slides=[
 dict(hook="Why your\nChina supplier\n*keeps failing*\n*you.*", hs=112, swipe=True, kick="It's usually not the factory.",
      scene=ground(60, 840, 400) + factory(250, 400, 0.8) + box(520, 400, 0.8, q=True) + figure(720, 400, 0.9, "shrug", "sad", flip=True, confused=True), vh=420),
 dict(text=["Meet Sam. He found a supplier online. Great price, fast replies. *He paid 100% upfront.*",
            "Six weeks later the order arrived late, and *half of it was wrong.*"], fs=50,
      scene=ground(60, 840, 400) + laptop(190, 400, 0.85, "PAY 100%") + arrow(330, 260, 440, 260, -60) + ship(570, 400, 0.45) + box(780, 400, 0.75, q=True), vh=420),
 dict(head="What went wrong:", items=["**A middleman**: he thought it was the factory, it was a trader",
                                      "**Vague specs**: \"good quality\" means nothing in a contract",
                                      "**No leverage**: all his money was already gone",
                                      "**Quality fade**: order 1 is perfect, order 3 quietly isn't"], **{"is": 42},
      scene=ground(60, 840, 300) + figure(160, 300, 0.7, "think", "flat") + bubble(420, 120, 0.85, "\"Good quality\"", 360, "left") + check(420, 240, 1.0, False) + box(720, 300, 0.7, q=True), vh=320),
 dict(head="Sam's next order:", items=["Confirm *who* you're really talking to",
                                       "Write every spec down: size, colour, material, packaging",
                                       "Pay a deposit, *balance after inspection*",
                                       "Inspect *every* order, not just the first"], **{"is": 44},
      scene=ground(60, 840, 300) + board(170, 300, 0.6, "SPEC") + check(170, 70, 0.9, True) + magnifier(420, 300, 0.75) + box(620, 300, 0.7) + figure(800, 300, 0.7, "up", "grin", flip=True), vh=320),
 cta(),
]),
# ================================================================ 2 · VISAS
dict(id="39-visas", pillar="Travel", title="Do you even need a visa for China?",
 caption=caption("Do you even need a visa for China? Maybe not.",
                 "There are 3 ways in: 30-day visa-free entry, 240-hour visa-free transit, or the right visa (L, M, X or Z). Rules change, so always check your embassy before booking. Save this for your trip.",
                 "#chinavisa #visafree #traveltips #visitchina"),
 slides=[
 dict(hook="Do you even\n*need a visa*\nfor China?", swipe=True, kick="Most people check the wrong thing.",
      scene=ground(60, 840, 420) + door(200, 420, 0.75) + door(450, 420, 0.75, open_=True) + door(700, 420, 0.75, lock=True)
      + _t(200, 70, "1", 60, 800) + _t(450, 70, "2", 60, 800, G) + _t(700, 70, "3", 60, 800), vh=440),
 dict(head="Door 1: 30 days, no visa.", text=["Passport holders from *40+ countries*, including most of Europe, can enter China for up to *30 days* visa-free.",
                                               "For tourism, business, family visits and transit. Runs through *Dec 31, 2026.*"], fs=46,
      scene=ground(60, 840, 330) + figure(200, 330, 0.8, "wave", "grin") + plane(560, 230, 0.8), vh=350, src=VF30),
 dict(head="Door 2: 240-hour transit.", items=["**57 nationalities**, including the US and UK",
                                               "Fly in, then fly out to a *third* country",
                                               "Stay up to *10 days* in 24 provinces",
                                               "You need a confirmed onward ticket"], **{"is": 44},
      scene=ground(60, 840, 300) + pin(170, 300, 0.7) + _p("M170,140 Q430,0 680,140", 7) + pin(680, 300, 0.7, G) + plane(430, 120, 0.45) + clock(840, 300, 0.5), vh=320, src=TWT),
 dict(head="Door 3: get the right visa.", items=["**L visa**: tourism", "**M visa**: business & trade", "**X visa**: study", "**Z visa**: work"],
      text=["Visa-free entry does *not* let you work or study."], **{"is": 46}, fs=42,
      scene=ground(60, 840, 260) + board(200, 260, 0.55, "L  M") + board(470, 260, 0.55, "X  Z") + figure(720, 260, 0.62, "point", "happy", flip=True), vh=280,
      src="Rules change; check your embassy before booking"),
 cta(),
]),
# ================================================================ 3 · ALIBABA
dict(id="40-not-just-alibaba", pillar="Sourcing", title="Stop sourcing only on Alibaba",
 caption=caption("Stop sourcing only on Alibaba. Here's why.",
                 "Many 'factories' are trading companies, badges show who paid, and everyone sees the same top listings. Use it as a starting point, then cross-check, verify and meet suppliers in person.",
                 "#alibaba #1688 #sourcing #importexport"),
 slides=[
 dict(hook="Stop sourcing\n*only* on\nAlibaba.", swipe=True, kick="Here's what nobody tells you.",
      scene=ground(60, 840, 420) + laptop(280, 420, 1.0, "Alibaba") + check(280, 150, 1.4, False) + figure(640, 420, 0.95, "point", "wow", flip=True), vh=440),
 dict(text=["In 2011, Alibaba found *2,326* of its paid \"Gold Suppliers\" had defrauded buyers.",
            "Its CEO and COO resigned over it. The lesson still holds: *a badge is not a guarantee.*"], fs=50,
      scene=ground(60, 840, 360) + tag(250, 360, 1.1, "GOLD") + check(250, 120, 1.0, False) + figure(560, 360, 0.85, "shrug", "sad", confused=True) + moneybag(760, 360, 0.6), vh=380, src=ALI11),
 dict(head="The problem today:", items=["Many \"factories\" are *trading companies* adding a markup",
                                        "Paid badges show who *paid*, not who's best",
                                        "Prices are often higher than on *1688*, China's domestic site",
                                        "Every buyer sees the same top listings"], **{"is": 42},
      scene=ground(60, 840, 300) + figure(150, 300, 0.7, "hold", "grin", tie=True) + box(330, 300, 0.6) + arrow(410, 190, 520, 190, -50) + tag(620, 300, 0.75, "+$") + factory(800, 300, 0.4), vh=320),
 dict(head="Use it as a starting point:", items=["Cross-check prices on **1688**",
                                                 "Verify the business licence on **gsxt.gov.cn**",
                                                 "Meet suppliers at the **Canton Fair**",
                                                 "Visit the factory, or send an inspector"], **{"is": 44},
      scene=ground(60, 840, 300) + laptop(170, 300, 0.6, "1688") + magnifier(400, 300, 0.7) + stall(610, 300, 0.55) + figure(800, 300, 0.7, "up", "grin", flip=True), vh=320),
 cta(),
]),
# ================================================================ 4 · TIERS
dict(id="41-tier1-vs-tier2", pillar="Best cities", title="Tier 1 or new Tier 1 China?",
 caption=caption("Tier 1 or 'new Tier 1' China? Most people pick the wrong one.",
                 "China has 4 first-tier cities and 15 'new first-tier' cities (what most people call Tier 2). Here's who each one is for: career, cost, or standing out.",
                 "#shanghai #chengdu #hangzhou #movetochina"),
 slides=[
 dict(hook="Tier 1 or\n*Tier 2*\nChina?", swipe=True, kick="Most people pick the wrong one.",
      scene=ground(60, 840, 420) + skyline(260, 420, 0.95) + signpost(560, 420, 0.95, ("TIER 1", "TIER 2")) + figure(780, 420, 0.8, "think", "flat", flip=True, confused=True), vh=440),
 dict(text=["China ranks its cities in tiers.", "*4* first-tier cities. *15* \"new first-tier\" cities. Then hundreds more.",
            "Sam almost moved to the wrong one."], fs=50,
      scene=ground(60, 840, 340) + pin(170, 340, 0.75, G) + pin(330, 340, 0.75, G) + pin(490, 340, 0.6) + pin(610, 340, 0.6) + pin(730, 340, 0.6) + pin(830, 340, 0.6), vh=360, src=YICAI),
 dict(head="Tier 1: the big four", items=["**Shanghai**: finance & global brands", "**Beijing**: government, tech, universities",
                                          "**Shenzhen**: hardware & startups", "**Guangzhou**: trade & the Canton Fair"], **{"is": 46},
      text=["Most jobs and international schools. *Highest rent.*"], fs=42,
      scene=ground(60, 840, 260) + skyline(300, 260, 0.7) + chip(640, 250, 0.6) + stall(800, 260, 0.45), vh=280, src=YICAI),
 dict(head="Tier 2: the rising cities", text=["Officially \"new first-tier\": *Chengdu, Hangzhou, Chongqing, Wuhan, Suzhou* and 10 more.",
                                                  "Usually cheaper to live in, growing fast, and fewer foreigners: *more room to stand out.*"], fs=46,
      scene=ground(60, 840, 330) + panda(190, 330, 0.75) + phone(420, 330, 0.7, "LIVE") + noodles(620, 330, 0.65) + figure(800, 330, 0.75, "up", "grin", flip=True), vh=350, src=YICAI),
 cta(),
]),
# ================================================================ 5 · HOW TO SOURCE
dict(id="42-how-to-source", pillar="Sourcing", title="How to source from China the right way",
 caption=caption("Sam's second China order went perfectly. Here's what he did differently.",
                 "5 steps: shortlist 3 suppliers, verify the business licence, approve a sample, pay smart, inspect before shipping. Save this for your next order.",
                 "#sourcing #madeinchina #ecommerce #amazonfba"),
 slides=[
 dict(hook="How to source\nfrom China\n*the right way.*", hs=116, swipe=True, kick="Sam's second order went perfectly.",
      scene=ground(60, 840, 400) + factory(170, 400, 0.65) + arrow(290, 280, 400, 280, -60) + ship(500, 400, 0.38) + figure(700, 400, 0.8, "up", "grin", flip=True), vh=520),
 dict(head="1. Shortlist 3 suppliers, not 1.", text=["Find them on 1688, Alibaba and at trade fairs.",
                                                     "Send all three the *same spec sheet*, so you compare like for like."], fs=50,
      scene=ground(60, 840, 360) + factory(170, 360, 0.5) + factory(380, 360, 0.5) + factory(590, 360, 0.5) + board(790, 360, 0.5, "SPEC"), vh=380),
 dict(head="2. Verify.  3. Sample.", items=["Ask for the business licence", "Search its 18-character code on *gsxt.gov.cn*",
                                            "Check it's active and the scope says *manufacturing*", "Approve a sample and keep it as your reference"], **{"is": 42},
      scene=ground(60, 840, 280) + laptop(200, 280, 0.6, "gsxt") + check(200, 60, 0.8, True) + box(470, 280, 0.6) + magnifier(650, 280, 0.6) + figure(810, 280, 0.62, "point", "happy", flip=True), vh=300, src=NECIPS),
 dict(head="4. Pay smart.  5. Inspect.", items=["Deposit up front, *balance after inspection*", "Put price, specs and deadlines in a signed contract",
                                                "Third-party inspection *before* it ships", "Plan around Chinese New Year"], **{"is": 44},
      scene=ground(60, 840, 300) + coins(170, 300, 0.75, 3) + arrow(260, 180, 350, 180, -50) + magnifier(460, 300, 0.7) + arrow(560, 180, 640, 180, -50) + ship(760, 300, 0.36), vh=320),
 cta(),
]),
# ================================================================ 6 · CNY SHUTDOWN
dict(id="43-cny-shutdown", pillar="Sourcing", title="China is about to shut down",
 caption=caption("If you buy from China, read this now.",
                 "Chinese New Year 2027 is Feb 6. The official holiday is 9 days, but factories slow down for 6-8 weeks. Here's why, and what to do before January.",
                 "#chinesenewyear #sourcing #supplychain #ecommerce"),
 slides=[
 dict(hook="China is\nabout to\n*shut down.*", swipe=True, kick="If you buy from China, read this now.",
      scene=ground(60, 840, 420) + factory(260, 420, 0.95) + door(560, 420, 0.7, lock=True) + figure(770, 420, 0.85, "shrug", "wow", flip=True), vh=440),
 dict(text=["Chinese New Year 2027 is *Feb 6.* The official holiday: *Feb 5-13.*",
            "But factories slow down for *6-8 weeks*, from mid-January to mid-March."], fs=52,
      scene=ground(60, 840, 360) + clock(200, 360, 0.8) + arrow(320, 220, 470, 220, -60) + factory(620, 360, 0.6) + _t(620, 60, "zzz", 50, 800, G), vh=380, src=CNY),
 dict(head="Why it takes so long:", items=["Over *300 million* migrant workers travel home",
                                           "Some don't come back, so factories rehire and retrain",
                                           "Many run at about *half capacity* into early March",
                                           "Trains, flights and freight are packed"], **{"is": 42},
      scene=ground(60, 840, 300) + crowd(250, 300, 0.85, 5) + arrow(450, 180, 560, 180, -50) + plane(710, 200, 0.5), vh=320, src=CNY),
 dict(head="What to do now:", items=["Place orders *now*, not in January", "Get the factory's last ship date in writing",
                                     "Stock up to cover February and March", "Avoid China travel *Feb 5-13*: trains sell out"], **{"is": 44},
      scene=ground(60, 840, 300) + figure(160, 300, 0.7, "phone", "happy") + box(360, 300, 0.6) + box(480, 300, 0.6) + box(420, 210, 0.6) + check(640, 120, 1.0, True) + ship(780, 300, 0.33), vh=320),
 cta(),
]),
# ================================================================ 7 · STUDENTS
dict(id="44-student-money", pillar="Scholarships", title="Can you make money as a student in China?",
 caption=caption("Can you make money as a student in China? A follower asked, so here's the honest answer.",
                 "Yes, but only the legal way: school approval plus a work-study or internship endorsement on your residence permit. Plus scholarships and on-campus roles. Always check with your school's international office.",
                 "#studyinchina #cscscholarship #internationalstudents #studyabroad"),
 slides=[
 dict(hook="Can you\n*make money*\nas a student\nin China?", hs=116, swipe=True, kick="A follower asked. Here's the honest answer.",
      scene=ground(60, 840, 380) + figure(240, 380, 0.85, "think", "flat", confused=True) + board(560, 380, 0.75, "?") + coins(780, 380, 0.65, 4), vh=400),
 dict(text=["Yes. But *not any job you want.*", "A student residence permit doesn't cover off-campus work on its own. Get it wrong and *you can lose your visa.*"], fs=52,
      scene=ground(60, 840, 360) + figure(220, 360, 0.85, "shrug", "wow") + door(560, 360, 0.7, lock=True) + check(760, 160, 1.0, False), vh=380),
 dict(head="The legal way:", items=["Get your *school's approval* first", "Get the work-study or internship *recorded on your residence permit*",
                                    "Work only for that employer, place and role", "No endorsement? *Don't take the job.*"], **{"is": 42},
      scene=ground(60, 840, 280) + board(200, 280, 0.55, "OK") + arrow(310, 170, 410, 170, -50) + phone(510, 280, 0.6, "PERMIT") + check(690, 80, 0.9, True) + figure(820, 280, 0.6, "up", "grin", flip=True), vh=300, src=STUDY),
 dict(head="Other ways to fund your studies:", items=["**CSC scholarship**: tuition, a dorm and a monthly stipend",
                                                      "**On-campus roles** like teaching or research assistant, with approval",
                                                      "**After you graduate**: get a work (Z) visa and work full time"], **{"is": 44},
      scene=ground(60, 840, 320) + board(220, 320, 0.7, "CSC") + figure(440, 320, 0.75, "wave", "happy") + tower(700, 320, 0.5), vh=340,
      src="Check your school's international student office before taking any work"),
 cta(),
]),
]
