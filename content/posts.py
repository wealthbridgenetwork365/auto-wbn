# Content for Nov 6-30, 2026. Every number below was checked against the source named on its slide.
S = dict(
    cnnic="Source: CNNIC 57th Statistical Report, data as of Dec 2025",
    cnnic_mid="Source: CNNIC, data as of June 2025",
    qm="Source: QuestMobile, mid-2025",
    nomura="Source: Nomura via TechNode, July 2026 data",
    tencent="Source: Tencent Q2 2026 results (as of June 30, 2026)",
    ks="Source: Kuaishou Q2 2026 results",
    bili="Source: Bilibili Q2 2026 results",
    xhs="Source: QuestMobile via 36Kr, March 2026",
    nbs="Source: National Bureau of Statistics, full-year 2025",
    sport="Source: General Administration of Sport & NBS, 2024 data (released Mar 2026)",
    t240="Source: Shanghai Municipal Gov't (Jul 2026); Beijing Municipal Gov't (Aug 2026). Rules change, check your embassy before booking",
    hainan="Source: Beijing Municipal Gov't, Aug 2026. Rules change, check your embassy before booking",
    nia="Source: National Immigration Administration via Xinhua, Jan-Jun 2025",
    alipay="Source: WanderInChina Alipay guide, 2026. Fees can change, check in-app",
    canton="Source: China Daily, April 2026 (139th Canton Fair)",
    teach="Source: Migaku 2026 China teaching salary guide. Ranges vary by employer",
    permit="Source: China Briefing, Feb 2026 (2025 wage basis)",
    csc="Source: CSC program pages (SUFE, 2026) & Study-Abroad.org. Check the official site for this cycle",
    schw="Source: UNH Fellowships Office (Schwarzman); UC Berkeley (Yenching). Check official sites",
    gdp="Source: Xinhua via Henan Gov't (Feb 2026); Caproasia (Jan 2026); 36Kr",
)

FX = "USD at 6.67 RMB (Oct 26, 2026)"
CTA_CREATOR = dict(type="cta", title="Want a brand deal\nin *China?*",
    sub="We're signing **UGC creators** and **athletes** for China brand partnerships.",
    points=["Follow for weekly China opportunities", "DM us your media kit to get started"])
CTA_TRAVEL = dict(type="cta", title="Going to *China?*",
    sub="Follow for travel, city and money guides that actually help.",
    points=["Save this for your trip", "DM us if you're a creator heading to China"])
CTA_CAREER = dict(type="cta", title="Build your future\nin *China.*",
    sub="Jobs, scholarships and brand deals, explained every week.",
    points=["Follow so you don't miss the next one", "DM us your questions"])

