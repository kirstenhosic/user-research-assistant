# Method: benchmarking

Measure how well a product works with a few set numbers, then compare
them with something: an earlier version, a competitor, a published figure
or a goal the team set. Repeat it to see whether the experience is getting
better.

## Use it when

- A version of the product is finished or live, and the question is "is
  it better than before?", "did the redesign work?" or "how do we compare
  with X?".
- The team wants a few numbers to track from release to release, or to
  show what design work changed.
- A redesign is about to start. Measure now, so there is a starting point
  (a baseline) to compare against later.

## Don't use it when

- You need to know why something is hard. A benchmark says how much, not
  why. Pair it with moderated usability testing, before or after.
- The design is still changing every week. A benchmark is a snapshot of
  one version; measure a version that will hold still.
- You can only get five or six people. That's a usability test, not a
  benchmark; numbers from it carry too much error to compare.

## What to measure

- A few numbers tied to what the product is for. Common ones: task
  success rate, time on task, an ease rating after each task (the Single
  Ease Question), a questionnaire score after the session (the System
  Usability Scale), or something analytics records, such as how many
  people finish a form or come back after eight weeks. Support contacts
  about a task can count too.
- If the team has a metrics framework, pick from it. One common one
  names five kinds of measure: happiness (attitudes: satisfaction, ease),
  engagement (how often and how deeply people use it), adoption (new
  users in a period), retention (who's still there later) and task
  success (completion, time, errors). Not every project needs all five;
  a tool people must use at work may care about task success and
  happiness and not engagement. For each goal the team names, decide
  what people would do or say if it were met (the signal), then how to
  count it as a rate or a per-user figure, not a raw count that grows
  with the user base (the metric).
- Start tasks from the home screen, not inside the flow. Analytics only
  sees people who got into a flow; it can't count the ones who wanted to
  and never found the way in. A benchmark that starts each task from
  the top catches them, and failing to find the start is often the
  biggest problem.
- Choose what you'll compare against before you measure. A number on its
  own means nothing. In the first round there is no earlier version, so
  compare with a competitor, a published figure or a goal the team agrees
  on.

## How to collect

Quantitative usability testing (fixed tasks, many people, usually
unmoderated), analytics, or a survey. Analytics is quick to repeat;
testing rounds take longer and cost more.

## Sample

- Twenty or more people per user group for task numbers or questionnaire
  scores, and the same kind of people each round.
- Every score gets its range: a t-interval around the mean for SUS and
  SEQ, the geometric mean with its interval for task times below about
  25 people, the adjusted-Wald interval for completion rates (stage 7,
  "Numbers from small samples"). Halving a range takes four times the
  people, so plan the sample from the precision the decision needs.
- Comparing two rounds: the same people on both is a paired comparison;
  different people is a two-sample one. Say which.
- Recruit people who would really do these tasks.

## Keep it comparable

Use the same tasks, wording, order, success criteria, kind of participant
and way of collecting every round. Write them in the study record so the
next round can repeat them exactly. If one has to change, say so in the
report; the comparison is weaker for it.

## How often

The team decides. Testing rounds might run once a year or after a major
release; analytics can be checked after every change.

## Analysis

Each number with its sample size and margin of error, next to what it's
compared with. Test the difference before calling it a change (stage 7).
Say what else changed between rounds besides the design (a new kind of
customer, a price change, a season).

Report a change in its own unit ("12 points higher completion", "20
seconds faster"), with the range it probably sits in, and say what it
means at the product's volume ("about 400 more completed orders a
month"). Agree before the round what size of change would count as
worth acting on; deciding afterwards makes any result look like the
one the team wanted.

A SUS score is not a percentage. Across about 500 studies the average
is 68; above 68 is better than average, and a 74 is only a little
above it. Report it against that average, or as a percentile, so the
team doesn't read 68 as "a D". Two large published sets of SUS scores
had means near 70 and near 62 with a typical spread of about 22 points
either way, so single-study differences of a few points sit inside the
noise; give the interval. SUS also tracks the likelihood-to-recommend
question: a rough rule is recommend score ≈ SUS ÷ 10, and in one large
set people who would recommend averaged a SUS of about 81 against
about 52 for those who wouldn't, so a SUS above 80 is a fair "people
would recommend it" bar. If the team wants a letter, use the curved
grading scale built on those percentiles rather than a school scale:
68 is a C (about the 50th percentile), roughly 72.6 to 74 is a B−,
78.9 to 84 is an A, 84.1 and above is an A+, and below 51.7 is an F.
Averages also differ by kind of product: in the same data, enterprise
software averaged about 68, public consumer software about 74,
websites about 67 and phone-and-speech systems about 60, so compare
against the closest kind where one exists, and say which was used.

Net Promoter Score (NPS) is a single likelihood-to-recommend item on
0 to 10, promoters (9 or 10) minus detractors (0 to 6) as percentages.
Collapsing eleven points to three loses sensitivity, and there is no
agreed interval for it. If the team tracks it, keep the raw 0 to 10
answers, report their mean with a t-interval, and when a range on the
NPS itself is needed, recode each answer to −1, 0 or +1 and compute a
t-interval on that; the book calls this an untested but reasonable
approach. Ask why alongside it; the number alone says nothing about
what to change.

## Worked example

> **Decision.** Whether the BrightPay (payroll) pay-run redesign, live
> since March, is better than the old one, and whether to roll it out to
> the remaining accounts.
>
> **Measures, chosen before March.** Task success and time for "run this
> month's payroll for 12 employees with one new starter", from the home
> screen; an ease rating after the task; SUS after the session; from
> analytics, pay runs completed in one sitting. Comparison: the same
> study run on the old version in January.
>
> **Sample.** 42 payroll admins per round, unmoderated, same screener,
> same tasks and wording.
>
> **Result, as reported.** Success 31 of 42 (74%) against 22 of 40 (55%)
> in January: 19 points higher, likely between 1 and 36. Median time 11
> minutes against 16. SUS 71 against 62 (both reported against the
> 68 average, not as percentages). What else changed: a pricing change
> in February. The agreed bar was 10 points on success; met, with a wide
> range, so the readout says "better, by how much is uncertain".

## Pitfalls

- A number with nothing to compare it to.
- Changing the tasks or their wording between rounds.
- Calling a difference an improvement when it sits inside the margin of
  error.
- Measuring, then never finding out why the number moved.

## Template

Adapt `templates-usability-test-script.md`: fixed tasks with written
success criteria, the ease rating after each task, the questionnaire at
the end, and no probing during tasks.

## Basis

S73 (what benchmarking is; a summative snapshot of one version, run at
the end of a design cycle; example measures, including support data;
comparison with an earlier version, a competitor, an industry figure or a
stakeholder goal; analytics, surveys and quantitative usability testing
as the usual ways to collect; how often is the team's call). S11
(benchmarking as tightly scripted and summative, at the launch and assess
phase). S38 (the Single Ease Question, the System Usability Scale, twenty
or more people for questionnaire numbers). S12 (report the interval;
test before claiming a difference). S97 (the HEART
categories happiness, engagement, adoption, retention and task success;
goals, signals and metrics; not every category fits every project;
normalize counts into rates or per-user figures; define terms before
tracking). S87 (log data misses people who wanted to start a task and
never found it; a behavioral benchmark that starts from the home page
captures intent and shows navigation failures). S96 (the average SUS
score across about 500 studies is 68; a score isn't a percentage; report
it as a percentile against that average). S84 and S85 (report raw
differences in their own units with intervals; make them concrete at
the product's volume; set the "big enough" bar before the data arrives).
S100 (pp. 19–31: a confidence interval's width depends on confidence
level, variability and sample size, and halving the margin of error
takes about four times the sample; t-interval for rating-scale means;
geometric mean for task times below 25; adjusted-Wald for rates. p. 93:
two-sample t for different users, paired for the same users. pp.
200–201: the Bangor et al. set of 2,324 SUS questionnaires with a mean
of 70.14 and standard deviation 21.71, and the Lewis and Sauro set of 324
with a mean of 62.10 and standard deviation 22.24; p. 236: SUS against
likelihood to recommend across 2,201 users, correlation 0.623, LTR ≈
SUS/10, promoters averaging 81 and detractors 52.5; pp. 203–205: raw SUS
scores converted to percentile ranks, the curved grading scale (C at
68, A from 78.9, A+ from 84.1, F below 51.7), and Table 8.6 means by
interface type (global 68.0, business-to-business 67.6,
business-to-consumer 74.0, web 67.0, cell phone 64.7, internal software
76.7, voice response 79.9, web plus voice 59.2); p. 235: NPS defined
as promoters minus detractors, loss of sensitivity from collapsing the
scale, no well-defined interval, the −1/0/+1 recoding as an untested
way to get one).
Keeping every round the same and naming what else changed: practitioner
judgment.

---

Part of Magpie version 2026-10-31, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
