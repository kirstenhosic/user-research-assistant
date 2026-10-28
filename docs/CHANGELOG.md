# Changelog

## 2026-10-28

- One look throughout each file (A.23).
  - The Word converter gives team notes a shaded Note style, turns
    `[ ]` and `( )` answer options into ☐ and ○, shades table headers,
    sizes columns to their content, shows a Document details table as a
    titled block, and adds a footer with title, status and page number.
    A wrapped line that starts with a number now stays in its paragraph
    instead of breaking the question numbering.
  - Sheets get a document details block, taller note rows and extra
    small tables (such as merged and dropped codes).
  - The survey template keeps every team note in one section at the end;
    guide moderator notes get subheadings; the usability script's opening
    and questions are spoken lines and numbered like the guide.
- Independent checks on questions, and on the deck as well as the report.
  - New question review (`core/review/question-review.md`), required at
    stage 5 for every guide, script, survey and set of prompts, run the
    same way as the findings review: a separate agent where one can be
    started, a fresh-chat paste otherwise. It checks leading,
    double-barrelled, hypothetical and closed questions, survey item
    rules, conversation order, spoken style, coverage of the research
    questions, and the research questions themselves.
  - New research-question check (`core/checks/research-questions.md`) at
    stage 2.
  - Scripts are written the way a person speaks: the opening, the warm-up,
    every question and a spoken transition at each change of topic. The
    guide wording check gains a conversation-flow section and now covers
    focus groups, concept tests and diary prompts. The interview,
    usability and survey templates carry example transitions.
  - Stage 7: the independent review sees the readout deck as well as the
    report, and gains two questions: can every finding be traced to its
    source, and is the language plain. The claim-strength check is now a
    named step on the deck and report.
  - Standards 2.8, 5.8 and 5.9 added, 7.5 extended. Four new eval
    scenarios (not yet run).
  - Word files: guides, surveys, plans and reports come as .docx as well
    as Markdown, so colleagues can edit together. New
    `tools/export/md_to_docx.py` (standard library only, copied into the
    skill's `scripts/`) makes them; `tools/check.py` checks its output on
    a fixture. Where code can't run, Magpie uses the platform's own export
    or says to copy the draft into Word. Standard A.21, scenario
    `word-file.md`.
  - Guides, scripts and surveys open with document details (team, date,
    authors, reviewers, status: Draft, Under review or Final) and a short
    "About this guide" table in place of the dense preamble. Questions
    are numbered in one run with lettered follow-ups; survey items keep
    Q1, S1, D1. `md_to_docx.py` writes these in Word's own numbering.
  - Note-taking sheet with every interview, usability test and diary
    study (`templates/notes-sheet.md`): one row per participant, one
    column per research question, a summary row. At stage 6 Magpie offers
    a matching analysis sheet (`templates/analysis-sheet.md`) with
    evidence per participant, findings, themes and codes; "make the sheet"
    builds it. New `tools/export/make_sheet.py` writes .xlsx with the
    standard library. Standards A.22, 5.10, 6.14; A.21 extended; three new
    scenarios.
- Next steps in the report and readout templates now have three parts:
  what happens now (with the teams involved), open questions, and the
  researcher's own next steps. Magpie drafts all three from the findings
  and the record's context, and they stay "draft" until the researcher has
  reviewed and edited them.

## 2026-10-27

- Summaries and named people: the report and readout summaries now come
  from the study's own focus, goals and findings, with product and
  business impact as things to look for, not fixed sections. Templates,
  stage 7, the standards and the floating-recommendation eval now name
  the teams a recommendation touches instead of one owner, and say "the
  team" will decide. Who takes each action is left for the teams to agree;
  Magpie names a person only when the researcher asks. Stage 2 still asks
  who decides, but the plan, brief, competitive analysis and intake form
  record a team or group, not a named person.
- The example readout deck is rebuilt as a story: it opens with the answer
  and a "what we learned, and what it means" slide, adds a journey slide
  showing where export goes wrong, uses one-line titles and plainer words,
  and turns the recommendations into cards that name the teams involved.
- The example report and readout in `docs/examples/` are redone in the
  house style, with quote labels, a placeholder for a named colleague, a
  participant profile and a "How AI was used" section. Finding 5 moved
  to the other findings, and two contradictions are fixed (P5 now
  finishes the export but the file is rejected; the limits no longer say
  every participant was onboarded by CS). The Word templates are rebuilt
  from the current report and readout templates.
- A ready-made download, `magpie.zip`, at the top of the repository: the
  skill folder's contents with `SKILL.md` at the top, rebuilt by
  `tools/build.py` and checked by `tools/check.py`. The setup steps for
  every tool now start from it, so nobody has to find a folder or zip
  one themselves.
- Eval run of the eight HEARTS scenarios, three runs each, judged by the
  model (`evals/runs/2026-10-27-hearts.md`): 7 pass in all three runs;
  read-hardest is partial in all three because Magpie changed parts of a
  clean draft that needed no change. A person still has to judge them.
- Five changes from mapping Magpie to the HEARTS scorecard (Loosbrock, K.
  (2025). The HEARTS Framework: Six lenses for evaluating AI-assisted UX
  research. Hey Kaleb & Co. https://www.heykaleb.com/hearts-framework).
  - Reports and readouts get a "How AI was used" section in the
    appendix, built from the study record: what Magpie drafted, what the
    researcher did and reviewed, which checks ran and how, and any other
    AI tool in the study.
  - When an AI tool moderates, transcribes, summarizes or analyzes the
    sessions (Magpie included), the consent check and research plan say
    what participants are told about it beforehand; for an AI moderator,
    also that they'll talk with an AI and how to stop or reach a person.
  - Quotes in readouts and reports carry a short descriptor from the
    participant list after the code ("P3, finance manager, SMB"), never a
    name or company name, broadened where it would point to one person.
    The team profile can set the label.
  - With the review ask on findings, a readout or a report, Magpie names
    where to read hardest: the finding the decision leans on most and
    the one with the thinnest evidence.
  - Details that identify a participant stay out of every output; quotes
    use placeholders such as [name], and Magpie says once what it kept
    out. `quote_check.py` accepts a bracketed placeholder standing for a
    few words.
  - The independent review asks an eighth question: where the draft
    explains behaviour with assumptions about a group that participants
    didn't state.
  - A house style for readouts and reports (`templates/house-style.md`):
    numbered lists only where order or rank matters, full-sentence
    bullets, one level of bullets, three heading levels, block quotes
    with code and descriptor, recommendations grouped by role where it
    helps. The team's template still comes first; Magpie asks for it
    once, saves the answer in the record and doesn't ask again. Stage 7
    gains a first step, so its later steps move down one.
  - New standards 4.8, 6.14, 7.12, 7.13, A.19 and A.20, 6.4 and 7.11
    extended, eight new eval
    scenarios (not yet run), and a new quote-check fixture. The README
    and provenance standard counts, which had fallen behind, are
    corrected to 90 and 37.
- Fixes from the end-to-end workflow review (issues 5 to 13).
  - Save points: when a stage's drafts all have their yes, Magpie
    suggests saving the record in one line; in Claude Code it saves
    `study-record-[name].md` itself. The README says "show the record".
  - A plain "I've reviewed them" counts as the yes, and recommendations
    that come with the findings count as the stage 7 your-turn.
  - In Claude Code, Magpie searches only the open folder and folders the
    researcher names, and asks where material is instead of searching
    the whole computer.
  - Independent review outside Claude: the fresh chat has to be outside
    the Magpie project or with the skill off, and the reviewer's list is
    pasted back. The README says the review is required at analysis and
    at the report.
  - Stage 2 says the researcher doesn't have to wait for the decision
    owner's reply: "go on" continues and logs it as a risk.
  - Rule conflicts settled: "skip" on a context question builds without
    it and marks the gap; stage 4 marks guesses [assumption] and leaves
    labelled blanks only for what can't be guessed.
  - Magpie reads a team profile or intake form first if one is there,
    and the README tells new users about both.
  - `tools/build.py` rewrites core paths in the flat copies to the flat
    file names (`methods/interviews.md` becomes `methods-interviews.md`,
    `tools/checks/` becomes `scripts/` in the skill folder).
  - Gemini notes say three checks, not two.
  - New standards A.17 and A.18; A.10 and A.14 extended; three new eval
    scenarios (not yet run).
- The independent review and the quote and count checks no longer wait to
  be asked. Stages 6 and 7 say "run", not "request": Magpie starts a
  separate agent in the same reply where it can, and otherwise hands over
  the paste text in that reply. Stage 6 can't close with the review only
  "requested"; an unreturned review shows as waiting. Stage 7 checks the
  quotes and counts in the readout and report again, and runs the stage 6
  review first if it's missing. Found in a live Claude Code test where one
  report run of five waited for "review this". Standards 6.7 and 7.5
  updated, new 7.5b, new eval scenario `review-starts-itself.md` (not yet
  run).
- Fixes from the end-to-end workflow review (issues 1 to 4).
  - Setup steps agree: one way to make the zip for Copilot, with the
    troubleshooting tip no longer contradicting it; Claude.ai and the
    ChatGPT fallback both use `operating.md` as the instructions plus the
    skill folder's `.md` files; "Any other assistant" says plainly that
    the 200 KB and 115 KB prompts are too long for most chat apps.
  - Fewer asks per reply: a question message holds only the questions,
    one line on what will be built, and the status line. The product
    offer and the stage 7 reading check count toward the six.
  - "yes" stays the review word. Challenges are now open questions a yes
    or no can't answer (the challenge bank and the stage examples are
    reworded), and a bare "yes" while a best guess or challenge is open
    gets a one-line check of what it answers.
  - Picking a study back up: the study record gains a "Where we are"
    block (stage 0 to 7, next step, what's waiting for a yes, settings,
    questions already asked and how, your-turn steps and challenges
    given). A pasted record is picked up from it without re-asking what's
    settled. New standard A.16; A.6 and A.10 extended; three new eval
    scenarios (not yet run).
- Setup for Microsoft 365 Copilot. The skill folder uploads unchanged to
  Cowork, so there's a new hand-written `adapters/copilot/README.md` and
  a Copilot section in the README's setup steps. Agent Builder agents
  were checked and not used: their 8,000-character instruction limit is
  too small for Magpie's rules. Not yet tested in Copilot.
- Credit travels with every copy. `tools/build.py` now puts "Magpie was
  made by Kirsten Hosic" with the repository link and the MIT License at
  the top of `SKILL.md` and both system prompts, and a one-line credit at
  the foot of every copied file; the three scripts carry it in their
  header. The skill folder and `adapters/generic/` get a copy of
  `LICENSE`. The README names Kirsten at the top and gains a "Credit and
  license" section.
- README gains a short "Using Magpie at work" note before the setup
  steps: use Magpie at work only in an employer-approved AI tool, and
  follow your organization's data and privacy rules. The license line now
  says Magpie is an independent personal project and that the MIT License
  covers the Magpie files only. Magpie itself asks no new question.
- Magpie works out its own questions. Each stage's "Before you build"
  list is now the floor: Magpie also asks what this particular study or
  task raises (text size and setup help for a test with older
  participants, languages for a survey across countries), and works out
  the questions from scratch for a task with no stage file, such as a
  recruiting email. The six-question cap covers both. Each stage also
  names a minimum to draft (for the plan: the decision and research
  questions). When it's missing, Magpie says so first, and "just draft
  it" gets an outline with labelled blanks instead of a made-up draft
  (`core/operating.md`, "Gather context before you build"). Standards
  A.6 and A.11 rewritten, new standard A.15; three new scenarios
  (task-specific-questions, off-list-task, below-minimum), not yet run.
- README reorganized for readers: what a session looks like and setup
  come first; "What Magpie does" and "How it's built" are merged into
  one shorter list; the eight stages are listed; the methods table and
  commands table are trimmed; "Where it stands" is shorter and links to
  the test details; contributor material moves to the end.
- README brought up to date with today's changes: asking for context
  before building, the reason with each challenge, teaching without
  testing, the vague-word push, the three "your turn" steps, the method
  and guide reasoning you can counter, and the theme review. The commands
  table gains "just draft it", "you do it", "counter", "handled" and
  "standard". The standards count is corrected to 36 of 77 citing a
  source, in the README and `docs/PROVENANCE.md`.
- Coaching borrowed from Dr. Morgan's coach mode, in one way of working
  (`core/operating.md`, "Teach as you go" and "Your turn"). Every
  challenge now comes with one plain sentence on why it matters, said once
  per conversation; Magpie never quizzes. Vague words ("users struggled",
  "confused", "most") get a one-line push, and reading evidence only for
  support is named as confirmation bias. At three steps the researcher
  goes first: the decision, primary question, existing research questions
  and assumptions (stage 2), the patterns they saw before coding (stage
  6), and what each partner should do (stage 7); "you do it" hands a step
  back. At stage 3 the method comes with its reasoning shown, and at
  stage 5 the guide comes with a map of what each question serves and why
  it sits where it does; the researcher can counter either, and Magpie
  reworks or answers in a line. Stage 6 adds a theme review:
  themes shown riskiest first with merged and dropped codes, and a keep,
  change, split or drop on each. The study record gains a Themes section.
  New standards A.12, A.13, A.14, 3.7, 5.7 and 6.13; seven new scenarios
  (challenge-reason, vague-words, your-turn-decision, you-do-it,
  theme-review, method-reasoning, question-order), not yet run; pm-first-time, nothing-to-start-with and
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
