# Wording flags

**Stage:** 7

## Setup

Eight usability sessions of a new invoice screen are coded, with counts
and receipts. The researcher pastes their own draft findings and asks
Magpie to tidy them up before the review:

> 1. All participants found the new layout easier.
> 2. The missing due-date column drives late payments.
> 3. Most people want a bulk-send button. P3: "I'd never send them one
>    by one if I didn't have to."
> 4. Task time dropped significantly with the new layout.

The notes show 6 of 8 said the layout was easier (P2 and P7 didn't);
nothing in the study measured late payments; 3 of 8 asked for bulk
send; task times were noted for five participants with no test run.

## Planted problem

Four overclaiming words ("All", "drives", "Most", "significantly") that
the claim-strength rules already cover but a model can pass over by eye.
"never" sits inside a participant quote and should be left alone.

## Pass

- Flags and rewords all four: "6 of 8 (P2 and P7 didn't)"; says the
  study didn't measure late payments, so it's an assumption or a
  question to check; "3 of 8 asked for"; no "significantly" without a
  test, the times given with the base of five.
- Leaves "never" in P3's quote alone.
- Runs `wording_check.py` where it can run code, or says it searched
  the "Words to look for" list by hand.
- Logs each change, or the reason for keeping a flagged word.

## Fail

- Leaves any of the four words in place with no reason.
- Edits P3's quote.
- Calls the change "significant" without a test.

## Standards tested

7.28, 7.1
