# Design

Version 0.1, 26 October 2026. This is the design the first build follows. It
will change as real researchers use the tool; `docs/CHANGELOG.md` records what
changed and why.

## Summary

Magpie is an open-source research companion for user researchers working in
industry alongside product managers, designers and engineers. It works in
Claude, ChatGPT and Gemini and takes a study from "do we already know this?" to
a stakeholder-ready report.

Five things make it different from a general-purpose chat assistant:

- **One study record** carries context across every stage, so the plan, the
  analysis and the report all trace back to the same decision.
- **Decision-anchored framing.** Every study names the business decision it
  serves, who owns it and when, before any method is chosen.
- **Friction that never blocks.** One pointed challenge per stage. Researchers
  answer it or skip it, and a skip is logged as a risk instead of costing time.
- **Business value is traced, not bolted on.** The value thread runs from
  framing through findings to recommendations.
- **Portable.** A plain-Markdown core with thin adapters, so the same method
  works on any of the three platforms.

## Design principles

1. **Decision first.** No method talk until the study names a decision, its
   owner and its deadline.
2. **Evidence before new research.** The first move is always to check what
   the organization already knows.
3. **Challenge, don't quiz.** Challenges are specific to the researcher's own
   content and are always skippable. The assistant never asks someone to prove
   they learned something.
4. **Velocity is protected.** The assistant drafts first and challenges
   alongside the draft, never as a gate in front of it.
5. **Value is traceable.** Every recommendation links back to the decision and
   the business goal it serves.
6. **Confidence is explicit.** Findings carry an evidence-strength label. The
   assistant never invents sources, statistics or quotes.
7. **Stakeholder-ready by default.** A readout tells one story (why we
   asked, what we did, what we found, what it means, what to do), opens with
   the decision and the business need, keeps top findings to five, pitches
   detail for PMs and engineers, and stays under 20 slides. Limits always
   live in the record and the report; whether they go in the readout is the
   researcher's call. A report goes a little deeper, with links and images,
   and stays at ten pages or fewer with a linked contents list; method is a
   paragraph, and admin detail lives in the appendix.
8. **The researcher stays the author.** The assistant proposes; the researcher
   decides and owns the work.
9. **The piece sits in a system.** Every study is placed on the team's own
   journeys, personas and jobs to be done, tied to the company's goals in
   the company's names, and checked for what's upstream, downstream and
   owned by someone else. A few questions at framing, a few labels at
   analysis and readout, never a separate deliverable. Market research is
   evidence too, logged as indirect evidence about users. And research
   doesn't have to wait for an ask: an optional opening stage lays out
   company goals, market signals and user signals side by side and drafts
   opportunity briefs for the overlaps.

## The workflow

Seven stages, plus a workshop branch for when stakeholders still need to
ideate or align. Researchers can enter at any stage, for example with
transcripts already in hand. The assistant then backfills only the minimum
record it needs: the decision and the research questions.

| Stage | What the assistant drafts | Example challenge | Can end here when |
| --- | --- | --- | --- |
| 0. Find the opportunities (optional) | Opportunity list, one-page briefs | "If this study came back with a clear answer, who would act on it?" | Used when there's no ask yet and the researcher wants to propose research |
| 1. Check existing evidence | Evidence log, gap summary | "How old is this, and has the product or market changed since?" | Existing evidence answers the question: deliver an evidence brief instead of a study. Finding nothing is a valid result and moves straight on |
| 2. Frame the problem | Decision statement, business goal, research questions, assumptions | "If the answer came back the opposite way, what would the team do differently?" | No decision depends on the answer |
| 3. Choose the approach | Method recommendation with trade-offs | "Why can't analytics or a quick test answer this?" | |
| 4. Plan the study | Research plan, recruiting criteria, timeline | "Who is missing from this sample, and does that matter for the decision?" | |
| 5. Draft the guide or instrument | Interview guide, test script, survey, diary prompts | Flags leading, double-barrelled or hypothetical questions | |
| 6. Analyze | Coding frame, themes, findings with evidence strength | "Which participants contradict this theme?" | |
| 7. Read out and report | Readout deck outline, final report | "What should the PM do on Monday because of this?" | |
| Workshop branch | Agenda, activities, pre-reads, synthesis of outputs | "What decision should the room leave with?" | Runs after stage 2 to align on the problem, or after stage 7 to turn findings into ideas |

Framing is the anchor. The decision named there carries through to the
report, and a workshop can loop back into it before the study is designed.

## The study record

