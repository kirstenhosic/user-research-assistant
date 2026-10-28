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

- Moderated: five per distinct user group finds most of the serious problems.
  Run another round after fixes rather than a bigger first round.
- Unmoderated: twenty or more per group if you want task-success rates you
  can compare.
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

## What makes it good

- Tasks have a written success criterion before the session.
- Tasks are realistic and in a realistic order.
- The moderator doesn't help. "What would you do if I weren't here?"
- Observers take notes against the tasks, not freeform.
- Severity is rated per issue: how many hit it, how badly it blocked them,
  how often it would happen in real use.

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
  It needs twenty or more people per round to mean much; with five, use
  it as a conversation starter, not a score.

A participant's rating and what they did can disagree. Someone who failed
the task may still rate it easy. Report both; what they did comes first.

## Analysis

Issue list: each issue with the task, how many participants hit it, severity,
and a short description of what happened. Stage 7 covers this. For
unmoderated studies: success rate, time on task, and clips of the failures.

Ease ratings from a moderated study go next to each participant's result
and reason ("P2: failed, rated 5 of 7, 'I assumed it saved'"). Don't
average five ratings or report them as a percentage; the reasons are the
finding. With twenty or more unmoderated participants, ratings can be
summarized, following stage 7's survey data rules.

## Pitfalls

- Leading tasks that name the feature or the button.
- Fixing a prototype between sessions without noting it.
- Counting "they found it eventually" as success.
- Reporting five participants as a percentage.
- Asking the rating, then not asking why.
- Probing during the task, so the question changes what they do next.

## Template

`templates/usability-test-script.md`

## Basis

Follow-up questions: S38 (the Single Ease Question after each task, on
seven points, while the task is fresh; SUS after the session with wording
and order unchanged, ten items, a 0 to 100 score that isn't a percentage;
twenty to thirty users or more for questionnaire numbers; pair a rating
with "why"); S12 (numbers from small qualitative studies carry large
error). Probing after rather than during the task, and the debrief:
practitioner judgment. Remote, moderated: S78 (advantages and the
extra preparation; choosing a call tool; how tasks reach the participant,
with the moderator reading them as the weakest choice; a tech check the
day before on something else; reminders; observers; recruiting extra and
spare time; a pilot that tests the test; recording consent at the start).
Background: S7. The rest of this guide:
practitioner judgment, consistent with widely published usability testing
guidance.
