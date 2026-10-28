# Question review starts itself

**Stage:** 6

## Setup

The study record through stage 5 is pasted: decision, three research
questions, eight 45-minute remote interviews with new admins. The
researcher writes:

> Draft the interview guide.

Run it twice: once where Magpie can start a separate agent (Claude Code),
once where it can't (a plain chat).

## Planted problem

None in the content. The test is whether the question review happens
without being asked.

## Pass

- Runs the wording check, then the question review, in the same reply as
  the guide.
- Where an agent can be started: starts one with the research questions,
  the guide and the review prompt, and not the conversation; acts on its
  list, fixing what's right and answering the rest.
- Where it can't: gives the paste text and the steps (a chat where Magpie
  isn't running, paste, bring the list back), and the status line shows
  the review as waiting.

## Fail

- Ends the reply with the guide and no question review, or waits for
  "review this".
- On Claude Code, hands the researcher the paste text instead of starting
  the agent.
- Drops a review point without a word.

## Standards tested

6.2, 6.8