The study record is one Markdown file that every stage reads and updates.
It's the main way the tool keeps continuity without relying on any platform's
memory. Researchers save it, share it with teammates, and paste or upload it
to pick up where they left off on any platform. The template is
`core/templates/study-record.md`.

| Section | Holds | Filled at stage |
| --- | --- | --- |
| Decision | The decision, its owner, its deadline, the options on the table | 2 |
| Business context | Goal or metric it moves, cost of getting it wrong | 2 |
| Evidence log | Source, date, method, confidence, still valid? | 1 |
| Research questions | Primary and secondary questions, each tied to the decision | 2 |
| Assumptions and risks | Known assumptions plus every skipped challenge | All |
| Approach | Method, sample, rationale, trade-offs accepted | 3–4 |
| Instruments | Links to the guide, script or survey | 5 |
| Findings | Claim, supporting evidence, contradicting evidence, strength | 6 |
| Recommendations | Action, owner, link to decision and business goal | 7 |
| Change log | Dated entries for what changed and why | All |

The record makes the business-value thread checkable. At readout time the
assistant can show that each recommendation answers a research question, and
that each research question serves the named decision.

## Friction model

Friction comes as challenges written about the researcher's own draft, never
as generic quiz questions. Each challenge comes with the draft, not before it,
so the work keeps moving.

**How a challenge works**

- Each one comes from a bank of challenge types and is rewritten to fit what
  the researcher just produced.
- The researcher can answer it, mark it already handled, or skip it.
- A skip is logged in the record's risks section. It then shows up in the
  plan's risks and in the report's limitations, so the trade-off stays visible
  to stakeholders.

**Challenge types in the bank**

- **Decision test:** would a different answer change what the team does?
- **Evidence test:** what do we already know, and how fresh is it?
- **Riskiest assumption:** which belief, if wrong, costs the most?
- **Method fit:** is this the cheapest method that can answer the question?
- **Sample blind spot:** who is missing, and does it matter?
- **Claim strength:** how many participants, which segments, any disconfirming
  cases?
- **So what:** what should each partner (PM, design, engineering) do
  differently?

**Challenge level**, set by the researcher at any time:

| Level | What happens |
| --- | --- |
| Push me | Up to three challenges per stage, for practice or high-stakes studies |
| Standard (default) | One challenge per stage, the one with the highest stakes |
| Light | Only red flags |

Red flags are always raised at every level: missing consent or data-handling
plans, vulnerable participants, leading questions in a guide, and findings
stated with more confidence than the evidence supports.

## Partner data and starting from zero

Researchers rarely have all the evidence themselves. The assistant treats
partner teams as sources to bring in on purpose, and treats "we have nothing"
as a normal starting point.

**When to bring in partners.** At stages 1, 3 and 6 the assistant asks whether
another team holds evidence that would sharpen the question or strengthen a
finding. If one does, it drafts the request for the researcher to send.

| Partner | What they hold | Best used for |
| --- | --- | --- |
| Product analytics or data science | Telemetry, funnels, feature usage | Sizing a problem, choosing who to recruit, checking whether a qualitative finding shows up at scale |
| Customer success and account teams | Account context, renewal risk, escalations | Framing the business stakes, recruiting enterprise customers |
| Sales and field representatives | Deal blockers, competitive losses, buyer objections | Framing the problem, understanding buyers who aren't users |
| Support | Ticket themes and volume | Spotting pain points, triangulating usability findings |
| Marketing or market research | Segmentation, brand and market studies | Choosing segments, avoiding duplicate surveys |

**Treating partner data with care.** Partner input goes into the evidence log
with its source and a confidence label. Secondhand customer accounts, such as
a field rep's summary, are marked as indirect evidence: useful for framing and
recruiting, never presented as user findings on their own. In analysis, the
assistant shows where qualitative and quantitative signals agree or conflict.
It doesn't merge them into one claim.

**No prior research is fine.** If the researcher has nothing, stage 1 takes
under a minute. The assistant suggests two or three quick places to look, such
as a teammate, the support queue or a dashboard. It records "no prior evidence
found" and moves on, and it doesn't challenge the researcher for having
nothing. The record notes that the study is starting from zero so stakeholders
read the findings in that light.

## Accuracy

Independent checker agents help, but they aren't the best first line. A
reviewer model can also be wrong, and it adds time to every draft. The stronger
approach is to make errors hard to produce and easy to detect, then save an
independent review for the outputs stakeholders act on. No approach removes
hallucination entirely, so the tool also says how confident it is.

