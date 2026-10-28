# Method: analytics and A/B tests

Learn from records of what people do in a live product. Analytics shows
what happens and where: which pages people reach, what they search for,
where they leave a form. An A/B test splits live traffic between the
current version (A) and a changed one (B) to see which does better on a
measure chosen in advance. Both show what people do, at scale. Neither
shows why.

## Use it when

Analytics:

- You need to know where to look: where people drop off, what they search
  for, which paths they take. Use it before choosing whom to talk to or
  what to test.
- You saw a problem in a few sessions and want to know how big it is. A
  small test finds the spot; analytics on that spot gives thousands of
  data points.
- You want to check whether something heard in interviews or seen in
  tests shows up in real use.

A/B tests:

- The team is choosing between two versions of a live page or flow, the
  versions differ in one thing, and the result can be judged on a measure
  the business already tracks (sign-ups, completed orders, people still
  using it after a month).
- The page gets enough traffic. A reliable answer often takes thousands
  of people.

## Don't use it when

- The question is why. Pair it with interviews or usability sessions.
- Nothing is live yet. There's no data.
- For an A/B test: the page gets little traffic; the versions differ in
  many things at once, so you couldn't tell which change mattered
  (testing several changes together needs even more traffic); or there's
  no idea from research about why B should do better.
- For analytics: there's no question yet. Without one, it's easy to spend
  days in interesting numbers that lead nowhere.

## Before you start

**Analytics**

- Write the question, and which numbers would answer it.
- Check that the step you care about is tracked. Some need setting up
  first.
- Read numbers as clues, in context. Long time on a page could mean
  interest or confusion; it isn't good or bad on its own.
- Remember who the logs can't see. A funnel starts counting when
  someone enters it. People who wanted to do the task and never found
  the way in aren't in the data, so an 80% completion rate inside the
  flow can hide a 40% success rate for everyone who tried. When the
  question includes "can people find it", pair analytics with a
  benchmark or a first-click test that starts from the top
  (`methods/benchmarking.md`,
  `methods/card-sorting-and-tree-testing.md`).
- If the team has a metrics framework (`methods/benchmarking.md`, "What
  to measure"), ask which goal and signal each number serves. A number
  with no goal behind it is a chart, not an answer.

**A/B tests**

- One hypothesis, based on research: "Showing the delivery date on the
  basket page will mean fewer people leave at shipping, because in
  sessions people left to look for it."
- One main measure, plus a few guardrail measures: things that mustn't
  get worse, such as returns or people coming back.
- Set how long it runs before it starts, from how often the thing happens
  now, the smallest change worth detecting, and how sure you need to be
  (usually 95%). Run at least one to two full weeks so weekday and weekend
  behavior are both in. Don't stop early because B looks ahead.
- With a new testing tool, run both groups on the same version first. If
  the tool shows a winner, the tool is wrong.

## Who does it

Usually a partner team (analytics, growth or engineering) owns the tools
and the data. Magpie drafts the question and the request (stage 4,
partner data) and helps read the results. It doesn't run the test.

## Analysis

- **Analytics:** each number with its time period, what it counts and
  what it doesn't track. Say what it suggests and what it can't tell you.
- **A/B tests:** the result on the main measure and the guardrails, and
  whether the difference passed the test set in advance. Then whether
  it's big enough to matter to the business, which is a separate
  question, answered against a bar agreed before the test. "No clear
  winner" is a result: keep the current version.
- **Report the difference in its own unit,** with the range it probably
  sits in: "2.1 percentage points more sign-ups (likely between 0.8 and
  3.4)", not a standardized effect size. Say what it means at volume:
  2.1 points on 50,000 visitors a month is about 1,050 sign-ups. Small
  differences add up when the thing happens often; a 17-second saving
  on a task done a hundred times a day is weeks a year.
- **The range and the p value usually agree.** When one says
  "different" and the other doesn't, both are sitting near the cutoff.
  Treat a result at 94% confidence like one at 95% unless the setting
  demands a guarantee; a rigid cutoff is for publication, not product
  decisions. For two conversion rates, the test is the N−1
  two-proportion test and the range is the adjusted-Wald interval
  around the difference (stage 7, "Numbers from small samples"). Read
  the low end of the range at volume too: a small lower limit can still
  be a lot of orders.

## Worked example

> **Decision.** Whether Harbor (team task board) shows the "invite your
> team" step during setup or after the first board is built. Growth
> decides in a month.
>
> **Analytics first.** Question: where in setup do new admins stop? The
> funnel showed 61% of admins who started setup invited someone within a
> week (data for September, 2,140 admins); it can't see admins who
> wanted to invite and never found the button. Interviews earlier found
> most admins build a board before inviting.
>
> **A/B test.** Hypothesis from research: moving the invite step to
> after the first board is built will raise invites within a week,
> because admins want something to show. Main measure: admins who
> invited within seven days. Guardrails: boards created in the first
> week; admins active at day 30. Run for two full weeks, size set from
> September's rate and a smallest change worth detecting of 4 points.
>
> **Result, as reported.** 66.2% against 61.1%: 5.1 points more, likely
> between 2.0 and 8.2; guardrails unchanged; at about 2,000 admins a
> month, about 100 more teams invited a month. The agreed bar (4 points)
> was met. Why it worked is from the interviews, not the test.

## Pitfalls

- Reading why from what. The numbers show people left; sessions show why.
- Stopping an A/B test the day it looks like a win.
- Judging on one measure and missing harm somewhere else.
- Calling a statistically significant difference an important one.
- Treating a test with no winner as a failure. Many tests end that way,
  which is why the hypothesis should come from research.

## Template

No template. Draft the request in the study record under partner data:
the question, the numbers, the time period and when they're needed.

## Basis

S75 (three uses of analytics: spotting issues, investigating them, and
checking findings from qualitative research; numbers as clues read in
context; a small test finds the spot and analytics sizes it; the risk of
data with no question). S74 (what an A/B test is; live product and
enough traffic, often thousands of users; one change at a time; a
hypothesis from research; main and guardrail measures; duration set in
advance, at least one to two weeks; an A/A test of a new tool; don't stop
early; statistically significant is not the same as important; many tests
find no winner; it shows
how behavior changes, not why; pair it with qualitative research). S11
(analytics, clickstream and A/B testing as measuring methods for a live
product). S13 (combine methods so one covers another's limits). S87
(analytics can't see users who never found the task's entry point; the
80% inside the flow against 40% of those who tried; pair with
benchmarking or a first-click test for navigation). S97 (goals, signals,
metrics). S84 and S85 (raw differences with intervals over standardized
effects; make them concrete at volume; small effects add up with
repeated exposure; set the action threshold before collecting data).
S100 (pp. 78–93: the N−1 two-proportion test for two groups of
different users, recommended when every expected cell count is above 1,
Fisher exact otherwise; the adjusted-Wald interval around the difference
between two proportions, adding one success and one failure to each
group; an A/B example at 90% confidence where even the low end of the
range meant a lot of revenue at volume; p values fluctuate by a few
points with the method chosen; a confidence interval and a p value usually point the
same way, and 94% against 95% confidence shouldn't change an applied
decision; a rigid 0.05 cutoff for publication). Who does the work:
practitioner judgment.
