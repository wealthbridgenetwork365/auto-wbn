# Membership carousel (Free, Silver, Gold, Green) in the doodle storytelling format.
# List-slide format (big numbered list + bold icon row), one tier per slide. Prices/perks from admin.wbn.world/membership (Nov 27, 2026).
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


def icons(*parts):
    """Row of bold doodle icons under the list (Hormozi-style list slide)."""
    return ground(40, 860, 250) + "".join(parts)


TIER = dict(hd=84, fs=58, **{"is": 54}, ah=330)

POSTS = [
dict(id="m1-memberships", pillar="Membership", title="Which membership is right for you?",
 caption=caption("Free, Silver, Gold or Green: which Wealth Bridge membership is right for you?",
                 "Silver ($12.99/mo): apartment listings, weekly newsletter, access to brand deals, jobs and universities, and member-only webinars. Gold ($34.99/mo): everything in Silver plus A.I. tools, early access to ALL opportunities, first in line for brand deals and jobs, vetted manufacturers and priority support. Green: free for approved companies. Tap the link in bio to join.",
                 "#ugccreator #branddeals #creatoreconomy #membership"),
 slides=[
 dict(hook="Which\n*membership*\nis right\nfor you?", hs=124, swipe=True, kick="Free, Silver, Gold or Green. Here's the difference.",
      scene=ground(40, 860, 440) + _p("M50,440 L50,380 L210,380 L210,300 L370,300 L370,220 L530,220 L530,140 L690,140 L690,440", 9)
      + _t(130, 360, "FREE", 38, 900) + _t(290, 280, "SILVER", 38, 900) + _t(450, 200, "GOLD", 38, 900) + _t(610, 120, "GREEN", 38, 900, G)
      + figure(790, 440, 0.85, "up", "grin", flip=True), vh=460),
 dict(head="Free ($0):", text=["Every free member gets:"],
      items=["A free account", "Weekly China tips", "Upgrade any time"],
      scene=icons(phone(170, 250, 0.75, "WBN"), board(450, 250, 0.6, "TIPS"), check(720, 230, 1.1, True)), vh=260, **TIER),
 dict(head="Silver ($12.99/mo):", text=["Normally $25. Members get:"],
      items=["Apartment listings + maid, chef & nanny", "Weekly newsletter & updates", "Brand deals, jobs & universities",
             "Member-only webinars", "Silver symbol on your profile"],
      scene=icons(door(130, 250, 0.6), board(330, 250, 0.55, "NEWS"), magnifier(520, 250, 0.8), laptop(700, 250, 0.55, "LIVE"), tag(840, 250, 0.6, "S")), vh=260,
      **{**TIER, "is": 50, "fs": 54, "hd": 80}),
 dict(head="Gold ($34.99/mo):", text=["Normally $45. Members get:"],
      items=["Everything in Silver", "*A.I. tools*", "Early access to ALL opportunities", "First in line for brand deals & jobs",
             "Vetted manufacturers", "Priority support & events", "Gold symbol on your profile"],
      scene=icons(handshake_hands(130, 200, 0.55), chip(330, 225, 0.65), factory(520, 250, 0.42), trophy(690, 250, 0.65), tag(845, 250, 0.55, "G")), vh=260,
      **{**TIER, "is": 46, "fs": 54, "hd": 80}),
 dict(head="Green (companies):", text=["Free. Approved companies get:"],
      items=["Their own application track", "The green symbol", "A green badge on our marketing"],
      scene=icons(factory(180, 250, 0.5), board(450, 250, 0.6, "APPLY"), check(640, 230, 1.0, True), tag(800, 250, 0.65, "G")), vh=260,
      **TIER),
 dict(head="How to join:", hd=84,
      items=["Tap the *link in bio*", "Sign up *free*", "Upgrade to *Silver* or *Gold*", "Companies: apply for *Green*"], **{"is": 58},
      scene=icons(phone(170, 250, 0.75, "JOIN"), arrow(280, 150, 400, 150, -50), check(500, 230, 1.0, True), figure(740, 250, 0.6, "up", "grin", flip=True)), vh=260, ah=330),
 cta("Ready to cross the bridge?"),
]),
]
