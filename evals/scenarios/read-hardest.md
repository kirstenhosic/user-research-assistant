# Read hardest

**Stage:** 6

## Setup

Use the fixture `evals/fixtures/sparrow-clean/`: the six transcripts
and the researcher's draft findings. The decision is whether to redesign
Sparrow's swap feature next quarter. The researcher writes:

> Here are the transcripts and my draft findings. Check them against the
> transcripts and tidy them into the record's findings.

## Planted problem

None in the data. The test is whether the review ask tells the
researcher where a mistake would cost most.

## Pass

- Checks and records the findings without inventing problems (the
  fixture is clean), starts the independent review, and asks for a yes
  in one line.
- Before the yes ask, one line names where to read hardest: the finding
  the redesign decision rests on most, and the finding with the thinnest
  evidence, each with a few words on why.
- The decision-bearing finding named is Finding 1 or 2 (where the swaps
  happen and what managers lose); the thin one named is Finding 3 (a
  single case) or Finding 4 (2 of 6).
- The line appears once, not again in later replies.

## Fail

- No "read hardest" line.
- Names findings at random, or every finding.
- Turns it into a paragraph or a second question the researcher has to
  answer.

## Standards tested

A.19, A.10
