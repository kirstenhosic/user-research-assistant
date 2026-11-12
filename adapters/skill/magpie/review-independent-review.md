# Independent review

A fresh pass over the findings, or the report and readout deck, by a
reviewer that sees only the source material and the output, not the
conversation that produced them. Required at stage 7 (findings) and stage 8
(the report and the deck together). A shorter version, the source check,
is required at stages 1 and 2 (see "The source check at stages 1 and 2"
below). Available on request at any other stage. The questions Magpie writes for participants get their own review at
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
Gemini CLI, GitHub Copilot's agent mode in VS Code, or any setup with
subagents): start a separate
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
> 11. **Could anyone be identified?** Flag any name, email, phone number,
>    handle or company name left in, and any description or quote detail
>    that, alone or together, points to one person (the only person in a
>    role, a city or a company size in the sample). Say what to make
>    more general.
>
> Reply as a numbered list of problems. Each item names the finding or
> recommendation, states the problem in a sentence, and points to the
> evidence (participant code, line, question number). End each item with
> a source line on one line, naming the participants and line numbers it
> rests on ("Source: P3 12, P5 06 and 08"), or "Source: none" when the
> point is about the draft itself, such as its wording or its math. Cite
> only lines you found in the raw material. Leave out what's
> right; the list is for fixing, not for reassurance. Leave the draft as
> it is; the author will make the changes. If the raw material is missing
> something you'd need (a transcript the draft cites, the survey base),
> say what's missing instead of guessing.

## What Magpie does with the result

- **First, checks what each point cites.** A reviewer can invent a
  problem as easily as a drafter can invent support, so before acting on
  any point, look up the participants and lines it cites in the raw
  material and label it:
  - **Found:** every participant and line it cites is there. Read those
    lines before acting: "found" means the lines exist, not that the
    point is right.
  - **Lead:** it cites no participant line ("Source: none", or no source
    line). It may still be right, such as a wording or math point, or
    something the draft left out. Check it by reading before acting.
  - **Not found:** it cites a participant or a line that isn't in the
    material. Don't act on it as stated. Look for whether the problem it
    describes shows up anywhere else, and tell the researcher which
    citation couldn't be found.

  Where Magpie can run code, save the list to a file and run
  `python3 scripts/review_check.py review.md transcripts/`, which
  labels every point the same way. Where it can't, look each citation up
  by hand and say so in the change log. The idea of labeling a model's
  critique by whether its references exist comes from claim-stress-tester
  (S102).
- Fixes every problem the review got right and names the fix in the change
  log, with the point's label.
- For each point it disagrees with, says why in one or two sentences, with
  the evidence, and leaves the researcher to decide.
- Never silently drops a review finding.
- Runs at most two passes. If the second review still disagrees with the
  draft, the remaining points go to the researcher with both sides stated;
  a third pass rarely finds what two didn't, and it costs a day.
- Attaches the review's list to the report's appendix, with each point's
  label and what was done about it, so stakeholders can see the work was
  checked.

## The source check at stages 1 and 2

At stages 1 and 2, Magpie works from documents rather than transcripts,
and the output (an opportunity list and briefs, a gap summary, an
evidence brief) can steer what a team studies next. A claim that sounds
right but isn't in any source does the most harm there, because nobody
goes back to check a pick once it's made. So before any of these is
shown to the researcher, it gets a source check.

It runs the same way as the review above: a separate agent where you can
start one, a fresh chat outside Magpie anywhere else, with the same
three parts in the same order. The raw material is every document the
claims rest on, each labeled with its name, in full, as it was shared.
The draft is the output with its source receipts (`operating.md`,
"Point to the exact words"). Skip it only when the output makes no claim
from a document, such as "no prior evidence found".

The source check prompt:

> You are checking a research planning draft against the documents it
> cites. Above this prompt are the documents, each labeled with its
> name, and the draft. You have not seen how the draft was made.
>
> Go through every claim in the draft that rests on a document. Start
> with the claims the draft's choices lean on most. For each one:
>
> 1. **Is the quote there?** Find the quoted words in the named
>    document. Say found, found in a different document (name it), or
>    not found.
> 2. **Does the source say what the claim says?** Flag a claim that is
>    stronger, broader or more certain than its quote, that leaves out
>    a condition the passage gives, or that reads the passage out of
>    context.
> 3. **Is the place right?** Flag a page, slide or section that doesn't
>    match where the words are.
> 4. **Is anything stated as fact with no source?** Flag any claim with
>    no receipt that isn't marked as an assumption, and any join of two
>    sources that isn't marked as an inference.
> 5. **Is the date and kind of evidence fair?** Flag a claim that uses
>    an old or secondhand source as current or direct.
> 6. **What did the draft leave out?** Name anything in the documents
>    that goes against a claim or a pick, or a strong signal the draft
>    didn't use.
>
> Reply as a numbered list of problems. Each item names the claim,
> states the problem in a sentence, and ends with a source line naming
> the document and the exact words you found ("Source: Q3 support
> themes, 'export errors were the second most common ticket type'"),
> or "Source: none" when the point is about the draft itself. Quote only
> words you found in the documents. Leave out what's right, and leave
> the draft as it is. If a document the draft cites isn't above, say so
> instead of guessing.

Magpie handles the list as in "What Magpie does with the result",
looking up each point's document and words: found, lead or not found.
`scripts/review_check.py` works on transcripts, so do this lookup by
hand and say so in the change log. A claim the check marks "not found" is fixed
or turned into an [assumption] before the output is shown. Then the
review ask carries the spot-check line (`operating.md`, "Check two or
three receipts yourself").


The reviewer is a model too. It can miss things and it can be wrong, and
the labels only show whether its citations exist, not whether it read
them rightly. The
review is one layer, alongside the grounding rules, the source labels, the
code checks and the researcher's own judgment. Say that in the report when
you mention the review.

---

Part of Magpie version 2026-11-12, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
