# Membership carousel: bold cards, each tier in its own colour theme.
# Render: python3 scripts/render_cards.py content/membership.py $PWD/posts/
# Perks from admin.wbn.world/membership (Nov 27, 2026) plus user notes. No prices on slides (user: send people to link in bio).
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from china_stories import caption

LINK = "Join at the *link in bio.*"

POSTS = [
dict(id="m1-memberships", pillar="Membership", title="Join our network",
 caption=caption("Join the Wealth Bridge Network: Free, Silver, Gold and Green.",
                 "Free: create an account, browse and get the newsletter. Silver: apartment listings, brand deals, jobs and universities, and member-only webinars. Gold: everything in Silver plus A.I. tools, early access to ALL opportunities and vetted manufacturers. Green (coming soon): list your company. Go to the link in bio to join.",
                 "#ugccreator #branddeals #creatoreconomy #membership"),
 slides=[
 dict(type="cover", title=["Join", "our", "*network.*"], size=184,
      sub="Four memberships. One bridge to China.",
      pills=[("FREE", "free"), ("SILVER", "silver"), ("GOLD", "gold"), ("GREEN", "green")]),
 dict(type="tier", theme="free", name="Free", letter="F", kicker=LINK,
      items=["Create your account", "Browse the network", "Access to the newsletter", "Limited features"], **{"is": 50, "gap": 30}),
 dict(type="tier", theme="silver", name="Silver", letter="S", kicker=LINK, size=236,
      items=["Apartments + maid, chef & nanny", "Weekly newsletter & updates", "Brand deals, jobs & universities",
             "Member-only webinars", "Silver symbol on your profile"], **{"is": 42, "gap": 28}),
 dict(type="tier", theme="gold", name="Gold", letter="G", kicker=LINK,
      items=["Everything in Silver", "*A.I. tools*", "Early access to ALL opportunities", "First in line for brand deals & jobs",
             "Vetted manufacturers", "Priority support & events", "Gold symbol on your profile"], **{"is": 37, "gap": 18}),
 dict(type="tier", theme="green", name="Green", letter="G", kicker="Coming soon. For companies.", size=236,
      items=["List your company", "Free for approved companies", "Green company symbol", "Join the list at the link in bio"], **{"is": 46, "gap": 30}),
 dict(type="cta", title=["Ready", "to *join?*"], size=210,
      sub="Pick your membership and join the network today.",
      pills=[("FREE", "free"), ("SILVER", "silver"), ("GOLD", "gold"), ("GREEN", "green")], button="Link in bio"),
]),
]