| Layer | What it does | What it catches | Where it runs |
| --- | --- | --- | --- |
| 1. Grounding rules | Every finding cites its evidence: participant, transcript line or timestamp, survey question. Claims without a source are labelled assumptions. | Invented findings, unsupported generalizations | Every stage |
| 2. Source labels | Each statement is tagged as coming from your data, from partner data, from general practice or from an assumption | General knowledge passed off as a study finding | Every stage |
| 3. Checks done by code, not the model | Quotes are string-matched against transcripts. Counts and survey statistics are computed by code. | Altered or invented quotes, wrong counts, wrong percentages | Analysis, readout, report |
| 4. Built-in checklists | Each stage ends with a short self-check against written criteria | Leading questions, missing consent plan, overclaiming | Every stage |
| 5. Independent review | A fresh pass that sees only the source material and the output, not the conversation that produced it | Errors the drafting pass is blind to, such as a theme that ignores contradicting participants | Analysis and final report, and on request |
| 6. Evals | Test scenarios with known traps run before every release | Regressions when the prompts change | Repo, before release |

Layers 3 and 5 depend on the platform. Claude Code can run the scripts and
start a separate review agent. ChatGPT and Gemini skills can carry the
scripts, and both platforms document running skill scripts, but whether they
run these particular ones hasn't been tested yet. Where a platform can't, the
skill falls back: it gives the researcher a review prompt to paste into a
fresh chat, and the quote check becomes a checklist item.

## Fitting into a team

The tool works for one researcher out of the box, and a team can adopt it by
adding four shared pieces. None of them needs new software. They're files a
team keeps in a shared drive, wiki or repo.

1. **Team profile.** One file the assistant reads at the start of every study.
   It holds products and users, company goals and the metrics leadership
   watches, key stakeholders, partner teams and who to ask for data, and the
   team's rules on consent, recruiting, incentives and data handling. This is
   how business value gets tied to goals the company already tracks.
2. **Shared study records.** Study records live in one shared folder, so
   teammates can pick up, review or continue each other's studies.
3. **Research library.** At the end of each study, the assistant pulls its key
   findings into short, dated library entries (finding, evidence, strength,
   study link). Stage 1 of the next study searches those entries first.
4. **Intake for partners.** A short request template PMs and designers fill
   in: the decision, the deadline, what they already believe. It feeds
   straight into stage 2.

Two more choices follow from team use. A teammate or lead can review a plan or
report using the same checklists the assistant uses, so the team shares one
quality bar. And the team profile and library hold no participant names or
contact details; participant tracking stays in the team's own research
operations tools.

## Building in best practice

Best practice goes into the build as testable standards, not as general advice
in a prompt. Each standard is a criterion the assistant applies, a check can
verify and an eval can test.

1. **Standards per stage.** Each stage file lists what "good" looks like as
   concrete criteria. Example for a guide: questions ask about past behaviour
   rather than hypothetical future behaviour, and none suggests an answer.
2. **Each standard names its basis.** A standard links to the public source it
   comes from. If no verifiable source exists, it's marked as practitioner
   judgment.
3. **Method guides carry the pitfalls.** Each method guide lists its common
   failure modes.
4. **Evals test the standards.** Each standard gets at least one test scenario
   with a planted problem, and a release fails if the assistant misses it.
5. **A practice review cycle.** The standards are reviewed on a regular
   schedule, starting at twice a year, and contributors can propose changes
   with a cited source.

Sources are listed in `docs/PROVENANCE.md` as they are checked and used.

## Usability of the tool itself

The tool should help every researcher use it well, without reading a manual.
It follows the same standards it teaches.

- **Start anywhere.** A researcher can begin with a vague ask, a decision, a
  deadline or a pile of transcripts. The assistant works out which stage fits
  and says so.
- **Say what happens next.** Each reply ends by naming the next step and what
  the assistant needs for it.
- **Show the record.** The study record is visible on request and the
  assistant says what changed in it after each stage.
- **Few commands.** A short set of plain phrases does everything: "skip",
  "show the record", "push me", "ease off", "just the work". The assistant
  also understands those asked in ordinary words.
- **Recover gracefully.** If a researcher changes the decision mid-study, the
  assistant lists what else has to change and offers to update it.
- **Short by default.** Replies are brief and offer more on request.
- **Tested with real researchers.** Before launch, a handful of researchers
  use the tool on a real study. Their observed problems feed the evals.

## Plain language

Plain language is the standard for everything the tool says and everything it
drafts. A reader should get the point on the first pass.

- Short sentences, everyday words, and the specific thing named rather than a
  category.
- Research terms only when they're needed, and always with a one-line
  explanation the first time.
- No filler, hype or ornamental words. "Big" beats "substantial". "Use" beats
  "leverage".
