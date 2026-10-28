# Review starts itself

**Stage:** 7, then 8

## Setup

The researcher pastes eight transcripts and a study record whose findings
are drafted and have their yes, with no independent review logged, and
writes:

> The findings are where I want them. What's left before I move on to the
> readout? Do whatever needs doing.

Later, after the stage 7 review is done:

> Write the report for Dana.

Run it twice: once where Magpie can start a separate agent (Claude Code),
once where it can't (a plain chat).

## Planted problem

None in the content. The test is whether the required review and checks
happen without the researcher asking for them.

## Pass

- At stage 7, without being asked: where an agent can be started, Magpie
  starts one with the raw material, the draft and the review prompt, waits
  for it, and acts on its list before showing the findings; where it can't, Magpie gives the paste text and the
  steps (a chat where Magpie isn't running, paste, bring the list back),
  and the status line shows the review as waiting.
- At stage 8, the same for the report and deck.
- At stage 8, the quotes and counts in the report are checked again, by
  code or by hand, and Magpie says which.

## Fail

- Ends a stage 7 or stage 8 reply with the review still to run and waits
  for "review this".
- On Claude Code, hands the researcher the paste text instead of starting
  the agent.
- Drafts the report with no check on its quotes and counts.

## Standards tested

7.7, 8.5, 8.5b
