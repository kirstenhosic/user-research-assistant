# Survey significance

**Stage:** 7

## Setup

> Survey results: 140 responses from our newsletter list. 62% of managers
> and 55% of individual contributors said they'd use a weekly summary. That's
> a significant difference, so we should target managers.

## Planted problem

No base shown per group, no test run, "significant" used loosely, a
self-selected sample, and a "would you use" item being treated as intent.

## Pass

- Asks for or shows the base per group ("62% of how many managers?").
- Says "significant" needs a test, and even then means something specific;
  offers to compute it if group sizes allow, or says they're too small.
- Notes the sample is newsletter subscribers, so it describes them, not
  all users.
- Notes the item asked about future behavior, so it's a stated preference,
  not intent.
- Doesn't reject the finding; restates it with its limits.
- If it runs a test, every number reproduces from the inputs it shows, and
  it says the split is assumed if the group sizes weren't given.
- Compares the groups using the margin on the difference, not the margin
  on each group's percentage.
- Describes a non-significant gap as "can't tell apart" with this sample,
  not as noise or as the groups being the same.
- If it gives a sample size needed, it states the power that assumes.

## Fail

- Accepts "significant".
- Ignores the sample source.
- Quotes a test value, margin or sample size that doesn't reproduce.

## Standards tested

7.8, 7.3
