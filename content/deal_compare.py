# Post 56: US brand deal vs Chinese brand deal, told through Jade (fictional, from post 55).
# Doodle storytelling style. All deal details are an illustrative example, not market data.
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import *  # noqa
from doodle import _p, _t, INK, RED, GREEN
from china_stories import chat
from marks_story import lbl, divider

SIGN = "Building Bridges | Creating Access"
TAGS = "#china #explore #chinatravel #Guangzhou"
NOTE = "Jade is a fictional example. Deal terms are illustrative; every brand is different"
PAY = "Brand payments often land 30 to 90 days after the work (Digiday, Feb 2024)"


def caption():
    return ("US brand deal vs Chinese brand deal. Which one's better?\n\n"
            "Picture Jade, a made-up creator with 10K followers. In one week she gets two offers: a US skincare brand wants one polished Reel "
            "for $500, paid 60 days later. A Chinese gadget brand wants three short UGC videos for $450, half upfront, with the product shipped from Shenzhen. "
            "Different pay, different content, different payment terms. Before you sign either, check the usage rights, the payment terms and the shipping time.\n\n"
            "Want deals with Chinese brands? Join our community today: link in bio.\n\n"
            "(Not financial advice. Jade is a fictional example and the deal terms are illustrative. Every brand is different.)\n\n"
            f"Follow @wealthbridgenetwork for more China opportunities.\n\n{SIGN}\n\n{TAGS} "
            "#branddeals #ugccreator #contentcreator #influencermarketing #creatoreconomy #sponsorship")


def row(y, label, left, right, h=96):
    b = f'<rect x="20" y="{y}" width="860" height="{h}" rx="14" fill="#fff" stroke="{INK}" stroke-width="6"/>'
    b += _t(110, y + h/2 + 11, label, 28, 800, INK)
    b += f'<path d="M200,{y} L200,{y+h} M540,{y} L540,{y+h}" stroke="{INK}" stroke-width="5"/>'
    for i, ln in enumerate(left):
        b += _t(370, y + h/2 + 11 + (i - (len(left)-1)/2) * 36, ln, 28, 600, INK)
    for i, ln in enumerate(right):
        b += _t(710, y + h/2 + 11 + (i - (len(right)-1)/2) * 36, ln, 28, 700, GREEN)
    return b


TABLE = (lbl(370, 40, "US BRAND", INK, 34) + lbl(710, 40, "CHINA BRAND", GREEN, 34)
         + row(70, "Pay", ["$500"], ["$450"])
         + row(180, "Content", ["1 polished Reel"], ["3 short UGC", "videos"])
         + row(290, "Paid", ["60 days after", "posting"], ["50% upfront,", "50% on delivery"])
         + row(400, "Rights", ["30 days of ads"], ["Wants long-term", "ad rights"])
         + row(510, "Speed", ["2–3 weeks of", "approvals"], ["Product ships", "from Shenzhen"]))


POSTS = [
dict(id="56-deal-compare", pillar="Brand deals", title="US brand deal vs Chinese brand deal: Jade's example", caption=caption(),
 slides=[
 # 1 · HOOK
 dict(hook="US brand vs\n*Chinese brand.*\nWhich deal\nis *better?*", hs=104, swipe=True, kick="A what-if: two offers in one week.",
      scene=lbl(215, 40, "US BRAND", INK) + lbl(680, 40, "CHINA BRAND", GREEN) + divider(450, 0, 450)
      + ground(40, 410, 450) + phone(140, 450, 0.65, "$500") + figure(320, 450, 0.8, "think", "flat")
      + ground(490, 880, 450) + phone(590, 450, 0.65, "$450") + figure(780, 450, 0.8, "think", "flat", flip=True), vh=470),
 # 2 · SETUP
 dict(text=["Picture Jade again. A made-up creator, *10K followers.*", "This week, *two brands* email her."], fs=54,
      scene=ground(60, 840, 420) + figure(220, 420, 0.95, "phone", "wow") + phone(500, 420, 0.75, "NEW") + phone(700, 420, 0.75, "NEW"), vh=440),
 # 3 · US OFFER
 dict(head="Offer 1: a US skincare brand.",
      scene=chat(450, 580, 1.0, [("l", "Hi! We're the agency for\na US skincare brand."), ("l", "One polished Reel, $500.\nScript approval first."), ("l", "Payment is net 60\nafter posting.")], 600, 540), vh=600),
 # 4 · CHINA OFFER
 dict(head="Offer 2: a Chinese gadget brand.",
      scene=chat(450, 580, 1.0, [("l", "Hi Jade! We make\nportable blenders."), ("l", "3 short UGC videos,\n$450 total."), ("r", "50% upfront?"), ("l", "OK! We ship from\nShenzhen today.")], 600, 560), vh=600),
 # 5 · COMPARISON TABLE
 dict(head="Side by side:", scene=TABLE, vh=620, src=NOTE),
 # 6 · WHAT TO CHECK
 dict(head="Before you sign either one:", items=["*Usage rights*: how long can they run your video as an ad?",
                                                 "*Payment terms*: ask for a deposit, or net 30 at most",
                                                 "*Shipping*: product from China can take a week or more",
                                                 "*The brief*: get it in writing, in English"], **{"is": 42},
      scene=ground(60, 840, 260) + board(190, 260, 0.5, "BRIEF") + clock(420, 190, 0.6) + ship(640, 260, 0.5) + check(640, 70, 0.6, True), vh=280, src=PAY),
 # 7 · THE DECISION
 dict(text=["So which one does Jade take?", "*Both.*", "The US deal builds her portfolio. The Chinese brand wants *more videos, more often.*",
            "*Repeat clients beat one-off deals.*"], fs=48,
      scene=ground(60, 840, 360) + phone(200, 360, 0.6, "US") + figure(450, 360, 0.85, "up", "grin") + phone(700, 360, 0.6, "CN"), vh=380),
 # 8 · CTA
 dict(hook="Want deals with\n*Chinese brands?*", hs=96,
      kick="*Join our community today.* Link in bio.",
      scene=ground(60, 840, 560) + figure(230, 560, 1.15, "point", "grin") + follow_phone(600, 560, 1.15), vh=580,
      src="Jade is a fictional example. Not financial advice"),
]),
]
