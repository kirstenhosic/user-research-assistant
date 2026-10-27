# Session persists

**Stage:** 2, then across later turns

## Setup

Turn 1. The researcher starts Magpie:

> /magpie Our onboarding team wants to know why new admins don't finish
> setup. Decision is whether to rebuild the setup wizard next quarter.

Magpie replies. Then, later in the same conversation and without naming
Magpie again:

> Turn 2: Unrelated, but can you tidy this note to my PM? "hey, research
> plan coming thurs, need 6 admins from the trial list."

> Turn 3: PM just said the decision moved up, they need an answer by the
> 14th, not end of quarter.

## Planted problem

None in the content. The test is whether Magpie says it's on, stays on
for the whole conversation without being called again, and shows that it
is still on.

## Pass

- The first reply opens with the "Magpie is on" line and ends with the
  status line.
- Turn 2 is answered as Magpie: the note is tidied, and the reply still
  ends with the status line. Magpie may note that "6 admins from the trial
  list" is a sample decision worth logging.
- Turn 3 is treated as a change of decision: Magpie lists the record
  sections that depend on the deadline and offers to update each, and the
  status line is still there.
- Never asks the researcher to start or name Magpie again.

## Fail

- Drops the status line on turn 2 or 3, or answers as a general assistant
  with the study forgotten.
- Asks the researcher to call Magpie again.
- Treats the deadline change as small talk.

## Standards tested

A.9, A.2
