# Changelog

## 2026-10-27

- Coaching borrowed from Dr. Morgan's coach mode, in one way of working
  (`core/operating.md`, "Teach as you go" and "Your turn"). Every
  challenge now comes with one plain sentence on why it matters, said once
  per conversation; Magpie never quizzes. Vague words ("users struggled",
  "confused", "most") get a one-line push, and reading evidence only for
  support is named as confirmation bias. At three steps the researcher
  goes first: the decision and primary question (stage 2), the patterns
  they saw before coding (stage 6), and what each partner should do
  (stage 7); "you do it" hands a step back. Stage 6 adds a theme review:
  themes shown riskiest first with merged and dropped codes, and a keep,
  change, split or drop on each. The study record gains a Themes section.
  New standards A.12, A.13, A.14 and 6.13; five new scenarios
  (challenge-reason, vague-words, your-turn-decision, you-do-it,
  theme-review), not yet run; pm-first-time, nothing-to-start-with and
  readout-without-audience updated.
- Magpie says it's on at the start of a conversation, stays on for the
  rest of it without being called again, and ends every reply with a
  status line showing the stage, anything waiting for review, and the next
  step. "stop Magpie" ends the session (`core/operating.md`, "The
  session"). Standard A.9, scenario `session-persists`.
- Every output Magpie drafts waits for the researcher's "yes". Asked once
  in one line, tracked in a new Outputs table in the study record and in
  the status line. A readout or report stays labelled "draft" until it and
  its findings have a yes. Standards A.10 and 7.10, scenario `review-yes`.
- Every count lists the participants and lines behind it ("3 of 8 (P1 06,
  P5 06, P7 06)"). New `tools/checks/evidence_check.py` checks the list
  matches the count, every code is a real participant, and every cited
  line exists and is that participant speaking. Standard 6.11, scenario
  `uncoded-count`.
- `quote_check.py` now checks who a quote is credited to: a quote found
  only in another participant's transcript, or in the interviewer's lines,
  is flagged. It also lists short quoted text it didn't check, and pairs
  quote marks correctly when a short quote comes first. Standard 6.4
  extended, scenario `misattributed-quote`.
- Evals can now fail in the ways that matter: each run proves Magpie was
  loaded, runs one scenario without Magpie to test that proof, keeps
  answers and project notes out of the session, runs each scenario three
  times, and has a person judge at least ten replies. New run template
  (`evals/runs/TEMPLATE.md`) and a clean fixture with no planted problems
  (`evals/fixtures/sparrow-clean/`) to count false alarms. The 27 October
  run is marked unconfirmed.
- Stage 7's last two steps were both numbered 15; fixed.
- Context before the work. Magpie now asks for the context an output
  needs before it builds it, instead of drafting from guesses first. Each
  stage file from 0 and 2 to 7 has a "Before you build" list (for
  example, the plan needs the decision, goal, hypotheses, participants,
  consent rules and dates; the readout needs its audience, format and
  template). Magpie asks only for what's missing, in one message, six
  questions at most, offering best guesses to confirm; then it builds the
  whole output and adds one challenge. "Just draft it" builds straight
  away with gaps marked [assumption] and logged as risks. The study record
  and research plan gain a Hypotheses section; stage 2 records them and
  stage 6 marks each supported, contradicted or not addressed. Standards
  A.1, A.6 and A.7 rewritten; new standards 2.7, 6.12, 7.11 and A.11.
  Evals question-cascade, pm-first-time and nothing-to-start-with
  rewritten; three new (just-draft-it, readout-without-audience,
  hypothesis-check), not yet run. README, design notes, prompt style and
  voice updated.
- Product context, optional. The study record opens with a Product
  section: what the product is, what it does, the part under study, its end users, its
  buyers or admins if different, where it stands and recent changes.
  Magpie offers it once, early, drafting from the team profile, product
  docs or what the researcher said; if the researcher declines, it works
  without it and doesn't ask again. Where it's filled, stages 1 to 7 use
  it (freshness, framing, method choice, recruiting end users,
  tasks in participants' words, roles in analysis, a product line in the
  readout). The plan, readout and report templates, the intake form and
  the team profile gain a product line. Standards 2.6 and 4.7 and one
  eval scenario (unknown product, not yet run).
- Four new method guides: focus groups, participatory design (co-design),
  field studies and expert review (heuristic evaluation and cognitive
  walkthrough). A new lens for including disabled people and assistive
  technology users, applied at planning, drafting, sessions and analysis.
  Stages 3, 4 and 5, contextual inquiry and the workshop guide point to
  them. Interviews gain ratings with a "why that number?" follow-up;
  usability testing gains a post-task ease rating with "why that
  rating?", a debrief, and guidance on SUS; both templates updated.
  Standards 3.5, 3.6 and 4.6, four eval scenarios (focus group asked for,
  expert review as evidence, no access plan, averaged ratings, not yet
  run), and ten sources (S31–S40) read and recorded.
- Readouts and reports keep up to five top findings and add an "Other
  findings" slide and section for every other finding that met the
  evidence bar, tagged "unexpected" where it fell outside the research
  questions, so nothing is dropped. Stage 6 and 7 guides, readout and
  report templates, standard 7.1, three eval scenarios, README and the
  examples (Markdown, Word and PowerPoint) updated.
- GitHub Actions workflow runs `tools/check.py` on every pull request and
  push to main, so the maintenance check shows as a status on the PR.
- README reviewed for plain language and American English spelling,
  punctuation and dates.
- README: a methods table saying what each of the eleven methods is for
  and what Magpie gives you, a "How it's built" section with the five
  ideas behind it, and a dated "Where it stands" section with what has
  been tested, what backs the rules, what hasn't been tested and how to
  report a problem. A work-in-progress line under the title.
- First recorded eval run: all 36 scenarios run blind in Claude Code and
  judged against their pass and fail lists (`evals/runs/2026-10-27.md`):
  31 pass, 5 partial with reasons, 0 fail. One rule added from it: when the
  researcher uses no research vocabulary, Magpie gives the stage as a plain
  phrase and leaves stage numbers and commands out (`core/operating.md`).
- Two fixture studies with answer keys under `evals/fixtures/`: Harbor
  trial invites (8 interviews, 11 planted traps) and Tally receipt capture
  (6 usability sessions, 12 traps). The code-check tests now run against
  them.
- Eighteen more standards cite a source (34 of 60), all from pages read on
  the open web: Nielsen Norman Group articles, the GOV.UK Service Manual
  and the GOV.UK content principles (S11 to S30 in `docs/PROVENANCE.md`).
  Where a page supports only part of a standard, the basis says so.
- S10 (Papas) citation completed with publisher and edition dates.
- `docs/examples/`: a fictional filled-in report and readout, the two
  templates as Word files and the readout as a PowerPoint deck.
- README says where Magpie has and hasn't been tested, in one place.
- AI-assisted research check (`core/checks/ai-assisted-research.md`), from
  a passage of Papas, *AI-Powered UX Research* (S10) supplied by the
  author: AI moderators get a wording check, scope boundaries, a fallback
  for unclear answers and a first-three-transcript audit; AI summaries,
  Magpie's own included, are drafts until a person has read the passages;
  receipts (two participant references or a labelled single case) before
  any finding reaches a readout; participant quality planned (fraud risk,
  threshold, replacement) and screened before coding. Standards 4.5, 5.6,
  6.10, 7.9 with three eval scenarios.

## 2026-10-26

- Lessons from an assessment of the earlier tool (see `docs/PROVENANCE.md`,
  Disclosure): `tools/check.py` maintenance check with fixture tests for the
  code checks; the independent review capped at two passes and told to
  start with the riskiest finding; "a record is not evidence" rule for
  resumed studies; a reader test at stage 7; standards 7.7, 7.8, A.7, A.8
  with three new eval scenarios (PM first time, reader test, record as
  evidence); `core/standards/` no longer shipped in the adapters; a lean
  generic prompt (rules, stages, lenses, checks) for assistants with short
  instruction limits.
- README rewritten for a first-time user: what Magpie does, setup steps
  per tool (Claude Code, Claude.ai, ChatGPT, Gemini, anything else), a
  first conversation, the plain commands, and troubleshooting.
- Sources: nine public sources checked and recorded in `docs/PROVENANCE.md`
  (ICC/ESOMAR code 2025, Braun and Clarke, six Nielsen Norman Group
  articles); 12 standards now cite one in full or in part. The rest stay
  practitioner judgment.
- Phase 4: one skill package at `adapters/skill/magpie/` replaces the
  planned Custom GPT and Gem adapters, since both platforms now take the
  same `SKILL.md` folder format (and are retiring GPTs and Gems). Setup
  notes for Claude, ChatGPT and Gemini under `adapters/`, with the limits
  checked and the date. Scripts moved to `scripts/` inside the skill.
- Phase 3: stages 6 and 7, the independent review, the claim-strength check,
  stakeholder workshops, five more method guides (contextual inquiry, concept
  testing, diary studies, card sorting and tree testing, evidence review),
  readout, report and workshop templates, team profile, intake form and
  library entry, standards for stages 6 to 7, eleven more eval scenarios,
  and two code checks (quotes, counts). Readout and report templates
  reshaped around Kirsten's readout and report principles. A larger-system
  lens (systems thinking, company goals, jobs to be done, journeys and
  personas) added to framing, analysis and readout. Market research as
  indirect evidence, and an optional stage 0 for finding research
  opportunities with an opportunity brief template. A where-to-look guide
  for collecting evidence, with a use-what-you-can-reach rule. Competitive
  analysis added as the eleventh method, with a fit-matrix template.
  Prompts revised against the platforms' current prompt-writing guidance:
  explicit precedence (the researcher wins, two fixed points), rules with
  their reasons, draft-before-asking, specific reply sizing, the review
  prompt reordered to material first, a say-this-not-that voice table, and
  `docs/PROMPT-STYLE.md` recording the conventions and sources.
- Phase 2: operating rules, voice, stages 1 to 5, the challenge bank, three
  checks, three method guides, partner request templates, four instrument
  templates, standards for stages 1 to 5, twelve eval scenarios, and the
  Claude skill adapter.
- Phase 1: design, provenance record, contributing guide, study record
  template, build script and the generic adapter it generates.
