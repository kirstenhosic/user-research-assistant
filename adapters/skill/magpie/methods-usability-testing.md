# Method: usability testing

Watch people try to do real tasks with a design, and learn where and why
they struggle. Moderated (you're there) or unmoderated (a tool records them).

## Use it when

- You have something to test: a prototype, a live product, a competitor's.
- The question is *does this work for the people it's for*, and *where does
  it break*.
- You need to know why people fail, not just that they do (moderated), or
  task success at a larger scale (unmoderated).

## Don't use it when

- You don't yet know what problem the design is solving. Interview first.
- The question is about desirability or value, not usability. Test the
  concept instead.

## Sample

- Moderated: five people from one user group find most of the problems.
  With two distinct groups, three or four from each; with three or more,
  three from each. Run another small round after fixes rather than one big
  first round.
- Why five: across many studies the average chance that one person hits
  any given problem in one round is about 0.31, so five people reveal
  about 85% of the problems that round can show. It was never 85% of
  the product's problems. Nielsen's own account is fishing in ponds: a
  round empties the easy problems from one pond, and the next round,
  with the fixes and often new tasks or a new group, fishes a new one.
  Five only works as part of that loop. A mature website with the easy
  problems already removed, or loosely structured tasks, can have a
  per-person chance near 0.03, where five people show about 14% and
  85% takes about 65. If late participants keep finding new problems,
  the round isn't done.
- How often a problem appears says nothing about how severe it is;
  plan as if the two are unrelated, and expect serious problems from
  late participants too.
- Rates from a small test (completion, time) follow stage 7's "Numbers
  from small samples": an adjusted-Wald interval, the geometric mean for
  times.
- Unmoderated, for rates (task success, time on task): more than thirty
  people, and forty or more if you want ranges narrow enough to compare.
  Five people can show problems but can't give you a rate.
- Recruit people who would actually do these tasks.

## Session shape (moderated, 30 to 60 minutes)

1. Opening: we're testing the design, not you. Think aloud. There are no
   wrong answers. What's recorded.
2. Brief context questions about how they do this today.
3. Tasks, one at a time, as scenarios: "You want to…", never "Click the…".
4. After each task: a rating of how easy or hard it was, then "why that
   rating?", then what they expected to happen. See "Follow-up questions"
   below.
5. Debrief: go back to the moments that mattered, then overall
   impressions, anything missing, thanks.

## Remote, moderated

The same session over a video call with screen sharing. It's often
cheaper and quicker than meeting in person, easier for participants, and
reaches people who can't travel. It takes more preparation.

- Pick a call tool that participants, observers and the moderator can all
  use. Check it works on the participant's device and browser while
  screening.
- Decide how tasks reach the participant: a document with one task per
  page that they don't read ahead in, or one task at a time in the chat,
  read aloud by the participant. Reading tasks aloud yourself is the
  weakest choice.
- Hold a short tech check the day before (about 15 minutes), using
  something other than the design you're testing: install the tool,
  check sound and screen sharing, and do the consent form.
- Remind participants the day before: charged device, headset, a strong
  connection, somewhere quiet and private.
- Keep observers muted, keep team chat where the participant can't see
  it, and give observers the task list and what to watch for.
- Recruit a few extra people, leave spare time in each session for tech
  trouble, and have a backup plan.
- Run a pilot first. It tests the test, not the design, so a colleague
  can do it.
- At the start, ask permission to record and confirm the end time.

## Testing with assistive technology

Some sessions, in most studies, should be with people who use a screen
reader, magnification, speech input, switch access or the keyboard
alone. `lenses-accessibility.md` covers recruiting and running them; the
points that change the test itself:

- **Clear the obvious first.** Have someone who knows accessibility check
  the design against a standard (WCAG) before the sessions, and fix what
  that finds. Then the sessions find what only users can show.
- **Match the participant to the audience.** An expert screen-reader user
  suits a tool for specialists; a public service needs people who are
  new to their assistive technology too. Recruit a range; one person's
  experience doesn't stand for everyone with that disability.
- **Their own setup.** Their device, their software, their settings.
  Check in the tech check that the prototype works with it at all; if it
  doesn't, that's a finding, not a session.
- **Think-aloud, with more help from the moderator.** Ask what they hear
  and what they're trying to do, and point tasks at the parts of the
  design the team is unsure about.
- **Analyze the cause, not only the failure.** An error can come from the
  content, the browser, the assistive technology, the person's
  familiarity with it, or plain bad design. Record which, with the
  technology and settings next to each issue, and report what blocked
  people ahead of time on task.
- **Don't generalize from a few.** Say in the report who took part, with
  what technology, and that the sessions were not a conformance check.
  The team needs both.

## What makes it good

- Tasks have a written success criterion before the session.
- Tasks are realistic and in a realistic order.
- The moderator doesn't help. "What would you do if I weren't here?"
- Observers take notes against the tasks, not freeform.
- Severity is rated per issue on three things: how many hit it (frequency),
  how hard it was to get past (impact), and whether it would keep bothering
  people or only the first time (persistence).

## Follow-up questions

Watching shows where people struggle; follow-up questions show why. Ask
them after the task, not during it, so you don't change what happens.

**After each task**

- One ease rating, in the style of the Single Ease Question (SEQ): how
  easy or difficult the task was, on seven points from very difficult to
  very easy. Ask it while the task is fresh, and word it the same way
  every time.
- "Why that rating?" Then probe the reason: "You paused on the payment
  screen. What were you thinking there?"
- "What did you expect to happen?" and, if they didn't finish, "What would
  you have tried next?"

**Debrief at the end (five to ten minutes)**

- Go back to one or two moments you saw: "When you went back to the menu
  the second time, what were you looking for?" Name what they did, not
  what you think it meant.
- "What was the hardest part?" and "Was anything different from what you
  expected?"
- If you're tracking perceived usability across releases, a standard
  questionnaire such as the System Usability Scale (SUS: ten fixed items,
  a score from 0 to 100) goes here, with the wording and order unchanged.
  It needs twenty to thirty or more people per round to mean much; with
  five, use it as a conversation starter, not a score.
- SUS details: ten items on a five-point agree scale, odd items worded
  positively and even items negatively; people answer all ten right
  after using the product and before any debrief, picking the middle
  point if they can't answer one. Score each odd item as its position
  minus 1, each even item as 5 minus its position, add the ten and
  multiply by 2.5. Swapping "system" for "website" or "product", or
  "awkward" for the original "cumbersome", doesn't change the result.
  It measures perceived usability as one number; it says nothing about
  which part of the product caused it.

A participant's rating and what they did can disagree. Someone who failed
the task may still rate it easy. Report both; what they did comes first.

## Analysis

Issue list: each issue with the task, how many participants hit it, severity,
and a short description of what happened. Stage 7 covers this. For
unmoderated studies: success rate, time on task, and clips of the failures.

Ease ratings from a moderated study go next to each participant's result
and reason ("P2: failed, rated 5 of 7, 'I assumed it saved'"). Don't
average five ratings or report them as a percentage; the reasons are the
finding. With more than thirty unmoderated participants, ratings can be
summarized, following stage 7's survey data rules.

## Worked example

> **Decision.** Whether Tally (expense tracking) ships the redesigned
> receipt capture flow next month or holds it for another round.
>
> **Research question.** Can people photograph a receipt and file it to
> the right expense claim without help, and where do they get stuck?
>
> **Sample.** Five people who filed an expense claim in the last month,
> moderated, remote, 45 minutes.
>
> **Tasks.** "You've just paid for a client lunch and have the receipt.
> Add it to this month's claim." Success: receipt attached to the March
> claim with the amount matching. Then the ease rating and "why that
> number?"
>
> **Issue, as reported.** 4 of 5 attached the receipt to a new claim
> instead of the existing one (P1, P2, P4, P5), because the "Add to
> claim" sheet opens on "New claim". Severity: high (frequent, blocked
> the task, would happen every time). Ease ratings 3, 4, 6, 2, 5 of 7,
> each next to its reason; no average reported.

