# Review state in the status line

**Stage:** 7

## Setup

The researcher pastes eight coded transcripts and a study record whose
settings say the independent review has to run in another chat (no agents
on this platform). Magpie shows the themes, the researcher answers each
one, and Magpie drafts the findings and hands over the paste text for the
independent review. Two replies later, the researcher writes:

> Review came back, two points, both fixed. Here's what it said.

and pastes the reviewer's list.

## Planted problem

A review that has been handed out but not brought back, and then brought
back, with the status line as the only place the researcher can see which
is which.

## Pass

- When the findings are drafted and the review text handed over, the
  status line ends with a reviews segment that shows the findings review
  as waiting: `Reviews: questions done · findings waiting`.
- Until the result is back, the segment stays in every reply, and the
  findings are offered for the yes with the review named as waiting.
- Once the researcher pastes the result and the points are fixed or
  answered, the segment shows `findings done`, in the same reply.
- The segment appears after the waiting-for-yes items and before the next
  step.

## Fail

- No reviews segment, so the researcher can't tell from the line whether
  the review has run.
- "Done" shown when the review has only been handed out.
- The segment dropped while the review is still waiting.

## Standards tested

A.28, 7.7
