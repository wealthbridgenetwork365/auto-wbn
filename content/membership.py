# Membership carousel (Free, Silver, Gold, Green) in the doodle storytelling format.
# Split-screen slides compare two tiers side by side. Prices/perks from admin.wbn.world/membership (Nov 27, 2026).
# Render: python3 scripts/render_doodle.py content/membership.py $PWD/posts/
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from doodle import *  # noqa
from doodle import _p, _t, INK
from china_stories import caption, cta, G

MINT = "#2FE08A"


def column(cx, name, price, perks, fill="#fff", old=None):
    """One half of the split screen: tier pill, price (optional struck-out old price), perk lines."""
    b = f'<rect x="{cx-190}" y="10" width="380" height="96" rx="48" fill="{fill}" stroke="{INK}" stroke-width="8"/>'
    b += _t(cx, 76, name.upper(), 50, 900)
    if old:
        b += _t(cx - 120, 166, old, 34, 700, "#9A9A9A") + _p(f"M{cx-158},154 L{cx-82},154", 5, color="#9A9A9A")
        b += _t(cx + 50, 166, price, 42, 800, G)
    else:
        b += _t(cx, 166, price, 42, 800, G)
    y = 236
    for p in perks:
        lines = p.split("\n")
        b += _p(f"M{cx-200},{y-16} l12,14 l26,-32", 8, color=G)
        for k, ln in enumerate(lines):
            b += _t(cx - 150, y + 40 * k, ln, 34, 600, anchor="start")
        y += 40 * len(lines) + 22
    return b


def split(left, right, vh=800):
    return (column(225, **left) + column(675, **right)
            + _p(f"M450,0 L450,{vh-20}", 7, color="#BBBBBB"))


POSTS = [
dict(id="m1-memberships", pillar="Membership", title="Which membership is right for you?",
 caption=caption("Free, Silver, Gold or Green: which Wealth Bridge membership is right for you?",
                 "Silver ($12.99/mo): apartment listings, weekly newsletter, selected opportunities and member-only webinars. Gold ($34.99/mo): early access to ALL opportunities, first in line for brand deals and jobs, vetted manufacturers and priority support. Green: free for approved companies. Tap the link in bio to join.",
                 "#ugccreator #branddeals #creatoreconomy #membership"),
 slides=[
 dict(hook="Which\n*membership*\nis right\nfor you?", hs=124, swipe=True, kick="Free, Silver, Gold or Green. Here's the difference.",
      scene=ground(40, 860, 440) + _p("M50,440 L50,380 L210,380 L210,300 L370,300 L370,220 L530,220 L530,140 L690,140 L690,440", 9)
      + _t(130, 360, "FREE", 38, 900) + _t(290, 280, "SILVER", 38, 900) + _t(450, 200, "GOLD", 38, 900) + _t(610, 120, "GREEN", 38, 900, G)
      + figure(790, 440, 0.85, "up", "grin", flip=True), vh=460),
 dict(head="Free *vs* Silver", hd=80,
      scene=split(dict(name="Free", price="$0", fill=MINT, perks=["Free account", "Follow weekly\nChina tips", "Upgrade\nany time"]),
                  dict(name="Silver", price="$12.99/mo", old="$25", perks=["Apartment listings\n(maid, chef & nanny)", "Weekly newsletter\n& industry updates",
                       "Access to selected\nopportunities", "Member-only\nweekly webinars", "Silver badge\non your profile"])), vh=800),
 dict(head="Gold *vs* Green", hd=80,
      scene=split(dict(name="Gold", price="$34.99/mo", old="$45", perks=["Everything in Silver", "Early access to\nALL opportunities",
                       "First in line for\nbrand deals & jobs", "Vetted\nmanufacturers", "Priority support\n& exclusive events",
                       "Gold badge\non your profile"]),
                  dict(name="Green", price="FREE", fill=MINT, perks=["For companies", "Apply under\nCompanies", "Approved companies\nget the green badge"]), vh=800), vh=800),
 dict(head="How to join:", items=["Tap the *link in bio*", "Sign up *free*", "Upgrade to *Silver* or *Gold* any time", "Companies: apply for *Green*"], **{"is": 50},
      scene=ground(60, 840, 360) + phone(200, 360, 0.8, "JOIN") + arrow(310, 220, 420, 220, -60) + check(540, 200, 1.1, True)
      + figure(740, 360, 0.85, "up", "grin", flip=True), vh=380),
 cta("Ready to cross the bridge?"),
]),
]
