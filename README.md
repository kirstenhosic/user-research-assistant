# Magpie

Magpie is a free, open-source research partner for user researchers. You
add it to an AI tool you already use, such as Claude, ChatGPT, Gemini or
Copilot. It works with you on a study from the first question, "Do we
already know this?", to a report your product manager, designer and
engineer can act on. It takes on much of the drafting and checking, so
you can spend more of your time on the thinking only you can do. It's
built for researchers, and for PMs and designers doing their own
research.

Made by Kirsten Hosic.

Why a magpie: it collects the shiny bits of evidence that already exist,
then helps you figure out which ones matter for the decision in front of
you.

**Work in progress.** Magpie has been tested only in Claude Code so far,
and it improves often. Read [Can I trust it?](#can-i-trust-it) before
you rely on it, and [check for updates](#keep-magpie-up-to-date) every
week or two.

**On this page**

- [Get started](#get-started)
- [How Magpie works](#how-magpie-works)
- [What you get](#what-you-get)
- [The stages](#the-stages)
- [Methods it covers](#methods-it-covers)
- [Words that steer it](#words-that-steer-it)
- [Pick up where you left off](#pick-up-where-you-left-off)
- [Make Magpie ask fewer questions](#make-magpie-ask-fewer-questions)
- [Can I trust it?](#can-i-trust-it)
- [When something goes wrong](#when-something-goes-wrong)
- [Keep Magpie up to date](#keep-magpie-up-to-date)
- [For contributors](#for-contributors)
- [Thanks to](#thanks-to)
- [Credit and license](#credit-and-license)

## Get started

Three steps: pick your AI tool, set Magpie up, and start your first
study. If you'd like to know how Magpie works first, read
[How Magpie works](#how-magpie-works).

### Pick your AI tool

Magpie works best in an **agent tool**, such as Claude Code, OpenAI
Codex, Gemini CLI or OpenCode. There it can run its own quote and count
checks and start its independent checker agents for you. A **chat**,
such as Claude.ai, ChatGPT, Gemini or Copilot, is a good way to try it
out. [Compare the two](#which-kind-of-ai-tool-to-use).

### Using Magpie at work

Anything you share with Magpie goes to the AI tool it runs in. For work
projects, use Magpie only in an AI tool your employer has approved, and
follow your organization's rules on data, privacy and confidentiality.
That includes participant data, transcripts, recordings and anything
your company treats as internal. An agent tool can open files on your
computer, so open only the study folder, and keep in it only what you
mean to share. If you aren't sure what's allowed, ask your manager or
your privacy or security team before you start.

### Set up Magpie

Download
**[magpie.zip](https://github.com/kirstenhosic/user-research-assistant/releases/latest/download/magpie.zip)**.
It holds everything Magpie needs. Gemini and Copilot use their own
versions, linked in their steps below.

#### Claude Code

You need the Claude Code desktop app or the command-line tool (it runs
in a Terminal window).

1. Download `magpie.zip` and open Claude Code.
2. Ask Claude Code to install it, for example: *"Unzip
   ~/Downloads/magpie.zip into ~/.claude/skills/magpie/"*. Magpie then
   works in all your projects on this computer. (`~` is short for your
   home folder.)
3. Start a conversation and ask for help with a study, or say "magpie".

To share Magpie with a team, put it in a shared project's
`.claude/skills/magpie/` folder instead. Folders that start with a dot
are hidden: on a Mac, press Cmd+Shift+. in Finder to show them; on
Windows, turn on **Hidden items** in File Explorer's **View** menu. More
in Claude Code's [skills docs](https://code.claude.com/docs/en/skills)
(checked October 28, 2026).

#### Other agent tools (Codex, OpenCode, Gemini CLI)

These tools can load Magpie the same way Claude Code does, but **Magpie
hasn't been tested in them yet.** Ask your tool to install it, for
example: *"Install the skill in ~/Downloads/magpie.zip so it works in all
my projects."* It knows where its own skills go. Then start a
conversation and ask for help with a study, or say "magpie". If
something doesn't work, please
[open an issue](https://github.com/kirstenhosic/user-research-assistant/issues).

#### Claude.ai

You need a Claude.ai account with Projects.

1. Create a new Project.
2. Unzip `magpie.zip` and add all the files whose names end in `.md` to
   the project's knowledge.
3. Paste the contents of `operating.md` (Magpie's main instructions) into
   the project's instructions.
4. Start a chat in the project and describe your study.

#### ChatGPT

ChatGPT adds Magpie as a skill. OpenAI's help center lists skills for
Business, Enterprise, Healthcare and Edu workspaces (checked October 26,
2026); on a personal plan, try the steps anyway.

1. In the sidebar, open **Plugins**, then the **Skills** tab.
2. Choose **Create** > **Upload from your computer** and upload
   `magpie.zip`.
3. If ChatGPT says **Needs Review**, read what it flags. The only code in
   the package is seven small scripts that check quotes, counts and
   wording and make Word and Excel files; none of them connects to the
   internet.
4. Install it, then start a chat and type `@magpie`, or just describe
   your study.

**If there's no Skills page:** unzip `magpie.zip`, create a Project,
paste `operating.md` as the project instructions, and add the other `.md`
files as project files.

#### Gemini

You need a Google account signed in to Gemini, with Keep Activity turned
on.

1. Go to gemini.google.com. In the sidebar, open **Customize** (it may be
   under **More**), then **Skills**.
2. Choose **Create** > **Upload** and pick
   **[magpie-gemini.zip](https://github.com/kirstenhosic/user-research-assistant/releases/latest/download/magpie-gemini.zip)**,
   not `magpie.zip`. Gemini won't load a skill that contains code, and
   this copy leaves the code checks out. Magpie does those checks by hand
   instead.
3. Check what Gemini shows, then choose **Create**.
4. In a chat, type `/magpie`, or just describe your study.

Uploading works in the web app and the Mac app, not the phone apps.

#### Copilot

Use **Cowork** in Microsoft 365 Copilot. At work you need a Copilot
license, and your admin has to turn Cowork on. On a personal Microsoft
account you need Microsoft 365 Premium or Pro, in the US or Canada.
Personal, Family and the free Copilot app don't have Cowork.

1. Download
   **[magpie-copilot.zip](https://github.com/kirstenhosic/user-research-assistant/releases/latest/download/magpie-copilot.zip)**,
   not `magpie.zip`. It has its files combined to fit Copilot's file limit.
2. In Cowork, open **Customize** > **Skills**, choose the arrow next to
   **Add**, then **Upload skill**, and pick `magpie-copilot.zip`.
3. When it appears under **Your skills**, start a chat and describe your
   study.

More detail is in the [Copilot setup notes](adapters/copilot/README.md).

#### Any other AI tool

Upload `magpie.zip` if the tool takes skills. If it has projects or
knowledge files instead, set it up like Claude.ai: paste `operating.md`
as the instructions and add the other `.md` files.

### Your first study, step by step

Once Magpie is set up:

1. **Make a folder for the study** (agent tool only). Put in what you
   already have: a brief, notes, past research, transcripts. Open that
   folder in your agent tool, so Magpie can read it and save its work
   there.
2. **Say what you're working on, in your own words.** One or two
   sentences is enough, for example: *"A PM wants to know if we should
   build an onboarding checklist. Deadline is two weeks."* or *"Here are
   eight interview transcripts. Help me find what matters."* In a chat,
   upload or paste what you have in the same message. If Magpie doesn't
   start, say "magpie".
3. **Answer its questions.** Magpie says which stage it thinks you're at
   (tell it if that's wrong), then asks up to six short questions under
   "Questions for you to answer". A line each is enough, and you can skip
   the ones marked optional. The more you share at the start, such as a
   brief or past research, the fewer questions it asks. To share less
   each time, see
   [Make Magpie ask fewer questions](#make-magpie-ask-fewer-questions).
4. **Read the draft, then say "yes".** Nothing counts as done until you
   do. Start with the points marked "read hardest": where the decision
   leans most and the evidence is thinnest. If you'd do something
   differently, say what and why, and Magpie reworks it.
5. **Take your turn.** At three points you go first: framing the
   problem, spotting patterns in the data, and deciding what each team
   should do. Use your own words. That thinking is what makes the work
   yours. Say "you do it" to hand a step back.
6. **Keep going, one stage at a time.** A study takes many messages.
   Every reply ends with a short line such as *Magpie · Planning the
   study*, so you know Magpie is still on. Say "stop Magpie" when you're
   done.
7. **Save your place.** Magpie keeps a study record you can bring to a
   new conversation. See
   [Pick up where you left off](#pick-up-where-you-left-off).

**Your tool knows itself best.** Whenever you're not sure how to do
something, ask the tool you're using, for example: *"How do I add files
to this conversation?"*, *"How do I open a folder here?"* or *"How do I
install a skill from a zip file?"* Each tool works a little differently,
and it can walk you through its own way.

**Tip:** a small study you've already finished makes a good first try.
You'll know the answers, so you can see how well Magpie does.

## How Magpie works

Magpie works with you on a whole study, over many messages. It asks you
questions, drafts the work, and waits for you to check it before moving
on.

### What Magpie is: one skill that brings in agents

A **prompt** is one message you send an AI tool, and it applies only to
that request. Magpie isn't a prompt. It's a **skill**: a saved set of
instructions and reference files that you add to your AI tool once.
After that, the tool follows Magpie's process whenever you ask for help
with a study, so you never have to explain how you work. It's one skill
with many parts: a guide for each stage and method, checklists, and a
few small programs that check quotes and counts. In an agent tool,
Magpie also brings in **independent checker agents** at three required
points: your guide or survey questions, your findings, and your report
and deck. More on that below.

Each AI company uses these words a little differently. ChatGPT also
calls a saved set of instructions a GPT, and Copilot calls one an agent.
If a word in your tool doesn't match this page, ask the tool what it
means.

### Why one skill, with independent checker agents

Magpie is a single skill on purpose, and it brings in independent
checker agents where independence matters most. A study is one line of
thinking: the decision shapes the method, the method shapes the
questions, and the questions shape what you find. Keeping it all in one
place means nothing gets lost between steps, and you work with one
research partner.

But whoever drafts something can't check it with fresh eyes. So at three
required points, Magpie brings in an **independent checker agent**: a
separate AI that sees only your raw material and the draft, never the
conversation behind it.

- **Before you talk to participants:** the questions in your guide or
  survey.
- **After analysis:** the findings.
- **Before you share:** the report and the readout deck.

The checker doesn't know what anyone hoped to find, so it can only go by
the evidence. It checks that each finding matches the evidence, lists the
participants whose answers went against it, recounts the numbers, and
flags questions that push people toward an answer. Magpie then checks
each point against your material before acting on it, because a checker
can be wrong too. Then you read the result before you say yes. The
checkers make Magpie's work easier to trust, not automatically right
(see [Can I trust it?](#can-i-trust-it)).

In an agent tool, Magpie starts the checker agent on its own, and small
programs also match every quote to its transcript and recount every
number. A chat can't start a separate agent, so you play that part:
Magpie gives you the text to paste into a new chat, and you paste the
result back.

### Which kind of AI tool to use

Where you add Magpie changes how much of the checking it can do for you.
There are two kinds of AI tool:

- **A chat**, such as Claude.ai, ChatGPT, Gemini or Copilot, in a web
  browser or app. It works with what you paste or upload into the
  conversation.
- **An agent tool**, such as Claude Code, OpenAI Codex, Gemini CLI or
  OpenCode. It's the same kind of AI, but it can take steps on its own:
  open the files in a folder you choose, save new files there, run small
  programs, and start a checker agent. You talk to it in plain words,
  and it asks before it changes anything.

**Magpie works best in an agent tool**, because there it can use all of
its files and run its own checks:

| | Agent tool | Chat |
| --- | --- | --- |
| Quote and count checks | Done by a small program | Done by reading, which is less reliable |
| Independent checker agent | Starts on its own | You paste the draft into a new chat and paste the result back |
| Word and Excel files | Saved to your folder | Made by the chat if it can, or you copy into Word |
| Study record (a running summary of your study's decisions and findings) | Saved and kept up to date for you | You copy it into a document |
| Setup | A few more steps, which it can do for you | Upload a file and go |

A chat is a good way to try Magpie out, and it works well for planning
a study and drafting a guide. The extra checks matter most when you
analyze data and write the report, because that's where a wrong quote or
count is most likely to slip through. You can start in a chat and move
later without losing your work.

## What you get

- **Help from wherever you're starting:** a vague request, a deadline, a
  half-written plan or a folder of transcripts.
- **The right method for the question.** Magpie checks whether you need
  to hear what people say or see what they do, and tells you up front
  what you'll have at the end.
- **Coaching as you go.** After each draft it asks the one question most
  likely to improve it, and says why. It asks what vague words like
  "confused" or "most" really mean, and explains why it chose a method or
  question order. You can push back on any of it.
- **Findings you can check.** Every claim says where it came from. Magpie
  never makes up a quote, a number or a participant, and every count
  names the participants behind it.
- **Honest about how sure it is.** Each finding is labeled strong,
  moderate or weak, and ranked by how much it matters. With small
  samples, it gives a range rather than one number and says what a
  handful of people can and can't tell you.
- **A second look before anything goes out.** An independent checker
  agent reviews guides, surveys, findings and reports for leading
  questions, findings the data doesn't support, and unclear language.
  Before a readout or report is shared, Magpie also checks that nobody
  can be identified.
- **Files your team can edit.** Word files for guides, surveys, plans and
  reports, and Excel sheets for notes and findings.
- **Readouts people will read.** Up to five top findings first,
  recommendations that name the teams they affect, and next steps that
  say how the team will know a change worked.

## The stages

Magpie works in eight stages. It tells you which one you're in, and you
can start at any of them or go back (say "back to stage 4"). Knowing them
helps you tell Magpie where you are.

1. Find the opportunities, when nobody has asked for research yet
2. Check existing evidence
3. Frame the problem
4. Choose the approach
5. Plan the study
6. Draft the guide or survey
7. Analyze
8. Read out and report

## Methods it covers

Tell Magpie what you're trying to learn and it will suggest a method, or
name one yourself. Each method guide includes a worked example, so you
can see what good looks like.

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
| [Card sorting, tree testing and first-click testing](core/methods/card-sorting-and-tree-testing.md) | How people group and name things, whether they can find them, and where they go first | Card and task lists, findings |
| [Evidence review](core/methods/evidence-review.md) | What the organization already knows | Evidence log, gaps, one-page brief |
| [Coding customer feedback](core/methods/customer-feedback-coding.md) | What people write in about, and how that's changing | Code frame, counted themes with their limits |
| [Stakeholder interviews](core/methods/stakeholder-interviews.md) | What the project is for and what stakeholders believe, before research is planned | Interview guide, success measures, beliefs logged as hypotheses |
| [Journey maps and personas](core/methods/journey-maps-and-personas.md) | The shape of a journey, or the kinds of user, built from findings | Map and personas with participant codes in every cell |
| [Competitive analysis](core/methods/competitive-analysis.md) | How other tools solve the same job | Comparison built around the user's job |
| [Stakeholder workshops](core/workshops/stakeholder-workshops.md) | Agreement on the problem, or actions from findings | Agenda, actions with the teams involved, summary |
| [Finding opportunities](core/stages/01-find-opportunities.md) | Where company goals and user signals overlap | Opportunity briefs with a decision and the team that would make it |

To see what a finished report and readout look like, open the examples in
[`docs/examples/`](docs/examples/).

## Words that steer it

You never need these: plain words always work. They're shortcuts. The
five you'll use most are first.

| Say | Magpie does |
| --- | --- |
| yes | Marks what's waiting as reviewed |
| just draft it | Skips the optional questions and marks the gaps as assumptions |
| you do it | Takes over a step where you were asked to go first |
| fresh start | Gets your study record ready to take to a new conversation (unlike "start over", it keeps your study) |
| stop Magpie | Ends the session and offers the record to save |
| skip | Moves on from the current question and notes it as a risk |
| handled | Closes a challenge you've already dealt with, without noting a risk |
| go on | Moves to the next stage without waiting for the team's reply to a summary |
| final | Changes a reviewed draft's label from Draft to Final |
| counter: ... | Reconsiders a method or question order with your reasoning |
| push me | Challenges you more, up to three questions per stage |
| ease off | Only raises serious problems, like consent or leading questions |
| standard | Goes back to one question per stage |
| just the work | Drops the personality for the session |
| show the record | Shows the full study record |
| make the sheet | Builds the analysis spreadsheet (Excel) |
| review this | Brings in an independent checker for your guide, survey, findings or report |
| back to stage 4 | Returns to that stage and says what depends on it |

## Pick up where you left off

Magpie keeps a **study record**: the decision, questions, method,
participants, findings and risks in one document. In an agent tool it
saves the record to a file for you. In a chat, say "show the record" and
paste it into a document; Magpie reminds you at the end of each stage.
Next time, give it back to Magpie, in any AI tool, and it carries on
without asking what you've already answered.

### When to start a new conversation

Every AI tool can hold only so much of one conversation. When a
conversation gets very long, the tool starts to lose or shorten the
earlier parts, and the work gets less careful, often before you'd notice.
Magpie can't see how full the conversation is, so it suggests a new one
at natural break points: before analysis and before the report. It also
offers one if a lot of material arrives at once.

Starting a new conversation is a good idea if you notice any of these:

- The status line at the end of each reply has stopped appearing.
- Magpie asks again about something you already settled.
- It forgets a decision, a participant or your house style.
- A quote doesn't match the transcript, or participants get mixed up.
- Its answers get vaguer than they were earlier.

To move: say **"fresh start"**. Magpie updates the study record and gives
you a line to paste. Start a new conversation, start Magpie, and paste
the record and that line. Nothing is lost, and Magpie won't ask again
what you've already answered.

Some tools show how much of the conversation they can still hold. Ask
yours: *"Does this tool show how full this conversation is?"*

## Make Magpie ask fewer questions

These are optional. Fill in the [team profile](core/team/team-profile.md)
once with your products, users, goals and research rules, and attach it
when you start a study, so Magpie doesn't have to ask about them. Send
the [intake form](core/team/intake-form.md) to PMs and designers who ask
you for research; Magpie can start from a filled one.

## Can I trust it?

- **It's early.** Magpie has been tested only in Claude Code. Other agent
  tools should work the same way, but that hasn't been checked yet. The
  setup steps for other tools come from each company's help pages, so
  expect small differences.
- **Its tests are promising but not confirmed.** Magpie is tested against
  realistic study scenarios with planted problems, such as a leading
  question or a finding the data doesn't support. Most pass, but so far an
  AI model has judged the results, not a person.
- **Its rules are written down.** Where a rule comes from published
  research practice, such as Nielsen Norman Group or the ICC/ESOMAR code
  (the market research industry's code of conduct),
  the source is listed in [`docs/PROVENANCE.md`](docs/PROVENANCE.md).
  Where it's professional judgment, it says so.
- **It can be wrong.** Like any AI tool, Magpie makes mistakes, and
  its independent reviews are done by an AI too. The study record and the
  participant references are there so you can check its work. Please do.

Found a problem? [Open an issue](https://github.com/kirstenhosic/user-research-assistant/issues)
with the tool you used, the step, and what you saw.

## When something goes wrong

- **Your AI tool doesn't seem to know Magpie.** In Claude Code, check the
  file is at `~/.claude/skills/magpie/SKILL.md` (or in your project's
  `.claude/skills/magpie/`). In other tools, check the skill is installed
  and turned on, then say "magpie".
- **Gemini says Magpie "contains executable components" or "couldn't be
  loaded".** You uploaded `magpie.zip`. Replace it with `magpie-gemini.zip`.
- **It won't take the upload.** Use `magpie.zip` exactly as downloaded,
  without unzipping and re-zipping it. If it's still refused, try
  uploading the unzipped folder, and please open an issue saying what
  happened.
- **It asks questions when you just want a draft.** Say "just draft it".
  If something important is missing, Magpie shows its best guess first,
  and one "yes" is enough.
- **It's working on the wrong stage.** Say which stage you're at ("we're
  planning the study") and it switches.
- **The status line stopped appearing.** The session may have dropped in a
  long conversation. Say "Magpie, pick up where we were", or paste your
  study record. A new conversation always needs Magpie started again.
- **Magpie forgets things or asks again about what you settled.** The
  conversation has probably grown too long for the tool to hold all of
  it. Say "fresh start" and move to a new conversation (see "When to
  start a new conversation").
- **Magpie seems to follow old rules after an update.** You may have two
  copies. Ask your tool to list its skills, remove every copy of Magpie,
  install the new one again, and start a new conversation.
- **The quote or count check didn't run.** Not every AI tool can run
  small programs. When it can't, Magpie checks by reading and tells you so.

## Keep Magpie up to date

Magpie gets better often. Check for a new version every week or two.
Updating takes a few minutes.

**Keep only one copy.** If your AI tool has two copies of Magpie, it may
use the old one, or mix rules from both, without telling you. So each
time, remove the old copy before you add the new one.

1. **See what's new.** Open the [changelog](docs/CHANGELOG.md). The
   newest changes are at the top, with the date. To see which version
   you have, ask Magpie: *"Which version of Magpie is this?"*
2. **Save your study record** if you're in the middle of a study (in a
   chat, say "show the record" and paste it into a document). Then you
   can carry on with the new version.
3. **Download the new version:**
   **[magpie.zip](https://github.com/kirstenhosic/user-research-assistant/releases/latest/download/magpie.zip)**,
   or `magpie-gemini.zip` or `magpie-copilot.zip` if you use Gemini or
   Copilot. Delete the old zip from your Downloads folder first. If you
   don't, your browser may save the new one as `magpie (1).zip`, and
   it's easy to upload the old one by mistake.
4. **Remove the old copy, then add the new one.** How you do this
   depends on your tool:
   - **Agent tool** (Claude Code, Codex, Gemini CLI, OpenCode): ask it,
     for example: *"Remove my old Magpie skill and install the new one
     from ~/Downloads/magpie.zip. Then check there's only one copy of
     Magpie left."* If you also put Magpie in a shared project folder,
     update that copy too.
   - **Chat with skills** (ChatGPT, Gemini, Copilot): delete the old
     Magpie skill, then upload the new zip. Check that only one Magpie
     is listed.
   - **Claude.ai project:** remove all the old Magpie files from the
     project's knowledge, add the new `.md` files, and replace the
     project instructions with the new `operating.md`. Or make a new
     project for the new version, and keep the old one only until you've
     finished the studies in it.
5. **Start a new conversation.** A conversation that's already open
   keeps using the version it started with. If you were mid-study, give
   Magpie your study record and it picks up from there.

Not sure how to do a step? Ask your tool, for example: *"How do I delete
a skill here?"*

## For contributors

To change Magpie or see how it's built and tested, start with
[`docs/CONTRIBUTING.md`](docs/CONTRIBUTING.md). The reasoning behind its
design is in [`docs/DESIGN.md`](docs/DESIGN.md), and changes are listed in
[`docs/CHANGELOG.md`](docs/CHANGELOG.md).

## Thanks to

Magpie's rules build on published work by many people. The ones it leans
on most:

- The authors of Nielsen Norman Group's articles, including Jakob
  Nielsen, Maria Rosala, Page Laubheimer and many others, each named in
  the source list.
- Carl J. Pearson, for his writing on surveys, effect sizes and minimum
  viable rigor.
- Jeff Sauro and James R. Lewis, for *Quantifying the User Experience*
  and the MeasuringU articles.
- Kaleb Loosbrock, for the HEARTS framework: Loosbrock, K. (2025). The
  HEARTS Framework: Six lenses for evaluating AI-assisted UX research.
  Hey Kaleb & Co. https://www.heykaleb.com/hearts-framework
- Virginia Braun and Victoria Clarke, for reflexive thematic analysis.
- The UK Government Digital Service and NHS England, for their service
  manuals, and ICC/ESOMAR, for its research code.
- Constantine Papas, for *AI-Powered UX Research*.
- Henri Lipmanowicz and Keith McCandless (Liberating Structures), IBM
  Enterprise Design Thinking, the Design Council, Pew Research Center,
  User Interviews and the W3C Web Accessibility Initiative.

Every source, with its authors, year, title and link, is listed in
[`docs/PROVENANCE.md`](docs/PROVENANCE.md). A short copy, `sources.md`,
comes with Magpie, so you can ask it where any rule comes from.

## Credit and license

Magpie was made by Kirsten Hosic. It's an independent personal project, not
made, endorsed or supported by any employer.

It's released under the MIT License (see [`LICENSE`](LICENSE)), so you're
free to use, change and share it. The one condition is that copies, and
substantial parts of it, keep the copyright notice and the license text.
Every Magpie file carries a credit line to make that easy; if you share or
adapt part of Magpie, please keep it.

To cite Magpie in a paper, talk or other project, use **Cite this
repository** in the sidebar of the GitHub page. It gives the citation in
APA and BibTeX.

The license covers the Magpie files only. It doesn't give permission to
use any particular AI tool at work, or to share any data with one; see
[Using Magpie at work](#using-magpie-at-work).
