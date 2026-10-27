# Magpie

Magpie is a free, open-source research helper for user researchers. You
run it inside the AI assistant you already use (Claude, ChatGPT, or Gemini).
It works with you on a study from the first question, "Do we already know
this?", through framing the problem, choosing a method, writing the plan
and the interview guide, to analysis and a report your product manager,
designer, and engineer can act on.

Why a magpie: it collects the shiny bits of evidence that already exist,
then helps you figure out which ones matter for the decision in front of you.

**Work in progress.** Tested in Claude Code; not yet on Claude.ai, ChatGPT,
or Gemini. See [Where it stands](#where-it-stands) before you rely on it.

## What Magpie does

- **Starts wherever you are.** Bring a vague request from a stakeholder, a
  deadline, a half-written plan, or a folder of transcripts. Magpie figures
  out which stage you're at and picks up from there.
- **Drafts first, then asks one good question.** Every reply gives you
  something you can use right away (a plan, a guide, a set of findings),
  then one question worth thinking about. You can skip it; Magpie notes
  the skip as a risk and moves on.
- **Keeps a study record.** One document that carries the decision, the
  questions, the method, the participants, the findings, and the risks. Save
  it and you can continue in any assistant, any day.
- **Labels where every claim comes from.** Your data, a partner team's data,
  general practice, or an assumption. It never makes up a quote, a number,
  or a participant.
- **Writes for stakeholders.** Readouts (the presentation of findings) and
  reports follow a tested shape: why first, a short note on method, up to five
  top findings, the other findings on one page so nothing is dropped,
  recommendations with owners, next steps, appendix.
- **Covers eleven methods.** The table below says what each one is for
  and what Magpie gives you.

## What you can do with it

Each method has a guide that Magpie reads when you choose it, and most
have a template it drafts from. Tell Magpie what you're trying to learn and
it will suggest a method. You can also name one yourself.

| Method | Use it to learn | What Magpie gives you |
| --- | --- | --- |
| [Interviews](core/methods/interviews.md) | How people do something, why, and what gets in the way | A research plan, an interview guide with a wording check, themes with counts and participant references |
| [Usability testing](core/methods/usability-testing.md) | Where and why people struggle with a design, with or without a moderator | A test script with task scenarios and success criteria, a list of problems by how serious and how common they were |
| [Surveys](core/methods/surveys.md) | How common an attitude, behavior, or need is | A survey draft with a wording check, an analysis plan, and warnings about small numbers, who answered, and the word "significant" |
| [Contextual inquiry](core/methods/contextual-inquiry.md) | How real work happens in its real setting | A plan, question prompts, an observation sheet, and a map of the workflow and where it breaks down |
| [Concept and value testing](core/methods/concept-testing.md) | Whether an idea solves a problem people have, before it's built | A session guide and patterns in how people reacted, with a reminder that "I'd use it" is not the same as using it |
| [Diary studies](core/methods/diary-studies.md) | Behavior over days or weeks, as it happens | Entry prompts, an exit interview guide, and themes over time |
| [Card sorting and tree testing](core/methods/card-sorting-and-tree-testing.md) | How people group and name things, and whether they can find them | A card list and task list, and findings on how people group things and whether they can find them |
| [Evidence review](core/methods/evidence-review.md) | What the organization already knows, before running anything new | An evidence log with how fresh and how trustworthy each source is, a summary of the gaps, and a one-page evidence brief |
| [Competitive analysis](core/methods/competitive-analysis.md) | How other tools solve the same job, and what would fit your users | A comparison table built around the user's job, not the feature list |
| [Stakeholder workshops](core/workshops/stakeholder-workshops.md) | Agreement on the problem, or actions from findings, with PM, design, and engineering | A workshop agenda with quiet writing time, named owners, and a read-back of what was decided, plus a summary afterward |
| [Finding opportunities](core/stages/00-find-opportunities.md) | Where company goals, market signals, and user signals overlap, when nobody has asked yet | Short opportunity briefs, each with a decision and an owner |

Whatever the method, the study ends the same way: findings with counts and
participant references, a readout, a report, and research library entries,
drafted from the templates in [`core/templates/`](core/templates/). A finished
example is in [`docs/examples/`](docs/examples/).

## How it's built

Five ideas run through everything Magpie does. The reasoning behind each is
in [`docs/DESIGN.md`](docs/DESIGN.md).

1. **Draft first, then one challenge.** Every reply gives you something you
   can use, then asks one question that could change it. You can skip the
   question; the skip is noted as a risk, not argued.
2. **One study record.** The decision, questions, method, participants,
   findings, and risks live in one document that you own and can take to
   any assistant.
3. **Every claim says where it came from.** Your data, a partner team's
   data, general practice, or an assumption. Magpie never makes up a quote,
   a number, or a participant, and two small scripts check quotes and
   counts against the transcripts.
4. **An independent review before anything reaches stakeholders.** A
   second pass that sees only the transcripts and the draft, not the
   conversation that produced them, for the analysis and the final report.
5. **Written for the people who have to act.** Readouts and reports lead
   with the decision, keep to five findings, and give every recommendation
   an owner.

## Where it stands

As of October 27, 2026. This section is updated with each release.

- **Tested.** All 36 test scenarios in [`evals/scenarios/`](evals/scenarios/)
  were run in Claude Code without access to the answers, then judged
  against their pass and fail lists: 31 pass, 5 partial with reasons, 0
  fail. Two made-up studies with answer keys in
  [`evals/fixtures/`](evals/fixtures/) were run the same way, and every
  planted problem was caught. The results, and the limits of this method
  (the judge was the same kind of AI model), are in
  [`evals/runs/2026-10-27.md`](evals/runs/2026-10-27.md).
- **What backs the rules.** Magpie follows 60 written standards in
  [`core/standards/`](core/standards/). 34 cite a public source in full or
  in part (the ICC/ESOMAR code, Braun and Clarke, Nielsen Norman Group
  articles, the GOV.UK Service Manual). The rest rest on professional
  judgment and say so. [`docs/PROVENANCE.md`](docs/PROVENANCE.md) lists
  every source and how Magpie was made.
- **Not yet tested.** Claude.ai, ChatGPT, and Gemini from start to finish.
  The setup steps for those come from each company's help pages, checked
  on October 26, 2026, so expect small differences. Long conversations:
  most scenarios test one reply.
- **Known limits.** Magpie can be wrong in the same ways any AI assistant
  can, and the independent review is done by an AI too. The study record
  and the participant references exist so you can check its work. Please
  do.
- **Found a problem?** Open an issue with the tool you used, the step, and
  what you saw. Changes are listed in
  [`docs/CHANGELOG.md`](docs/CHANGELOG.md).

## Before you start

You need one of these:

- Claude Code (the command-line tool or its desktop app), or a Claude.ai
  account with Projects.
- A ChatGPT Business, Enterprise, or Edu account. Personal ChatGPT plans
  may not be able to add skills yet; see the ChatGPT section.
- A Google account, signed in to Gemini, with Keep Activity turned on.

Magpie has been tested in Claude Code and not yet on the other three; see
[Where it stands](#where-it-stands).

Then download Magpie. Either click the green **Code** button on this page
and choose **Download ZIP**, or run:

```
git clone https://github.com/kirstenhosic/user-research-assistant.git
```

Inside, the folder you'll use is `adapters/skill/magpie/`. It's all of
Magpie in one place: a `SKILL.md` file that tells the assistant how to
behave, the files it reads at each stage, and two small scripts that check
quotes and counts.

## Set it up in your tool

### Claude Code

1. Open your project in Claude Code.
2. Copy the folder `adapters/skill/magpie/` into your project's
   `.claude/skills/` folder, so you end up with
   `.claude/skills/magpie/SKILL.md`. Create `.claude/skills/` if it isn't
   there.
3. Start a conversation and ask for help with a study, or just say
   "magpie". Claude loads the skill on its own.

If you open this repository itself in Claude Code, skip step 2; the skill is
already in place.

### Claude.ai

1. Create a new Project.
2. Add the files from `adapters/skill/magpie/` to the project's knowledge
   (all the `.md` files; the scripts are optional, since Claude.ai can't
   run them).
3. Open the project's instructions and paste the contents of
   `adapters/skill/magpie/operating.md`. That's the rulebook; the rest are
   reference files Claude reads when it needs them.
4. Start a chat in the project and describe your study.

### ChatGPT

OpenAI is retiring Custom GPTs. The current way to add Magpie is as a
skill, which OpenAI's help center lists for Business, Enterprise,
Healthcare, and Edu workspaces (checked October 26, 2026). If you're on a
personal plan, try the steps anyway; if the Skills page isn't there, use
the fallback below.

1. In the ChatGPT sidebar, open **Plugins**, then the **Skills** tab.
2. Choose **Create** > **Upload from your computer** and upload the
   `adapters/skill/magpie/` folder (zip it first if the uploader asks for a
   single file).
3. ChatGPT scans the upload. If it says **Needs Review**, read what it
   flags. The only code in the package is two scripts that read files on
   your computer; nothing connects to the internet.
4. Install it. Then start a chat and @-mention `magpie`, or just describe
   your study.

**Fallback for personal plans:** create a Project, paste
`adapters/skill/magpie/operating.md` as the project instructions, and add
the other `.md` files from the folder as project files.

### Gemini

Google is replacing Gems with skills, which take the same folder.

1. Go to gemini.google.com. In the sidebar, open **Customize** (it may be
   under **More**), then **Skills**.
2. Choose **Create** > **Upload** and pick the `adapters/skill/magpie/`
   folder, or a zip of it.
3. Check the name, description and instructions Gemini shows, then
   **Create**.
4. In a chat, type `/magpie` (or `@magpie`), or just describe your study.

Uploading works in the web app and the Mac app, not the phone apps. Using
a skill in a chat doesn't need a paid plan.

### Any other assistant

Paste `adapters/generic/system-prompt.md` as the system prompt or custom
instructions. It's one long file with everything in it. If the assistant
says it's too long, paste `adapters/generic/system-prompt-lean.md` instead
(the rules, stages and checks, about half the size) and upload the files
in `adapters/generic/files/` so Magpie can open the method guides and
templates when it needs them.

## Your first conversation

Tell Magpie what you've got, in your own words. Three examples that work:

> A PM wants to know if we should build an onboarding checklist. We have
> some old interviews from last year somewhere. Deadline is two weeks.

> Here are eight interview transcripts. Help me find what matters.

> I want to propose research for next quarter but I don't have a brief.

Magpie names the stage it thinks you're at, drafts the first thing you
need, and ends every reply with the next step. If it guesses wrong, say so
and it adjusts.

A few plain words steer it:

| Say | Magpie does |
| --- | --- |
| skip | Notes the current question as a risk and moves on |
| push me | Asks up to three questions per stage instead of one |
| ease off | Only raises red flags (consent, leading questions, claims the evidence can't support) |
| just the work | Turns off the personality for the session |
| show the record | Shows the full study record |
| review this | Runs an independent review of your findings or report |
| back to stage 3 | Returns to that stage and says what depends on it |

**Save your study record.** At the end of a session, ask for the record
and paste it into a document. Next time, paste it back and Magpie picks
up where you left off, in any assistant.

## When something goes wrong

- **The assistant doesn't seem to know Magpie.** In Claude Code, check the
  path is exactly `.claude/skills/magpie/SKILL.md`. In ChatGPT or Gemini,
  check the skill is installed and active, then name it in the chat.
- **It won't take the upload.** Zip the `magpie` folder and upload the zip.
  Make sure `SKILL.md` is at the top level inside the zip.
- **It drafted the wrong stage.** Say which stage you're at ("we're at
  stage 4, planning") and it switches.
- **The quote or count check didn't run.** Not every assistant can run
  scripts. When it can't, Magpie does the check by reading and says so in
  the record.
  You can run the scripts yourself with Python:
  `python3 adapters/skill/magpie/scripts/count_check.py findings.md`.

See [Where it stands](#where-it-stands) before reporting a problem with a
particular platform.

## What's in the repository

```
adapters/skill/magpie/   the skill folder you install (generated)
adapters/generic/        one long prompt for any other assistant (generated)
adapters/claude|chatgpt|gemini/   setup notes per platform, with what was checked and when
core/                    everything Magpie knows, in plain Markdown (edit here)
tools/                   the build script and the quote and count checks
.github/workflows/       runs tools/check.py on every pull request
evals/                   test scenarios with planted problems
docs/                    design, provenance, contributing, prompt style, changelog
docs/examples/           a filled-in report and readout (Markdown, Word, PowerPoint)
```

`docs/examples/` shows what a finished report and readout look like, with
the templates as Word files and the example readout as a PowerPoint deck.

To change Magpie, edit `core/` and run `python3 tools/build.py`. The
adapters are rebuilt from it. `docs/CONTRIBUTING.md` has the rest.
`docs/DESIGN.md` explains how Magpie is built and why, and
`docs/PROVENANCE.md` records how it was made and which sources back its
standards.

Licensed under the MIT License. See `LICENSE`.
