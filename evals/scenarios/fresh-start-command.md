# Fresh start command

**Stage:** 7, in a chat tool with no file access

## Setup

Mid-analysis in a long conversation, after the findings have their yes,
the researcher writes:

> fresh start

## Planted problem

"fresh start" is easy to confuse with "start over", which begins a new
record.

## Pass

- Prints the full, up-to-date study record, with its "Where we are"
  block showing stage 7 done and the next step.
- Gives one line to paste into the new conversation with the record
  (for example, "Magpie, here's my study record. Pick up where we were.").
- Says the steps in one line: copy the record, start a new conversation,
  start Magpie, paste both.
- Keeps the session going here and doesn't start a new record.
- In Claude Code (a variant of this scenario), saves the record file and
  names it instead of printing it, and the paste line says to give
  Magpie that file.

## Fail

- Starts over or wipes the record.
- Ends the session.
- Gives a record without the "Where we are" block or with stale status.
- Long instructions about how the tool works.

## Standards tested

A.37, A.16
