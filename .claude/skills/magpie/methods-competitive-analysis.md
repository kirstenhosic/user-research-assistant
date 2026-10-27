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

## Shape

1. **Start from the job.** Name the user, the job and the journey step
   from the study record. Write the question: "How do people get [job]
   done in [tool], and what would fit our [persona]?"
2. **Pick the set.** Two to four tools, with one that solves the job
   differently. Say why each is in.
3. **Walk the job in each tool.** Do the task as the user would. Record
   what happens at each step: screenshots, the words the tool uses, where
   it asks for effort, where it decides for the user. Note what it assumes
   about the user.
4. **Compare on fit, not on count.** For each job step and each tool: how
   the tool handles it, what it assumes about the user, and whether that
   assumption holds for your persona. "Has feature X" is not a row.
5. **Separate what you saw from what you infer.** What the tool does is
   [their data] about the tool, observed directly. Why it does it, and
   whether their users like it, is [assumption] unless you have evidence
   (public reviews, support forums, a user who's used both).
6. **Draft the fit assessment.** For each pattern worth considering: what
   it would solve for your users, what it would cost them, which persona it
   suits, and what you'd need to check with real users before adopting it.

## What makes it good

- Doing the task in each tool, not reading their marketing.
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
per pattern. Stage 6 covers the write-up; `templates/competitive-analysis.md`
has the shape.

## What it feeds

- **Stage 2:** a sharper sense of what users may already expect.
- **Stage 3:** design options for a concept test.
- **Stage 7:** "here's how others handle it and why it would or wouldn't
  fit us", as context for a recommendation, never as the recommendation's
  evidence on its own.

## Pitfalls

- A feature checklist with ticks. It tells you what exists, not what fits.
- Assuming a competitor's choice is good because they're big.
- Treating public reviews as your users' views.
- Only looking at direct competitors, and missing the spreadsheet everyone
  actually uses.
- Letting the analysis become the recommendation. "Competitor X does it"
  is a reason to test, not a reason to build.

## Template

`templates/competitive-analysis.md`

## Basis

Practitioner judgment. Sources will be added to `docs/PROVENANCE.md` as they
are checked.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
