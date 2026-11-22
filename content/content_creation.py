# "Content Creation" series (drafted Nov 22, 2026): 7 illustrated carousels.
# Every number was checked against the source named on its slide (research notes in drafts/content-creation-sources.md).
# All people are faceless illustrations; "Mark" is an illustrative story, labelled as such.

SIGN = "Building Bridges | Creating Access"
TAGS = "#china #explore #chinatravel #Guangzhou"
FX = "USD at 6.71 RMB (PBOC, Nov 19, 2026)"


def caption(hook, body, extra="", follow="Follow @wealthbridgenetwork for more China opportunities."):
    return f"{hook}\n\n{body}\n\n{follow}\n\n{SIGN}\n\n{TAGS}{(' ' + extra) if extra else ''}"


CTA_CREATOR = dict(k="cta", art="vlog", title="Creators: let's get\nyou *to China.*",
                   sub="We connect **UGC creators, vloggers and athletes** with hotels, destinations and brands in China.",
                   pills=["DM US YOUR MEDIA KIT", "FOLLOW FOR MORE"])

POSTS = [
# =========================================================== 48 · HOTELS & TRAVEL CREATORS
dict(id="48-creator-stays", pillar="Content creation", title="Hosted stays in China for travel creators",
 caption=caption("Travel creators: China wants your content.",
   "Tourism boards and travel brands are already hosting foreign creators, from fully paid trips to hosted stays in exchange for content. "
   "Five places worth pitching: Guizhou, Xinjiang, Chengdu, Hainan and Zhangjiajie. Save this for your next pitch.",
   "#travelcreator #ugccreator #contentcreator #hotelcollab #zhangjiajie #chengdu"),
 slides=[
  dict(k="hero", art="vlog", label="Content creation · Travel", title="Get hosted\nin China.\n*For content.*",
       sub="Hotels, destinations and travel brands want creators. Here's where to start."),
  dict(k="panel", label="It's already happening", title="China is *inviting* creators", size=80, cards=[
       dict(k="Beijing · Jun 2025", h="All-expenses-paid trip", d="10 days in China offered to US influencers with 300K+ followers."),
       dict(k="Hunan · Jun 2026", h="20 creators, 11 countries", d="Hosted on a provincial tour that included Zhangjiajie."),
       dict(k="Trip.com · 2025", h="TripMates program", d="A creator program inviting foreign creators to make China content."),
       dict(k="2025 · all of China", h="30.08M visa-free entries", d="Up 49.5% on 2024. Audiences want to see China.", hi=True)],
       src="Sources: Bloomberg (Jun 10, 2025); Hunan Today (Jun 18, 2026); Jing Daily (Jun 2025); National Immigration Administration (Jan 30, 2026)"),
  dict(k="hero", art="guizhou", label="01 · Guizhou", title="Waterfalls, karst\nand *rice terraces.*",
       stat=("+267%", "foreign visitor entries in 2025, to 74,000+. Few creators have filmed it yet."),
       src="Source: China Daily, Jan 31, 2026"),
  dict(k="hero", art="xinjiang", label="02 · Xinjiang", title="Snow peaks, lakes\nand *open desert.*",
       stat=("323M", "tourist visits in 2025. Huge scenery, almost no English-language content."),
       src="Source: China Youth Daily, Jan 29, 2026"),
  dict(k="hero", art="chengdu", label="03 · Chengdu", title="Pandas, hotpot\nand *nightlife.*",
       stat=("Top 5", "Chinese city for inbound tourist spending (Jul 2024 to Jun 2025)."),
       src="Source: GoChengdu citing the World Tourism Alliance, Jan 12, 2026"),
  dict(k="hero", art="hainan", label="04 · Hainan", title="China's tropical\n*island.*",
       stat=("1.5M+", "inbound overnight visitors in 2025, up 35.2%. Beach resorts love creators."),
       src="Source: People's Daily, Jan 20, 2026"),
  dict(k="hero", art="zhangjiajie", label="05 · Zhangjiajie", title="The floating\n*mountains.*",
       stat=("1M+", "inbound visits to Wulingyuan in 2025, a first. Made for vertical video."),
       src="Source: Hunan Today, Jan 15, 2026"),
  dict(k="panel", label="How a hosted stay works", title="The *content-for-stay* trade", size=76, flow=[
       dict(h="Pitch with your media kit", d="Audience, niche, past work, what you'll make"),
       dict(h="Agree the deal", d="Hosted (free) stay, or a stay plus a fee", hi=True),
       dict(h="Film and post", d="Reels, vlogs, photos, honest reviews"),
       dict(h="They reuse it, you grow", d="Usage rights agreed up front; it's portfolio work for you")],
       note="Terms vary by property and audience. Always get the deal in writing."),
  dict(CTA_CREATOR, art="hainan"),
 ]),
# =========================================================== 49 · BRAND DEALS FOR VLOGGERS
dict(id="49-vlogger-deals", pillar="Brand deals", title="Brand deals for vloggers",
 caption=caption("Your China vlog could be a brand deal.",
   "Influencer marketing hit an estimated $32.55B in 2025, and 87.5% of brands plan to spend more. Here are the 4 deal types, what brands look for, and how a deal flows from pitch to payout.",
   "#vlogger #branddeals #ugccreator #contentcreator #influencermarketing"),
 slides=[
  dict(k="hero", art="vlog", label="Content creation · Brand deals", title="Your China vlog\ncould be a\n*brand deal.*",
       sub="What brands pay for, and how vloggers get picked."),
  dict(k="panel", label="The money is moving", title="Brands are spending *more* on creators", size=76, cards=[
       dict(v="$32.55B", h="Influencer marketing, 2025", d="Estimated global market, up from $24B in 2024.", hi=True),
       dict(v="87.5%", h="of brands", d="expect to raise their influencer budgets."),
       dict(v="45.9%", h="track with promo codes", d="Your code = proof you drive sales."),
       dict(v="26%", h="use affiliate links", d="Commission on every sale you send.")],
       src="Sources: Influencer Marketing Hub, Mar 3, 2026 and Benchmark Report, May 4, 2026"),
  dict(k="panel", label="The 4 deal types", title="How vloggers *get paid*", size=80, cards=[
       dict(k="01", h="Gifted / hosted", d="Free product, stay or trip in exchange for content."),
       dict(k="02", h="Paid post", d="A flat fee per video, reel or vlog segment."),
       dict(k="03", h="Affiliate", d="A commission on sales through your code or link."),
       dict(k="04", h="Ambassador", d="A longer deal: several posts over months.", hi=True)],
       note="Rates depend on audience, niche and usage rights. No deal is guaranteed."),
  dict(k="hero", art="chengdu", pos="top", label="What brands look for", title="Not just *followers.*",
       sub="**1.** A clear niche (travel, food, fitness, tech)\n**2.** Real engagement and comments\n**3.** Clean edits with subtitles\n**4.** A one-page media kit with stats"),
  dict(k="panel", label="The system", title="How a deal *flows*", size=80, flow=[
       dict(h="You", d="vlogger with a real, engaged audience"),
       dict(h="Wealth Bridge Network", d="matches you with the brand and manages the deal", hi=True),
       dict(h="Brief and contract", d="deliverables, dates, usage rights, fee"),
       dict(h="Film, post, report", d="share results and your promo-code sales"),
       dict(h="Get paid", d="plus product, stays and portfolio work")]),
  CTA_CREATOR,
 ]),
# =========================================================== 50 · ATHLETE ENDORSEMENTS
dict(id="50-athlete-endorsements", pillar="Brand deals", title="Chinese brands are signing athletes",
 caption=caption("Chinese brands are signing athletes. NBA stars went first.",
   "Anta, Li-Ning and 361° have signed Klay Thompson, Kyrie Irving, Stephen Curry's Curry Brand, Dwyane Wade, Jimmy Butler and Nikola Jokic. "
   "As Chinese brands go global, NCAA, soccer, track and other athletes are on the radar. Athletes: DM us.",
   "#athletes #nil #ncaa #nba #soccer #sponsorship #endorsement", follow="Athletes: DM @wealthbridgenetwork to talk China brand deals."),
 slides=[
  dict(k="hero", art="arena", label="Content creation · Athletes", title="Chinese brands\nare signing\n*athletes.*",
       sub="NBA stars went first. NCAA, soccer and more are next."),
  dict(k="panel", label="The proof", title="Who's *already* signed", size=80, cards=[
       dict(k="Anta · Feb 2026", h="Klay Thompson", d="Anta's first-ever lifetime deal.", hi=True),
       dict(k="Li-Ning · Jun 2026", h="Stephen Curry's Curry Brand", d="A long-term partnership."),
       dict(k="Anta · Jul 2023", h="Kyrie Irving", d="5-year deal + Chief Creative Officer."),
       dict(k="361° · Jan 2024", h="Nikola Jokić", d="Endorsement deal with the 3x MVP."),
       dict(k="Li-Ning · 2018", h="Dwyane Wade", d="A lifetime deal."),
       dict(k="Li-Ning · Nov 2020", h="Jimmy Butler", d="A multi-year shoe deal.")],
       src="Sources: ANTA newsroom (2026); Li-Ning via PRNewswire (Jun 2026); Front Office Sports (2023); Formula4Media (2024); NBA.com (2018); Hypebeast (2020)"),
  dict(k="hero", art="skyline", label="Why now", title="Chinese brands are\n*going global.*",
       sub="Sportswear brands like Anta and Li-Ning use athlete deals to win fans outside China. That opens the door beyond the NBA.",
       src="Source: Daxue Consulting, Jun 23, 2026"),
  dict(k="panel", label="College athletes", title="NIL changed *everything*", size=80, timeline=[
       dict(w="July 1, 2021", h="NIL goes live", d="NCAA athletes can earn from their name, image and likeness."),
       dict(w="June 6, 2025", h="House v. NCAA approved", d="Schools can now share up to $20.5M a year with athletes.", hi=True),
       dict(w="Heads up", h="International students", d="F-1 visa rules restrict NIL earnings inside the US. Check with your compliance office first.")],
       src="Sources: CBS Sports (Jun 30, 2021); NPR (Jun 6, 2025); Front Office Sports (Feb 21, 2025)"),
  dict(k="panel", label="Who brands look for", title="Athletes *we're* talking to", size=80, cards=[
       dict(h="NBA & WNBA", d="Pros and recent alumni"), dict(h="NCAA", d="D1 to D3, any sport with a following"),
       dict(h="Soccer", d="Pro, semi-pro and college"), dict(h="Track, combat, fitness", d="Athletes who create content"),
       dict(h="What matters", d="Performance + personality + content you can post consistently.", hi=True, wide=True)], one=False,
       note="No deal is guaranteed. Every deal is reviewed with you before you sign."),
  dict(k="cta", art="arena", label="Athletes", title="Your next sponsor\ncould be *in China.*",
       sub="We connect athletes with Chinese brands going global.", pills=["DM US \"ATHLETE\"", "FOLLOW FOR MORE"]),
 ]),
# =========================================================== 51 · JOBS $2-6K
dict(id="51-jobs-2k-6k", pillar="Job offers", title="Jobs in China paying $2K-$6K a month",
 caption=caption("Jobs in China paying $2K to $6K a month.",
   "English teaching, international schools, sports coaching, tech and marketing. Many roles add housing, flights and paid holidays. Here's what each sector pays and what you need to get the work visa.",
   "#jobsinchina #teachinchina #workabroad #expat #careers"),
 slides=[
  dict(k="hero", art="skyline", label="Content creation · Jobs", title="Jobs in China\npaying *$2K–$6K*\na month.",
       sub="The sectors hiring foreigners right now, and what they pay."),
  dict(k="panel", label="Monthly pay, by sector", title="What each sector *pays*", size=72, max=7,
       ranges=[("English teaching", 2.2, 3.7, "$2.2K–$3.7K", "Public schools & training centres · RMB 15–25K"),
               ("International schools", 3.7, 6.0, "$3.7K–$6K+", "Licensed teachers · RMB 25–40K+"),
               ("Sports coaching", 2.5, 2.9, "$2.5K–$2.9K", "Basketball coach job ad · plus housing allowance"),
               ("Tech & engineering", 4.6, 4.9, "~$4.8K", "Tier-1 city benchmark (algorithm engineer)"),
               ("Marketing & sales", 5.8, 6.1, "~$6K", "Senior executive · job-board estimate")],
       ticks=["$0", "$1K", "$2K", "$3K", "$4K", "$5K", "$6K", "$7K"],
       src=f"Sources: Teach Away (2026); HoopDirt job ad; 51job 2025 via China Briefing (Jun 2026); eChinaCities (2025). {FX}"),
  dict(k="hero", art="classroom", label="On top of the salary", title="The *perks* add up",
       sub="Many teaching contracts include:\n**Free housing** or a housing allowance · **flight reimbursement** · **paid summer & winter breaks** · **end-of-contract bonus** · **health insurance**",
       src="Source: ESL Base China guide, Oct 22, 2026. Benefits vary by employer"),
  dict(k="panel", label="The work visa (Z visa)", title="What you *usually* need", size=80, rows=[
       "A **bachelor's degree**", "**2 years' experience**, or a **120-hour TEFL** for teaching jobs",
       "A **clean criminal record check** (apostilled)", "A **medical check**",
       "About **12–16 weeks** from offer to arrival"],
       src="Sources: ESL Base (Oct 2026); TEFL.org (Jun 2026). Rules change; check with your employer and embassy"),
  dict(k="cta", art="skyline", label="Wealth Bridge Network", title="Build your future\nin *China.*",
       sub="Jobs, scholarships and brand deals, explained every week.", pills=["FOLLOW FOR MORE", "DM US YOUR QUESTIONS"]),
 ]),
# =========================================================== 52 · FEIE
dict(id="52-feie-100k", pillar="Money", title="Earn $100K abroad, pay $0 US income tax (FEIE)",
 caption=caption("Earn $100K abroad. Pay $0 US federal income tax. It's called the FEIE.",
   "The Foreign Earned Income Exclusion lets qualifying Americans exclude up to $132,900 of foreign earned income in 2026 (IRS). "
   "You must have a tax home abroad and pass the 330-day or bona fide residence test, and you still file (Form 2555). "
   "Read the fine print: the country you live in may tax you, and self-employment tax still applies. Not tax advice; talk to a tax professional.",
   "#feie #expat #taxes #americansabroad #workabroad #digitalnomad"),
 slides=[
  dict(k="hero", art="passport", label="Content creation · Money", title="Earn $100K abroad.\nPay *$0* US\nincome tax.",
       sub="It's legal. It's called the **FEIE**."),
  dict(k="panel", label="Foreign Earned Income Exclusion", title="What the *FEIE* is", size=80, cards=[
       dict(v="$132,900", h="Tax year 2026", d="Foreign earned income you can exclude from US federal income tax.", hi=True),
       dict(v="$130,000", h="Tax year 2025", d="The limit for the return you file in 2026."),
       dict(h="Plus: housing", d="A foreign housing exclusion can cover some rent above a base amount."),
       dict(h="Earned income only", d="Wages and fees. Not investments, pensions or US government pay.")], src="Source: IRS (Rev. Proc. 2025-32, Oct 9, 2025; FEIE page, Jun 2026)"),
  dict(k="panel", label="The math", title="$100K salary, *$0* US income tax", size=74, compare=[
       dict(k="YOUR SALARY ABROAD", lines=[("Foreign earned income", "$100,000"), ("FEIE limit (2026)", "$132,900")],
            v="$100K", d="Fully under the limit", pct=75),
       dict(k="US FEDERAL INCOME TAX", g=True, lines=[("Excluded", "$100,000"), ("Taxable (US)", "$0")],
            v="$0", d="If you qualify and file Form 2555", pct=100)],
       note="Example for a single filer with only foreign wages. Your situation may differ.", src="Source: IRS FEIE page, Jun 2026"),
  dict(k="panel", label="How to qualify", title="Pass *one* test", size=80, flow=[
       dict(h="Tax home abroad", d="Your main place of work is outside the US"),
       dict(h="Physical presence test", d="330 full days abroad in any 12 months in a row", hi=True),
       dict(h="Or: bona fide residence", d="A resident abroad for a full tax year"),
       dict(h="Still file every year", d="Claim it on Form 2555 with your US return")], src="Source: IRS FEIE page, Jun 2026"),
  dict(k="panel", label="The fine print", title="Read this *before* you move", size=80, rows=[
       "**The country you live in can tax you.** China taxes residents (183+ days) at 3%–45%.",
       "China exempts some foreigner allowances (housing, kids' education, language) **until Dec 31, 2027**.",
       "**Self-employed?** The FEIE doesn't remove self-employment tax.",
       "Some **US states** may still tax you. **Talk to a tax professional.**"],
       src="Sources: PwC Tax Summaries (Jul 2026); MOF/STA Announcement 2023 No. 29 via China Briefing; IRS. Not tax advice"),
  dict(k="cta", art="passport", label="Wealth Bridge Network", title="Work abroad.\n*Keep more.*",
       sub="Jobs, scholarships and brand deals in China, explained every week.", pills=["SAVE THIS", "FOLLOW FOR MORE"]),
 ]),
# =========================================================== 53 · UNIVERSITIES & SCHOLARSHIPS
dict(id="53-scholarships", pillar="Scholarships", title="Study in China for free: universities & scholarships",
 caption=caption("Study in China. Fully funded.",
   "China has 5 universities in the QS world top 50, and scholarships that cover tuition, housing and a monthly stipend: "
   "the Chinese Government Scholarship (CSC), Schwarzman Scholars, Yenching Academy and the International Chinese Language Teachers Scholarship. "
   "Yenching's deadline is Nov 30, 2026. Check the official sites before you apply.",
   "#studyinchina #scholarship #fullyfunded #studyabroad #cscscholarship #schwarzman"),
 slides=[
  dict(k="hero", art="campus", label="Content creation · Scholarships", title="Study in China.\n*Fully funded.*",
       sub="Tuition, housing and a monthly stipend. Most people never apply."),
  dict(k="panel", label="QS World University Rankings 2027", title="5 in the *world top 50*", size=80, cards=[
       dict(v="#13", h="Peking University", d="Beijing", hi=True), dict(v="#14", h="Tsinghua University", d="Beijing"),
       dict(v="#26", h="Fudan University", d="Shanghai"), dict(v="#36", h="Shanghai Jiao Tong", d="Shanghai"),
       dict(v="#47", h="Zhejiang University", d="Hangzhou", wide=True)],
       src="Source: QS World University Rankings 2027 (released Jun 18, 2026)"),
  dict(k="panel", label="Chinese Government Scholarship (CSC)", title="The big one: *CSC*", size=80, cards=[
       dict(h="Covers", d="Tuition, on-campus housing, medical insurance and a monthly stipend.", hi=True),
       dict(v="RMB 2,500", h="Bachelor's / month", d="≈ $373"), dict(v="RMB 3,000", h="Master's / month", d="≈ $447"),
       dict(v="RMB 3,500", h="PhD / month", d="≈ $522"), dict(h="Apply", d="Via campuschina.org. Windows vary by country, often Nov to Apr.", wide=True)],
       src=f"Source: StudyChina (China Daily), Aug 2025; Chinese Consulate Melbourne. {FX}"),
  dict(k="panel", label="Fully funded master's", title="The *elite* programs", size=80, cards=[
       dict(k="Tsinghua", h="Schwarzman Scholars", d="1-year master's in global affairs. Tuition, housing, living costs, flights and a laptop.", hi=True),
       dict(k="Peking University", h="Yenching Academy", d="Master's in China studies. Tuition, housing, stipend and airfare."),
       dict(k="Any level", h="Int'l Chinese Language Teachers Scholarship", d="4 weeks up to a PhD. Tuition, housing, allowance, insurance."),
       dict(k="Also", h="University & city scholarships", d="Many universities run their own. Check each school's site.")],
       src="Sources: Al-Fanar Media (Jun 2026); Yenching Academy admissions; BLCU (Mar 2026)"),
  dict(k="panel", label="Deadlines", title="Mark your *calendar*", size=80, timeline=[
       dict(w="Nov 30, 2026", h="Yenching Academy", d="International deadline, 9:00 Beijing time. Still open.", hi=True),
       dict(w="Nov to Apr", h="CSC scholarship", d="Opens late in the year; deadlines vary by country."),
       dict(w="Apr · May · Sep · Oct", h="Chinese Language Teachers Scholarship", d="Several rounds a year (2026: Apr 15, May 15, Sep 15, Oct 31)."),
       dict(w="September", h="Schwarzman Scholars", d="2026 round closed Sep 9 for Aug 2027 entry.")],
       src="Sources: official program pages. Check the official site for this cycle before applying"),
  dict(k="cta", art="campus", label="Wealth Bridge Network", title="Your degree could\nbe *paid for.*",
       sub="Save this and send it to someone who should apply.", pills=["SAVE THIS", "FOLLOW FOR MORE"]),
 ]),
# 54 (Mark's story) moved to content/marks_story.py (doodle style, Nov 22 2026)
]
