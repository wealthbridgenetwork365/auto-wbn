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


SM = {"is": 40}   # small perk text under the big tier name

POSTS = [
dict(id="m1-memberships", pillar="Membership", title="Join our network",
 caption=caption("Join the Wealth Bridge Network: Free, Silver, Gold and Green.",
                 "Free: create an account, browse and get the newsletter. Silver ($12.99/mo): apartment listings, brand deals, jobs and universities, and member-only webinars. Gold ($34.99/mo): everything in Silver plus A.I. tools, early access to ALL opportunities and vetted manufacturers. Green (coming soon): list your company. Tap the link in bio to join.",
                 "#ugccreator #branddeals #creatoreconomy #membership"),
 slides=[
 dict(hook="Join\nour\n*network.*", hs=172, swipe=True, kick="Free, Silver, Gold and Green.",
      scene=ground(40, 860, 300) + figure(160, 300, 0.75, "wave", "grin") + bridge(450, 300, 0.75, 360) + figure(740, 300, 0.75, "up", "grin", flip=True), vh=320),
 dict(hook="*Free*\nmembership", hs=128, kick="$0",
      items=["Create your account", "Browse the network", "Access to the newsletter", "Limited features"], **SM,
      scene=icons(phone(200, 250, 0.6, "WBN"), magnifier(420, 250, 0.7), board(640, 250, 0.5, "NEWS")), vh=260, ah=260),
 dict(hook="*Silver*\nmembership", hs=128, kick="$12.99/month (normally $25)",
      items=["Apartment listings + maid, chef & nanny", "Weekly newsletter & updates", "Brand deals, jobs & universities",
             "Member-only webinars", "Silver symbol on your profile"], **SM,
      scene=icons(door(160, 250, 0.5), board(360, 250, 0.45, "NEWS"), laptop(580, 250, 0.45, "LIVE"), tag(780, 250, 0.5, "S")), vh=260, ah=230),
 dict(hook="*Gold*\nmembership", hs=128, kick="$34.99/month (normally $45)",
      items=["Everything in Silver", "*A.I. tools*", "Early access to ALL opportunities", "First in line for brand deals & jobs",
             "Vetted manufacturers", "Priority support & events", "Gold symbol on your profile"], **{"is": 36},
      scene=icons(chip(180, 225, 0.55), factory(420, 250, 0.38), trophy(640, 250, 0.55), tag(820, 250, 0.5, "G")), vh=260, ah=200),
 dict(hook="*Green*\nmembership", hs=128, kick="Coming soon · for companies",
      items=["List your company", "Free for approved companies", "Green symbol on your company"], **SM,
      scene=icons(factory(200, 250, 0.45), board(450, 250, 0.55, "SOON"), tag(700, 250, 0.6, "✓")), vh=260, ah=260),
 cta("Ready to join?"),
]),
]
