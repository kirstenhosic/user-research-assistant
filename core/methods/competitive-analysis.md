# Method: competitive analysis

Look at how other tools solve the same problem your users have, and work
out what would fit your users and what wouldn't. The unit of comparison is
the user's job, not the feature list.

## Use it when

- The team is deciding whether or how to build something others already
  offer.
- You want to know what users will expect because they've seen it
  elsewhere.
- You need a quick, cheap source of design options before a concept test.
- Sales or marketing keep citing a competitor and nobody has looked
  properly.

## Don't use it when

- You want to know what *your* users do or need. Competitors can show you
  options; only your users can tell you what fits.
- The decision is "copy them or not". That's not a research question.
- Nobody can name the user problem the comparison is about.

## Sample

- Two to four products that your users could plausibly use instead,
  including at least one that isn't a direct competitor but solves the
  same job another way (a spreadsheet, a manual process, an adjacent
  tool).
- Three to five user jobs or journey steps to compare across them, taken
  from the study record, not from a feature list.

## Access: hands-on or public sources only

Find out early which of two routes this is. Ask once if it isn't clear.

- **Hands-on.** Someone can use each tool: an account, a free tier, a
  trial the team has set up. The researcher walks the job, or Magpie does
  where the setup lets it open the tool.
- **Public sources only.** Nobody on the team can get into the tools.
  This is common and still worth doing. Build the comparison from what's
  public, best first:
  1. Help docs, tutorials and onboarding guides. They often show the real
     screens step by step.
  2. The product's own demo videos, webinars and walkthroughs.
  3. Public pages of the product itself (a sign-up flow, a public
     template gallery, a pricing and plans page).
  4. Release notes and changelogs, for what changed and when.
  5. Public reviews, community forums and app store listings, for what
     users say goes wrong. These are other people's users, not yours.
  6. Marketing pages and analyst summaries, for positioning and claims.

  Help docs and demos show how a task is meant to go, not how it goes for
  a user. Errors, dead ends and slow steps rarely show up in them, so the
  fit assessment leans harder on "check with our users", and "What this
  can't tell us" says so.

Either way, mark each tool and each cell with how it was seen:

- **walked:** someone did the task in the tool.
- **shown:** material that shows the real screens: screenshots, a screen
  recording, help docs with screen images, a demo video.
- **described:** someone's words about the tool: marketing copy, a review,
  an analyst note, a sales deck.

A cell that is only **described** is a claim, not an observation. Never
call a marketing page an observation.

## What Magpie can take in

What Magpie can read depends on the tool it's running in. It says which
of these it can use in this setup, in one line, and never pretends to
have read something it couldn't.

- **Screenshots and photos.** Magpie reads what's on screen: the step, the
  words the tool uses, the choices offered. It asks which step each image
  shows if that isn't clear, and doesn't guess what happens off screen.
- **Screen recordings and demo videos.** Where Magpie can take video, it
  works through it and cites the moment (timestamp) for each step. Where
  it can't, it says so and asks for a still of each step, a transcript,
  or a short written walk-through. It never describes a video it hasn't
  seen.
- **Web pages and links.** Where Magpie has web access, it reads public
  pages and logs each one with its URL and the date read. Where it
  doesn't, it says so and asks for the page text or a screenshot. It
  doesn't sign up for accounts or trials, enter anyone's details, or get
  around a login or paywall; that's the researcher's call and the
  researcher's account.
- **Notes.** A researcher's written walk-through of a tool counts as
  **walked** for the steps they did.

## Shape

1. **Start from the job.** Name the user, the job and the journey step
   from the study record. Write the question: "How do people get [job]
   done in [tool], and what would fit our [persona]?"
2. **Pick the set.** Two to four tools, with one that solves the job
   differently. Say why each is in.
3. **Walk the job in each tool, or trace it from public sources.** Do the
   task as the user would. Record what happens at each step: screenshots,
   the words the tool uses, where it asks for effort, where it decides for
   the user. Note what it assumes about the user. With public sources
   only, trace each step through help docs and demos, and leave a step
   blank, marked "not shown publicly", rather than guess.
4. **Compare on fit, not on count.** For each job step and each tool: how
   the tool handles it, what it assumes about the user, and whether that
   assumption holds for your persona. "Has feature X" is not a row.
5. **Separate what you saw from what you infer.** What the tool does is
   [their data] about the tool when it was walked or shown, with the
   source. Why it does it, and
   whether their users like it, is [assumption] unless you have evidence
   (public reviews, support forums, a user who's used both).
6. **Draft the fit assessment.** For each pattern worth considering: what
   it would solve for your users, what it would cost them, which persona it
   suits, and what you'd need to check with real users before adopting it.

## What makes it good

- Doing the task in each tool where you can. Where you can't, using
  material that shows the real screens over marketing claims, and saying
  which cells rest on which.
- A tool from outside the category in the set.
- Every "they do X" paired with "and that fits or doesn't fit our users
  because".
- Honest about what you can't see: their data, their users' satisfaction,
  why they made a choice.
- Dated. Competitors change; the analysis has a shelf life. Say when it
  was done.

## Analysis

A fit matrix: job steps down the side, tools across, each cell saying how
the tool handles it and what it assumes. Then the patterns: what everyone
does (users will expect it), what nobody does (a gap or a dead end), what
one tool does well that would suit your persona. Then the fit assessment
per pattern. Stage 7 covers the write-up; `templates/competitive-analysis.md`
has the shape.

## What it feeds

- **Stage 3:** a sharper sense of what users may already expect.
- **Stage 4:** design options for a concept test.
- **Stage 8:** "here's how others handle it and why it would or wouldn't
  fit us", as context for a recommendation, never as the recommendation's
  evidence on its own.

## Pitfalls

- A feature checklist with ticks. It tells you what exists, not what fits.
- Calling a marketing page or a demo video an observation of how the tool
  works for users. A demo shows the happy path.
- Filling a cell from memory of how a tool used to work.
- Assuming a competitor's choice is good because they're big.
- Treating public reviews as your users' views.
- Only looking at direct competitors, and missing the spreadsheet everyone
  actually uses.
- Letting the analysis become the recommendation. "Competitor X does it"
  is a reason to test, not a reason to build.

## Template

`templates/competitive-analysis.md`

## Basis

S24 (compare on the key tasks users need to complete; look at tangentially
related businesses for perspective; the aim is to beat the competition,
not copy it; observe what users actually do). Separating what was observed
from what is inferred, the fit matrix and the shelf-life note: practitioner
judgment.
