# Membership carousel (Free, Silver, Gold, Green) in the doodle storytelling format.
# Split-screen slides compare two tiers side by side. DRAFT: prices/perks marked [PRICE] are placeholders.
# Render: python3 scripts/render_doodle.py content/membership.py $PWD/posts/
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import *  # noqa
from doodle import _p, _t, INK
from china_stories import caption, cta, G

MINT = "#2FE08A"


def column(cx, name, price, perks, fill="#fff"):
    """One half of the split screen: tier pill, price, perk lines with check bullets."""
    b = f'<rect x="{cx-190}" y="10" width="380" height="96" rx="48" fill="{fill}" stroke="{INK}" stroke-width="8"/>'
    b += _t(cx, 76, name.upper(), 50, 900)
    b += _t(cx, 166, price, 42, 800, G)
    y = 236
    for p in perks:
        lines = p.split("\n")
        b += _p(f"M{cx-200},{y-16} l12,14 l26,-32", 8, color=G)
        for k, ln in enumerate(lines):
            b += _t(cx - 150, y + 44 * k, ln, 37, 600, anchor="start")
        y += 44 * len(lines) + 26
    return b


def split(left, right, vh=580):
    return (column(225, *left) + column(675, *right)
            + _p(f"M450,0 L450,{vh-20}", 7, color="#BBBBBB"))


POSTS = [
dict(id="m1-memberships", pillar="Membership", title="Which membership is right for you?",
 caption=caption("Free, Silver, Gold or Green: which Wealth Bridge membership is right for you?",
                 "Start free with weekly China opportunities, or upgrade for priority review, brand matching, contract support and 1:1 help. Tap the link in bio to pick your tier.",
                 "#ugccreator #branddeals #creatoreconomy #membership"),
 slides=[
 dict(hook="Which\n*membership*\nis right\nfor you?", hs=124, swipe=True, kick="Free, Silver, Gold or Green. Here's the difference.",
      scene=ground(40, 860, 440) + _p("M50,440 L50,380 L210,380 L210,300 L370,300 L370,220 L530,220 L530,140 L690,140 L690,440", 9)
      + _t(130, 360, "FREE", 38, 900) + _t(290, 280, "SILVER", 38, 900) + _t(450, 200, "GOLD", 38, 900) + _t(610, 120, "GREEN", 38, 900, G)
      + figure(790, 440, 0.85, "up", "grin", flip=True), vh=460),
 dict(head="Free *vs* Silver", hd=80,
      scene=split(("Free", "$0 · forever", ["Weekly China\nopportunities", "Apply as a creator\nor athlete", "Community\nupdates"], MINT),
                  ("Silver", "$[PRICE]/month", ["Everything in Free", "Priority application\nreview", "Monthly brand-deal\nlist"])), vh=580),
 dict(head="Gold *vs* Green", hd=80,
      scene=split(("Gold", "$[PRICE]/month", ["Everything\nin Silver", "Brand matching\nin your niche", "Contract and\npayment support"]),
                  ("Green", "$[PRICE]/month", ["Everything in Gold", "1:1 strategy calls\nwith our team", "China trip and\non-the-ground help"], MINT)), vh=580),
 dict(head="How to join:", items=["Tap the *link in bio*", "Choose *Free, Silver, Gold or Green*", "Our team *emails your next steps*"], **{"is": 52},
      text=["Start free. *Upgrade any time.*"], fs=46,
      scene=ground(60, 840, 360) + phone(200, 360, 0.8, "JOIN") + arrow(310, 220, 420, 220, -60) + check(540, 200, 1.1, True)
      + figure(740, 360, 0.85, "up", "grin", flip=True), vh=380),
 cta("Ready to cross the bridge?"),
]),
]
