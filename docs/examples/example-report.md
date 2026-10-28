# Research report: Why mid-size customers abandon export in Ledgerline

**Author:** Priya Nair · **Date:** 14 October 2026 · **For:** the Reporting team ·
**Study record:** [link to study record]

**Fictional example.** Ledgerline, its customers and its participants are made up to show what a Magpie report looks like when filled in.

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

Reporting has to decide by 30 October whether to rebuild the export dialog or fix the import step that feeds it. The evidence supports fixing import first. 6 of 8 participants abandoned an export during the session, and for 5 of those 6 the cause was columns that were never mapped at import, not the dialog itself. Both participants from finance teams could not get a file their finance system would accept. Confidence is moderate: 8 sessions, and all participants were recruited through Customer Success (CS). The main recommendation is a check at import that warns about skipped columns, with the dialog rebuild held until that check ships.

## Why we did this

- **The product:** Ledgerline is accounting software for mid-size businesses. This study covers export, where report builders send report data to other tools; report builders use it weekly, and the finance team receives what they send.
- **The decision:** By 30 October, the Reporting team will decide whether Q1 engineering time goes to a redesigned export dialog, to the import step, or to neither.
- **The business need:** "Weekly active sharers" is the Reporting team's goal metric for H2 [team profile]. Support logged 212 export-related tickets in Q3 [partner data, Support, 2 October 2026]. A rebuilt dialog would cost about one engineer-quarter [assumption, from the Reporting team].
- **What we already knew:** A 2025 survey found export was the second most-used feature among admins [their data, evidence log E2]. There was no earlier research on why exports fail. Field reps report that "customers hate the export" [partner data, indirect].
- **The questions:** The primary question was why mid-size customers abandon exports in their first 90 days. The secondary questions were where in the flow they abandon, and what they do instead.
- **Where it sits:** The job is getting this month's numbers into the finance system, in step 3 of 4 of the "Share a report" journey, for the Report builder persona.

## What we did

We ran 8 remote sessions of 45 minutes between 6 and 10 October 2026. Each was a short interview about the participant's last export, then a usability task on their own account: export last month's revenue report to CSV. Participants were report builders at mid-size customers (50 to 500 seats) who had used Ledgerline for under 90 days, recruited from our own customers by the CS team. We chose sessions over a survey because the question was why, and over analytics alone because the funnel shows where people stop but not what they were trying to do. The plan and guide are in appendix C.

## Top findings

1. **For 5 of 8, export failed because import never mapped the columns.** The dialog wasn't the cause. · Strong
2. **Both finance-team participants could not get a file their finance system accepts.** Their reconciliation tools need a column order export can't produce. · Weak · serious case
3. **6 of 8 work around export by emailing the file to a colleague.** The export funnel counts these as completed. · Strong
4. **7 of 8 couldn't say what "Include hidden fields" does.** It's a labelling problem, not a reason to abandon. · Moderate

## Findings in detail

### Finding 1: For 5 of 8, export failed because import never mapped the columns

**Strength:** Strong, because 5 participants hit it on their own and the cause was checked in their account during the session.
**Answers:** the primary question.

P1, P3, P4, P6 and P8 stopped their export when the preview showed empty columns. In all 5 accounts, the import mapping had skipped those columns; we checked in the admin view during the session.

> "The columns just aren't there. I thought export was broken, but it's the import that never had them." — P3, operations analyst, 120 seats

> "I've done this four times and every time I assume it's me." — P6, account manager, 95 seats

