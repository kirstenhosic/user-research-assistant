# Word file

**Stage:** 6

## Setup

The study record through stage 5 is pasted. The researcher writes:

> Draft the interview guide. My PM and our designer will edit it with me
> in Word.

Run it twice: once where Magpie can run code (Claude Code), once where it
can't (a plain chat).

## Planted problem

None in the content. The test is whether the guide comes in a form the
team can edit together.

## Pass

- Where code runs: writes the guide as Markdown, runs
  `md_to_docx.py`, and gives both files. The Word file has the headings,
  the spoken lines and the lists, and opens without errors.
- Where it can't: says so in one line and gives the platform's own export
  or the copy-into-Word step.
- Later, when the researcher sends back an edited Word file, works from
  it and says what changed since its own version.

## Fail

- Gives only Markdown with no word about Word.
- Rebuilds from its own draft and loses the team's edits.

## Standards tested

A.21
