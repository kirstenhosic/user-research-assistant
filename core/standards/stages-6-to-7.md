# Standards: stages 6 to 7 and workshops

What "good" looks like in analysis, reporting and workshops. Each standard
is something Magpie applies, a check can verify, and an eval in `evals/` can
test. A basis like **S2** points to that row in the sources table in
`docs/PROVENANCE.md`; "practitioner judgment" means no checked source yet.
Where a source supports part of a standard, the basis says which part.

## Stage 6: analysis

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 6.1 | Every finding answers a research question or is tagged "also noticed"; a tagged finding meets the same evidence bar and still reaches the readout | S1b (a theme is a shared meaning, not a topic summary); the "also noticed" rule: practitioner judgment | `evals/scenarios/theme-restates-question.md` |
| 6.2 | Every finding names its counter-evidence: the participants who didn't fit | S2, Art. 9(d) (no undue selectivity) | `evals/scenarios/dropped-participants.md` |
| 6.3 | Counts are stated as numbers ("6 of 8"), never as vague quantities; no percentages from small qualitative samples | S2, Art. 9(c) (conclusions adequately supported); the wording rule itself: practitioner judgment | `evals/scenarios/overclaimed-theme.md` |
| 6.4 | Every quote carries a participant code and location, matches the source, and is the words of the participant it's credited to | practitioner judgment | `evals/scenarios/altered-quote.md`, `evals/scenarios/misattributed-quote.md` |
| 6.5 | Strength labels match the evidence and don't drift between record and readout | S2, Art. 9(c) | `evals/scenarios/overclaimed-theme.md` |
| 6.6 | Partner data is shown alongside the study data as agreeing, disagreeing or silent, never merged into one claim | S13 (check whether other data supports a result); S14 (no data source automatically overrules another) in part; the three labels: practitioner judgment | `evals/scenarios/telemetry-merge.md` |
| 6.7 | The independent review is run at stage 6 in the same reply as the findings, by a separate agent where one can be started, or by handing the researcher the paste text and the steps; its findings are acted on or answered, never dropped | practitioner judgment | `evals/scenarios/review-finding-dropped.md`, `evals/scenarios/review-starts-itself.md` |
| 6.8 | Survey results show the base and say who answered; no significance claim without a test | S12 (report the sample size and do the math before stating a number from a sample; significance at p < 0.05) | `evals/scenarios/survey-significance.md` |
| 6.9 | Findings whose cause lies outside the studied piece are kept and labelled with where the cause sits; findings are mapped to the journey step and persona they affect | practitioner judgment | `evals/scenarios/one-step-study.md` |
| 6.10 | A tool's summary of transcripts, Magpie's own included, is treated as a draft that says which transcripts to read, never as findings; smoothed contradiction is caught and the dissenting participants restored | S10 | `evals/scenarios/smoothed-summary.md` |
| 6.11 | Every count lists the participants and lines behind it ("3 of 8 (P1 06, P5 06, P7 06)"), so the count can be checked by code: as many codes as the count claims, each a real participant, each line theirs | practitioner judgment | `evals/scenarios/uncoded-count.md` |
| 6.12 | Each hypothesis is marked supported, contradicted or not addressed, with the findings behind it, after the findings are drafted | practitioner judgment | `evals/scenarios/hypothesis-check.md` |
| 6.13 | Before findings are written, the researcher reviews each candidate theme, shown riskiest first with its count, a quote and its risk, plus the merged and dropped codes; each theme gets its own keep, change, split or drop, a blanket "looks good" is followed up, and a skipped review is logged as a risk | practitioner judgment | `evals/scenarios/theme-review.md` |

## Stage 7: readout and report

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 7.1 | The readout opens with why: the decision, the business need, what was known. Method is one factual slide. Top findings are five or fewer, and every other finding that met the evidence bar is listed on one slide, so nothing is dropped. The decision-first order is offered for senior or short readouts | S20 (one or two slides on what you did, then findings, then next steps) in part; the five-finding cap, the other-findings slide and decision-first option: practitioner judgment | `evals/scenarios/method-first-readout.md` |
| 7.2 | Every recommendation has an owner, rests on a named finding, and names the decision or goal it serves | S22 (name the finding, tie it to a metric, make it concrete); S23 (specific, prioritised) in part; the owner column: practitioner judgment | `evals/scenarios/floating-recommendation.md` |
| 7.3 | Recommendations are detailed actions with owners; partner sections where they help | practitioner judgment | `evals/scenarios/floating-recommendation.md` |
| 7.3a | The deck is sized to the audience and slot; 20 slides or fewer by default, appendix not counted | S21 (layer a report for headline, theme and detail readers) in part; the slide counts: practitioner judgment | `evals/scenarios/method-first-readout.md` |
| 7.4 | Limits, including skipped challenges, are always in the record and the report; for the readout, Magpie drafts them and the researcher decides whether they go in, never silently either way | S2, Art. 9(a) (enough on method and sampling to assess the conclusions); the readout rule: practitioner judgment | `evals/scenarios/buried-limits.md` |
| 7.5 | The independent review is run on the report, in the same reply as the report, and summarized in it | practitioner judgment | `evals/scenarios/review-finding-dropped.md`, `evals/scenarios/review-starts-itself.md` |
| 7.5a | The report is ten pages or fewer (images and appendix aside), has a linked contents list, keeps method to one paragraph, and moves timelines, recruiting and consent detail to the appendix | practitioner judgment | `evals/scenarios/methods-paper-report.md` |
| 7.5b | Quote and count checks are run again on the readout and report, by code or by hand, and the method is stated | practitioner judgment | `evals/scenarios/review-starts-itself.md` |
| 7.6 | Library entries are written for findings worth keeping | practitioner judgment | `evals/scenarios/method-first-readout.md` |
| 7.7 | The summary passes the reader test: each named reader can tell from it what it means for them and what they'd do next, or is told there's nothing for them | practitioner judgment | `evals/scenarios/reader-test.md` |
| 7.8 | The independent review runs at most two passes; remaining disagreements go to the researcher with both sides stated | practitioner judgment | `evals/scenarios/review-finding-dropped.md` |
| 7.9 | No finding enters a readout or report without receipts (two participant references with locations, or a labelled single case), and Magpie asks once whether the researcher has read the passages behind each top finding, logging "not yet" as a risk | S10 | `evals/scenarios/smoothed-summary.md` |
| 7.10 | A readout or report stays labelled "draft" until it and the findings it rests on have the researcher's yes; Magpie drafts it anyway and says what's waiting | practitioner judgment | `evals/scenarios/review-yes.md` |
| 7.11 | Before building a readout or report, Magpie asks who will see it and what each reader needs to decide or do, the format and slot, and the team's template, unless these are already known | practitioner judgment | `evals/scenarios/readout-without-audience.md` |

## Workshops

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| W.1 | A workshop has a one-sentence outcome the room leaves with, or it isn't run | S17 (articulate the goal as the ideal end state first); S30 (each workshop type has a defined outcome); "or it isn't run": practitioner judgment | `evals/scenarios/workshop-without-outcome.md` |
| W.2 | Silent writing comes before discussion in every generative step | S15 (written ideation before the group avoids groupthink and dominance); S16 (silent post-up and brainwriting) | `evals/scenarios/workshop-without-outcome.md` |
| W.3 | Actions leave the room with owners and are read back | practitioner judgment | `evals/scenarios/workshop-without-outcome.md` |