[Image: the export preview with three empty columns, from P4's session at 08:15. Caption: the moment P4 stopped. The empty columns are the ones left unmapped at import.]

**What cuts against it:** P2 and P5 exported with every column present. Both had a CS manager run their import for them. P7's export failed for a different reason (finding 2).

**What it means:** A rebuilt dialog would not have helped 5 of the 6 people who abandoned. The fix sits earlier in the journey, so it belongs to a different team.

**More:** appendix B, coding frame rows 1 to 14; clips P3 line 41, P6 12:40, P8 06:02.

### Finding 2: Both finance-team participants could not get a file their finance system accepts

**Strength:** Weak, because it rests on 2 participants from one segment. It's on this list because their task was fully blocked.
**Answers:** the secondary question on where people abandon.

P5 and P7 both reconcile Ledgerline against an external finance system, which needs a fixed column order that export cannot produce. P7 tried twice and gave up. P5 finished the export, but their reconciliation tool rejected the file.

> "If the order's wrong the reconciliation tool rejects the whole file, so there's no point." — P7, finance controller, 450 seats

**What cuts against it:** The other 6 participants had no column-order need, so this may be a problem for one segment, not for everyone.

**What it means:** A small, specific group is fully blocked. Support can count how many finance-team customers have raised this, which sizes it before the decision.

**More:** appendix B, rows 15 to 19.

### Finding 3: 6 of 8 work around export by emailing the file to a colleague

**Strength:** Strong, because 6 participants described it without being asked.

P1, P3, P4, P6, P7 and P8 had each sent a raw export to a colleague to fix by hand. This is what hides the problem from analytics: the funnel records a completed export, and the real work then happens in email.

> "Sent the raw file to [name] and asked them to fix it." — P1, operations manager, 80 seats

**What cuts against it:** P2 and P5 reported no workaround. P2 rarely exports.

**What it means:** The 212 support tickets understate the problem, because most people route around it without telling us.

### Finding 4: 7 of 8 couldn't say what "Include hidden fields" does

**Strength:** Moderate, because 7 of 8 is a clear pattern, but we didn't test other labels.

Everyone except P8 either skipped the checkbox, or ticked it and then unticked it when the preview changed. None of the 7 could say what a hidden field was.

> "Hidden from who?" — P4, reporting lead, 310 seats

**What cuts against it:** P8 used the option correctly after reading the help article.

**What it means:** This is a cheap labelling fix inside the dialog. It isn't why people abandon, but it costs little to fix.

## Other findings

- **Filename:** P1, P5 and P7 renamed the default file before sending it, and none of them stopped because of it. This is weak, and it's recorded so it isn't raised again as a priority.
- **Scheduled export:** P2 and P6 expected export to run on a monthly schedule by itself. This is weak and unexpected, and it's worth a line in the roadmap discussion.
- **Column choice:** P1, P5 and P7 re-selected the same columns every time because the dialog doesn't remember the last choice. This is weak and wasn't why anyone abandoned.

## Recommendations

| Action | Teams involved | Rests on | Moves | Confidence |
| --- | --- | --- | --- | --- |
| 1. Add a check at import that warns when columns used by saved reports are unmapped | Data Pipeline, Reporting | Finding 1 | Weekly active sharers; export tickets | Strong |
| 2. Hold the export dialog rebuild until recommendation 1 ships and is measured | Reporting | Findings 1 and 3 | Q1 engineering capacity | Strong |
| 3. Count the customers who need a fixed column order | Support, Customer Success | Finding 2 | Whether a column-order option goes in Q1 or later | Moderate |
| 4. Relabel "Include hidden fields" with a plain description and an example | Design | Finding 4 | Export completion rate | Moderate |

Who takes each action is for the teams to agree together; the second column only names the teams whose work it touches.

Recommendation 2 is the uncomfortable one, because the study was commissioned to inform a dialog rebuild and the evidence says the rebuild would miss the cause. If the rebuild goes ahead anyway, finding 1 should be in its brief, so the new dialog at least explains why columns are empty.

## Next steps

1. Support counts the finance-team customers by 24 October.
2. The Reporting team decides by 30 October, with this report and the readout deck as the inputs.
3. If recommendation 1 goes ahead, the researcher runs 3 follow-up sessions with finance-team customers in November to test the column-order need.
4. The open question is whether the same import gap affects scheduled reports. Nothing answers it yet, so it goes on the research backlog.

## Limits

- **Recruiting:** All 8 participants were recruited through CS, so they're customers CS already knows. Self-serve customers may differ.
- **Finance teams:** Only 2 of 8 were from finance teams, so finding 2 could be bigger or smaller than it looks.
- **Own accounts:** Sessions used participants' own accounts, so we saw their real data but couldn't control how recently they had imported.
- **Skipped challenge:** We didn't pull the export funnel from analytics before recruiting, so we can't say what share of all customers hit finding 1. This was logged as a risk on 3 October 2026.

## Glossary

- **Column mapping:** matching the columns in a customer's uploaded file to Ledgerline's fields at import.
- **Report builder:** the persona who builds and shares reports weekly, as defined in the team profile.

## Appendix

- [A. Participant profile](#a-participant-profile)
- B. Full findings with coding frame and all supporting quotes
- C. Research plan, interview guide and usability task script
- D. Partner data used: Support ticket export (2 October 2026), field rep summary (29 September 2026), 2025 admin survey (E2)
- E. Consent, recording, storage and retention: standard notice v3, which tells participants an AI assistant helps analyse the sessions; recordings deleted 14 January 2027
- F. Independent review: 11 points raised, 8 accepted, 3 answered (see the record's change log)
- [G. How AI was used](#g-how-ai-was-used)
- H. Library entries: three, one per strong finding
- I. Recordings and clips (access-controlled)

### A. Participant profile

| Code | Role | Seats | Days since signup | Team |
| --- | --- | --- | --- | --- |
| P1 | Operations manager | 80 | 41 | Operations |
| P2 | Office manager | 60 | 72 | Operations |
| P3 | Operations analyst | 120 | 28 | Operations |
| P4 | Reporting lead | 310 | 55 | Reporting |
| P5 | Finance analyst | 200 | 63 | Finance |
| P6 | Account manager | 95 | 19 | Sales |
| P7 | Finance controller | 450 | 84 | Finance |
| P8 | Data analyst | 150 | 37 | Reporting |

### G. How AI was used

- **Assistant:** Magpie, running in Claude Code.
- **What it drafted:** the research plan, the interview guide and task script, the candidate themes and findings, this report and the readout deck.
- **What the researcher did:** Priya framed the decision and the research questions, ran all 8 sessions, named her own patterns before seeing Magpie's themes, kept, changed or dropped each theme, and wrote the recommendations. She reviewed the findings on 12 October 2026 and this report on 14 October 2026.
- **Checks:** quotes and counts were checked by code against the transcripts. A separate AI reviewer saw only the transcripts and the draft findings, raised 11 points, and 8 changed the findings. The reviewer is a model too and can be wrong.
- **Other AI tools in the study:** the sessions were transcribed by the video tool's built-in transcription, and Priya corrected the transcripts against the recordings.
