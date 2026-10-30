# Method: expert review

Reviewers, not users, inspect a design for likely problems. Two common
forms: a heuristic evaluation checks the design against a set of usability
principles; a cognitive walkthrough steps through a task as a new user
would. Neither involves users, so neither is user research.

## Use it when

- You want to clear obvious problems cheaply before testing with users,
  so the sessions find the problems only users can show you.
- The team needs a quick read on a design and there's no time to recruit.
- You're deciding what to test: the review shows which tasks look risky.
- Cognitive walkthrough: the system is new or unfamiliar to its users
  (new patterns, a kiosk, a first-time flow), and learnability is the
  question.

## Don't use it when

- The decision needs evidence about users. A review predicts problems;
  only users show them.
- The design follows familiar patterns throughout. A walkthrough of a
  standard checkout is overkill.
- You'd be the only reviewer. One reviewer misses problems, and someone
  who made the design is too close to it to see them.

## How Magpie labels the results

Every issue from an expert review is a reviewer's prediction. Label it
[assumption], not a finding, until a usability test or other evidence from
users confirms it. A review can sit in the study record's evidence log
and shape what to test; it can't stand behind a recommendation on its own.

In a readout or report, review issues get their own section or slide,
titled as predictions ("What our review predicts, to test with users"),
never "Top issues", "Findings" or "Key insights". Say what the review is
good for: a cheap first pass that clears obvious problems and picks what
to test first. The number of reviewers who flagged each issue is shown
only if the researcher gave it.

## Heuristic evaluation

1. **Prepare.** Pick the heuristics (Nielsen's ten usability heuristics
   are the common set, S95: visibility of system status, match with the
   real world, user control and freedom, consistency and standards, error
   prevention, recognition over recall, flexibility and efficiency,
   aesthetic and minimalist design, help with errors, help and
   documentation; add domain-specific ones if needed). Narrow the
   scope to a task, a section, a user group or a device. Agree how issues
   will be recorded.
2. **Review alone.** Three to five reviewers, each working independently
   for one to two hours. Go through the scope once to learn it, then again
   noting each place a heuristic is broken and why.
3. **Combine.** Only after everyone has finished, group the issues, discuss
   where reviewers disagree, and decide which issues matter most and which
   need data from users.

## Cognitive walkthrough

1. **Prepare.** Pick a few tasks, ideally the ones users do most or the
   ones the decision is about. Agree who the user is and what they know.
2. **Walk through.** A cross-functional group (design, product,
   engineering, someone who knows the domain). A facilitator does the task
   one step at a time. At each step the group asks:
   1. Will users try to achieve the right result?
   2. Will users notice that the correct action is available?
   3. Will users connect the correct action with what they're trying to do?
   4. After the action, will users see that they're making progress?
3. **Record.** Any "no" marks that step as a likely failure, with the
   reason. A note-taker records each answer.
4. **Summarize.** The failure points per task, and what to test with users.

## What makes it good

- Independent reviews before discussion, so one reviewer doesn't set the
  list.
- A narrow scope. The narrower it is, the more detailed the review.
- Each issue tied to the principle or the walkthrough question it fails,
  and to where it happens.
- Treating a broken heuristic as a question, not a verdict. Context
  matters, and principles are guidelines, not laws.

## Analysis

An issue list: where, which heuristic or question it fails, how many
reviewers found it, and a note on whether users need to confirm it. Then
the short list of tasks to put in front of users. Keep it separate from
findings from users, in the record and in any readout.

## Worked example

> **Decision.** Which tasks to put in next month's usability test of
> Tally's (expense tracking) new approvals flow, and what to fix before
> it.
>
> **Review.** Heuristic evaluation, four reviewers (two designers, a
> content designer, a support lead), independently, 90 minutes each, on
> the approvals flow only, against Nielsen's ten heuristics.
>
> **Combined list.** 23 issues; 6 found by three or more reviewers.
> Top: no confirmation after "Approve" (visibility of system status,
> 4 of 4 reviewers); "Reject" and "Return for changes" look the same
> (error prevention, 3 of 4).
>
> **As recorded.** Every issue is [assumption] in the evidence log:
> "Reviewers predict people won't know an approval went through." The
> two top issues become test tasks; three cheap fixes (labels) go in
> before the test. Nothing from the review appears as a finding.

## Pitfalls

- Presenting review issues as "users struggle with…".
- One reviewer, or reviewers who compare notes before they finish.
- Using a review instead of testing with users, rather than before it.
- Ranking issues by how many principles they break rather than by what
  they'd cost users.

## Template

An issue list with columns: location, heuristic or walkthrough question,
what happens, reviewers who found it, confirm with users (yes or no).

## Basis

S34 (heuristic evaluation: three to five independent reviewers, one to two
hours each, narrow scope, consolidate afterwards, heuristics are
guidelines, it can't replace user research); S35 (cognitive walkthrough:
the four questions, a cross-functional group, a facilitator and a recorder,
best for new or unfamiliar systems, to be combined with usability
testing); S95 (the ten heuristics by name). The [assumption] label and keeping results apart from user
findings follow `operating.md`. Avoiding self-review, the pitfalls and
the issue-list columns: practitioner judgment.
