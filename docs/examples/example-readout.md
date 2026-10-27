# Readout: Why mid-size customers abandon export in Ledgerline

**Fictional example.** 15 slides for a 30-minute slot with the product trio (PM, designer, engineering lead) and two engineers. Each heading is one slide, and each slide title is the slide's message.

## 1. Fix import before rebuilding the export dialog

Why mid-size customers abandon export · 14 October 2026 · Priya Nair, UX Research · Decision owner: Sam Okafor, PM Reporting

## 2. We studied export to decide where Q1 engineering time goes

- **The decision:** Sam decides by 30 October whether Q1 goes to a redesigned export dialog or to the import step.
- **The business need:** "Weekly active sharers" is our H2 goal, and Support logged 212 export tickets in Q3 [Support].
- **What we already knew:** Export is the second most-used admin feature [2025 survey], and nobody had studied why it fails.
- **The question:** Why do mid-size customers abandon exports in their first 90 days?
- **Where it sits:** Export, which report builders use weekly: step 3 of 4 of "Share a report", for the Report builder persona.

## 3. We watched 8 report builders try a real export on their own accounts

We ran 8 remote sessions of 45 minutes, 6 to 10 October 2026. Participants were report builders at mid-size customers who had signed up under 90 days ago, recruited by CS. Each session was a short interview about their last export, then a live export task on their own account.

## 4. Four findings the decision rests on, ranked

1. For 5 of 8, export failed because import never mapped the columns · **Strong**
2. Both finance-team participants couldn't get a file their finance system accepts · **Weak · serious case**
3. 6 of 8 work around export by emailing the file to a colleague · **Strong**
4. 7 of 8 couldn't say what "Include hidden fields" does · **Moderate**

## 5. For 5 of 8, export failed because import never mapped the columns

**Finding 1 of 4 · Strong**

- 5 of 8 stopped when the preview showed empty columns, and in all 5 accounts import had skipped those columns.
- Receipts: P1 line 13, P3 line 41, P4 08:15, P6 12:40, P8 06:02.
- **What cuts against it:** P2 and P5 exported every column; both had CS run their import.
- **What it means:** A new dialog wouldn't have helped 5 of the 6 who abandoned.

> "I thought export was broken, but it's the import that never had them." — P3, operations analyst, 120 seats

## 6. Both finance-team participants couldn't get a file their finance system accepts

**Finding 2 of 4 · Weak · serious case**

- P5 and P7 reconcile against an external system that needs a fixed column order export can't produce.
- Receipts: P5 18:05, P7 22:10.
- **What cuts against it:** The other 6 had no column-order need.
- **What it means:** A small group is fully blocked, so size it before deciding.

> "If the order's wrong the reconciliation tool rejects the whole file." — P7, finance controller, 450 seats

## 7. 6 of 8 work around export by emailing the file to a colleague

**Finding 3 of 4 · Strong**

- 6 of 8 had sent a raw file to a colleague to fix by hand, without being asked.
- Receipts: P1 line 15, P3 line 48, P4 11:00, P6 14:20, P7 25:00, P8 07:30.
- **What cuts against it:** P2 and P5 reported no workaround.
- **What it means:** The funnel counts these exports as complete, so tickets understate the problem.

> "Sent the raw file to [name] and asked them to fix it." — P1, operations manager, 80 seats

## 8. 7 of 8 couldn't say what "Include hidden fields" does

**Finding 4 of 4 · Moderate**

- 7 of 8 skipped the checkbox or guessed what it did.
- Receipts: P1 line 30, P2 line 22, P3 line 55, P4 09:30, P5 16:00, P6 15:10, P7 27:40.
- **What cuts against it:** P8 used it correctly after reading the help article.
- **What it means:** It's a cheap labelling fix, and not why people abandon.

> "Hidden from who?" — P4, reporting lead, 310 seats

## 9. Three more findings, kept so nothing is lost

- 2 of 8 expected export to run on a monthly schedule by itself · **Weak** · unexpected
- 3 of 8 re-selected the same columns every time, because the dialog doesn't remember them · **Weak**
- 3 of 8 renamed the default filename, and nobody stopped because of it · **Weak**

Every finding that met the evidence bar is in this deck. The full table is in the appendix.

## 10. Most exports fail at import, so fix import first

- We asked why people abandon export.
- Mostly they fail at import and only notice it at export.
- A smaller group, finance teams, is fully blocked by column order.
- Confidence is moderate overall: 8 sessions, all recruited through CS.

## 11. Four actions, each with an owner

| Action | Owner | Rests on | Moves |
| --- | --- | --- | --- |
| 1. Warn at import when saved reports use unmapped columns | Data Pipeline (Lena) | Finding 1 | Weekly active sharers; export tickets |
| 2. Defer the dialog rebuild until the import check ships and is measured | Sam | Findings 1 and 3 | Q1 capacity |
| 3. Count finance-team customers who need a fixed column order | Support (Marco), with CS | Finding 2 | Whether column order goes in Q1 or later |
| 4. Relabel "Include hidden fields" with a plain description | Design (Aisha) | Finding 4 | Export completion |

Action 2 is the uncomfortable one: the study was commissioned for a dialog rebuild, and the evidence says the rebuild would miss the cause.

## 12. Sam decides on 30 October, after Support sizes finding 2

1. Marco returns the finance-team count by 24 October.
2. Sam decides by 30 October, with this deck and the report as the inputs.
3. If the import check is approved, Priya runs 3 follow-up sessions with finance-team customers in November.
4. Whether the import gap also affects scheduled reports is an open question for the backlog.

## 13. What this study can't tell us

- All 8 participants were recruited through CS, so self-serve customers may differ.
- Only 2 were from finance teams, so finding 2 could be bigger or smaller than it looks.
- We didn't pull the export funnel before recruiting, so we can't say what share of customers hit finding 1.

Magpie drafted this slide and the researcher chose to keep it in. The limits are in the report either way.

## 14. Appendix: for the deeper dive

- Participant profile, with role, seats and team for P1 to P8
- Full findings with the coding frame and every quote
- The interview guide and task script
- Independent review: 11 points, 8 accepted, 3 answered
- Links to the study record, the report and the recordings (access-controlled)

## 15. Appendix: how AI was used

- **Assistant:** Magpie, running in Claude Code.
- **What it drafted:** the plan, the guide and task script, the themes and findings, the report and this deck.
- **What the researcher did:** ran all 8 sessions, named her own patterns first, decided on each theme, wrote the recommendations, and reviewed the findings (12 October) and this deck (14 October).
- **Checks:** quotes and counts checked by code; a separate AI reviewer raised 11 points, and 8 changed the findings. The reviewer is a model too and can be wrong.
- **Other AI tools:** the video tool transcribed the sessions, and Priya corrected the transcripts.
