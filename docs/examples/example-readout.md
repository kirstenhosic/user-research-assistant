# Readout: Why mid-size customers abandon export in Ledgerline

**Fictional example.** 16 slides for a 30-minute slot with the product trio (PM, designer, engineering lead) and two engineers. Each heading is one slide, and each slide title is the slide's message, on one line. The deck opens with the answer and a short summary drawn from the study's findings, then tells the story of how we know.

## 1. Export isn't the problem. Import is.

Why new customers give up on export, and what to do about it · 14 October 2026 · Priya Nair, UX Research · For the Reporting team

## 2. What we learned, in short

We set out to learn why new customers give up on export. The answer points earlier in the journey than we expected.

- **Import is where it breaks.** For 5 of the 6 people who gave up, import had quietly skipped columns. A new export screen wouldn't have helped them.
- **The problem is bigger than our numbers show.** 6 of 8 fix the file by emailing it to a colleague, so these exports count as successes.
- **Finance teams are fully blocked.** Only 2 people, but neither could get a file their finance system accepts.

So: fix import first, then decide whether the export screen still needs a rebuild.

## 3. The team is choosing where Q1 effort goes

- **Option A:** Rebuild the export screen.
- **Option B:** Fix the import step that feeds it.
- **Decision by:** 30 October, by the Reporting team.
- **Why it matters:** 212 export tickets last quarter, and more weekly sharing is the team's goal for the second half of the year.
- **What we asked:** Why do new customers give up on export in their first 90 days?
- **What we already knew:** Export is the second most-used admin feature (2025 survey). Field reps hear that "customers hate the export". Nobody had asked why it fails.

## 4. We watched 8 customers try a real export

8 customers, one at a time · 45 minutes each, by video call · under 90 days since they signed up · 6 to 10 October 2026.

Each person told us about the last export they tried, then exported last month's revenue report on their own account while we watched. They all build and share reports at companies with 50 to 500 Ledgerline seats, and our Customer Success team helped us find them.

## 5. We expected the export screen to be the problem

The study was set up to help plan a new export screen. Field reps said customers hate it. Watching people use it told a different story.

## 6. The trouble starts before export

The journey has four steps: import data, build a report, export the file, send to finance.

- **Step 1, import data:** 5 of 8 had columns that import skipped. Nobody noticed until the export came out with gaps.
- **Step 2, build a report:** no problems here.
- **Step 3, export the file:** 7 of 8 didn't understand the "Include hidden fields" checkbox.
- **Step 4, send to finance:** 2 of 8, both from finance teams, had the file rejected for its column order. 6 of 8 fixed the file by emailing it to a colleague.

## 7. 5 of 8 hit columns that import had skipped

**Finding 1 of 4 · Strong evidence · Heard from P1, P3, P4, P6, P8**

When the export preview showed empty columns, they stopped. In every case, import had skipped those columns weeks earlier.

> "I thought export was broken, but it's the import that never had them." — P3, operations analyst, 120 seats

- **Who didn't fit:** P2 and P5 had no gaps. Customer Success had set up their import for them.
- **What it means:** A new export screen wouldn't have helped 5 of the 6 people who gave up.

## 8. Finance teams can't use the file at all

**Finding 2 of 4 · Weak evidence · Serious: fully blocked · Heard from P5, P7**

Both people from finance teams need columns in a fixed order for their finance system. Export can't do that, so the file is rejected.

> "If the order's wrong the reconciliation tool rejects the whole file." — P7, finance controller, 450 seats

- **Who didn't fit:** The other 6 didn't need a fixed order. This may only affect finance teams.
- **What it means:** A small group is completely stuck. Support can count how many customers this affects.

## 9. 6 of 8 email the file to someone to fix

**Finding 3 of 4 · Strong evidence · Heard from P1, P3, P4, P6, P7, P8**

When the file is wrong, people send it to a colleague to fix by hand. They told us this without being asked.

> "Sent the raw file to [name] and asked them to fix it." — P1, operations manager, 80 seats

- **Who didn't fit:** P2 and P5 didn't do this. P2 rarely exports.
- **What it means:** Our numbers count these exports as successes, so the 212 tickets undercount the problem.

## 10. 7 of 8 didn't understand one checkbox

**Finding 4 of 4 · Moderate evidence · Heard from P1 to P7**

Almost everyone skipped "Include hidden fields" or guessed what it does. Nobody could say what a hidden field is.

> "Hidden from who?" — P4, reporting lead, 310 seats

- **Who didn't fit:** P8 used it correctly after reading the help article.
- **What it means:** A quick wording fix on the export screen. It isn't why people give up.

## 11. Three smaller things we noticed

- 2 of 8 expected export to run every month by itself. We didn't ask about this; it's worth raising in roadmap planning.
- 3 of 8 picked the same columns every time, because the export screen doesn't remember last time's choice.
- 3 of 8 renamed the file before sending it. Nobody gave up over this, so it isn't a priority.

All weak evidence. Every finding from the study is in this deck or the report's appendix.

## 12. Four things to do, in this order

1. Warn people at import when columns their reports use were skipped. Teams involved: Data Pipeline, Reporting. Fixes finding 1.
2. Hold the export screen rebuild until the import warning is live and measured. Teams involved: Reporting. Based on findings 1 and 3.
3. Count how many finance-team customers need a fixed column order. Teams involved: Support, Customer Success. Sizes finding 2.
4. Rename "Include hidden fields" and add a one-line explanation. Teams involved: Design. Fixes finding 4.

Who takes each one is for the teams to agree together.

## 13. The team decides by 30 October

1. **24 October:** Support counts the finance-team customers, so we know how big finding 2 is.
2. **30 October:** the team decides, using this deck and the report.
3. **November:** 3 follow-up sessions with finance teams, if the import warning goes ahead.
4. **January:** check it worked. Fewer exports abandoned after a recent import is the sign.
5. **Later:** one open question. Does the import problem affect scheduled reports too?

## 14. What this study can't tell us

- **Who we spoke to:** Customer Success helped find all 8 people. Customers who set up on their own may differ.
- **Finance teams:** Only 2 of the 8, so finding 2 could be bigger or smaller than it looks.
- **How many:** We didn't check the export numbers first, so we can't say what share of all customers hit finding 1.

Magpie drafted this slide and the researcher chose to keep it. The limits are in the report either way.

## 15. Who we spoke to

| Code | Role | Seats | Team |
| --- | --- | --- | --- |
| P1 | Operations manager | 80 | Operations |
| P2 | Office manager | 60 | Operations |
| P3 | Operations analyst | 120 | Operations |
| P4 | Reporting lead | 310 | Reporting |
| P5 | Finance analyst | 200 | Finance |
| P6 | Account manager | 95 | Sales |
| P7 | Finance controller | 450 | Finance |
| P8 | Data analyst | 150 | Reporting |

## 16. How AI was used

- **Magpie, an AI research assistant,** drafted the plan, the interview guide, the findings, the report and this deck.
- **The researcher** ran every session, noted their own patterns before seeing Magpie's, decided on each finding, and wrote the recommendations. They reviewed the findings on 12 October and this deck on 14 October.
- **Checks:** quotes and counts were checked by code against the transcripts. A separate AI reviewer raised 11 points, and 8 changed the findings. That reviewer can be wrong too.
- **Transcripts** came from the video tool, and the researcher corrected them against the recordings.
