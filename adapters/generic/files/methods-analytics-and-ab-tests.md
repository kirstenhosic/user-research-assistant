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

**A/B tests**

- One hypothesis, based on research: "Showing the delivery date on the
  basket page will mean fewer people leave at shipping, because in
  sessions people left to look for it."
- One main measure, plus a few guardrail measures: things that mustn't
  get worse, such as returns or people coming back.
- Set how long it runs before it starts, from how often the thing happens
  now, the smallest change worth detecting, and how sure you need to be
  (usually 95%). Run at least one to two full weeks so weekday and weekend
  behaviour are both in. Don't stop early because B looks ahead.
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
  question. "No clear winner" is a result: keep the current version.

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

S72 (three uses of analytics: spotting issues, investigating them, and
checking findings from qualitative research; numbers as clues read in
context; a small test finds the spot and analytics sizes it; the risk of
data with no question). S71 (what an A/B test is; live product and
enough traffic, often thousands of users; one change at a time; a
hypothesis from research; main and guardrail measures; duration set in
advance, at least one to two weeks; an A/A test of a new tool; don't stop
early; statistically significant is not the same as important; many tests
find no winner; it shows
how behaviour changes, not why; pair it with qualitative research). S11
(analytics, clickstream and A/B testing as measuring methods for a live
product). S13 (combine methods so one covers another's limits). Who does
the work: practitioner judgment.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
