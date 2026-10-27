# Method: surveys

Ask many people the same questions to measure how common an attitude,
behaviour or need is.

## Use it when

- The question is *how many*, *how often*, or *which groups differ*.
- You already understand the problem well enough to write good closed
  questions. (If you don't, interview first.)
- You can reach enough of the right people to say something about them.

## Don't use it when

- The question is *why*. Surveys get thin answers to why.
- You'd be surveying whoever's easiest to reach and calling it "users".
- A number already exists in analytics.

## Sample

- Who answers matters more than how many. A self-selected sample describes
  the people who chose to answer.
- Rough guide: a few hundred responses for an overall picture; enough in
  each group you want to compare that the comparison means something. Plan
  the cross-tabs before you send.
- Say the response rate and who answered in the readout.

## Survey shape (under ten minutes)

1. Intro: what it's for, how long, what's done with answers.
2. Screener: behaviour-based.
3. Main sections, general to specific, one topic each.
4. One or two optional open-ends where a story helps.
5. Demographics last, each with "prefer not to say".
6. Thanks, and what happens next.

## What makes it good

- Every item maps to a research question.
- Run `checks/survey-wording.md` before sending.
- Pilot with five people, watch them fill it in, and fix what confuses them.
- Decide the analysis plan before the data arrives.

## Analysis

Descriptives first: counts and percentages with the base shown. Cross-tabs
only where groups are big enough. Open-ends coded like interview data. Say
what the numbers can and can't support; don't claim significance without a
test, and even with one explain it in plain words. Stage 6 covers this,
including how to state a test result, a margin of error or a sample size.

## Pitfalls

- "Would you use…?" items. Ask about the past, not the future.
- Agree/disagree batteries that people agree their way through.
- A 25-item survey that gets ten honest answers and fifteen fast ones.
- Reporting percentages from forty responses as if they were the market.

## Template

`templates/survey.md`

## Basis

Practitioner judgment, consistent with widely published survey design
guidance. Sources will be added to `docs/PROVENANCE.md` as they are checked.