POSTS = [
# ---------------- 1 ----------------
dict(id="01-five-apps", slot="2026-11-06T11:00", pillar="Untapped market", title="China's apps by the numbers", slides=[
 dict(type="cover", label="China · Untapped market", title="Five apps.\nBillions of\n*users.*", sub="Most Western creators have never posted on any of them."),
 dict(type="bars", label="Monthly active users", title="Who's *online*", max=1439, bars=[
   ["WeChat (Weixin + WeChat)", 1439, "1.44B"], ["Kuaishou", 797.3, "797M"], ["Bilibili", 371, "371M"], ["Xiaohongshu (RED)", 245, "245M"]],
   note="Monthly active users, latest reported", src="Sources: Tencent, Kuaishou, Bilibili Q2 2026 results; QuestMobile via 36Kr (RED, Mar 2026)"),
 dict(type="stat", label="Daily, not monthly", value="714M", title="people open *Douyin* every day", sub="China's version of TikTok, and daily use is still growing.", src=S["nomura"]),
 dict(type="split", top=dict(label="Where you post now", title="Saturated.", points=["Millions of creators competing", "Hard to stand out", "Same brands, same pitches"]),
   bottom=dict(title="*China.*", points=["Huge audiences, few foreign creators", "Brands want fresh faces", "We handle the bridge for you"], best_label="Your edge:", best="being early.")),
 CTA_CREATOR]),
# ---------------- 2 ----------------
dict(id="02-240-hours", slot="2026-11-06T20:00", pillar="Travel", title="240-hour visa-free transit", slides=[
 dict(type="cover", label="China · Travel", title="10 days in China.\n*No visa.*", sub="The 240-hour visa-free transit, explained in one swipe."),
 dict(type="tiles", label="The policy in numbers", title="240 hours, *visa-free*", tiles=[["57", "countries eligible, including the US"], ["65", "entry ports"], ["24", "provinces you can travel between"], ["10", "days maximum stay"]], src=S["t240"]),
 dict(type="flow", label="How it works", title="The *one rule* to remember", steps=[
   dict(t="Fly from Country A", d="your home country"), dict(t="Enter China", d="at one of the 65 eligible ports", hi=True), dict(t="Leave to Country C", d="a third country, never back to A"), dict(t="Show your onward ticket", d="confirmed seat and date, at arrival")], src=S["t240"]),
 dict(type="list", label="Good to know", title="Before you *book*", items=["Tourism, business and visits are allowed", "**Work, study and reporting** need a proper visa", "Cross-province travel is allowed within the 24 provinces", "Stay inside the 24 eligible provinces"], note="Rules change. Check your embassy before you book.", src=S["t240"]),
 CTA_TRAVEL]),
# ---------------- 3 ----------------
dict(id="03-deal-flow", slot="2026-11-08T11:00", pillar="Brand deals", title="How a China brand deal flows", slides=[
 dict(type="cover", label="China · Brand deals", title="How a China\nbrand deal\n*actually works.*", sub="From first DM to getting paid."),
 dict(type="flow", label="The system", title="How a deal *flows*", steps=[
   dict(t="You", d="creator or athlete with a real audience"), dict(t="Wealth Bridge", d="matches you and manages the deal", hi=True), dict(t="Chinese brand", d="hotel, café, fashion, sportswear"), dict(t="Campaign", d="you visit, film and post"), dict(t="You get paid", d="plus stays, products and portfolio work")]),
 dict(type="split", join="&", top=dict(label="Who gets what", title="Brand", points=["New customers", "Fresh, authentic content", "A foreign voice in their market"]),
   bottom=dict(title="Creator", points=["A paid deal", "Free stays or products", "Content for your portfolio"], best_label="Wealth Bridge:", best="finds the match, keeps it on track.")),
 dict(type="list", label="What brands look for", title="Get *deal-ready*", items=["A clear niche (travel, food, fitness, fashion)", "Engaged followers, not just big numbers", "A media kit with rates and past work", "Clean, well-lit video with captions"]),
 CTA_CREATOR]),
# ---------------- 4 (jobs opener for week of Nov 9) ----------------
dict(id="04-jobs-5k", slot="2026-11-09T11:00", pillar="Jobs", title="Jobs in China paying up to $5,000 a month", slides=[
 dict(type="cover", label="China · Jobs", title="Jobs in China\nthat pay up to", size=104, big="$5,000", unit="/ month", sub="Which roles pay the most, what you need, and where to start."),
 dict(type="ranges", label="Monthly pay in USD · teaching", title="Who pays *the most*", max=5400, bars=[
   ["International schools", 2700, 5250, "$2,700-$5,250+"], ["Licensed kindergartens", 2400, 3750, "$2,400-$3,750"], ["Training centers", 2100, 2700, "$2,100-$2,700"], ["Public schools", 1800, 3000, "$1,800-$3,000"], ["Universities", 1800, 2700, "$1,800-$2,700"]],
   note="International schools pay **18,000-35,000+ RMB** a month. Housing and flights are often extra.", src="Source: Migaku 2026 China teaching salary guide. " + "USD at 6.67 RMB (Oct 26, 2026)"),
 dict(type="tiles", label="The top end", title="Where *$5K+* lives", tiles=[["35K+", "RMB/month at top international schools (~$5,250)"], ["45K", "RMB/month, top of the 2026 teaching range (~$6,750)"], ["49,736", "RMB/month: Shanghai's Category B pay benchmark"], ["47,748", "RMB/month: Beijing's Category B pay benchmark"]], vsize=72,
   src="Sources: Migaku 2026; China Briefing, Feb 2026. " + "USD at 6.67 RMB (Oct 26, 2026)"),
 dict(type="list", label="Work permit · Category B", title="What you *need*", items=["A **bachelor's degree** or higher", "**2+ years** of relevant work experience", "**Under 60**, with a health check from the last 6 months", "A **criminal record certificate**, verified by a Chinese embassy", "Teaching? Add a **120-hour TEFL**"], src="Sources: Shenzhen Municipal Gov't (work permit guide); Migaku 2026"),
 dict(type="list", label="International marketing for manufacturers", title="Factory jobs *beyond the factory*", tsize=80, items=["**Foreign trade sales**: find overseas buyers, send quotes", "**International marketing manager**: brand and campaigns abroad", "**Cross-border e-commerce**: run Amazon and Shopify stores", "**Digital ads specialist**: Google, Meta and TikTok ads, SEO", "**English content creator**: product videos, catalogs, copy", "**Trade show liaison**: Canton Fair booths and buyers"]),
 dict(type="split", top=dict(label="Two paths to $5K", title="Teaching", points=["Clear pay bands by school type", "Housing often included", "TEFL + degree to start"], best_label="Fastest start:", best="international schools"),
   bottom=dict(title="Manufacturing", points=["Sell and market China-made goods abroad", "Native English is your edge", "Ask about base pay vs commission"], best_label="Best hubs:", best="Guangzhou and Shenzhen"), src="Sources: Migaku 2026; China Daily (Canton Fair, Apr 2026)"),
 dict(type="cta", title="Want a job\nin *China?*", sub="Follow for job breakdowns, salaries and requirements every week.", points=["Save this for your job search", "DM us **JOBS** and tell us your field"])]),
# ---------------- 5 ----------------
dict(id="05-short-video", slot="2026-11-08T20:00", pillar="Untapped market", title="1 billion short-video users", slides=[
 dict(type="cover", label="China · Untapped market", title="Over *1 billion*\npeople watch\nshort video.", sub="That's more than three times the US population."),
 dict(type="donut", label="Share of China's internet users", title="Almost *everyone*", pct=95.1, center="95%", side="**1.068 billion** short-video users, 95.1% of everyone online in China.", src=S["cnnic_mid"]),
 dict(type="stat", label="Time online", value="7.97", title="*hours a day* on mobile internet", sub="Attention is there. The question is who captures it.", src=S["qm"]),
 dict(type="bars", label="Avg. minutes per user, per day", title="Where the *minutes* go", max=120, bars=[["Douyin", 120, "112-120"], ["Bilibili", 113, "113"], ["WeChat", 85, "82-85", "dim"]],
   src="Sources: Nomura via TechNode (Douyin, WeChat, July 2026); Bilibili Q2 2026 results"),
 CTA_CREATOR]),
# ---------------- 6 ----------------
dict(id="06-gz-vs-sz", slot="2026-11-09T20:00", pillar="Best cities", title="Guangzhou vs Shenzhen", slides=[
 dict(type="cover", label="China · Best cities", title="Guangzhou\nor *Shenzhen?*", sub="Two Guangdong neighbors. Very different reasons to go."),
 dict(type="split", top=dict(label="City · Where should you base?", title="Guangzhou", points=["Home of the Canton Fair", "Wholesale fashion, beauty, leather", "Lower cost than Shenzhen"], best_label="Best for:", best="sourcing and business"),
   bottom=dict(title="Shenzhen", points=["China's tech and hardware hub", "Strong pay at bilingual schools", "240-hour visa-free entry port"], best_label="Best for:", best="tech and teaching jobs"), src="Sources: China Daily (Canton Fair, Apr 2026); Migaku 2026; Shanghai Gov't 240-hr list"),
 dict(type="tiles", label="Guangzhou's Canton Fair, phase 1", title="The world *shows up*", tiles=[["167K", "overseas buyers in one phase"], ["216", "countries and regions"], ["12K+", "exhibitors"], ["25K+", "booths"]], vsize=86, src=S["canton"]),
 dict(type="list", label="Content ideas", title="What to *film* there", items=["Guangzhou: wholesale market hauls and factory visits", "Guangzhou: Cantonese food tours", "Shenzhen: gadget markets and tech reviews", "Shenzhen: skyline and day trips to Hong Kong"]),
 CTA_CREATOR]),
# ---------------- 7 ----------------
dict(id="07-retail", slot="2026-11-11T11:00", pillar="Untapped market", title="China's $7 trillion retail market", slides=[
 dict(type="cover", label="China · Untapped market", title="A *$7 trillion*\nshopping\nmarket.", sub="China's 2025 retail sales, and how much happens online."),
 dict(type="stat", label="Total retail sales, 2025", value="50.12T", size=210, title="yuan, about *$7.15 trillion*", sub="Up 3.7% on 2024.", src=S["nbs"]),
 dict(type="bars", label="2025, trillion yuan", title="Online is *growing faster*", max=50.12, bars=[["All retail sales", 50.12, "50.12T", "dim"], ["Online retail (all)", 15.97, "15.97T"], ["Online physical goods", 13.09, "13.09T"]],
   note="Online retail grew **8.6%**, more than twice the total.", src=S["nbs"]),
 dict(type="donut", label="Share of all retail", title="Online's *slice*", pct=26.1, center="26%", side="Physical goods sold online were **26.1%** of all retail sales in 2025. Creators drive a lot of that buying.", src=S["nbs"]),
 CTA_CREATOR]),
# ---------------- 8 ----------------
dict(id="08-alipay", slot="2026-11-11T20:00", pillar="Travel", title="Paying in China with your own card", slides=[
 dict(type="cover", label="China · Travel", title="Cash is out.\n*Your phone*\nis your wallet.", sub="How visitors pay in China with a foreign card."),
 dict(type="flow", label="Set up before you fly", title="Alipay in *4 steps*", steps=[
   dict(t="Download Alipay", d="the international version works"), dict(t="Verify your identity", d="passport scan and face scan"), dict(t="Link Visa or Mastercard", d="direct card binding", hi=True), dict(t="Scan to pay", d="shops, taxis, metro, street food")], src=S["alipay"]),
 dict(type="split", top=dict(label="The fee rule", title="Under 200 RMB", points=["No 3% fee", "About US$30 or less", "Covers most meals and rides"]),
   bottom=dict(title="Over 200 RMB", points=["3% fee added per payment", "201 RMB becomes about 207 RMB", "Ask to split bigger bills"], best_label="Tip:", best="start with small payments first."), src=S["alipay"]),
 dict(type="list", label="Avoid surprises", title="Pay like a *local*", items=["Set up Alipay before you land", "Add WeChat Pay as a backup", "Keep a little cash for emergencies", "Big first purchases can trigger a 'system busy' block"], src=S["alipay"]),
 CTA_TRAVEL]),
# ---------------- 9 ----------------
dict(id="09-csc", slot="2026-11-13T11:00", pillar="Scholarships", title="Get paid to study in China", slides=[
 dict(type="cover", label="China · Scholarships", title="Get *paid*\nto study in China.", size=100, big="3,500 RMB", bsize=150, unit="/ month (~$525)", chips=["**Tuition**: 100% covered", "**Free dorm** on campus", "**Stipend**: 2,500-3,500 RMB/mo", "**Health insurance** included", "**Bachelor's, Master's, PhD** · apply Nov-Apr"], src=S["csc"] + ". " + FX),
 dict(type="list", label="What it covers", title="Fully *funded*", items=["**Tuition** paid in full", "**Free dorm** on campus", "**Health insurance** (CNY 800 a year)", "**A monthly stipend** on top"], src=S["csc"]),
 dict(type="bars", label="Monthly stipend, RMB", title="What you *receive*", max=3500, bars=[["PhD", 3500, "3,500"], ["Master's", 3000, "3,000"], ["Bachelor's", 2500, "2,500"]], note="About US$375-$525 a month at Oct 2026 rates, with no rent to pay", src=S["csc"]),
 dict(type="timeline", label="The application cycle", title="When to *apply*", items=[
   dict(w="Nov-Feb", t="Apply to your university", d="some schools open in November"), dict(w="Jan-Apr", t="Embassy or university channel", d="dates vary by country", hi=True), dict(w="Late March", t="University nominates you to CSC"), dict(w="June-July", t="Winners announced")], src=S["csc"]),
 CTA_CAREER]),
# ---------------- 10 ----------------
dict(id="10-ugc-vs-influencer", slot="2026-11-13T20:00", pillar="Brand deals", title="UGC creator vs influencer", slides=[
 dict(type="cover", label="China · Brand deals", title="Get paid for content.\n*Not followers.*", size=96, chips=["**Brand pays per video**, not per follower", "**Small following** is fine", "**15-60 sec** vertical 9:16 videos", "**Brands**: hotels, cafés, fashion, sportswear", "**Start with 3 sample videos** of products you own"]),
 dict(type="split", top=dict(label="Two ways to get paid", title="UGC creator", points=["Brand pays for the video", "Brand posts it on its own page or ads", "Small following is fine"]),
   bottom=dict(title="Influencer", points=["Brand pays for your reach", "You post it to your audience", "Followers and engagement matter"], best_label="Best:", best="do both as you grow.")),
 dict(type="list", label="Winning UGC", title="What brands *buy*", items=["A hook in the first 2 seconds", "Real use of the product, on camera", "Clear audio and captions", "Vertical 9:16, 15-60 seconds"]),
 dict(type="flow", label="Start this week", title="Your first *UGC deal*", steps=[dict(t="Make 3 sample videos", d="any products you already own"), dict(t="Build a 1-page media kit", d="samples, niche, rates"), dict(t="DM us", d="we match you with brands in China", hi=True)]),
 CTA_CREATOR]),
# ---------------- 11 ----------------
dict(id="11-visa-free-boom", slot="2026-11-15T11:00", pillar="Travel", title="China's visa-free travel boom", slides=[
 dict(type="cover", label="China · Travel", title="Everyone is\n*going to China.*", size=100, big="13.64M", bsize=170, unit="visa-free entries", chips=["**+53.9%** in one year", "**38.05M** foreign trips, Jan-Jun 2025", "**Hotels & brands** want foreign guests", "**Few English creators** cover it"], src=S["nia"]),
 dict(type="stat", label="Visa-free entries, Jan-Jun 2025", value="13.64M", size=200, title="foreign visitors, *no visa needed*", sub="Up **53.9%** on the same period a year earlier.", src=S["nia"]),
 dict(type="bars", label="Jan-Jun 2025, millions", title="The *growth*", max=38.05, bars=[["All foreign trips", 38.05, "38.05M", "dim"], ["Visa-free entries", 13.64, "13.64M"]],
   note="Foreign trips grew 30.2%. Visa-free entries grew 53.9%.", src=S["nia"]),
 dict(type="list", label="Why it matters for creators", title="The *window* is open", items=["Travelers search for China content before they go", "Few English-speaking creators cover it well", "Hotels and brands want foreign guests", "Early creators own the niche"]),
 CTA_CREATOR]),
# ---------------- 12 ----------------
dict(id="12-athletes", slot="2026-11-15T20:00", pillar="Brand deals", title="Why athletes should look at China", slides=[
 dict(type="cover", label="China · Athletes", title="Athletes: China's\nsports market is *huge.*", size=92, big="$540B", bsize=180, unit="industry", chips=["**72%** is services: training, events, fitness", "**Sportswear & gear** campaigns", "**Gyms & fitness apps**", "**Events, clinics, appearances**", "**Nutrition & recovery** brand deals"], src=S["sport"]),
 dict(type="stat", label="Sports industry total output, 2024", value="3.84T", size=230, title="yuan, about *US$540.6 billion*", sub="Sport was **1.19%** of China's GDP in 2024.", src=S["sport"]),
 dict(type="donut", label="Where the value comes from", title="Mostly *services*", pct=72, center="72%", side="**Sports services** made up 72% of value added. Goods manufacturing was 26.5%. Training, events and fitness need athletes.", src=S["sport"]),
 dict(type="list", label="Deals that fit athletes", title="How *you* fit in", items=["Sportswear and gear campaigns", "Gym, training and fitness app content", "Events, clinics and appearances", "Nutrition and recovery brands"]),
 dict(type="cta", title="Athletes,\nlet's *talk.*", sub="We're signing **athletes** and **UGC creators** for brand deals in China.", points=["Follow for weekly China opportunities", "DM us your sport, stats and media kit"])]),
# ---------------- 13 ----------------
dict(id="13-sh-vs-bj", slot="2026-11-16T11:00", pillar="Best cities", title="Shanghai vs Beijing", slides=[
 dict(type="cover", label="China · Best cities", title="Shanghai\nor *Beijing?*", size=110, chips=["**Shanghai** avg. wage: **12,434 RMB**/mo", "**Beijing** avg. wage: **11,937 RMB**/mo", "**Foreigner pay bar**: **49,736 RMB** (SH)", "**Foreigner pay bar**: **47,748 RMB** (BJ)", "**Shanghai**: finance & fashion · **Beijing**: culture & study"], src="Sources: China Briefing (Feb 2026), 2025 wage basis, Category B work permit benchmarks"),
 dict(type="split", top=dict(label="Both passed 5 trillion yuan GDP", title="Shanghai", points=["2025 GDP: 5.6 trillion yuan", "Avg. wage: 12,434 RMB/month", "Finance, fashion, nightlife"], best_label="Best for:", best="brand and lifestyle content"),
   bottom=dict(title="Beijing", points=["2025 GDP: over 5 trillion yuan", "Avg. wage: 11,937 RMB/month", "History, culture, universities"], best_label="Best for:", best="culture, study and history content"), src="Sources: Caproasia (Jan 2026); Xinhua via Henan Gov't (Feb 2026); China Briefing (Feb 2026)"),
 dict(type="bars", label="Work permit bar for Category B, RMB/month", title="The *pay bar* for foreigners", max=49736, bars=[["Shanghai", 49736, "49,736"], ["Beijing", 47748, "47,748"]],
   note="Category B work permits are benchmarked at **4x the local average wage**. Check your own category with your employer.", src=S["permit"]),
 dict(type="tiles", label="China's big-city club", title="*29 cities* over 1 trillion yuan", tiles=[["5.6T", "Shanghai GDP, 2025"], ["5T+", "Beijing GDP, 2025"], ["2.30T", "Hangzhou GDP, 2025"], ["2.21T", "Wuhan GDP, 2025"]], vsize=86, src=S["gdp"]),
 CTA_TRAVEL]),
# ---------------- 14 ----------------
dict(id="14-platform-fit", slot="2026-11-16T20:00", pillar="Untapped market", title="Which Chinese app fits your content", slides=[
 dict(type="cover", label="China · Platforms", title="Which Chinese app\nfits *your* content?", size=96, chips=["**Douyin**: **714M** daily users", "**Xiaohongshu**: **245M** monthly", "**Bilibili**: **113 min**/day per user", "**Niches**: food, fitness, beauty", "**Travel, fashion, gaming, education**: there's an app for each"], src="Sources: Nomura via TechNode (Jul 2026); QuestMobile via 36Kr (Mar 2026); Bilibili Q2 2026"),
 dict(type="split", top=dict(label="Short video vs lifestyle", title="Douyin", points=["714M daily users", "Fast, trend-driven video", "Like TikTok, built for China"], best_label="Fits:", best="entertainment, food, fitness"),
   bottom=dict(title="Xiaohongshu", points=["245M monthly users", "Young, mostly female, big cities", "Reviews, travel, beauty, fashion"], best_label="Fits:", best="lifestyle and travel"), src="Sources: Nomura via TechNode (Jul 2026); QuestMobile via 36Kr (Mar 2026); CBBC"),
 dict(type="stat", label="Bilibili · long-form video", value="113", title="*minutes a day* per user", sub="371M monthly users who watch longer videos, like YouTube.", src=S["bili"]),
 dict(type="flow", label="Pick your lane", title="Your content → *your app*", steps=[dict(t="Quick, funny, trending", d="Douyin"), dict(t="Travel, beauty, recommendations", d="Xiaohongshu", hi=True), dict(t="Deep dives, gaming, education", d="Bilibili")]),
 CTA_CREATOR]),
# ---------------- 15 ----------------
dict(id="15-hainan", slot="2026-11-18T11:00", pillar="Travel", title="Hainan's 30-day visa-free entry", slides=[
 dict(type="cover", label="China · Travel", title="China's tropical island\nis *visa-free.*", size=96, big="30 days", bsize=170, unit="no visa", chips=["**61 countries** eligible", "**Beaches, resorts, duty-free**", "**Film**: hotel reviews, water sports", "**vs 240-hr transit**: 10 days, 57 countries"], src=S["hainan"] + "; Shanghai Gov't (Jul 2026)"),
 dict(type="split", top=dict(label="Two visa-free routes", title="Hainan", points=["Up to 30 days", "61 eligible countries", "Beaches, resorts, duty-free"], best_label="Best for:", best="a beach and resort trip"),
   bottom=dict(title="240-hour transit", points=["Up to 10 days", "57 eligible countries", "Must exit to a third country"], best_label="Best for:", best="a multi-city stopover"), src=S["hainan"] + "; Shanghai Gov't (Jul 2026)"),
 dict(type="tiles", label="Hainan at a glance", title="Why *creators* go", tiles=[["30", "days visa-free in Hainan"], ["61", "countries eligible for Hainan"], ["10", "days on 240-hour transit"], ["57", "countries for 240-hour transit"]], src=S["hainan"] + "; Shanghai Gov't (Jul 2026)"),
 dict(type="list", label="Content ideas", title="What to *film*", items=["Resort and hotel reviews", "Beach and water sports days", "Tropical food markets", "Duty-free shopping hauls"]),
 CTA_TRAVEL]),
# ---------------- 16 ----------------
dict(id="16-teach-reqs", slot="2026-11-18T20:00", pillar="Jobs", title="What you need to teach in China", slides=[
 dict(type="cover", label="China · Jobs", title="Teach English in China.\n*Here's what you need.*", size=88, big="$5,250+", bsize=160, unit="/ month at top schools", chips=["**Bachelor's** in any subject", "**120-hour TEFL**, TESOL or CELTA", "**Age 18-60** + background check", "**Public schools**: $1,800-$3,000/mo", "**Schools**: international, kindergartens, training centers, universities"], src=S["teach"] + ". " + FX),
 dict(type="list", label="The checklist", title="What you *need*", items=["A **bachelor's degree** in any subject", "A **120-hour TEFL**, TESOL or CELTA", "A **background check** (within 6 months, apostilled)", "**Age 18-60** and a post-arrival medical"], src=S["teach"]),
 dict(type="split", top=dict(label="Passports schools prefer", title="Easiest", points=["US, UK, Ireland, Canada", "Australia, New Zealand", "South Africa"]),
   bottom=dict(title="Possible", points=["Other passports can work", "Approval is harder", "Strong experience helps"], best_label="International schools:", best="need a license + 2 yrs."), src=S["teach"]),
 dict(type="flow", label="Your path", title="From *application* to *classroom*", steps=[dict(t="Get your TEFL", d="120 hours"), dict(t="Gather documents", d="degree, background check"), dict(t="Interview and sign", d="read the contract closely", hi=True), dict(t="Work visa, then fly")]),
 CTA_CAREER]),
# ---------------- 17 ----------------
dict(id="17-deal-timeline", slot="2026-11-20T11:00", pillar="Brand deals", title="A 4-week brand deal timeline", slides=[
 dict(type="cover", label="China · Brand deals", title="Your first paid\nbrand deal in *4 weeks.*", size=92, chips=["**Week 1**: matched with a brand", "**Week 2**: brief, dates, **payment**", "**Week 3**: visit & film", "**Week 4**: post & **get paid**", "**Brands**: hotels, cafés, fashion, sportswear · **plus free stays & products**"]),
 dict(type="timeline", label="Week by week", title="The *4-week* deal", items=[
   dict(w="Week 1", t="Media kit and match", d="we find a brand that fits your niche", hi=True), dict(w="Week 2", t="Brief and agreement", d="deliverables, dates, payment"), dict(w="Week 3", t="Visit and film", d="the hotel, café or product"), dict(w="Week 4", t="Post and get paid", d="report results to the brand")]),
 dict(type="split", top=dict(label="Your job vs ours", title="You", points=["Create great content", "Post on time", "Share your results"]),
   bottom=dict(title="Wealth Bridge", points=["Find and vet brands", "Handle language and contracts", "Keep payment on track"]), join="&"),
 dict(type="list", label="Speed it up", title="Be *ready* on day one", items=["Media kit with rates", "3 recent examples in your niche", "Your audience stats (age, location)", "Your travel dates if you're visiting China"]),
 CTA_CREATOR]),
# ---------------- 18 ----------------
dict(id="18-chengdu", slot="2026-11-20T20:00", pillar="Best cities", title="Chengdu: the savings city", slides=[
 dict(type="cover", label="China · Best cities", title="Earn less.\n*Save more.*", size=110, big="16,000 RMB", bsize=140, unit="/ mo + free housing", chips=["**Shanghai**: 22,000 − **8,000 rent** = 14,000", "**Tier-2 teacher pay**: **14k-22k RMB** (~$2,100-$3,300)", "**Cities**: Chengdu, Hangzhou, Wuhan, Xi'an"], src=S["teach"] + ". Example offer; yours will differ. " + FX),
 dict(type="bars", label="Monthly, RMB, after rent", title="What's *left over*", max=16000, bars=[["Chengdu: 16,000 + free housing", 16000, "16,000"], ["Shanghai: 22,000 - 8,000 rent", 14000, "14,000", "dim"]],
   note="Example from a 2026 teaching salary guide. Your offer will differ.", src=S["teach"]),
 dict(type="ranges", label="Typical teacher pay, RMB/month", title="Tier-2 cities *pay well*", max=25000, bars=[["Chengdu", 14000, 22000, "14k-22k"], ["Hangzhou", 14000, 22000, "14k-22k"], ["Wuhan", 14000, 22000, "14k-22k"], ["Xi'an", 14000, 22000, "14k-22k"]], src=S["teach"]),
 dict(type="list", label="Why Chengdu", title="More than *pandas*", items=["Lower rent than tier-1 cities", "240-hour visa-free entry port", "Famous food scene for content", "Big, growing city with jobs"], src="Sources: Migaku 2026; WanderInChina 240-hour port list"),
 CTA_CAREER]),
# ---------------- 19 ----------------
dict(id="19-online-shoppers", slot="2026-11-22T11:00", pillar="Untapped market", title="976 million online shoppers", slides=[
 dict(type="cover", label="China · Untapped market", title="Shoppers who buy\nwhat *creators* recommend.", size=88, big="976M", bsize=180, unit="online shoppers", chips=["**15.97T yuan** online retail, 2025", "**87%** of internet users shop online", "**1.068B** short-video users", "**Review → save → buy**: creators move product"], src="Sources: CNNIC (Jun 2025); NBS 2025"),
 dict(type="donut", label="Share of internet users who shop online", title="Shopping is *default*", pct=86.9, center="87%", side="**976 million** people shop online in China, 86.9% of internet users.", src=S["cnnic_mid"]),
 dict(type="tiles", label="The scale", title="China online, *in numbers*", tiles=[["1.125B", "internet users"], ["1.068B", "short-video users"], ["976M", "online shoppers"], ["15.97T", "yuan online retail, 2025"]], vsize=78,
   src="Sources: CNNIC (Dec 2025, Jun 2025); NBS 2025"),
 dict(type="flow", label="How creators move product", title="From *video* to *sale*", steps=[dict(t="Creator posts a review"), dict(t="Viewers search and save it", d="especially on Xiaohongshu"), dict(t="They buy in-app or in-store", hi=True), dict(t="Brand pays for more")]),
 CTA_CREATOR]),
# ---------------- 20 ----------------
dict(id="20-contract-flags", slot="2026-11-22T20:00", pillar="Jobs", title="Red flags in a China job contract", slides=[
 dict(type="cover", label="China · Jobs", title="5 *red flags*\nin a China job contract.", size=96, chips=["**Early termination penalties**", "**Salary withheld** as a deposit", "**Unclear overtime** rules", "**Vague housing** terms", "**No English version** of the contract"], sub="Read this before you sign anything.", src=S["teach"]),
 dict(type="list", label="Watch for", title="Red *flags*", items=["Big **early termination penalties**", "Salary **withheld as a deposit**", "**Unclear overtime** rules", "**Vague housing** terms", "**No English version** of the contract"], src=S["teach"]),
 dict(type="split", top=dict(label="Good vs bad offer", title="Red flag", points=["'Housing provided' with no details", "Pay held back until you finish", "Hours 'as needed'"]),
   bottom=dict(title="Green flag", points=["Housing address or stipend amount", "Pay on a fixed date each month", "Weekly hours written down"], best_label="Rule:", best="if it's not written, it's not real.")),
 dict(type="list", label="Also remember", title="Before you *sign*", items=["Salaries are taxed under China's income tax", "Ask current teachers about the school", "Confirm who pays for your work visa", "Keep copies of everything"], src=S["teach"]),
 CTA_CAREER]),
# ---------------- 21 ----------------
dict(id="21-media-kit", slot="2026-11-23T11:00", pillar="Brand deals", title="Build a media kit brands say yes to", slides=[
 dict(type="cover", label="China · Brand deals", title="The *media kit*\nthat gets you paid.", size=100, chips=["**Niche** + one-line bio", "**Audience**: size, age, location", "**Results**: views, saves, engagement", "**3 best examples** with links", "**Clear rates**: per video and per package"], sub="One page. Five sections. Brands say yes faster."),
 dict(type="list", label="What goes in it", title="Your *one-pager*", items=["**Who you are**: niche and one-line bio", "**Your audience**: size, age, top locations", "**Results**: views, saves, engagement", "**3 best examples** with links", "**Rates**: per video, per package"]),
 dict(type="split", top=dict(label="Weak vs strong", title="Weak", points=["'I have 8K followers'", "No examples", "'Rates on request'"]),
   bottom=dict(title="Strong", points=["'8K followers, 60% aged 18-34'", "3 videos in your niche", "Clear package prices"], best_label="Result:", best="faster yeses.")),
 dict(type="flow", label="Then", title="Send it to *us*", steps=[dict(t="Export as a PDF"), dict(t="DM us 'MEDIA KIT'", hi=True), dict(t="We match you with China brands")]),
 CTA_CREATOR]),
# ---------------- 22 ----------------
dict(id="22-canton-fair", slot="2026-11-23T20:00", pillar="Best cities", title="Guangzhou's Canton Fair guide", slides=[
 dict(type="cover", label="China · Guangzhou", title="The world's\nbiggest *trade fair.*", size=100, big="167K", bsize=170, unit="overseas buyers", chips=["**216** countries & regions", "**12K+** exhibitors", "**Niches**: advanced manufacturing", "**Home & lifestyle** goods", "**Jobs**: foreign trade sales, cross-border e-commerce"], src=S["canton"]),
 dict(type="tiles", label="Spring 2026, phase 1", title="By the *numbers*", tiles=[["167K", "overseas buyers"], ["216", "countries and regions"], ["12K+", "exhibitors"], ["+5.9%", "buyers vs last edition"]], vsize=86, src=S["canton"]),
 dict(type="timeline", label="Spring 2026 schedule", title="Three *phases*", items=[
   dict(w="Phase 1 · ended Apr 19", t="Advanced manufacturing", d="theme: advancing manufacturing"), dict(w="Phase 2 · Apr 23-27", t="Home and lifestyle goods", hi=True), dict(w="Phase 3 · through May 5", t="Final phase of the fair")], src=S["canton"] + ". Check cantonfair.org.cn for 2027 dates"),
 dict(type="list", label="Tips for creators", title="Make it *content*", items=["Hotels fill up and prices rise during the fair", "Film booth tours and supplier interviews", "Base in Guangzhou, day-trip to nearby cities", "Use the 240-hour transit if eligible"], src="Sources: China Daily (Apr 2026); WanderInChina"),
 CTA_TRAVEL]),
# ---------------- 23 ----------------
dict(id="23-trip-checklist", slot="2026-11-25T11:00", pillar="Travel", title="First trip to China checklist", slides=[
 dict(type="cover", label="China · Travel", title="First trip to China:\n*the checklist.*", size=96, chips=["**Visa-free?** 57 countries, 10 days", "**Alipay** + your own card", "**WeChat Pay** as a backup", "**Under 200 RMB**: no card fee", "**Offline maps, translator** and a little cash"], sub="Save this before you book.", src=S["t240"].split(". Rules")[0] + "; " + S["alipay"].replace("Source: ", "")),
 dict(type="list", label="Before you book", title="Step *one*", items=["Check if your passport qualifies for visa-free entry", "240-hour transit? Book an exit to a **third country**", "Not eligible? Apply for a tourist visa early", "Check that your passport isn't close to expiring"], src=S["t240"]),
 dict(type="list", label="Before you fly", title="Step *two*", items=["Set up **Alipay** and link your card", "Add **WeChat Pay** as a backup", "Download offline maps and a translator", "Carry a little cash"], src=S["alipay"]),
 dict(type="flow", label="When you land", title="Step *three*", steps=[dict(t="Show passport and onward ticket"), dict(t="Make a small test payment", d="under 200 RMB, no fee", hi=True), dict(t="Start creating")], src=S["alipay"]),
 CTA_TRAVEL]),
# ---------------- 24 ----------------
dict(id="24-schwarzman-yenching", slot="2026-11-25T20:00", pillar="Scholarships", title="Fully funded master's in China", slides=[
 dict(type="cover", label="China · Scholarships", title="A free master's at\nChina's *top* universities.", size=88, big="$0", bsize=180, unit="tuition, plus a stipend", chips=["**Schwarzman · Tsinghua**: Global Affairs, 1 year", "**Yenching · Peking U**: China Studies", "**Covers**: tuition, housing, travel", "**Ages 18-28** (Schwarzman)"], src=S["schw"]),
 dict(type="split", top=dict(label="Two elite scholarships", title="Schwarzman", points=["Tsinghua University, Beijing", "1-year master's in Global Affairs", "Ages 18-28"], best_label="Covers:", best="tuition, room, travel, stipend"),
   bottom=dict(title="Yenching", points=["Peking University, Beijing", "Master's in China Studies", "Preferably 25 or younger"], best_label="Covers:", best="tuition, housing, living costs"), src=S["schw"]),
 dict(type="list", label="Schwarzman covers", title="Everything, *basically*", items=["Tuition and fees", "Room and board", "Round-trip travel to Beijing", "In-country study tour", "Health insurance and a stipend"], src=S["schw"]),
 dict(type="list", label="How to stand out", title="Apply *smart*", items=["Show leadership, not just grades", "Explain why China, specifically", "Start essays months early", "Check official sites for this cycle's deadlines"]),
 CTA_CAREER]),
# ---------------- 25 ----------------
dict(id="25-why-now", slot="2026-11-27T11:00", pillar="Untapped market", title="Why now is the time for China", slides=[
 dict(type="cover", label="China · Untapped market", title="Why *now*\nis the time for China.", size=100, chips=["**+53.9%** visa-free entries", "**+8.6%** online retail growth", "**+19%** Douyin daily users", "**57 countries** visa-free transit", "**Brand deals, jobs, travel**: the window is open"], src="Sources: NIA via Xinhua (H1 2025); NBS 2025; Nomura via TechNode (Jul 2026); Shanghai Gov't"),
 dict(type="tiles", label="Three trends", title="The *window*", tiles=[["+53.9%", "visa-free entries, H1 2025"], ["+8.6%", "online retail growth, 2025"], ["+19%", "Douyin daily users, year on year"], ["57", "countries with 240-hr transit"]], vsize=78,
   src="Sources: NIA via Xinhua; NBS; Nomura via TechNode (Jul 2026); Shanghai Gov't"),
 dict(type="split", top=dict(label="Then vs now", title="Before", points=["Hard to visit", "Payments confusing for visitors", "Few creator connections"]),
   bottom=dict(title="Now", points=["Visa-free routes for many", "Link your own card to Alipay", "Teams like us bridge the gap"], best_label="Your move:", best="get in early.")),
 dict(type="bars", label="Daily users, millions", title="Douyin keeps *growing*", max=714, bars=[["Douyin DAU, July 2026", 714, "714M"], ["Douyin DAU, one year earlier", 600, "~600M", "dim"]],
   note="Up 19% year on year, per Nomura. Prior-year figure derived from that growth.", src=S["nomura"]),
 CTA_CREATOR]),
# ---------------- 26 ----------------
dict(id="26-confucius", slot="2026-11-27T20:00", pillar="Scholarships", title="Study Chinese for free", slides=[
 dict(type="cover", label="China · Scholarships", title="Learn Chinese\n*for free* in China.", size=100, big="3,000 RMB", bsize=140, unit="/ month max stipend", chips=["**Full tuition**", "**Free dorm**", "**Stipend**: 2,500-3,000 RMB/mo", "**1,500 RMB** settlement allowance", "**Bilingual = better jobs & brand deals**"], src=S["csc"]),
 dict(type="list", label="What it covers", title="The *package*", items=["**Full tuition**", "**Free dorm**", "**2,500-3,000 RMB** monthly stipend", "**1,500 RMB** one-time settlement allowance", "Basic health insurance"], src=S["csc"]),
 dict(type="split", top=dict(label="Two scholarships", title="Confucius", points=["Focus: learning Chinese", "Apply via a Confucius Institute", "Usually due Jan-Apr"]),
   bottom=dict(title="CSC", points=["Focus: full degrees", "Apply via embassy or university", "Jan-Apr, varies by country"], best_label="Tip:", best="start in winter."), src=S["csc"]),
 dict(type="flow", label="Why it helps your career", title="Language → *leverage*", steps=[dict(t="Learn Chinese in China"), dict(t="Build local connections"), dict(t="Land jobs and brand deals", d="that need bilingual talent", hi=True)]),
 CTA_CAREER]),
# ---------------- 27 ----------------
dict(id="27-hz-wuhan", slot="2026-11-29T11:00", pillar="Best cities", title="Hangzhou and Wuhan", slides=[
 dict(type="cover", label="China · Best cities", title="Cities you've\n*never heard of*\nwith huge economies.", size=88, big="2T+", bsize=170, unit="yuan GDP each", chips=["**Hangzhou**: **2.30T** · tech & e-commerce", "**Wuhan**: **2.21T** · universities", "**Wuhan teacher pay**: 14k-22k RMB", "**29 cities** over 1T yuan"], src=S["gdp"] + "; Migaku 2026"),
 dict(type="bars", label="2025 GDP, trillion yuan", title="Bigger than *you think*", max=5.6, bars=[["Shanghai", 5.6, "5.6T", "dim"], ["Hangzhou", 2.3011, "2.30T"], ["Wuhan", 2.2147, "2.21T"]],
   note="China now has **29 cities** with GDP over 1 trillion yuan.", src=S["gdp"]),
 dict(type="split", top=dict(label="Two rising cities", title="Hangzhou", points=["Tech and e-commerce hub", "Famous West Lake scenery", "240-hour entry port"], best_label="Best for:", best="tech, travel, lifestyle"),
   bottom=dict(title="Wuhan", points=["Central China's biggest city", "Huge university population", "Teacher pay 14k-22k RMB"], best_label="Best for:", best="teaching and student life"), src="Sources: WanderInChina; Migaku 2026"),
 dict(type="list", label="Content ideas", title="What to *film*", items=["Hangzhou: West Lake sunrise and tea fields", "Hangzhou: day in the life in a tech city", "Wuhan: street food breakfast tour", "Wuhan: campus life as a foreign teacher"]),
 CTA_TRAVEL]),
# ---------------- 28 ----------------
dict(id="28-creator-recruit", slot="2026-11-29T20:00", pillar="Recruitment", title="We're signing creators and athletes", slides=[
 dict(type="cover", label="Now signing", title="We need *UGC creators*\nand athletes.", size=96, chips=["**Paid brand partnerships**", "**Free hotel stays & products**", "**Niches**: travel, food, beauty, fashion", "**Athletes & fitness** creators", "**We handle** brands, contracts and payment"], sub="Brand deals in China, managed for you. DM your media kit."),
 dict(type="list", label="Who we're looking for", title="Is this *you?*", items=["UGC creators in travel, food, beauty, fashion", "Athletes and fitness creators", "Clean, consistent video quality", "Open to visiting China, or filming remotely"]),
 dict(type="split", join="&", top=dict(label="What you get", title="Deals", points=["Paid brand partnerships", "Hotel stays and products", "China content for your page"]),
   bottom=dict(title="Support", points=["We find and vet brands", "We handle language and contracts", "We keep payment on track"])),
 dict(type="flow", label="How to apply", title="3 steps to *start*", steps=[dict(t="Follow @wealthbridgenetwork"), dict(t="DM us your media kit", hi=True), dict(t="We reply with matching brands")]),
 CTA_CREATOR]),
# ---------------- 29 ----------------
dict(id="29-kuaishou-bilibili", slot="2026-11-30T11:00", pillar="Untapped market", title="The apps beyond Douyin", slides=[
 dict(type="cover", label="China · Platforms", title="Beyond Douyin:\n*two giants* you've missed.", size=92, chips=["**Kuaishou**: **797M** monthly", "**+11.5%** in a year", "**Kuaishou**: **412M** daily · live shopping", "**Bilibili**: **371M** monthly", "**Bilibili**: **113 min**/day · long video & education"], src=S["ks"] + "; " + S["bili"].replace("Source: ", "")),
 dict(type="split", top=dict(label="Two more platforms", title="Kuaishou", points=["412M daily users", "797M monthly users", "Short video and live shopping"], best_label="Fits:", best="relatable, everyday content"),
   bottom=dict(title="Bilibili", points=["117M daily users", "371M monthly users", "113 minutes a day each"], best_label="Fits:", best="long videos and education"), src="Sources: Kuaishou & Bilibili Q2 2026 results"),
 dict(type="bars", label="Monthly users, millions, Q2 2026", title="Kuaishou is *growing*", max=797.3, bars=[["Kuaishou, Q2 2026", 797.3, "797M"], ["Kuaishou, Q2 2025", 714.8, "715M", "dim"]], note="Monthly users up **11.5%** in a year.", src=S["ks"]),
 dict(type="list", label="Takeaway", title="Don't put all eggs in *one app*", items=["Post short clips on Douyin and Kuaishou", "Post guides on Xiaohongshu", "Post long versions on Bilibili", "One shoot, four platforms"]),
 CTA_CREATOR]),
# ---------------- 30 ----------------
dict(id="30-month-recap", slot="2026-11-30T20:00", pillar="Recap", title="China opportunities: the recap", slides=[
 dict(type="cover", label="Save this", title="China in *one post.*", size=100, chips=["**1.125B** people online", "**714M** open Douyin daily", "**Jobs** up to **$5,000/mo**", "**3,500 RMB/mo** PhD stipend", "**Visa-free**: 57 countries, 10 days · **Hainan** 30 days"], sub="Jobs, scholarships, brand deals and travel, recapped.", src="Sources: CNNIC; Nomura via TechNode; Migaku 2026; CSC program pages; Shanghai & Beijing Gov't"),
 dict(type="tiles", label="The numbers to remember", title="China, *at a glance*", tiles=[["1.125B", "people online"], ["714M", "open Douyin daily"], ["57", "countries with 240-hr transit"], ["3,500", "RMB/month CSC PhD stipend"]], vsize=80,
   src="Sources: CNNIC; Nomura via TechNode; Shanghai Gov't; CSC program pages"),
 dict(type="flow", label="Your roadmap", title="Pick your *bridge*", steps=[dict(t="Creator or athlete?", d="brand deals in China"), dict(t="Want a career?", d="teaching and work permits"), dict(t="Want to study?", d="CSC, Schwarzman, Yenching"), dict(t="Just visiting?", d="240-hour transit and Hainan", hi=True)]),
 dict(type="list", label="Coming up", title="Next month on *our page*", items=["More city guides", "Real brand deal breakdowns", "Scholarship deadlines", "Creator and athlete spotlights"]),
 CTA_CREATOR]),
]

POSTS.sort(key=lambda p: p["slot"])
