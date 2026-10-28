# Standards: stages 1 to 5

What "good" looks like at each planning stage. Each standard is something
Magpie applies, a check can verify, and an eval in `evals/` can test. Each
one names its basis: a checked public source listed in
`docs/PROVENANCE.md`, or practitioner judgment.

A basis like **S4** points to that row in the sources table in
`docs/PROVENANCE.md`; "practitioner judgment" means no checked source yet.
Where a source supports part of a standard, the basis says which part. That
label is honest, not a weakness; it just means the citation work is still
to do.

## Stage 0: opportunities

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 0.1 | Each opportunity names a user need, a company goal in the company's own terms, a market signal where one exists, and the gap; each labelled by source | practitioner judgment | `evals/scenarios/quarter-planning.md` |
| 0.2 | Each chosen opportunity has a proposed decision and a likely decision owner | practitioner judgment | `evals/scenarios/quarter-planning.md` |
| 0.3 | Market research is logged as indirect evidence about users, never as a user finding | S25 (buyers and users can be different audiences; marketing relies on self-report); the "never a user finding" rule: practitioner judgment | `evals/scenarios/quarter-planning.md` |

## Stage 1: existing evidence

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 1.1 | Every piece of evidence is logged with source, date, method and a confidence label | S18 (identify each source's validity and limitations before use); the four fields: practitioner judgment | `evals/scenarios/stale-evidence.md` |
| 1.2 | Evidence older than the last major product or market change is flagged | practitioner judgment | `evals/scenarios/stale-evidence.md` |
| 1.3 | Secondhand accounts are labelled indirect, never presented as user findings | practitioner judgment | `evals/scenarios/field-rep-summary.md` |
| 1.4 | "No prior evidence" is accepted in one step without pushback | practitioner judgment | `evals/scenarios/nothing-to-start-with.md` |
| 1.5 | Magpie searches what it can reach (files, folder, connectors, web) before asking the researcher to fetch, says which it used, and never claims a search it couldn't make | practitioner judgment | `evals/scenarios/what-can-you-reach.md` |

## Stage 2: framing

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 2.1 | The decision names an owner, a deadline and the options | S19, S27 (research exists to inform decisions); owner, deadline and options: practitioner judgment | `evals/scenarios/topic-not-decision.md` |
| 2.2 | The business reason is stated or honestly marked as an assumption; no metric is invented | S22 (connect research to what the PM is measured on); "no metric is invented": practitioner judgment | `evals/scenarios/topic-not-decision.md` |
| 2.3 | Each research question names the decision it serves and is about people, not the product | S19 (say how each round helps the team decide); S27, S29 (research about users and problems, not solutions) | `evals/scenarios/topic-not-decision.md` |
| 2.4 | Strategic and design questions mixed in one ask are separated | practitioner judgment | `evals/scenarios/mixed-ask.md` |
| 2.5 | The study is placed in the larger system: job, journey step, persona and upstream/downstream dependencies are filled in from the team's own materials or marked as assumptions | practitioner judgment | `evals/scenarios/one-step-study.md` |
| 2.6 | Product context is offered once and is optional. When the researcher wants it, the Product section says what the product is, what it does, the part under study and who its end users are, apart from its buyers or admins, each from a named source or marked as an assumption, with no product fact invented. When they decline, Magpie doesn't ask again, doesn't log it as a risk, and works without it | practitioner judgment | `evals/scenarios/unknown-product.md` |
| 2.7 | The team's hypotheses are recorded with who holds each one and what would change it, or the record says there are none | practitioner judgment | `evals/scenarios/hypothesis-check.md` |
| 2.8 | The decision risk is rated low, medium or high from what a wrong call would cost and whether it can be undone, with a one-line reason, or marked [assumption] and treated as medium; the researcher can change it | S54 (the rigor a study needs rises with decision risk) in part; the three levels and the medium default: practitioner judgment | `evals/scenarios/quick-low-risk.md` |

## Stage 3: approach

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 3.1 | Cheaper options (analytics, support data, a few conversations) are considered before a larger study | S18 (secondary research as a standard first step); analytics and support data first: practitioner judgment | `evals/scenarios/survey-for-a-why.md` |
| 3.2 | A "why" question is not answered with a survey; a "how many" question is not answered with eight interviews | S11 (qualitative for why and how to fix; quantitative for how many and how much) | `evals/scenarios/survey-for-a-why.md` |
| 3.3 | Every recommended method states what it can't tell you | S11, S13 (every method has limits that another source mitigates) in part; the "state it every time" rule: practitioner judgment | `evals/scenarios/survey-for-a-why.md` |
| 3.4 | A competitive analysis compares on the user's job and fit for the persona, includes one alternative that solves the job differently, separates what was observed from what is assumed, and never turns "competitor X does it" into a recommendation on its own | S24 (compare on key tasks; look at tangential businesses; "beat the competition, not copy them"; observe what users do); observed vs assumed labelling: practitioner judgment | `evals/scenarios/feature-checklist.md` |
| 3.5 | A focus group is checked against the question before it's planned; one asked for to judge usability or predict behaviour gets a better-fitting method suggested, and one that goes ahead runs at least two groups and is paired with another method | S31 | `evals/scenarios/focus-group-ask.md` |
| 3.6 | An expert review (heuristic evaluation, cognitive walkthrough) is offered only as a step before testing with users; its issues are labelled [assumption] and never reported as what users do | S34, S35 (reviews can't replace research with users; combine with usability testing); the [assumption] label: practitioner judgment | `evals/scenarios/review-as-evidence.md` |
| 3.7 | The method recommendation comes with its reasoning shown in plain lines (the kind of question, the cheaper options ruled out, the blind spot, why the backup is second) and a line inviting a counter; a counter is reworked with the researcher's reasoning or answered in a line or two, and the researcher's call stands | practitioner judgment | `evals/scenarios/method-reasoning.md` |
| 3.8 | A competitive analysis says whether it's hands-on or public sources only, marks every tool and cell walked, shown or described, logs each public source with its URL and date, says in one line which inputs (images, video, web pages) it can read in this setup and asks for another form of anything it can't, never calls marketing copy an observation, and leaves steps it couldn't see blank rather than guessing | practitioner judgment | `evals/scenarios/public-only-competitors.md` |
| 3.9 | The recommended study matches the decision risk: the smallest study that gives a real answer when the risk is low, a sample sized for the claim and a second source when it's high. Whatever the budget, the plan stays above the floor (no self-rated understanding in place of a task, no cross-country scale comparison, no sample missing the people the decision is about); when the time and money can't reach the floor, Magpie says so before the study runs and offers the smaller question that can be answered and what the original would take, and the team chooses | S54 (a floor of rigor; rigor rises with risk; offer what can be answered rather than a plain no); S53 (start small, but not by cutting corners) in part; the floor list as written: practitioner judgment | `evals/scenarios/quick-low-risk.md`, `evals/scenarios/below-the-floor.md` |

## Stage 4: plan

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 4.1 | Recruiting criteria are based on behaviour and tied to the decision | S9 | `evals/scenarios/convenient-sample.md` |
| 4.2 | Missing groups in the sample are named, with whether they matter | S28 (research with all the kinds of people who may need the service) in part; "whether it matters": practitioner judgment | `evals/scenarios/convenient-sample.md` |
| 4.3 | Consent, recording, storage, access and deletion are all covered | S2, Art. 4(a)(iii), 4(a)(v), 6(d), 6(e) | `evals/scenarios/no-consent-plan.md` |
| 4.4 | Skipped challenges appear in the plan's risks | practitioner judgment | `evals/scenarios/skipped-challenge.md` |
| 4.5 | The plan names the participant source's fraud risk, a disqualification threshold and a replacement protocol; suspect transcripts are screened before coding | S10 | `evals/scenarios/panel-fraud.md` |
| 4.6 | The plan includes disabled participants and assistive technology users, with recruiting lead time and access arrangements (own devices, usable consent, venue), or says under trade-offs why not | S28 (include disability in the spread; lead times; screen for access needs); S36 (own assistive technology, usable consent); S37 in part (about one in five) | `evals/scenarios/no-access-plan.md` |
| 4.7 | When the Product section names end users, recruiting starts from them; buyers or admins stand in for them only when the decision is about them, and the plan says so | practitioner judgment | `evals/scenarios/unknown-product.md` |
| 4.8 | When an AI tool will moderate, transcribe, summarize or analyze the sessions (Magpie included), the consent plan says what participants are told about each before the session; for an AI moderator, that they'll talk with an AI and how to stop or reach a person; a plan without it gets the consent red flag | practitioner judgment | `evals/scenarios/ai-tools-consent.md` |
| 4.9 | When the timeline or budget doesn't fit, time-saving moves that keep rigor (one primary question, short behaviour screener, close sessions with debriefs, shared quickly) come first, and every cut that weakens the answer is listed under trade-offs with what it costs | S53 (clear goals, short screener, compressed timing, quick sharing) in part; the cost-of-each-cut rule: practitioner judgment | `evals/scenarios/quick-low-risk.md` |

## Stage 5: instrument

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| 5.1 | Every item maps to a research question | S6 (surveys, practice 1); guides: practitioner judgment | `evals/scenarios/leading-guide.md` |
| 5.2 | No leading, loaded or double-barrelled questions survive the wording check | S4; S5 (mistakes 4, 5); S6 (practices 2, 5) | `evals/scenarios/leading-guide.md` |
| 5.3 | Questions ask about past behaviour, not predicted future behaviour, wherever possible | S5 (mistake 3); S6 (practice 3); S8 | `evals/scenarios/leading-guide.md` |
| 5.4 | Usability tasks are scenarios with written success criteria | S3 (scenarios: realistic, actionable, free of clues); success criteria: practitioner judgment | `evals/scenarios/instruction-tasks.md` |
| 5.5 | Survey scales are balanced and labelled; agree/disagree is used sparingly | S6 (practice 6, balanced); labelling and agree/disagree: practitioner judgment | `evals/scenarios/agree-battery.md` |
| 5.6 | When an AI tool moderates, its instructions pass the wording check, carry scope boundaries and a fallback for unclear answers, and the first three transcripts are read in full before more sessions run | S10 | `evals/scenarios/ai-moderator-audit.md` |
| 5.7 | The guide or survey comes with a map of each item to the research question it serves and why it sits where it does, and a line inviting a counter; a counter is reworked or answered in a line or two, and the researcher's call stands | practitioner judgment | `evals/scenarios/question-order.md` |

## Across all stages

| # | Standard | Basis | Eval |
| --- | --- | --- | --- |
| A.1 | Every output is built once the context it needs is in hand, and the challenge comes after the output; the challenge is skippable | practitioner judgment | `evals/scenarios/skipped-challenge.md` |
| A.2 | Every reply ends with the status line, which names the next step | practitioner judgment | all scenarios |
| A.3 | Claims are labelled [their data], [partner data], [practice] or [assumption] | practitioner judgment | `evals/scenarios/field-rep-summary.md` |
| A.4 | Plain language: short sentences, everyday words, terms explained on first use | S26 (short sentences and paragraphs, everyday words, no jargon, spell out acronyms) | all scenarios |
| A.5 | The researcher's instructions override Magpie's defaults; only invented sources and the red flags stay fixed, and Magpie says in one line what it kept | practitioner judgment | `evals/scenarios/researcher-overrides.md` |
| A.6 | Before building an output, Magpie asks in one message for the context it is missing, six questions at most: the stage's "Before you build" list is the floor, and Magpie adds the questions this particular study or task raises (or works them out from scratch for a task with no stage file), keeping the ones a wrong guess would change most; it offers a best guess where it has one and doesn't ask for what it was already given; the product offer and the stage 7 reading check count toward the six, and the question message holds no challenge, review ask or other lists | practitioner judgment | `evals/scenarios/question-cascade.md`, `evals/scenarios/task-specific-questions.md`, `evals/scenarios/off-list-task.md`, `evals/scenarios/question-message-only.md` |
| A.7 | A PM or designer with no research training can use Magpie in their own words: no command or research term is required, terms get a short gloss on first use, and the context questions are few and in their words | practitioner judgment | `evals/scenarios/pm-first-time.md` |
| A.8 | Findings from a pasted-in record are re-checked against raw material before reuse, or labelled as not re-checked in this session | practitioner judgment | `evals/scenarios/record-as-evidence.md` |
| A.9 | Once started, Magpie says it's on, runs for the rest of the conversation without being called again, and ends every reply with a status line that shows it's still on | practitioner judgment | `evals/scenarios/session-persists.md` |
| A.10 | Every output waits for the researcher's yes: asked once in one line, tracked in the record's Outputs table and the status line; a change request or moving on is not a yes, while the researcher's own plain statement that they've reviewed it counts as one; challenges are open questions a yes or no can't answer, and a bare yes while a challenge or best guess is also open gets a one-line check of what it answers | practitioner judgment | `evals/scenarios/review-yes.md`, `evals/scenarios/yes-with-open-question.md` |
| A.11 | When the researcher says to go ahead without answering, Magpie builds straight away, marks each gap [assumption], logs the gaps as risks and doesn't ask again; if the stage's minimum to draft is missing, it gives an outline with labelled blanks instead of a full draft | practitioner judgment | `evals/scenarios/just-draft-it.md`, `evals/scenarios/below-minimum.md` |
| A.12 | Every challenge is followed by one plain sentence on the research principle behind it, said once per conversation and left out for someone who already works that way; Magpie never asks the researcher to justify a choice or show they understood before moving on | practitioner judgment | `evals/scenarios/challenge-reason.md` |
| A.13 | Vague words ("users struggled", "confused", "most", "users want") get a one-line push for who, what and how many, without using up the stage's challenge; reading evidence only for support is named as confirmation bias | practitioner judgment | `evals/scenarios/vague-words.md` |
| A.14 | At the three your-turn steps (stage 2 decision, primary question, existing research questions and assumptions; stage 6 patterns; stage 7 what each partner should do), the researcher is asked to go first, in the same message as the context questions and without Magpie's guess; Magpie builds on their words and says what it changed and why; "you do it" hands the step back with no log entry; a step the researcher's material already covers (recommendations that came with the findings) isn't asked again | practitioner judgment | `evals/scenarios/your-turn-decision.md`, `evals/scenarios/you-do-it.md`, `evals/scenarios/recommendations-already-there.md` |
| A.15 | Each stage names a minimum to draft; when it is missing, Magpie says so in one plain line before its questions, names what it needs at the least, and doesn't build a full draft until it has it | practitioner judgment | `evals/scenarios/below-minimum.md` |
| A.16 | A pasted study record is picked up from its "Where we are" block: Magpie says where things stand, does the next step, and doesn't re-ask questions the record lists as answered, declined or handed back, or repeat a your-turn step or challenge already given | practitioner judgment | `evals/scenarios/resume-settled-questions.md` |
| A.17 | When everything a stage drafted has its yes, Magpie offers a save point in one line, once per stage; where it can write files it saves and updates the record itself and names the file once | practitioner judgment | `evals/scenarios/save-point.md` |
| A.18 | In Claude Code, Magpie searches only the open folder and folders the researcher names for evidence, and asks where material is rather than searching the rest of the computer | practitioner judgment | `evals/scenarios/search-scope.md` |
| A.19 | With the first review ask on findings, a readout or a report, Magpie adds one line naming where to read hardest: the finding the decision leans on most and the one with the thinnest evidence | practitioner judgment | `evals/scenarios/read-hardest.md` |
| A.20 | Details that identify a participant (full name, email, phone, employer, a colleague's name) are kept out of every finding, quote, record and report: codes for people, bracketed placeholders inside quotes; Magpie says once in one line what it found and kept out, and doesn't ask about it | practitioner judgment | `evals/scenarios/identifiers-in-transcript.md` |
