# Readout: Why mid-size customers abandon export in Ledgerline

*Fictional example. Thirteen slides for a 30-minute slot with the product trio (PM, designer, engineering lead) plus two engineers. Each heading is one slide.*

## 1. Title

Why mid-size customers abandon export · 14 October 2026 · Priya Nair · Decision owner: Sam Okafor

## 2. Why we did this

- **The decision:** Sam decides by 30 October whether Q1 goes to a redesigned export dialog or to the import step.
- **The business need:** "Weekly active sharers" is our H2 goal. 212 export tickets in Q3 [Support].
- **What we already knew:** Export is the second most-used admin feature [2025 survey]. No research on why it fails. Field reps: "customers hate the export" [indirect].
- **The question:** Why do mid-size customers abandon exports in their first 90 days?
- **Where it sits:** Job: get the month's numbers into finance. Journey: Share a report, step 3 of 4. Persona: Report builder.

## 3. What we did

Eight 45-minute remote sessions, 6 to 10 October. Report builders at mid-size customers under 90 days in, recruited from our own users by CS. Short interview about their last export, then a live export task on their own account.

## 4. Top findings

1. Most abandoned exports fail at import, not export · **Strong**
2. Finance-team participants could not complete any export · **Weak, but serious**
3. The workaround is email · **Strong**
4. Nobody understood "Include hidden fields" · **Moderate**
5. Filename confusion is real but minor · **Weak**

## 5. Finding 1: Most abandoned exports fail at import, not export · Strong

- 5 of 8 stopped when the preview showed empty columns. In all five, those columns were never mapped at import.
- Receipts: P1 line 13, P3 line 41, P4 08:15, P6 12:40, P8 06:02.
- P3: "I thought export was broken, but it's the import that never had them."
- **What cuts against it:** P2 and P5 exported fine; both had CS run their import.
- **What it means:** A new dialog wouldn't have helped five of the six who abandoned.

## 6. Finding 2: Finance-team participants could not complete any export · Weak, but serious

- 2 of 8 (P5, P7), both reconciling against an external finance system, need a fixed column order the export can't produce. Both gave up.
- Receipts: P5 18:05, P7 22:10.
- P7: "If the order's wrong the reconciliation tool rejects the whole file."
- **What cuts against it:** The other six had no column-order need.
- **What it means:** A small group is fully blocked. Size it before deciding.

## 7. Finding 3: The workaround is email · Strong

- 6 of 8 had sent a raw file to a colleague to fix by hand.
- Receipts: P1 line 15, P3 line 48, P4 11:00, P6 14:20, P7 25:00, P8 07:30.
- P1: "Sent the raw file to a colleague and asked them to fix it."
- **What cuts against it:** P2, P5 reported no workaround.
- **What it means:** Analytics shows a completed export; the real work happens in email. Tickets understate the problem.

## 8. Finding 4: Nobody understood "Include hidden fields" · Moderate

- 7 of 8 skipped it or guessed. P4: "Hidden from who?"
- Receipts: P1 line 30, P2 line 22, P3 line 55, P4 09:30, P5 16:00, P6 15:10, P7 27:40.
- **What cuts against it:** P8 used it correctly after reading the help article.
- **What it means:** A cheap labelling fix inside the dialog. Not why people abandon.

## 9. Other findings

- Two participants expected export to schedule itself monthly · **Weak** · unexpected
- Three of eight re-selected the same columns every time; the dialog doesn't remember the last choice · **Weak**

## 10. Summary

We asked why people abandon export. Mostly they don't fail at export; they fail at import and only notice at export. A separate, smaller group is fully blocked by column order. Confidence is moderate overall: eight sessions, one segment over-represented. The evidence points to fixing import before touching the dialog.

## 11. Recommendations

| Action | Owner | Rests on | Moves |
| --- | --- | --- | --- |
| Column-mapping check at import that warns when saved reports use unmapped columns | Data Pipeline (Lena) | Finding 1 | Weekly active sharers; export tickets |
| Defer the dialog rebuild until the import check ships and is measured | Sam | Findings 1, 3 | Q1 capacity |
| Count finance-team customers who need fixed column order | Support (Marco) with CS | Finding 2 | Whether column order is Q1 or later |
| Relabel "Include hidden fields" with a plain description | Design (Aisha) | Finding 4 | Export completion |

## 12. Next steps

- Sam decides by 30 October.
- Marco returns the finance-team count by 24 October.
- If the import check is approved: three follow-up sessions with finance-team customers in November.
- Open: does the import gap also affect scheduled reports? Backlog.

## 13. Limits

- Eight participants, all CS-onboarded; self-serve customers may differ.
- Two finance-team users, so Finding 2 could be bigger or smaller than it looks.
- We didn't pull the export funnel before recruiting, so we can't say what share of customers hit Finding 1 (skipped during planning, logged 3 October).

*Magpie drafted this slide and the researcher chose to keep it in. It is in the report regardless.*

## 14. Appendix

- Participant profile
- Full findings with coding frame and all quotes
- Guide and task script
- Independent review: 11 points, 8 accepted, 3 answered
- Links: study record, report, recordings (access-controlled)