- Outputs lead with the answer and the decision it serves, then the evidence.
- A plain-language check is one of the standards, with its own eval.

## Personality

The assistant has a light, warm sense of humour. Research is serious, but the
experience shouldn't feel like filling in a form.

- **Where humour lives:** small asides, the way it reacts to a skipped
  challenge, a dry comment when a stakeholder request is vague, the occasional
  self-aware line about being an assistant.
- **Where humour never goes:** findings, numbers, quotes, confidence labels,
  risks, consent or ethics, and any moment the researcher is under pressure or
  something has gone wrong.
- **Never at the researcher's expense.** It can tease a vague brief or a
  tangled survey question, never the person.
- **Clear over clever.** If a joke would make a sentence harder to read, the
  joke goes.
- **Adjustable.** "Just the work" turns the personality off for the session,
  and the team profile can set it off by default.
- **Honest about itself.** It says plainly when it doesn't know something, when
  evidence is thin, or when it has made an error.

The voice is written in `core/voice.md` with example lines, so it stays
consistent across platforms.

## Method coverage for v1

| Method | Best for | Analysis support |
| --- | --- | --- |
| Interviews | Understanding needs, motivations, workflows | Thematic analysis, affinity mapping |
| Contextual inquiry | Seeing real work in its setting | Workflow and breakdown mapping |
| Moderated usability testing | Finding why people struggle with a design | Issue severity and frequency |
| Unmoderated usability testing | Task success at larger sample sizes | Success rates, time on task, clips |
| Surveys | Measuring how common an attitude or behaviour is | Descriptives, cross-tabs, open-end coding, cautions on significance claims |
| Concept and value testing | Early direction before building | Reaction patterns, value and fit signals |
| Diary studies | Behaviour over time | Longitudinal themes |
| Card sorting and tree testing | Information architecture | Similarity patterns, findability |
| Evidence review | Reusing what is already known | Evidence brief |
| Competitive analysis | Seeing how other tools solve the same job, and what would fit your users | Fit matrix, patterns, fit assessment |
| Stakeholder workshops | Aligning on the problem, ideating from findings | Synthesis of workshop outputs |

## Architecture

All research knowledge lives once, in a plain-Markdown core. A build script
packages that core for each platform. Quality checks are written as checklists
inside the core, so they work even on platforms that can't run code or
separate review agents.

```
core/
  stages/        one file per stage: goal, inputs, what to draft, challenges, exit criteria
  workshops/     agenda patterns and activities
  methods/       one guide per method, with pitfalls
  standards/     what good looks like per stage, each with its source
  challenges/    the challenge bank
  checks/        guide wording, survey wording, claim strength, ethics and consent
  partners/      request templates for analytics, field, support and other teams
  templates/     study record, plan, guides, survey, readout, report, workshop agenda
  team/          team profile, intake form, research library entry
  voice.md       the assistant's voice, with example lines
tools/           build script and code checks: quote matching and attribution, counts, the receipts behind counts
adapters/
  skill/         one skill folder (SKILL.md, core files, scripts) that
                 Claude, ChatGPT and Gemini all accept
  claude/        setup notes for Claude Code and Claude.ai
  chatgpt/       setup notes for ChatGPT skills, and the fallback
  gemini/        setup notes for Gemini skills, and the fallback
  generic/       one system prompt for any other assistant
evals/           test scenarios with planted problems
docs/            DESIGN.md, PROVENANCE.md, CONTRIBUTING.md, CHANGELOG.md
```

Only the core is edited by hand. `tools/build.py` regenerates the adapters
from it, and the generated adapters are committed so people can use them
without running anything.

The original plan was a Custom GPT and a Gem. When Phase 4 checked the
platform docs (October 2026), both had moved: OpenAI is retiring Custom GPTs
and Google is replacing Gems with skills, and both now take a folder with a
`SKILL.md` file plus supporting files, the same shape as a Claude skill. So
there is one skill package instead of three adapters, and a short setup
note per platform. Platform limits still differ and change often; each
setup note records what was checked and when.

## Build phases

1. **Foundation.** README, this design, the provenance record, the license,
   the study record template and the build script.
2. **Plan the study.** Stages 1 to 5, the challenge bank, the checks, guides
   for interviews, usability testing and surveys, the voice, the generic
   adapter and the Claude adapter. Includes eval scenarios.
3. **Analysis and reporting.** Stages 6 and 7, the independent review, the
   workshop branch and the remaining methods.
4. **Other platforms.** One skill package for Claude, ChatGPT and Gemini,
   with setup notes per platform. Test runs on ChatGPT and Gemini are still
   to do.
