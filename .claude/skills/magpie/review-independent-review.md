# Independent review

A fresh pass over the findings or the report, by a reviewer that sees only
the source material and the output, not the conversation that produced them.
Required at stage 6 (findings) and stage 7 (report). Available on request at
any other stage.

## Why it's separate

The pass that drafted the findings has a view of them. It's seen the
researcher's hopes, the stakeholder's hunches and its own early guesses. A
reviewer that hasn't can catch what the drafter is blind to: a theme that
quietly dropped the participants who didn't fit, a number that doesn't add
up, a recommendation that outruns its evidence.

## How to run it

**On Claude** (Claude Code or a setup with subagents): start a separate
agent with the review prompt below. Give it only the raw material and the
draft. Don't give it the conversation.

**Anywhere else:** the researcher opens a fresh chat, pastes the review
prompt, then the raw material, then the draft. Magpie tells them to do this
and what to paste.

**Either way:** the review comes back as a list. Magpie goes through it,
fixes what's right, says why it disagrees with what's wrong, and logs the
review in the record's change log.

## The review prompt

> You are reviewing a user research output. You have the raw material (the
> transcripts, notes or data) and the draft (the findings or the report).
> You have not seen how the draft was made, and that is the point.
>
> Check every claim in the draft against the raw material and answer these
> questions. Be specific: name the finding, the participant, the line.
>
> 1. **Does the evidence say what the draft says it says?** For each
>    finding, find the passages it rests on. If they're weaker, fewer or
>    different from what's claimed, say so.
> 2. **Who is missing?** For each finding, list the participants who said or
>    did something different. Does the draft mention them?
> 3. **Are the numbers right?** Recount every "N of M". Check every
>    percentage against its base.
> 4. **Are the quotes real?** Find each quote in the raw material. Flag any
>    that are altered, trimmed in a way that changes meaning, or missing.
> 5. **Is the strength label fair?** For each finding, say whether strong,
>    moderate or weak is right, and why.
> 6. **Do the recommendations follow?** For each recommendation, name the
>    finding it rests on. Flag any that go beyond what the findings support.
> 7. **What's stated as fact that is actually practice or assumption?**
>
> Report only problems and the evidence for them. Don't restate what's
> right. Don't rewrite the draft. Plain language, short.

## What Magpie does with the result

- Fixes every problem the review got right and names the fix in the change
  log.
- For each point it disagrees with, says why in one or two sentences, with
  the evidence, and leaves the researcher to decide.
- Never silently drops a review finding.
- Attaches the review's list to the report's appendix, so stakeholders can
  see the work was checked.

## Limits

The reviewer is a model too. It can miss things and it can be wrong. The
review is one layer, alongside the grounding rules, the source labels, the
code checks and the researcher's own judgment. Say that in the report when
you mention the review.
