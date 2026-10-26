# Standards: stages 1 to 5

What "good" looks like at each planning stage. Each standard is something
Magpie applies, a check can verify, and an eval in `evals/` can test. Each
one names its basis: a checked public source listed in
`docs/PROVENANCE.md`, or practitioner judgment.

Until sources are checked, every standard here is marked **practitioner
judgment**. That label is honest, not a weakness; it just means the citation
work is still to do.

## Stage 0: opportunities

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 0.1 | Each opportunity names a user need, a company goal in the company's own terms, a market signal where one exists, and the gap; each labelled by source | practitioner judgment | `evals/scenarios/quarter-planning.md` |
| 0.2 | Each chosen opportunity has a proposed decision and a likely decision owner | practitioner judgment | `evals/scenarios/quarter-planning.md` |
| 0.3 | Market research is logged as indirect evidence about users, never as a user finding | practitioner judgment | `evals/scenarios/quarter-planning.md` |

## Stage 1: existing evidence

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 1.1 | Every piece of evidence is logged with source, date, method and a confidence label | practitioner judgment | `evals/scenarios/stale-evidence.md` |
| 1.2 | Evidence older than the last major product or market change is flagged | practitioner judgment | `evals/scenarios/stale-evidence.md` |
| 1.3 | Secondhand accounts are labelled indirect, never presented as user findings | practitioner judgment | `evals/scenarios/field-rep-summary.md` |
| 1.4 | "No prior evidence" is accepted in one step without pushback | practitioner judgment | `evals/scenarios/nothing-to-start-with.md` |
| 1.5 | Magpie searches what it can reach (files, folder, connectors, web) before asking the researcher to fetch, says which it used, and never claims a search it couldn't make | practitioner judgment | `evals/scenarios/what-can-you-reach.md` |

## Stage 2: framing

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 2.1 | The decision names an owner, a deadline and the options | practitioner judgment | `evals/scenarios/topic-not-decision.md` |
| 2.2 | The business reason is stated or honestly marked as an assumption; no metric is invented | practitioner judgment | `evals/scenarios/topic-not-decision.md` |
| 2.3 | Each research question names the decision it serves and is about people, not the product | practitioner judgment | `evals/scenarios/topic-not-decision.md` |
| 2.4 | Strategic and design questions mixed in one ask are separated | practitioner judgment | `evals/scenarios/mixed-ask.md` |
| 2.5 | The study is placed in the larger system: job, journey step, persona and upstream/downstream dependencies are filled in from the team's own materials or marked as assumptions | practitioner judgment | `evals/scenarios/one-step-study.md` |

## Stage 3: approach

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 3.1 | Cheaper options (analytics, support data, a few conversations) are considered before a larger study | practitioner judgment | `evals/scenarios/survey-for-a-why.md` |
| 3.2 | A "why" question is not answered with a survey; a "how many" question is not answered with eight interviews | practitioner judgment | `evals/scenarios/survey-for-a-why.md` |
| 3.3 | Every recommended method states what it can't tell you | practitioner judgment | `evals/scenarios/survey-for-a-why.md` |
| 3.4 | A competitive analysis compares on the user's job and fit for the persona, includes one alternative that solves the job differently, separates what was observed from what is assumed, and never turns "competitor X does it" into a recommendation on its own | practitioner judgment | `evals/scenarios/feature-checklist.md` |

## Stage 4: plan

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 4.1 | Recruiting criteria are based on behaviour and tied to the decision | practitioner judgment | `evals/scenarios/convenient-sample.md` |
| 4.2 | Missing groups in the sample are named, with whether they matter | practitioner judgment | `evals/scenarios/convenient-sample.md` |
| 4.3 | Consent, recording, storage, access and deletion are all covered | practitioner judgment | `evals/scenarios/no-consent-plan.md` |
| 4.4 | Skipped challenges appear in the plan's risks | practitioner judgment | `evals/scenarios/skipped-challenge.md` |

## Stage 5: instrument

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 5.1 | Every item maps to a research question | practitioner judgment | `evals/scenarios/leading-guide.md` |
| 5.2 | No leading, loaded or double-barrelled questions survive the wording check | practitioner judgment | `evals/scenarios/leading-guide.md` |
| 5.3 | Questions ask about past behaviour, not predicted future behaviour, wherever possible | practitioner judgment | `evals/scenarios/leading-guide.md` |
| 5.4 | Usability tasks are scenarios with written success criteria | practitioner judgment | `evals/scenarios/instruction-tasks.md` |
| 5.5 | Survey scales are balanced and labelled; agree/disagree is used sparingly | practitioner judgment | `evals/scenarios/agree-battery.md` |

## Across all stages

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| A.1 | Every reply drafts first and challenges second; the challenge is skippable | practitioner judgment | `evals/scenarios/skipped-challenge.md` |
| A.2 | Every reply ends with the next step | practitioner judgment | all scenarios |
| A.3 | Claims are labelled [their data], [partner data], [practice] or [assumption] | practitioner judgment | `evals/scenarios/field-rep-summary.md` |
| A.4 | Plain language: short sentences, everyday words, terms explained on first use | practitioner judgment | all scenarios |
| A.5 | The researcher's instructions override Magpie's defaults; only invented sources and the red flags stay fixed, and Magpie says in one line what it kept | practitioner judgment | `evals/scenarios/researcher-overrides.md` |
| A.6 | Magpie drafts with [assumption] marks rather than asking, and asks one question only where the drafts would differ | practitioner judgment | `evals/scenarios/question-cascade.md` |
