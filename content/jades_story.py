# Jade's story (post 55), doodle storytelling style. A fictional "what-if" example:
# a small creator lands a brand deal with a Chinese brand, then sources her own product.
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
NOTE = "Jade is a fictional example. Example numbers, not a promise of earnings"


def caption():
    return ("What if one brand deal turned into your own product line?\n\n"
            "Picture Jade. She's a made-up example, but her path is real: a small creator with 10K followers gets a paid deal "
            "from a Chinese brand. The brand loves the video, so she asks who makes the product. They introduce her to the factory. "
            "She orders a sample, puts her logo on it, checks quality before shipping, and sells 500 units to her own audience.\n\n"
            "Brand deals open the door. Sourcing builds the business. Join our community today: link in bio.\n\n"
            "(Not financial advice. Jade is a fictional example and the numbers are illustrative. Margin isn't profit: "
            "samples, inspections, shipping and fees all cost money.)\n\n"
            f"Follow @wealthbridgenetwork for more China opportunities.\n\n{SIGN}\n\n{TAGS} "
            "#branddeals #ugccreator #contentcreator #sourcing #productlaunch #smallbusiness")


POSTS = [
dict(id="55-jades-story", pillar="Brand deals", title="What if one brand deal became your own brand? Jade's example", caption=caption(),
 slides=[
 # 1 · HOOK
 dict(hook="One *brand deal*.\nThen her\n*own product.*", hs=104, swipe=True, kick="A what-if story. Here's how it could happen.",
      scene=lbl(215, 40, "DEAL", INK) + lbl(680, 40, "BRAND", GREEN) + divider(450, 0, 470)
      + ground(40, 410, 470) + phone(150, 470, 0.7, "REC") + figure(320, 470, 0.85, "hold", "grin")
      + ground(490, 880, 470) + box(590, 470, 0.6, "JADE") + box(700, 470, 0.6, "JADE") + box(645, 380, 0.6, "JADE") + figure(820, 470, 0.8, "up", "grin", flip=True), vh=490),
 # 2 · BACKSTORY
 dict(text=["Picture Jade. She's not real, but *her path is.*", "A small creator. *10K followers.*", "Posting every week, mostly *for free.*"], fs=54,
      scene=ground(60, 840, 400) + figure(250, 400, 0.95, "phone", "flat") + phone(520, 400, 0.8, "10K") + tag(720, 400, 0.7, "$0"), vh=420),
 # 3 · THE DM
 dict(head="Then a Chinese brand messages her.",
      scene=chat(450, 560, 1.0, [("l", "Love your videos! Can\nyou review our blender?"), ("r", "Sure. My rate is $300\nfor one video."), ("l", "Deal. We'll ship it\ntoday.")], 600, 520), vh=580),
 # 4 · HOW THE DEAL WORKS
 dict(head="How she runs the deal:", items=["Get the *brief*: what to show, key points", "Agree price, deadline and *usage rights* in writing",
                                          "Ask for *50% upfront*, the rest on delivery", "Post, then send the brand *the stats*"], **{"is": 44},
      scene=ground(60, 840, 300) + board(190, 300, 0.55, "BRIEF") + phone(420, 300, 0.6, "REC") + coins(620, 300, 0.6, 4) + check(620, 90, 0.7, True) + figure(790, 300, 0.6, "up", "grin", flip=True), vh=320),
 # 5 · THE TURN
 dict(text=["The brand loves the video. Jade asks one question:", "*\"Who makes this?\"*", "They introduce her to *the factory.*"], fs=52,
      scene=ground(60, 840, 400) + figure(210, 400, 0.85, "think", "wow") + bubble(420, 110, 0.75, "Who makes it?", 330, "left") + arrow(420, 280, 540, 280, -50) + factory(700, 400, 0.7), vh=420),
 # 6 · SOURCING
 dict(head="So she makes her own version:", items=["*Sample first*: her logo, colour and box", "Order *500 units* at $6 each",
                                                   "*QC inspection* before anything ships", "Sell to her audience at *$29*"], **{"is": 44},
      scene=ground(60, 840, 300) + factory(170, 300, 0.5) + arrow(260, 190, 340, 190, -40) + box(430, 300, 0.55, "JADE") + magnifier(560, 250, 0.55) + check(560, 90, 0.6, True) + ship(760, 300, 0.55), vh=320),
 # 7 · THE MATH (split)
 dict(head="Same creator. Different math.",
      scene=lbl(215, 40, "BRAND DEAL", INK) + lbl(680, 40, "OWN PRODUCT", GREEN) + divider(450, 0, 700)
      + phone(215, 300, 0.75, "REC")
      + lbl(215, 400, "One video", INK, 34, 600) + lbl(215, 470, "$300", INK, 64) + lbl(215, 530, "paid once", INK, 30, 600)
      + box(680, 300, 0.75, "JADE")
      + lbl(680, 400, "500 units x $29", INK, 34, 600) + lbl(680, 470, "≈ $7,000", GREEN, 64) + lbl(680, 530, "profit if all sell", INK, 30, 600)
      + lbl(680, 600, "after ~$15/unit for", INK, 26, 600) + lbl(680, 640, "product, shipping & fees", INK, 26, 600), vh=700,
      src=NOTE),
 # 8 · CLOSE
 dict(text=["*Brand deals* open the door. *Sourcing* builds the business.",
            "Not financial advice, but there are *tons of global opportunities* waiting.",
            "*Join our community today. Link in bio.*"], fs=46,
      scene=ground(60, 840, 520) + figure(220, 520, 1.05, "point", "grin") + follow_phone(600, 520, 1.05), vh=540,
      src="Jade is a fictional example. Results vary; margin isn't profit"),
]),
]