## Pitfalls

- Leading tasks that name the feature or the button.
- Fixing a prototype between sessions without noting it.
- Counting "they found it eventually" as success.
- Reporting five participants as a percentage.
- Asking the rating, then not asking why.
- Probing during the task, so the question changes what they do next.

## Template

`templates-usability-test-script.md`

## Basis

What a test is: S47 (a facilitator, realistic tasks, a realistic
participant, thinking aloud; moderated and unmoderated, in person and
remote; the facilitator must avoid influencing behavior). Sample: S45
(five users find most problems; small rounds over one big one; three or
four per group for two groups, three per group for three or more); S46
(more than thirty for quantitative studies, forty or more for useful
ranges; five can't give rates). Tasks: S3. Severity: S48 (frequency,
impact, persistence). Follow-up questions: S38 (a post-task ease rating on
seven points while the task is fresh; SUS after the session, wording and
order unchanged, ten items, a 0 to 100 score that isn't a percentage; 20
to 30 or more users for questionnaire numbers; pair a rating with "why");
S12 (numbers from small qualitative studies carry large error). S100
(pp. 162–166: average problem-occurrence rate of 0.31 and the
1 − (1 − p)^n arithmetic behind "five users find 85%"; the guideline
misread as 85% of a product's problems; Nielsen's fishing analogy, five
being contingent on iteration with changed tasks or groups; the Spool
and Schroeder "eight is not enough" study reconciled as p near 0.029,
where five users find about 14% and 85% takes 65; serious problems found
at the same rate as others; Sauro's review of 24 tests giving p of about
0.37 for business applications, 0.23 for consumer software and 0.04 for
websites; p. 162: no reliable link between problem frequency and
severity. pp. 198–199: the SUS items, response rules, scoring and the
wording substitutions that make no difference; a single-number measure
that doesn't locate the cause).
Remote, moderated: S78 (advantages and the
extra preparation; choosing a call tool; how tasks reach the participant,
with the moderator reading them as the weakest choice; a tech check the
day before on something else; reminders; observers; recruiting extra and
spare time; a pilot that tests the test; recording consent at the start).
Background: S7. Testing with assistive technology: S98 (an expert
review for obvious barriers first; match assistive technology experience
to the audience; a range of participants, since one person doesn't stand
for all; think-aloud with high facilitator interaction and tasks aimed at
areas of concern; errors can come from content, browser, assistive
technology, unfamiliarity or poor design; focus on barriers over time on
task; combine with a conformance evaluation; don't generalize from a few;
report scope, methods and participants). Session timings, probing after
rather than during the task, the debrief, and the pitfalls: practitioner
judgment.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
