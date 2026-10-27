# Research report: Why mid-size customers abandon export in Ledgerline

**Author:** Priya Nair · **Date:** 14 October 2026 · **Decision owner:** Sam Okafor (PM, Reporting) ·
**Study record:** [link to study record]

*Fictional example. Ledgerline, its customers and participants are made up to show what a Magpie report looks like when filled in.*

## Contents

- [Summary](#summary)
- [Why we did this](#why-we-did-this)
- [What we did](#what-we-did)
- [Top findings](#top-findings)
- [Findings in detail](#findings-in-detail)
- [Other findings](#other-findings)
- [Recommendations](#recommendations)
- [Next steps](#next-steps)
- [Limits](#limits)
- [Glossary](#glossary)
- [Appendix](#appendix)

## Summary

Reporting has to decide by 30 October whether to rebuild the export dialog or fix the import step that feeds it. The evidence supports fixing import first. Six of eight participants abandoned an export at least once in the session, and in five of those six the cause was columns that were never mapped at import, not the dialog itself. Two participants from finance teams could not complete any export and gave up. Confidence is moderate: eight sessions, one segment over-represented. The main recommendation is to add a column-mapping check at import, owned by the Data Pipeline team, with the export dialog change deferred until that ships.

## Why we did this

- **The decision:** Sam Okafor will decide by 30 October whether Q1 engineering time goes to a redesigned export dialog or to the import step, choosing between those two options or neither.
- **The business need:** "Weekly active sharers" is the Reporting team's goal metric for H2 [team profile]. Support logged 212 export-related tickets in Q3 [partner data, Support, 2 October]. A rebuilt dialog costs roughly one engineer-quarter [assumption, from Sam].
- **What we already knew:** A 2025 survey found export was the second most-used feature among admins [their data, evidence log E2]. No prior research on why exports fail. Field reps report "customers hate the export" [partner data, indirect].
- **The questions:** Primary: why do mid-size customers abandon exports in the first 90 days? Secondary: where in the flow does abandonment happen, and what do people do instead?
- **Where it sits:** Job: get this month's numbers into the finance system. Journey: "Share a report", step 3 of 4. Persona: Report builder (builds and shares reports weekly). Upstream: import and column mapping; downstream: the finance team's reconciliation.

## What we did

Eight remote sessions of 45 minutes between 6 and 10 October, each a short interview about the last export the participant attempted followed by a usability task on their own account (export last month's revenue report to CSV). Participants were report builders at mid-size customers (50 to 500 seats) who had used Ledgerline for under 90 days, recruited from our own user base by the CS team. We chose sessions over a survey because the question was why, and over analytics alone because the funnel shows where people stop but not what they were trying to do. Plan and guide are in the appendix.

## Top findings

1. **Most abandoned exports fail at import, not export.** Five of eight participants hit missing columns that were never mapped when the data was imported. · Strong
2. **Finance-team participants could not complete any export.** Two of eight, both reconciling against an external system, gave up entirely. · Weak (two participants, one segment), but serious
3. **The workaround is email.** Six of eight had sent a raw file to a colleague to fix by hand at least once. · Strong
4. **Nobody understood the "Include hidden fields" option.** Seven of eight either ignored it or guessed. · Moderate
5. **Filename confusion is real but minor.** Three of eight mentioned the default filename; none abandoned because of it. · Weak

## Findings in detail

### Finding 1: Most abandoned exports fail at import, not export

**Strength:** Strong, because five of eight participants hit it independently and the cause is visible in their accounts.
**Answers:** the primary question.

Five of eight participants (P1, P3, P4, P6, P8) stopped their export when the preview showed empty columns. In every case the account's import mapping had skipped those columns (checked in the admin view during the session). P3, line 41: "The columns just aren't there. I thought export was broken, but it's the import that never had them." P6, 12:40: "I've done this four times and every time I assume it's me."

[Image: export preview with three empty columns, P4's session, 08:15. Caption: the moment P4 stopped. The empty columns are the ones unmapped at import.]

**What cuts against it:** P2 and P5 exported successfully with all columns; both had been onboarded by a CS manager who ran the import for them. P7's export failed for a different reason (Finding 2).

**What it means:** Rebuilding the dialog would not have helped five of the six people who abandoned. The fix is earlier in the journey, which also means it belongs to a different team.

**More:** appendix B, coding frame rows 1 to 14; clips P3 41, P6 12:40, P8 06:02.

### Finding 2: Finance-team participants could not complete any export

**Strength:** Weak on count (two of eight), labelled a serious case because the task was fully blocked.
**Answers:** the secondary question on where abandonment happens.

P5 and P7, both reconciling Ledgerline against an external finance system, needed a fixed column order that the export cannot produce. Both tried twice and gave up. P7, 22:10: "If the order's wrong the reconciliation tool rejects the whole file, so there's no point."

**What cuts against it:** The other six participants had no column-order requirement. This may be a segment problem rather than a general one.

**What it means:** A small, specific group is fully blocked. Worth sizing before deciding: Support can tell us how many finance-team customers have raised this.

**More:** appendix B rows 15 to 19.

### Finding 3: The workaround is email

**Strength:** Strong; six of eight described it unprompted.

P1, P3, P4, P6, P7 and P8 had sent a raw export to a colleague to fix by hand. P1, line 15: "Sent the raw file to a colleague and asked them to fix it." This is the behaviour that hides the problem from analytics: the export funnel shows a completion, then the real work happens in email.

**What cuts against it:** P2 and P5 did not report a workaround; P2 exports rarely.

**What it means:** The 212 support tickets understate the problem; most people route around it without telling us.

### Finding 4: Nobody understood "Include hidden fields"

**Strength:** Moderate; seven of eight, but we didn't test alternatives.

Seven of eight either skipped the checkbox or ticked it and then untick it when the preview changed. Nobody could say what a hidden field was. P4, 09:30: "Hidden from who?"

**What cuts against it:** P8 used it correctly, having read the help article.

**What it means:** A labelling fix, cheap, inside the dialog. Not the reason for abandonment, but a free improvement.

### Finding 5: Filename confusion is real but minor

**Strength:** Weak.

Three of eight mentioned renaming the default file. Nobody stopped because of it. Logged so it isn't raised again as a priority.

## Other findings

- Two participants (P2, P6) expected export to schedule itself monthly. Unexpected; worth a line in the roadmap discussion. Weak.
- Three of eight (P1, P5, P7) re-selected the same columns every time because the dialog doesn't remember the last choice. Not why they abandoned. Weak.

## Recommendations

| # | Action | Owner | Rests on | Moves | Confidence |
| -- | ------------------------------ | -------------- | ---------- | ---------------- | -------- |
| 1 | Add a column-mapping check at import that warns when columns used by saved reports are unmapped | Data Pipeline (Lena Fischer) | Finding 1 | Weekly active sharers; export support tickets | High |
| 2 | Defer the export dialog rebuild until recommendation 1 ships and is measured | Sam Okafor | Findings 1, 3 | Q1 engineering capacity | High |
| 3 | Size the finance-team blocker: count customers who need fixed column order | Support (Marco Ruiz) with CS | Finding 2 | Decides whether a column-order option is Q1 or later | Medium |
| 4 | Relabel "Include hidden fields" with a plain description and an example | Design (Aisha Bello) | Finding 4 | Export completion rate | Medium |

Recommendation 2 is the uncomfortable one: the study was commissioned to inform a dialog rebuild. The evidence says the rebuild would miss the cause. If the rebuild goes ahead anyway, Finding 1 should be in the brief so the new dialog at least shows why columns are empty.

## Next steps

- Sam decides by 30 October; this report and the readout deck are the inputs.
- Marco returns the finance-team count by 24 October.
- If recommendation 1 is approved, Priya runs three follow-up sessions with finance-team customers in November to test the column-order need.
- Open question: does the same import gap affect scheduled reports? Nothing yet; add to the research backlog.

## Limits

- Eight participants, all from accounts onboarded by CS; self-serve customers may differ.
- Two of eight were finance-team users, so Finding 2 could be bigger or smaller than it looks.
- Sessions were on participants' own accounts, so we saw their real data but could not control for how recently they imported.
- Challenge skipped during planning: we did not pull the export funnel from analytics before recruiting, so we can't say what share of all customers hit Finding 1. Logged as a risk on 3 October.

## Glossary

- **Column mapping:** matching the columns in a customer's uploaded file to Ledgerline's fields at import.
- **Report builder:** the persona who builds and shares reports weekly; defined in the team profile.

## Appendix

- A. Participant profile (eight rows: segment, seat count, days since signup, role)
- B. Full findings with coding frame and all supporting quotes
- C. Research plan, interview guide and usability task script
- D. Partner data used: Support ticket export (2 October), field rep summary (29 September), 2025 admin survey (E2)
- E. Consent, recording, storage and retention: standard notice v3; recordings deleted 14 January 2027
- F. Independent review: 11 points raised, 8 accepted, 3 answered (see change log)
- G. Library entries: three, one per strong finding
- H. Recordings and clips (access-controlled)
