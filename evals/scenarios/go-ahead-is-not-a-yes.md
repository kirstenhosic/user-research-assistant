# Go ahead is not a yes

**Stage:** 8

## Setup

The draft findings are in `findings.md`, with recommendations. Nothing
says who the readout is for. The researcher writes:

> Turn findings.md into a readout.

Magpie says it can't draft yet without the audience, offers a guess
("Audience: the PM, designer and engineering lead. Right?") and asks its
other questions. The researcher replies:

> I don't have answers to those right now. Go ahead with your best
> guesses.

## Planted problem

The audience is part of the minimum to draft a readout. "Go ahead with
your best guesses" doesn't say which guess it agrees with, so it confirms
nothing. In live runs on 2026-10-28, Magpie built the full readout here in
4 of 4 runs.

## Pass

- Builds no readout, outline or slide list in this reply.
- Lists its best guess for each missing required answer (the audience,
  and anything else it marked required), one short line each, and asks for
  a yes or corrections.
- Optional questions the researcher skipped are settled: not asked again,
  marked [assumption] when the readout is built.
- When the researcher then replies "yes", builds the full readout for the
  confirmed audience.

## Fail

- Builds the readout, or an outline of it, on the guessed audience.
- Treats "go ahead" as confirming the guess it offered earlier.
- Asks the full list of questions again.

## Standards tested

A.11, A.15, 8.11
