# Magpie

Magpie is a free, open-source research companion for user researchers. You
run it inside the AI assistant you already use (Claude, ChatGPT or Gemini),
and it works alongside you on a study from the first question, "do we
already know this?", through framing, method choice, the plan and the
interview guide, to analysis and a report your product manager, designer
and engineer can act on.

Why a magpie: it collects the shiny bits of evidence that already exist,
then helps you work out which ones matter for the decision in front of you.

## What Magpie does

- **Starts wherever you are.** Bring a vague stakeholder ask, a deadline, a
  half-written plan or a folder of transcripts. Magpie works out which
  stage you're at and picks up from there.
- **Drafts first, then asks one good question.** Every reply gives you
  something you can use right away (a plan, a guide, a set of findings),
  followed by one challenge worth thinking about. You can skip it; Magpie
  logs the skip as a risk and moves on.
- **Keeps a study record.** One document that carries the decision, the
  questions, the method, the sample, the findings and the risks. Save it and
  you can continue in any assistant, any day.
- **Labels where every claim comes from.** Your data, a partner team's data,
  general practice, or an assumption. It never invents a quote, a number or
  a participant.
- **Writes for stakeholders.** Readouts and reports follow a tested shape:
  why first, a brief method, five findings at most, recommendations with
  owners, next steps, appendix.
- **Covers eleven methods.** Interviews, usability testing, surveys,
  contextual inquiry, concept testing, diary studies, card sorting and tree
  testing, evidence review, competitive analysis, and stakeholder workshops.

## Before you start

You need one of these:

- Claude Code (the command-line tool or its desktop app), or a Claude.ai
  account with Projects.
- A ChatGPT Business, Enterprise or Edu account. Personal ChatGPT plans
  may not be able to add skills yet; see the ChatGPT section.
- A Google account, signed in to Gemini, with Keep Activity turned on.

Then download Magpie. Either click the green **Code** button on this page
and choose **Download ZIP**, or run:

```
git clone https://github.com/kirstenhosic/user-research-assistant.git
```

Inside, the folder you'll use is `adapters/skill/magpie/`. It's the whole
of Magpie in one place: a `SKILL.md` file that tells the assistant how to
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
Healthcare and Edu workspaces (checked 26 October 2026). If you're on a
personal plan, try the steps anyway; if the Skills page isn't there, use
the fallback below.

1. In the ChatGPT sidebar, open **Plugins**, then the **Skills** tab.
2. Choose **Create** > **Upload from your computer** and upload the
   `adapters/skill/magpie/` folder (zip it first if the uploader asks for a
   single file).
3. ChatGPT scans the upload. If it says **Needs Review**, read what it
   flags. The only code in the package is two scripts that read local
   files; nothing connects to the internet.
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

Uploading works in the web app and the Mac app, not the phone apps. Chats
with a skill don't need a paid plan.

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
and it moves.

A few plain words steer it:

| Say | Magpie does |
| --- | --- |
| skip | Logs the current challenge as a risk and moves on |
| push me | Asks up to three challenges per stage instead of one |
| ease off | Only raises red flags (consent, leading questions, overclaiming) |
| just the work | Turns off the personality for the session |
| show the record | Prints the full study record |
| review this | Runs an independent check on your findings or report |
| back to stage 3 | Returns to that stage and says what depends on it |

**Save your study record.** At the end of a session, ask for the record
and paste it into a document. Next time, paste it back and Magpie carries
on, in any assistant.

## When something goes wrong

- **The assistant doesn't seem to know Magpie.** In Claude Code, check the
  path is exactly `.claude/skills/magpie/SKILL.md`. In ChatGPT or Gemini,
  check the skill is installed and active, then name it in the chat.
- **It won't take the upload.** Zip the `magpie` folder and upload the zip.
  Make sure `SKILL.md` is at the top level inside it.
- **It drafted the wrong stage.** Say which stage you're at ("we're at
  stage 4, planning") and it switches.
- **The quote or count check didn't run.** Not every assistant can run
  scripts. Magpie then does the check by hand and says so in the record.
  You can run the scripts yourself with Python:
  `python3 adapters/skill/magpie/scripts/count_check.py findings.md`.

Not tested yet on ChatGPT or Gemini as of 26 October 2026. If you try it
and something breaks, please open an issue on this repository with the
tool, the step, and what you saw.

## What's in the repository

```
adapters/skill/magpie/   the skill folder you install (generated)
adapters/generic/        one long prompt for any other assistant (generated)
adapters/claude|chatgpt|gemini/   setup notes per platform, with what was checked and when
core/                    everything Magpie knows, in plain Markdown (edit here)
tools/                   the build script and the quote and count checks
evals/                   test scenarios with planted problems
docs/                    design, provenance, contributing, prompt style, changelog
```

To change Magpie, edit `core/` and run `python3 tools/build.py`; the
adapters are regenerated from it. `docs/CONTRIBUTING.md` has the rest.
`docs/DESIGN.md` explains how Magpie is built and why, and
`docs/PROVENANCE.md` records how it was made and which sources back its
standards.

Licensed under the MIT License. See `LICENSE`.
