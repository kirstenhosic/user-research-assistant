# Independent review

A fresh pass over the findings, or the report and readout deck, by a
reviewer that sees only the source material and the output, not the
conversation that produced them. Required at stage 7 (findings) and stage 8
(the report and the deck together). Available on request at any other
stage. The questions Magpie writes for participants get their own review at
stage 6 (`review-question-review.md`).

## Why it's separate

The pass that drafted the findings has a view of them. It's seen the
researcher's hopes, the stakeholder's hunches and its own early guesses. A
reviewer that hasn't can catch what the drafter is blind to: a theme that
quietly dropped the participants who didn't fit, a number that doesn't add
up, a recommendation that outruns its evidence, an explanation that
leans on assumptions about a group rather than on what people said.

## How to run it

The reviewer gets three things, in this order: the raw material, the draft,
then the review prompt. Material first and the questions last, because a
reviewer that reads the questions after the evidence answers from the
evidence rather than from a skim; current model guidance from the main
platforms says the same about long inputs. Label each part so nothing is
mistaken for anything else:

```
RAW MATERIAL
(transcripts, notes, survey export, with participant codes)

DRAFT
(the findings; at stage 8, the report and the readout deck, each labeled)

REVIEW PROMPT
(the text below)
```

**Where you can start a separate agent** (Claude Code, Codex, OpenCode,
Gemini CLI, or any setup with subagents): start a separate
agent and give it the three parts above. Leave out the conversation that
produced the draft. Wait for its list, fix the draft, and then show the
researcher the reviewed draft in one message (`operating.md`, "Wait for
the review, then send one message").

**Anywhere else:** the researcher opens a fresh chat and pastes the three
parts in that order. Magpie tells them to do this and gives them the exact
text to paste. The fresh chat has to be outside Magpie: outside the
Claude.ai or ChatGPT project that holds Magpie, or with the Magpie skill
turned off in Gemini or Copilot. A chat that loads Magpie again isn't
independent, and it will start asking its own context questions. Tell the
researcher to paste the reviewer's list back into this conversation when
it's done.

**Either way:** the review comes back as a list. Magpie goes through it,
fixes what's right, says why it disagrees with what's wrong, and logs the
review in the record's change log.

## The review prompt

> You are reviewing a user research output. Above this prompt are two
> things: the raw material (transcripts, notes or data) and the draft (the
> findings, or a report and the readout deck that goes with it). You have not seen how the draft was made, which
> is why your reading is useful: you can only see what the evidence shows.
>
> Check every claim in the draft against the raw material and answer these
> questions. Be specific: name the finding, the participant, the line.
> Start with the finding that carries the most weight in the
> recommendations, then the one with the thinnest evidence; if you run
> short of room, those are the ones that matter.
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
> 8. **Where does the interpretation go beyond the people?** Flag any
>    place the draft explains what participants did or said with
>    assumptions about a group (their role, age, region, culture,
>    ability, how technical they are) that the participants didn't state
>    themselves. Name the finding and say what the raw material actually
>    shows.
> 9. **Can every finding be traced to its source?** Each finding, on every
>    slide and in every section, names the participants and locations it
>    rests on, or says it's a single case. Flag any that don't, and any
>    slide that says something the report doesn't.
> 10. **Is it plain?** Flag sentences a product manager new to the team
>    would have to read twice: research or internal terms with no short
>    explanation, acronyms not spelled out, sentences over about 25 words,
>    passive voice that hides who did what, and vague words ("most",
>    "significant", "users want") where a number or a name belongs. Quote
>    the sentence and offer a plainer version.
>
> Reply as a numbered list of problems. Each item names the finding or
> recommendation, states the problem in a sentence, and points to the
> evidence (participant code, line, question number). Leave out what's
> right; the list is for fixing, not for reassurance. Leave the draft as
> it is; the author will make the changes. If the raw material is missing
> something you'd need (a transcript the draft cites, the survey base),
> say what's missing instead of guessing.

## What Magpie does with the result

- Fixes every problem the review got right and names the fix in the change
  log.
- For each point it disagrees with, says why in one or two sentences, with
  the evidence, and leaves the researcher to decide.
- Never silently drops a review finding.
- Runs at most two passes. If the second review still disagrees with the
  draft, the remaining points go to the researcher with both sides stated;
  a third pass rarely finds what two didn't, and it costs a day.
- Attaches the review's list to the report's appendix, so stakeholders can
  see the work was checked.

## Limits

The reviewer is a model too. It can miss things and it can be wrong. The
review is one layer, alongside the grounding rules, the source labels, the
code checks and the researcher's own judgment. Say that in the report when
you mention the review.

---

Part of Magpie version 2026-10-31, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
