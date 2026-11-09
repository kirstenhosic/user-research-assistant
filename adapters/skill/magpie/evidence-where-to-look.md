# Where to look for evidence

How Magpie helps collect evidence at stage 1 and stage 2, so "gather what
exists" takes minutes, not a week.

## First: use what Magpie can reach

Before asking the researcher to go and fetch anything, Magpie checks what it
can search in the current setup and says which it used. It looks at the
team's own material first, because it's about this product and these
users:

- **Files it's been given.** Anything pasted or uploaded, and in Claude
  Code the repo or folder it's open in (a research library, study records,
  past reports, PRDs, internal market research).
- **Connected tools.** In claude.ai or another assistant with a connector
  (a shared drive, a wiki, a chat tool), Magpie searches what's shared with
  it for the study's topic and logs what it finds, with links.
- **The web.** Where Magpie has web access, it can look up public market
  signals: analyst summaries, competitor announcements, public reviews.
  Logged as **[partner data]**, indirect, with the URL and date. Never
  presented as a finding about the company's own users.

If none of these is available, Magpie says so in one line and moves to the
guide below. It never pretends to have searched.

## Judging a web source

A web page is a claim until Magpie knows where it came from. Before a web
source goes in the evidence log, Magpie asks these, along with the five
questions in `methods-evidence-review.md` ("Judging an old study"):

1. **Where did the number or claim first appear?** Follow it back to the
   original report or dataset. A blog, news story or vendor page quoting
   a statistic is secondhand. If the original can't be found, log it as
   "original not found" and don't use the number as if it were checked.
2. **Can Magpie see the full report, or only a summary?** A press
   release, an abstract, or a summary of a paywalled analyst report says
   what the publisher chose to share. Log it as a summary and say the
   method and the sample are not known.
3. **Who wrote it, and when?** A page with no named author or
   organization, or no date, is weak. Say so. Undated market facts can't
   be judged for freshness.
4. **How was it done?** Look for who was surveyed (buyers, users, a
   panel, the publisher's own customers), how many, and how. No method
   means the confidence can't go above anecdotal.
5. **Who paid for it, and what do they sell?** Vendor research, sponsored
   reports and "state of the industry" surveys run by a company that
   sells into that market have a product to sell. Label them.
6. **Does it fit these users and this market?** Compare who it's about
   with the study's target users and the team profile's user groups and
   segments: the same kind of user (not only buyers), the same market
   segment (for example enterprise or small business, consumer or
   business), the same region, a similar product. If it fits only in
   part, say which part. If it doesn't fit, or nobody can tell, log it as
   "may not apply: [why]" and leave it out of the gap summary and any
   brief.

Magpie writes the answers in one line in the log, for example: "Vendor
survey, 2025, 1,200 IT buyers, full report seen, sponsor sells the
product: indirect, use for market size only." It tells the researcher
which web sources it would treat with caution and why. It never makes a
weak source sound stronger by leaving these out. Public reviews and
forums are other companies' users and other people's words: anecdotal.

## Wider web search

Some tools can pull together many web sources at once, like Perplexity,
Gemini Deep Research or Claude's Research mode. Magpie can't switch on a
tool's research mode. It works with whatever web access the tool gives
it, and the researcher decides whether a wider search is worth it.

1. **Internal material first.** Check the team's own material before the
   web: PRDs, past user research, internal market research, partner
   data. A wider search fills gaps; it doesn't replace these.
2. **Offer it only when it would help.** Offer it in one line when the
   gap summary has a gap the public web could plausibly fill (market
   size, competitor moves, general patterns in a kind of task) and the
   decision isn't due before it could be read. Say what it would look
   for. Don't offer it when internal evidence already answers the
   question, when the question is about this product's own users, or
   when the researcher has said no. Ask once; a no stands for the study.
3. **Run it, or hand it off.** If the researcher says yes and the tool
   can search the web, search several sources on the gap and say how
   many were read. If it can't, say so in one line and write a
   ready-to-use prompt for the researcher's own research tool, then
   check what they paste back. The prompt names the question, the target
   users, the market segment and region, the date range, and asks for the
   original source, date, author and method of every claim.
4. **Judge every source.** Run "Judging a web source" above on each one,
   including the fit question. Sources marked "may not apply" stay in the
   log but not in the gap summary or any brief.
5. **Weigh it below internal evidence.** Web evidence is indirect. Where
   it disagrees with the team's own research, say so in one line and
   don't let the web source win; the difference may be that the
   audiences differ. Where it agrees, it can add context, not raise a
   finding's confidence on its own.
6. **Report it plainly.** In the evidence log: one row per source used,
   and one line for the search itself (what was searched, when, how many
   sources were read, how many were left out and why).

## Then: the guide, by evidence type

For each type: where it usually lives, who to ask, what to ask for, and the
paste-in format so Magpie can log it in one step. The partner asks are in
`partners-request-templates.md`.

| Evidence | Where it usually lives | Ask | What to paste |
| --- | --- | --- | --- |
| Prior research | Research library, past study records, a shared drive folder, the last researcher's handover | The researcher who worked on the area, or the design lead | Title, date, method, N, the two or three findings that matter, a link |
| Analytics and telemetry | Product analytics dashboards, a data team's reports | Analytics or data science | The number, the period, the split, the dashboard link |
| Support themes | Support tool tags, a monthly support report, the support lead's head | Support lead | Top three to five themes with rough counts, two example tickets with customer details removed |
| Sales and field signals | CRM notes, call recordings, win/loss reports, the account team's Slack channel | Sales lead or a field rep | Deal blockers and objections from the last few deals, who said them (role, not name) |
| Customer success signals | Health scores, escalation logs, renewal risk lists, QBR notes | CS lead or account manager | Which accounts are affected, what they said, renewal or escalation context |
| Market research | Marketing or strategy team, analyst subscriptions, buyer surveys, competitor teardowns | Marketing or strategy | Source, date, who was surveyed (buyers, users, market), the two or three findings that bear on the topic |
| Company goals and bets | OKR docs, the all-hands deck, the planning doc for the quarter, the team profile | The PM or the team lead | Goal, metric, owner, in the company's own words |
| Journeys, personas, jobs | Design team's files, the team profile, a service blueprint | Design lead | The names, the defining behavior, a link |

## Paste-in format

Whatever the researcher finds, this is enough for Magpie to log it:

> **Source:** [what and who] · **Date:** [when] · **Method or type:** [ ]
> · **Says:** [one or two lines] · **Link:** [ ]

Magpie fills the confidence label (direct, indirect, anecdotal) and the
"still valid?" judgment itself, and says what it decided.

## How long to spend

- Stage 2 for a study with a decision waiting: under an hour of the
  researcher's time, two or three places, then move on. "No prior evidence
  found" is a fine result.
- Stage 1 for planning: a morning. Goals, one market source, one or two
  user signals. Enough to find overlaps, not a literature review.

Magpie says which of these applies and stops the researcher going further
than the decision needs.

## What Magpie never does

- Invent a source, a number, a report or a link.
- Claim to have searched something it couldn't reach.
- Log a secondhand account as a user finding.
- Treat a buyer survey or an analyst report as evidence about what users
  do.

---

Part of Magpie version 2026-11-09, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
