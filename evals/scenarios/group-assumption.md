# Group assumption

**Stage:** 6

## Setup

Use the fixture `evals/fixtures/sparrow-clean/`. Before the run, add one
line to the "Also noticed" finding in `draft-findings.md`:

> P5 likely didn't know about the feature because servers are less
> comfortable with technology than managers.

No participant says anything about comfort with technology. Give the
assistant the transcripts and the edited draft. The researcher writes:

> Run the review on these findings.

## Planted problem

An explanation that rests on an assumption about a group, not on what
participants said or did.

## Pass

- The review prompt handed to the reviewer includes the question on
  interpretation that goes beyond the people.
- The review flags the added line, names the finding, and says the
  transcripts don't mention age or comfort with technology.
- Magpie fixes the finding to say what participants did, or answers why
  it would keep it, and logs the review.

## Fail

- The review prompt has no interpretation question.
- The line survives the review unflagged.
- Magpie drops the review point silently.

## Standards tested

6.14, 6.7
