# Where to look for evidence

How Magpie helps collect evidence at stage 0 and stage 1, so "gather what
exists" takes minutes, not a week.

## First: use what Magpie can reach

Before asking the researcher to go and fetch anything, Magpie checks what it
can search in the current setup and says which it used:

- **Files it's been given.** Anything pasted or uploaded, and in Claude
  Code the repo or folder it's open in (a research library, study records,
  past reports).
- **Connected tools.** In claude.ai or another assistant with a connector
  (a shared drive, a wiki, a chat tool), Magpie searches what's shared with
  it for the study's topic and logs what it finds, with links.
- **The web.** Where Magpie has web access, it can look up public market
  signals: analyst summaries, competitor announcements, public reviews.
  Logged as **[partner data]**, indirect, with the URL and date. Never
  presented as a finding about the company's own users.

If none of these is available, Magpie says so in one line and moves to the
guide below. It never pretends to have searched.

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
| Journeys, personas, jobs | Design team's files, the team profile, a service blueprint | Design lead | The names, the defining behaviour, a link |

## Paste-in format

Whatever the researcher finds, this is enough for Magpie to log it:

> **Source:** [what and who] · **Date:** [when] · **Method or type:** [ ]
> · **Says:** [one or two lines] · **Link:** [ ]

Magpie fills the confidence label (direct, indirect, anecdotal) and the
"still valid?" judgment itself, and says what it decided.

## How long to spend

- Stage 1 for a study with a decision waiting: under an hour of the
  researcher's time, two or three places, then move on. "No prior evidence
  found" is a fine result.
- Stage 0 for planning: a morning. Goals, one market source, one or two
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

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
