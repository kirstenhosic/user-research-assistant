# Standards: stages 6 to 7 and workshops

What "good" looks like in analysis, reporting and workshops. Each standard
is something Magpie applies, a check can verify, and an eval in `evals/` can
test. A basis like **S2** points to that row in the sources table in
`docs/PROVENANCE.md`; "practitioner judgment" means no checked source yet.
Where a source supports part of a standard, the basis says which part.

## Stage 6: analysis

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 6.1 | Every finding answers a research question or is listed as "also noticed" | S1b (a theme is a shared meaning, not a topic summary); the "also noticed" rule: practitioner judgment | `evals/scenarios/theme-restates-question.md` |
| 6.2 | Every finding names its counter-evidence: the participants who didn't fit | S2, Art. 9(d) (no undue selectivity) | `evals/scenarios/dropped-participants.md` |
| 6.3 | Counts are stated as numbers ("6 of 8"), never as vague quantities; no percentages from small qualitative samples | S2, Art. 9(c) (conclusions adequately supported); the wording rule itself: practitioner judgment | `evals/scenarios/overclaimed-theme.md` |
| 6.4 | Every quote carries a participant code and location, and matches the source | practitioner judgment | `evals/scenarios/altered-quote.md` |
| 6.5 | Strength labels match the evidence and don't drift between record and readout | S2, Art. 9(c) | `evals/scenarios/overclaimed-theme.md` |
| 6.6 | Partner data is shown alongside the study data as agreeing, disagreeing or silent, never merged into one claim | practitioner judgment | `evals/scenarios/telemetry-merge.md` |
| 6.7 | The independent review is requested at stage 6 and its findings are acted on or answered, never dropped | practitioner judgment | `evals/scenarios/review-finding-dropped.md` |
| 6.8 | Survey results show the base and say who answered; no significance claim without a test | practitioner judgment | `evals/scenarios/survey-significance.md` |
| 6.9 | Findings whose cause lies outside the studied piece are kept and labelled with where the cause sits; findings are mapped to the journey step and persona they affect | practitioner judgment | `evals/scenarios/one-step-study.md` |

## Stage 7: readout and report

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 7.1 | The readout opens with why: the decision, the business need, what was known. Method is one factual slide. Top findings are five or fewer. The decision-first order is offered for senior or short readouts | practitioner judgment | `evals/scenarios/method-first-readout.md` |
| 7.2 | Every recommendation has an owner, rests on a named finding, and names the decision or goal it serves | practitioner judgment | `evals/scenarios/floating-recommendation.md` |
| 7.3 | Recommendations are detailed actions with owners; partner sections where they help | practitioner judgment | `evals/scenarios/floating-recommendation.md` |
| 7.3a | The deck is sized to the audience and slot; 20 slides or fewer by default, appendix not counted | practitioner judgment | `evals/scenarios/method-first-readout.md` |
| 7.4 | Limits, including skipped challenges, are always in the record and the report; for the readout, Magpie drafts them and the researcher decides whether they go in, never silently either way | S2, Art. 9(a) (enough on method and sampling to assess the conclusions); the readout rule: practitioner judgment | `evals/scenarios/buried-limits.md` |
| 7.5 | The independent review is run on the report and summarized in it | practitioner judgment | `evals/scenarios/review-finding-dropped.md` |
| 7.5a | The report is ten pages or fewer (images and appendix aside), has a linked contents list, keeps method to one paragraph, and moves timelines, recruiting and consent detail to the appendix | practitioner judgment | `evals/scenarios/methods-paper-report.md` |
| 7.6 | Library entries are written for findings worth keeping | practitioner judgment | `evals/scenarios/method-first-readout.md` |
| 7.7 | The summary passes the reader test: each named reader can tell from it what it means for them and what they'd do next, or is told there's nothing for them | practitioner judgment | `evals/scenarios/reader-test.md` |
| 7.8 | The independent review runs at most two passes; remaining disagreements go to the researcher with both sides stated | practitioner judgment | `evals/scenarios/review-finding-dropped.md` |

## Workshops

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| W.1 | A workshop has a one-sentence outcome the room leaves with, or it isn't run | practitioner judgment | `evals/scenarios/workshop-without-outcome.md` |
| W.2 | Silent writing comes before discussion in every generative step | practitioner judgment | `evals/scenarios/workshop-without-outcome.md` |
| W.3 | Actions leave the room with owners and are read back | practitioner judgment | `evals/scenarios/workshop-without-outcome.md` |
