# Magpie

Magpie is a free, open-source research helper for user researchers. You
run it inside the AI assistant you already use (Claude, ChatGPT, Gemini, or
Copilot). It works with you on a study from the first question, "Do we
already know this?", to a report your product manager, designer, and
engineer can act on. It's built for researchers, and for PMs and designers
doing their own research.

Made by Kirsten Hosic.

Why a magpie: it collects the shiny bits of evidence that already exist,
then helps you figure out which ones matter for the decision in front of you.

To get going, see [So how do I use this?](#so-how-do-i-use-this).

**Work in progress.** So far Magpie has been tested only in Claude Code.
Read [Can I trust it?](#can-i-trust-it) before you rely on it. Magpie is
improving often, so [check for updates](#keep-magpie-up-to-date) every
week or two.

Ready to try it? Jump to [Get started](#get-started).

## So how do I use this?

Magpie works with you on a whole study, over many messages. It asks you
questions, drafts the work, and waits for you to check it before moving
on. Here's how to set it up and what helps along the way.

### Two kinds of AI tool

Magpie runs in either kind:

- **A chat**, such as Claude.ai, ChatGPT, Gemini or Copilot, in a web
  browser or app. It works with what you paste or upload into the
  conversation.
- **An agent tool**, such as Claude Code, OpenAI Codex, Gemini CLI or
  OpenCode. It's the same kind of AI, but
  it can also work with files on your computer when you ask: open the
  files in a folder, save new files there, and run small programs. You
  talk to it in plain words, and it asks before it changes anything.

**Magpie works best in an agent tool.** There it checks every quote and
count with a small program, has a second AI review its drafts, and saves
Word and Excel files straight to your folder. In a chat, Magpie does
these checks by reading, or asks you to help, so they take more of your
time. A chat is a good way to try Magpie out.

### Your first study, step by step

1. **Set it up once.** Follow the steps for your tool in
   [Get started](#get-started). In Claude Code you can ask it to install
   Magpie for you.
2. **Make a folder for the study** (agent tool only). Put in what you
   already have: a brief, notes, old research, transcripts. Open that
   folder in your agent tool, so Magpie can read it and save its work
   there.
3. **Say what you're working on, in your own words.** One or two
   sentences is enough, for example: *"A PM wants to know if we should
   build an onboarding checklist. Deadline is two weeks."* In a chat,
   upload or paste what you have in the same message. If Magpie doesn't
   start, say "magpie".
4. **Answer its questions.** Magpie asks a few short questions before it
   drafts anything. A line each is enough. Optional ones are marked, and
   you can skip those.
5. **Read the draft, then say "yes".** Nothing counts as done until you
   do. If something's off, say what and why, and Magpie reworks it.
6. **Keep going, one stage at a time.** A study takes many messages, and
   often several days.
7. **Save your place.** In an agent tool, Magpie saves a study record in
   your folder. In a chat, say "show the record" and paste it into a
   document. Next time, start a new conversation and give Magpie the
   record, and it carries on where you left off.

**Your tool knows itself best.** Whenever you're not sure how to do
something, ask the tool you're using, for example: *"How do I add files
to this conversation?"*, *"How do I open a folder here?"* or *"How do I
install a skill from a zip file?"* Each tool works a little differently,
and it can walk you through its own way.

**Tip:** a small study you've already finished makes a good first try.
You'll know the answers, so you can see how well Magpie does.

### What helps

| How Magpie works | What helps |
| --- | --- |
| It asks questions before it drafts, so the draft fits your study. | Answer in a line or two. Skip the optional ones if you like. |
| A study moves in stages, over many messages. | Take it one stage at a time. Each one is quicker than doing it alone. |
| It reads whatever you give it. | Share the brief, notes or past research at the start, and it asks less. |
| A new conversation starts fresh. | Keep the study record and give it to Magpie next time. |
| Your "yes" is what marks a draft reviewed. | Read the "read hardest" items first: where the decision leans most and the evidence is thinnest. |
| At three points you go first: framing the problem, the patterns you saw, and what each team should do. | Use your own words. That thinking makes the work yours, and the draft better. |
| It reworks a method, question order or theme when you give a reason. | If you'd do it differently, say so and say why. |

## What a session looks like

Tell Magpie what you've got, in your own words. For example:

> A PM wants to know if we should build an onboarding checklist. We have
> some old interviews from last year somewhere. Deadline is two weeks.

> Here are eight interview transcripts. Help me find what matters.

> I want to propose research for next quarter but I don't have a brief.

Magpie tells you which stage it thinks you're at and asks up to six short
questions about what it doesn't know yet, with the optional ones marked;
a line each is enough. Then it drafts the work, asks
one question worth thinking about, and waits for you to reply "yes" once
you've reviewed it. Whatever it needs from you is in one place, under
the heading "Questions for you to answer", so you never have to hunt for
it. That list always holds everything still open, so you never have to
scroll back. Every reply ends with a short status line that shows
Magpie is still on:

> Magpie · Planning the study

If it guesses the stage wrong, tell it. Start Magpie once per
conversation; it stays on until you say "stop Magpie".

## What you get

- **Help from wherever you're starting.** A vague request, a deadline, a
  half-written plan or a folder of transcripts: Magpie picks up from
  there.
- **Questions before drafts.** Magpie asks about your goals, hypotheses,
  the decision and who will read the work before it builds anything.
  Share a brief, PRD or past research and it reads that first, so it only
  asks what's missing. It won't draft on guesses you haven't seen: if
  something important is missing, it shows its best guess and waits for
  your yes. Say "just draft it" to skip the optional questions.
- **A coach, not a quiz.**
  - After each draft it asks the one question most likely to improve it,
    and says why. You can skip it.
  - It explains a research principle once, then leaves it.
  - It asks what vague words like "confused" or "most" really mean.
  - When it rewrites your research question or hypothesis, it shows your
    version next to its own and says why.
  - At three points you go first: framing the problem, spotting patterns
    in analysis, and deciding what each team should do. Say "you do it" to
    hand a step back.
  - It explains why it chose a method and why the guide's questions are in
    that order, and you can push back.
  - In analysis, you decide whether to keep, change, split or drop each
    theme it suggests.
- **The right method for the question.** Magpie checks whether you need
  to hear what people say or see what they do, where the product is, and
  where the research has to happen. It tells you up front what you'll
  have at the end.
- **Findings you can check.** Every claim says where it came from: your
  data, another team's data, general practice, or an assumption. Magpie
  never makes up a quote, a number or a participant, and every count names
  the participants behind it.
- **Careful with numbers from small samples.** When you have ratings,
  completion rates, task times or survey results, Magpie gives a range,
  not just one number, and says what a result from a handful of people
  can and can't tell you. If your tool already reports the statistics,
  Magpie checks them instead of redoing them.
- **Findings ranked by how sure and how important.** Each finding is
  labeled strong, moderate or weak, with a one-line reason, and ranked by
  how much it matters. An important finding with weak evidence is marked
  "check next". You can move any finding up or down before you say yes.
- **A second look before anything goes out.** Nothing is final until you
  say "yes". Guides, surveys, findings and reports also get an independent
  review that checks for leading questions, findings that don't trace
  back to the data, and unclear language. Before a readout or report is
  shared, Magpie checks it fits the audience: no names or employers,
  nobody identifiable, and quotes used only as participants agreed.
- **Files your team can edit.** Guides, surveys, plans and reports come as
  Word files, with numbered questions and a header showing the team,
  authors, reviewers and status. Guides come with an Excel note-taking
  sheet, and analysis can come with a matching findings sheet. In Claude
  Code this happens on its own; elsewhere Magpie uses the assistant's own
  way to make a Word file, or you copy the draft into Word.
- **Readouts and reports people will read.** They open with why the study
  was done and up to five top findings, most important first. Each
  recommendation names the teams it affects, and the next steps say how
  the team will know the change worked. At the end, Magpie offers you a
  short private debrief that the team doesn't see.

## The stages

Magpie works in eight stages. You can start at any of them.

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

| Say | Magpie does |
| --- | --- |
| yes | Marks what's waiting as reviewed |
| just draft it | Skips the optional questions and marks the gaps as assumptions |
| you do it | Takes over a step where you were asked to go first |
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
| make the sheet | Builds the analysis spreadsheet |
| review this | Runs an independent review of your guide, survey, findings or report |
| back to stage 4 | Returns to that stage and says what depends on it |
| stop Magpie | Ends the session and offers the record to save |

## Pick up where you left off

Magpie keeps a **study record**: the decision, questions, method,
participants, findings and risks in one document. Say "show the record"
and paste it into a document; Magpie reminds you at the end of each stage.
In Claude Code it saves the record to a file for you. Next time, paste it
back, in any assistant, and Magpie carries on without asking what you've
already answered.

**Optional: a team profile and an intake form.** Fill in the
[team profile](core/team/team-profile.md) once with your products, users,
goals and research rules, and attach it when you start a study, so Magpie
asks fewer questions. Send the [intake form](core/team/intake-form.md) to
PMs and designers who ask you for research; Magpie can start from a
filled one.

## Get started

**Using Magpie at work.** Magpie runs inside whichever AI assistant you
install it in, so anything you share with Magpie goes to that assistant.
If you want to try it on work projects, use it only in an AI tool your
employer has approved, and follow your organization's rules on data,
privacy and confidentiality. That includes participant data, transcripts,
recordings and anything your company treats as internal. If you aren't
sure what's allowed, ask your manager or your privacy or security team
before you start.

First, download
**[magpie.zip](https://github.com/kirstenhosic/user-research-assistant/raw/main/magpie.zip)**.
It holds everything Magpie needs.

Then set it up in your tool.

### Which tool to use

| | Agent tool (Claude Code, Codex, Gemini CLI, OpenCode) | Chat (Claude.ai, ChatGPT, Gemini, Copilot) |
| --- | --- | --- |
| Quote and count checks | Done by a small program | Done by reading, which is less reliable |
| Independent review | Starts on its own | You paste it into a fresh chat and paste the result back |
| Word and Excel files | Saved to your folder | Made by the chat tool if it can, or you copy into Word |
| Study record | Saved and kept up to date for you | You copy it into a document |
| Setup | A few more steps, which it can do for you | Upload a file and go |

The extra checks matter most when you analyze data and write the report,
because that's where a wrong quote or count is most likely to slip
through. You can start in a chat and move later: give your study record
to Magpie in the agent tool and it carries on.

An agent tool can open files on your computer, so open only the study
folder, and keep in it only what you mean to share. The rules in
[Using Magpie at work](#get-started) apply either way.

### Claude Code

You need the Claude Code command-line tool or its desktop app.

1. Download `magpie.zip` and open Claude Code.
2. Ask Claude Code to install it, for example: *"Unzip
   ~/Downloads/magpie.zip into ~/.claude/skills/magpie/"*. Magpie then
   works in all your projects on this computer.
3. Start a conversation and ask for help with a study, or just say
   "magpie".

To share Magpie with a team, put it in a shared project's
`.claude/skills/magpie/` folder instead. Folders that start with a dot
are hidden: on a Mac, press Cmd+Shift+. in Finder to show them; on
Windows, turn on **Hidden items** in File Explorer's **View** menu. More
in Claude Code's [skills docs](https://code.claude.com/docs/en/skills)
(checked October 28, 2026).

### Other agent tools (Codex, OpenCode, Gemini CLI)

These tools can load Magpie the same way Claude Code does, but **Magpie
hasn't been tested in them yet.** Ask your tool to install it, for
example: *"Install the skill in ~/Downloads/magpie.zip so it works in all
my projects."* It knows where its own skills go. Then start a
conversation and ask for help with a study, or say "magpie". If
something doesn't work, please
[open an issue](https://github.com/kirstenhosic/user-research-assistant/issues).

### Claude.ai

You need a Claude.ai account with Projects.

1. Create a new Project.
2. Unzip `magpie.zip` and add all the `.md` files to the project's
   knowledge.
3. Paste the contents of `operating.md` into the project's instructions.
4. Start a chat in the project and describe your study.

### ChatGPT

ChatGPT adds Magpie as a skill. OpenAI's help center lists skills for
Business, Enterprise, Healthcare and Edu workspaces (checked October 26,
2026); on a personal plan, try the steps anyway.

1. In the sidebar, open **Plugins**, then the **Skills** tab.
2. Choose **Create** > **Upload from your computer** and upload
   `magpie.zip`.
3. If ChatGPT says **Needs Review**, read what it flags. The only code in
   the package is five small scripts that check quotes and counts and
   make Word and Excel files; none of them connects to the internet.
4. Install it, then start a chat and @-mention `magpie`, or just describe
   your study.

**If there's no Skills page:** unzip `magpie.zip`, create a Project,
paste `operating.md` as the project instructions, and add the other `.md`
files as project files.

### Gemini

You need a Google account signed in to Gemini, with Keep Activity turned
on.

1. Go to gemini.google.com. In the sidebar, open **Customize** (it may be
   under **More**), then **Skills**.
2. Choose **Create** > **Upload** and pick
   **[magpie-gemini.zip](https://github.com/kirstenhosic/user-research-assistant/raw/main/magpie-gemini.zip)**,
   not `magpie.zip`. Gemini won't load a skill that contains code, and
   this copy leaves the code checks out. Magpie does those checks by hand
   instead.
3. Check what Gemini shows, then choose **Create**.
4. In a chat, type `/magpie`, or just describe your study.

Uploading works in the web app and the Mac app, not the phone apps.

### Copilot

Use **Cowork** in Microsoft 365 Copilot. At work you need a Copilot
license, and your admin has to turn Cowork on. On a personal Microsoft
account you need Microsoft 365 Premium or Pro, in the US or Canada.
Personal, Family and the free Copilot app don't have Cowork.

1. Download
   **[magpie-copilot.zip](https://github.com/kirstenhosic/user-research-assistant/raw/main/magpie-copilot.zip)**,
   not `magpie.zip`. It has its files combined to fit Copilot's file limit.
2. In Cowork, open **Customize** > **Skills**, choose the arrow next to
   **Add**, then **Upload skill**, and pick `magpie-copilot.zip`.
3. When it appears under **Your skills**, start a chat and describe your
   study.

More detail is in the [Copilot setup notes](adapters/copilot/README.md).

### Any other assistant

Upload `magpie.zip` if the assistant takes skills. If it has projects or
knowledge files instead, set it up like Claude.ai: paste `operating.md`
as the instructions and add the other `.md` files.

### Keep Magpie up to date

Magpie is in its early days and gets better often. Check for a new
version every week or two, so you're always using the best one.

1. See what's new in the [changelog](docs/CHANGELOG.md). The newest
   changes are at the top, with the date.
2. If anything has changed since you set Magpie up, download
   **[magpie.zip](https://github.com/kirstenhosic/user-research-assistant/raw/main/magpie.zip)**
   again, or `magpie-gemini.zip` or `magpie-copilot.zip` if you use
   Gemini or Copilot.
3. Replace your old copy the same way you installed it: unzip it over the
   old `magpie` folder in Claude Code, upload the new zip in place of the
   old skill, or swap in the new `.md` files and `operating.md` in your
   project.

In the middle of a study? Start a new conversation with the new version
and paste in your study record, and Magpie picks up from there.

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
  research practice, such as Nielsen Norman Group or the ICC/ESOMAR code,
  the source is listed in [`docs/PROVENANCE.md`](docs/PROVENANCE.md).
  Where it's professional judgment, it says so.
- **It can be wrong.** Like any AI assistant, Magpie makes mistakes, and
  its independent reviews are done by an AI too. The study record and the
  participant references are there so you can check its work. Please do.

Found a problem? [Open an issue](https://github.com/kirstenhosic/user-research-assistant/issues)
with the tool you used, the step, and what you saw.

## When something goes wrong

- **The assistant doesn't seem to know Magpie.** In Claude Code, check the
  file is at `.claude/skills/magpie/SKILL.md`. In other tools, check the
  skill is installed and turned on, then name it in the chat.
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
- **The quote or count check didn't run.** Not every assistant can run
  scripts. When it can't, Magpie checks by reading and tells you so.

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

The license covers the Magpie files only. It doesn't give permission to
use any particular AI tool at work, or to share any data with one; see
[Using Magpie at work](#get-started).
