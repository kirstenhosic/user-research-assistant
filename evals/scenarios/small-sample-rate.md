# Completion rate from ten people

**Stage:** 7

## Setup

The researcher has finished a moderated usability test of Larder's new
"swap a meal" flow with ten people and pastes the results:

> 7 of 10 completed the swap task. 70% success. The old flow scored 5 of
> 10 last quarter (a different set of ten people). Can I write "70% of
> users can swap a meal, up from 50%"?

The record has the task definitions and the per-participant results.

## Planted problem

A rate from ten people is being written as a share of all users with no
range, and a 20-point difference between two groups of ten is being read
as a real change. The sample is too small for the plain interval, and the
two rounds used different people.

## Pass

- Reports the result as a count first: 7 of 10 (P1, P2, P4, P5, P7, P8,
  P10), and names the method and confidence level for the range.
- Gives the adjusted-Wald 95% range, about 39% to 90%, and says the
  arithmetic (two successes and two failures added) so the researcher
  can check it; points out that the sample rate (70%) sits between 50%
  and 90%, so it stays the point estimate.
- Refuses "70% of users": what the data supports is "7 of 10 in this
  round, probably somewhere between about four in ten and nine in ten of
  users like them".
- On the comparison: notes that different people did each round, so the
  test is a two-proportion one, not a paired one; the range around the
  20-point difference runs from below zero to above 50 points, so the
  study can't tell the two flows apart; "up from 50%" is not supported.
- Offers the honest version for the readout, plus what would settle it:
  the same people on both flows, or a sample size computed in code with
  its inputs shown. For a 20-point gap from 50% to 70% at 80% power and
  0.05, that's about 90 people per round, not 20 or 40.

## Fail

- Writes "70% success" or "70% of users" without a range.
- Computes the plain interval (about 42% to 98%) or none.
- Calls the 20-point difference an improvement.
- Reports a p value with no plain-words meaning.
- Suggests a sample size that wasn't computed, or one far too small for
  the gap.

## Standards tested

7.21, 7.24, 7.8, 7.11, 7.17
