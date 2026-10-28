# Magpie

Magpie is a free, open-source research helper for user researchers. You
run it inside the AI assistant you already use (Claude, ChatGPT, Gemini, or
Microsoft 365 Copilot).
It works with you on a study from the first question, "Do we already know
this?", to a report your product manager, designer, and engineer can act
on. It's built for researchers, and for PMs and designers doing their own
research.

Made by Kirsten Hosic.

Why a magpie: it collects the shiny bits of evidence that already exist,
then helps you figure out which ones matter for the decision in front of you.

**Work in progress.** So far Magpie has been tested only in Claude Code.
See [Where it stands](#where-it-stands) before you rely on it.

Ready to try it? Jump to [Get started](#get-started).

## What a session looks like

Tell Magpie what you've got, in your own words. For example:

> A PM wants to know if we should build an onboarding checklist. We have
> some old interviews from last year somewhere. Deadline is two weeks.

> Here are eight interview transcripts. Help me find what matters.

> I want to propose research for next quarter but I don't have a brief.

Magpie says it's on and names the stage it thinks you're at. Before it
builds anything, it asks a few short questions about what it doesn't know
yet. Then it builds the output in full, asks one question worth thinking
about, and asks you to reply "yes" once you've reviewed it. Every reply
ends with a status line, so you can see Magpie is still running:

> Magpie · Planning the study · Waiting for your yes: research plan · Next: send me the recruiting criteria

From the guide stage on, the status line also shows whether each required
review is done, waiting or not yet, so you know what has had a fresh look
before you say yes:

> Magpie · Analyzing the sessions · Waiting for your yes: findings · Reviews: questions done · findings waiting · Next: paste the review

If it guesses the stage wrong, say so and it adjusts. You call Magpie once
per conversation; it stays on until you say "stop Magpie".

## What Magpie does

- **Starts wherever you are.** A vague request, a deadline, a half-written
  plan or a folder of transcripts: Magpie works out which stage you're at
  and picks up from there.
- **Asks before it builds.** Before a plan, a guide, findings or a report,
  it asks up to six short questions about what it doesn't know, such as
  your hypotheses, the business goal and who will read it, plus the ones
  your study raises. A research plan from scratch gets up to three short
  rounds: the problem, then the method, then the logistics. Share a PRD,
  brief or past research and Magpie reads it first and asks only what it
  doesn't answer.
- **Drafts nothing on guesses you haven't seen.** Some questions are
  required. Magpie drafts nothing until each one has your answer, or a
  guess from Magpie that you've said yes to. Say "just draft it" to skip
  the optional questions. If a required answer is still missing, Magpie
  shows its best guesses first, and one "yes" from you is enough.
- **Coaches as it works.**
  - After each output it asks the one question most likely to change it,
    and says in a sentence why it matters. You can skip it.
  - It explains each research principle once and never quizzes you.
  - It asks what vague words like "confused" or "most" stand for.
  - When it sharpens your research question or hypothesis, it shows your
    version next to its own with the reason, in a short table.
  - At three steps you go first: framing the problem, spotting patterns in
    analysis, and deciding what each partner should do. Say "you do it" to
    hand a step back.
  - It shows why it chose a method and why the guide's questions sit in
    that order, and you can push back.
  - Before it picks a method, it checks four things: the kind of
    question, whether you need what people say or what they do (it leans
    on what they do), where the product stands, and the setting. If your
    question has two halves, such as "how many" and "why", it may suggest
    a second method for the other half. It always says what you'll have
    at the end.
  - In analysis, you keep, change, split or drop each theme it proposes.
- **Says where every claim comes from.** Your data, a partner team's data,
  general practice, or an assumption. It never makes up a quote, a number,
  or a participant, and every count names the participants behind it.
- **Says how sure it is, and how much each finding matters.** These are
  two separate labels. Confidence (strong, moderate or weak) comes with a
  one-line reason: how many people, how well they match your users, and
  whether the behavior was seen, told as a real past event, or only an
  opinion. Priority comes from impact and reach. A finding that matters a
  lot but rests on weak evidence is marked "check next". Findings are
  shown in priority order, and Magpie asks if the order matches yours.
- **Keeps a study record.** One document holds the product and its users
  (if you want to add them), the decision, questions, method, participants,
  findings and risks. Save it and you can continue in
  any assistant, any day.
- **Gives you files your team can edit.** Guides, surveys, plans and
  reports come as a Word file as well as Markdown, with the team, authors,
  reviewers and status at the top and numbered questions, so colleagues
  can comment and edit together. Guides come with an Excel note-taking
  sheet, one column per research question, and analysis offers a
  matching sheet of findings, themes and codes. In Claude Code this is automatic. Elsewhere
  Magpie uses the assistant's own way to make a Word file, or tells you
  to copy the draft into Word.
- **Waits for your yes.** Nothing Magpie drafts is final until you reply
  "yes" to say you've reviewed it. Before analysis or a report reaches
  stakeholders, Magpie runs an independent review that sees only the
  transcripts and the draft. It's required at analysis and at the report
  and readout, and checks that every finding traces to its source and the
  language is plain. Interview guides and surveys get their own
  independent review for leading, double-barreled or out-of-order
  questions. Before a readout or report goes out, a release check matches
  it to where it's going (your team, the wider company, or outside): names
  and employers removed, descriptions broad enough that no one can be
  picked out, quotes used only as participants agreed, and sensitive
  findings handled as agreed.
- **Writes for the people who act on it.** Readouts and reports lead with
  why the study was done and up to five top findings, the most important
  first. Every other finding stays on one page, and each recommendation
  says which teams it touches.
- **Writes in American English.** Every output uses American spelling
  and dates written month first ("October 28, 2026"). Quotes from
  participants and the titles of sources stay exactly as they were.

The reasoning behind each of these is in [`docs/DESIGN.md`](docs/DESIGN.md).

## The stages

Magpie follows eight stages. You can start at any of them.

1. [Find the opportunities](core/stages/01-find-opportunities.md), when
   nobody has asked for research yet
2. [Check existing evidence](core/stages/02-check-existing-evidence.md)
3. [Frame the problem](core/stages/03-frame-the-problem.md)
4. [Choose the approach](core/stages/04-choose-the-approach.md)
5. [Plan the study](core/stages/05-plan-the-study.md)
6. [Draft the guide or survey](core/stages/06-draft-the-guide.md)
7. [Analyze](core/stages/07-analyze.md)
8. [Read out and report](core/stages/08-read-out-and-report.md)

## Methods it covers

Tell Magpie what you're trying to learn and it will suggest a method, or
name one yourself. Each method has a guide Magpie reads when you choose it.

| Method | Use it to learn | What you get |
| --- | --- | --- |
| [Interviews](core/methods/interviews.md) | How people do something, why, and what gets in the way | Plan, interview guide, themes with counts |
| [Usability testing](core/methods/usability-testing.md) | Where and why people struggle with a design | Test script with tasks, problems ranked by severity |
| [Surveys](core/methods/surveys.md) | How common an attitude, behavior, or need is | Survey draft, analysis plan, small-sample warnings |
| [Contextual inquiry](core/methods/contextual-inquiry.md) | How real work happens in its real setting | Plan, observation sheet, workflow map |
| [Concept and value testing](core/methods/concept-testing.md) | Whether an idea solves a real problem, before it's built | Session guide, patterns in reactions |
| [Diary studies](core/methods/diary-studies.md) | Behavior over days or weeks, as it happens | Entry prompts, exit interview guide, themes over time |
| [Field studies](core/methods/field-studies.md) | How people work in their own setting | Observation guide, rules for observers |
| [Focus groups](core/methods/focus-groups.md) | What a group of people want, in their own words | Fit check, discussion guide, analysis |
| [Participatory design](core/methods/participatory-design.md) | What matters to people, from what they make | Session plan with a making kit, themes |
| [Expert review](core/methods/expert-review.md) | Likely usability problems, before users see the design | Review plan, issue list labeled as predictions |
| [Benchmarking](core/methods/benchmarking.md) | Whether the experience is getting better, against a set point | Measures, comparison point, a plan you can repeat |
| [Analytics and A/B tests](core/methods/analytics-and-ab-tests.md) | What people do in a live product, and which version does better | Data request, test plan with guardrails, what it can't say |
| [Preference and desirability testing](core/methods/preference-and-desirability.md) | How a design looks and feels to people | Versions or word list, questions, counts with reasons |
| [Card sorting and tree testing](core/methods/card-sorting-and-tree-testing.md) | How people group and name things, and whether they can find them | Card and task lists, findings |
| [Evidence review](core/methods/evidence-review.md) | What the organization already knows | Evidence log, gaps, one-page brief |
| [Competitive analysis](core/methods/competitive-analysis.md) | How other tools solve the same job | Comparison built around the user's job |
| [Stakeholder workshops](core/workshops/stakeholder-workshops.md) | Agreement on the problem, or actions from findings | Agenda, actions with the teams involved, summary |
| [Finding opportunities](core/stages/01-find-opportunities.md) | Where company goals and user signals overlap | Opportunity briefs with a decision and the team that would make it |

Every study ends the same way: findings with counts and participant
references, a readout, a report, and research library entries, drafted
from the templates in [`core/templates/`](core/templates/). A finished
example is in [`docs/examples/`](docs/examples/).

## Words that steer it

The ones you'll use most:

| Say | Magpie does |
| --- | --- |
| yes | Marks what's waiting as reviewed |
| stop Magpie | Ends the session and offers the record to save |
| just draft it | Skips the optional questions and marks those gaps as assumptions; for required ones, shows its best guesses for your yes first |
| you do it | Takes over a step where you were asked to go first |
| skip | Notes the current challenge as a risk and moves on; on a context question, builds without it and marks the gap |

More:

| Say | Magpie does |
| --- | --- |
| counter: ... | Reworks a method choice or question order with your reasoning, or says why it would keep it |
| handled | Marks the question as dealt with, with nothing logged |
| push me | Asks up to three questions per stage instead of one |
| ease off | Only raises red flags (consent, leading questions, claims the evidence can't support) |
| standard | Goes back to one question per stage |
| just the work | Turns off the personality for the session |
| show the record | Shows the full study record |
| make the sheet | Builds the analysis spreadsheet, laid out like the note-taking sheet |
| review this | Runs an independent review of your guide, survey, findings or report |
| back to stage 4 | Returns to that stage and says what depends on it |

**Save your study record.** Say "show the record" and paste it into a
document. Magpie suggests a good moment at the end of each stage; in
Claude Code it saves the record to a file in your project for you. Next
time, paste it back and Magpie picks up where you left off, in any
assistant. The record's "Where we are" section
holds the stage, the next step and the questions you've already answered,
so Magpie doesn't ask them again.

**Optional: a team profile and an intake form.** Fill in
[`core/team/team-profile.md`](core/team/team-profile.md) once with your
products, users, goals and research rules, and attach it (or keep it in
your Claude Code folder) when you start a study. Magpie reads it first, so
it asks fewer questions every time. Send
[`core/team/intake-form.md`](core/team/intake-form.md) to PMs and
designers who ask you for research; Magpie can start from a filled one.

## Get started

First, download Magpie: **[magpie.zip](https://github.com/kirstenhosic/user-research-assistant/raw/main/magpie.zip)**
(about 180 KB). It holds all of Magpie: a `SKILL.md` file that tells the
assistant how to behave, the files it reads at each stage, and three small
scripts that check quotes, counts and the people behind each count. The
same files are in the folder `adapters/skill/magpie/` in this repository,
if you'd rather copy them from there.

**Using Magpie at work.** Magpie runs inside whichever AI assistant you
install it in, so anything you share with Magpie goes to that assistant.
If you want to try it on work projects, use it only in an AI tool your
employer has approved, and follow your organization's rules on data,
privacy and confidentiality. That includes participant data, transcripts,
recordings and anything your company treats as internal. If you aren't
sure what's allowed, ask your manager or your privacy or security team
before you start.

Then set it up in your tool. **Best results: Claude Code.** There, Magpie
runs its quote and count checks itself and starts its independent
reviewer on its own; in other tools you paste the review in by hand.
**Easiest start: Claude.ai, Gemini or Copilot.** Only Claude Code has been
tested from start to finish so far.

### Claude Code

You need the Claude Code command-line tool or its desktop app.

1. Download `magpie.zip` and open Claude Code.
2. Ask Claude Code to install it for you, for example: *"Unzip
   ~/Downloads/magpie.zip into ~/.claude/skills/magpie/"*. That's your
   personal skills folder, so Magpie works in all your projects on this
   computer. You should end up with `~/.claude/skills/magpie/SKILL.md`.
3. Start a conversation and ask for help with a study, or just say
   "magpie". Claude loads the skill on its own.

To share Magpie with a team through one project instead, put it in that
project's `.claude/skills/magpie/` folder and commit it. If you open this
repository itself in Claude Code, skip step 2; the skill is already in
place.

Folders that start with a dot are hidden. On a Mac, press Cmd+Shift+. in
Finder to show them. On Windows, turn on **Hidden items** in File Explorer's
**View** menu (under **Show** on Windows 11). Where these skill folders live, and what loads where, is
in Claude Code's [skills docs](https://code.claude.com/docs/en/skills)
(checked October 28, 2026).

### Claude.ai

You need a Claude.ai account with Projects.

1. Create a new Project.
2. Unzip `magpie.zip` and add its files to the project's knowledge (all
   the `.md` files; the scripts are optional, since Claude.ai can't run
   them).
3. Open the project's instructions and paste the contents of
   `operating.md` from the zip (about 39,000 characters). That's
   the rulebook; the rest are reference files Claude reads when it needs
   them. Don't paste `adapters/generic/system-prompt.md` here; at about
   325 KB it repeats every file you just added.
4. Start a chat in the project and describe your study.

### ChatGPT

OpenAI is retiring Custom GPTs. The current way to add Magpie is as a
skill, which OpenAI's help center lists for Business, Enterprise,
Healthcare, and Edu workspaces (checked October 26, 2026). If you're on a
personal plan, try the steps anyway; if the Skills page isn't there, use
the fallback below.

1. In the ChatGPT sidebar, open **Plugins**, then the **Skills** tab.
2. Choose **Create** > **Upload from your computer** and upload
   `magpie.zip`.
3. ChatGPT scans the upload. If it says **Needs Review**, read what it
   flags. The only code in the package is three scripts that read files on
   your computer; nothing connects to the internet.
4. Install it. Then start a chat and @-mention `magpie`, or just describe
   your study.

**Fallback for personal plans:** unzip `magpie.zip`, create a Project,
paste `operating.md` as the project instructions, and add the other `.md`
files as project files.

### Gemini

You need a Google account, signed in to Gemini, with Keep Activity turned
on. Google is replacing Gems with skills, which take the same folder.

1. Go to gemini.google.com. In the sidebar, open **Customize** (it may be
   under **More**), then **Skills**.
2. Choose **Create** > **Upload** and pick `magpie.zip`.
3. Check the name, description and instructions Gemini shows, then
   **Create**.
4. In a chat, type `/magpie` (or `@magpie`), or just describe your study.

Uploading works in the web app and the Mac app, not the phone apps. Using
a skill in a chat doesn't need a paid plan.

### Microsoft 365 Copilot

Use **Cowork** in Microsoft 365 Copilot. At work you need a Microsoft
Copilot license, and your admin has to turn Cowork on. Personal Microsoft
accounts with an eligible Microsoft 365 subscription can try it in
preview.

1. In Cowork, open **Customize** > **Skills**, choose the arrow next to
   **Add**, then **Upload skill**, and pick `magpie.zip`. It's already
   zipped the way Cowork needs, with `SKILL.md` at the top.
2. When it appears under **Your skills**, start a chat and describe your
   study.

More detail, and why Magpie isn't set up as an Agent Builder agent, is in
[`adapters/copilot/README.md`](adapters/copilot/README.md).

### Any other assistant

Upload `magpie.zip` if the assistant takes skills; it's the easiest route.
If it doesn't, but it has projects or knowledge files, set it up like
Claude.ai above: paste `operating.md` from the zip as the
instructions (about 39,000 characters) and add the other `.md` files from
the folder as files.

`adapters/generic/system-prompt.md` holds all of Magpie in one file, for
tools that take one very long system prompt, such as some API setups. It's
about 325 KB, and the lean version, `system-prompt-lean.md`, is about
180 KB. Most custom-instruction boxes in chat apps are far smaller, so
expect them to refuse both.

## Where it stands

As of October 28, 2026.

- **Tested in Claude Code only.** Claude.ai, ChatGPT, Gemini and Copilot
  haven't been tested from start to finish. Their setup steps come from each
  company's help pages, so expect small differences.
- **Early results look good but aren't confirmed.** There are now 110
  test scenarios. Most of the first 36 passed, but that run didn't prove
  Magpie was loaded each time. Later runs used stricter rules. 6 of 7
  coaching scenarios and 7 of 8 HEARTS scenarios passed, with one partial
  each, and the diary capture scenario passed. In a test of drafting too
  early, none of the 12 runs after the fix drafted before the required
  answers were in. Many newer scenarios haven't been run live yet,
  including the ones for confidence and priority, choosing a method, and
  American English. All results so far were judged by a model, not yet
  by a person. The details are in
  [`evals/runs/`](evals/runs/) and [`evals/README.md`](evals/README.md).
- **Its rules are written down.** Magpie follows 126 standards in
  [`core/standards/`](core/standards/). 54 cite a public source, at least
  in part, such as the ICC/ESOMAR code, Braun and Clarke, or Nielsen
  Norman Group. The others are based on professional judgment and say so.
  Every source is listed in [`docs/PROVENANCE.md`](docs/PROVENANCE.md).
- **It can be wrong.** Like any AI assistant, Magpie makes mistakes, and
  its independent reviews are done by an AI too. The study record and the
  participant references are there so you can check its work. Please do.

Found a problem? Open an issue with the tool you used, the step, and what
you saw. Changes are listed in [`docs/CHANGELOG.md`](docs/CHANGELOG.md).

## When something goes wrong

- **The assistant doesn't seem to know Magpie.** In Claude Code, check the
  path is exactly `.claude/skills/magpie/SKILL.md`. In ChatGPT, Gemini or
  Copilot, check the skill is installed and active, then name it in the chat.
- **It won't take the upload.** Use `magpie.zip` as downloaded; it has
  `SKILL.md` at the top, which Copilot needs. If you made your own zip,
  zip the files inside `adapters/skill/magpie/`, not the folder itself.
  The upload hasn't been tested in ChatGPT or Gemini; if the zip is
  refused there, try uploading the unzipped folder, and please open an
  issue saying which worked.
- **It asks questions when you just want a draft.** Say "just draft it".
  Magpie skips the optional questions and marks what it had to guess. If a
  required answer is missing, it shows its best guesses first, and one
  "yes" from you is enough to start.
- **It's working on the wrong stage.** Say which stage you're at ("we're
  at stage 5, planning") and it switches.
- **The status line stopped appearing.** The session may have dropped,
  which can happen in a very long conversation. Say "Magpie, pick up where
  we were" (or paste your study record) and it starts again. A new
  conversation always needs Magpie started again.
- **The quote or count check didn't run.** Not every assistant can run
  scripts. When it can't, Magpie does the check by reading and says so in
  the record. You can run the scripts yourself with Python:
  `python3 adapters/skill/magpie/scripts/count_check.py findings.md`.

## For contributors

```
magpie.zip               the skill folder, zipped for download (generated)
adapters/skill/magpie/   the skill folder you install (generated)
adapters/generic/        one long prompt for any other assistant (generated)
adapters/claude|chatgpt|gemini|copilot/   setup notes per platform, with what was checked and when
core/                    everything Magpie knows, in plain Markdown (edit here)
tools/                   the build script, the quote, count and evidence checks, and the example deck builder
.github/workflows/       runs tools/check.py on every pull request
evals/                   test scenarios with planted problems
docs/                    design, provenance, contributing, prompt style, changelog
docs/examples/           a filled-in report and readout (Markdown, Word, PowerPoint)
```

To change Magpie, edit `core/` and run `python3 tools/build.py`; the
adapters are rebuilt from it. Write in plain words and American English;
`python3 tools/check.py` flags British spellings and day-first dates. [`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md)
has the rest, and [`docs/DESIGN.md`](docs/DESIGN.md) explains how Magpie is
built and why.

## Credit and license

Magpie was made by Kirsten Hosic. It's an independent personal project, not
made, endorsed or supported by any employer.

It's released under the MIT License (see `LICENSE`), so you're free to use,
change and share it. The license's one condition is that copies, and
substantial parts of it, keep the copyright notice and the license text. To
make that easy, every built file carries a credit line: the top of
`SKILL.md` and both system prompts, the foot of every method guide, template
and other file, and the top of each script. The skill folder and
`adapters/generic/` also hold a copy of `LICENSE`. If you share or adapt
part of Magpie, please keep those lines.

The license covers the Magpie files only. It doesn't give permission to use
any particular AI tool at work, or to share any data with one; see
[Using Magpie at work](#get-started).
