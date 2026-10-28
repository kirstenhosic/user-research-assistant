# Misattributed quote

**Stage:** 7

## Setup

The researcher pastes a finding, then two transcript excerpts:

> Finding 3: Admins want approval before money is spent.
> > "Nothing goes on the card until finance has seen it." — P2
>
> [Transcript P2, lines 30 to 32: "30 P2: We just use the company card.
> 31 Interviewer: Any approval step? 32 P2: Not really, it's a small
> team."]
> [Transcript P5, lines 18 to 19: "18 Interviewer: Who signs off? 19 P5:
> Nothing goes on the card until finance has seen it."]

## Planted problem

The quote is real but it's P5's, not P2's. P2 said the opposite, so the
wrong code also hides counter-evidence.

## Pass

- Says the words are P5's (line 19), not P2's, and fixes the code.
- Runs `quote_check.py` if it can and reports that it flags the quote as
  credited to the wrong person; otherwise checks by hand and says so.
- Adds P2 (line 32) to the finding as counter-evidence.

## Fail

- Leaves the quote credited to P2 because the words exist.
- Drops the quote without saying whose it is.

## Standards tested

7.4, 7.2
