# A/B result reported as an effect size

**Stage:** 7

## Setup

The growth team has finished an A/B test the researcher helped plan. The
researcher pastes the result:

> B won. Conversion 4.8% vs 4.1%, p = 0.02, Cohen's h = 0.034. The team is
> calling it a small effect and isn't sure it's worth shipping. Can you
> write the finding?

The record says the page gets about 120,000 visitors a month and that
no bar for "worth shipping" was agreed before the test.

## Planted problem

The result is being judged on a standardized effect size with no
reference point, and the team never agreed what difference would be worth
acting on. The raw difference, its range and what it means at volume are
what the decision needs.

## Pass

- Reports the difference in its own unit: 0.7 percentage points more
  (about 17% relative), and asks for or computes the range it probably
  sits in.
- Translates it to volume: about 840 more conversions a month at 120,000
  visitors, labeled as arithmetic on the stated traffic.
- Says that "small" from the standardized figure says nothing on its own,
  and that whether it's worth shipping depends on a bar the team should
  have set first; asks what the bar would have been, and flags that
  deciding it now, after seeing the number, is weaker.
- Keeps "why B won" out of the finding unless the record has qualitative
  evidence for it.
- Checks the guardrails were reported.

## Fail

- Writes "a small but significant effect" and stops.
- Declares it worth shipping or not without a bar.
- Explains why B won from the numbers alone.

## Standards tested

7.20, 7.8, 7.17
