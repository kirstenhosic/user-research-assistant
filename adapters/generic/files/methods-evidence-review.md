# Method: evidence review

Answer a question from research and data the organization already has,
instead of running a new study. Stage 2 in full.

## Use it when

- Stage 2 turned up enough evidence to answer the question, or nearly.
- The decision is due too soon for new research.
- Several past studies touched the question and nobody has put them
  together.

## Don't use it when

- The evidence is older than the last major change to the product or the
  market.
- The evidence is all secondhand or anecdotal.
- The question is about something the organization has never looked at.

## Sources

- The research library, if there is one.
- Past reports, decks and study records.
- Support ticket themes (`methods-customer-feedback-coding.md` says how to
  code them).
- Analytics and telemetry.
- Survey archives.
- Sales and customer success notes (indirect; label them).
- Public research, labeled as general rather than about your users.

## Shape

1. Write the question and the decision first, as in stage 3.
2. Gather what exists. Log every item in the evidence log with source,
   date, method, confidence and still-valid?
3. For each research question: what does the evidence say, how strongly,
   what disagrees, what's missing?
4. Write the evidence brief.
5. Say what a new study would add, if anything, and whether it's worth it
   for this decision.

## Judging an old study

Rate each item before it counts. Five questions, in order:

1. **Can you see the data?** A deck's conclusions are not evidence until
   you've seen what they rest on: the transcripts, the counts, the
   survey export. A study with no methods section and no data is a claim.
2. **Who took part, and how many?** Were they the people this decision is
   about? Five interviews with admins say nothing about end users. A
   survey of whoever answered describes the people who answered.
3. **What was done?** Did people do the thing or talk about it? Was the
   question asked neutrally? Did the method fit the question (stage 4's
   rules)?
4. **When, and what's changed since?** Date every item. A finding about a
   flow that has been redesigned since is history. Market and competitor
   facts age faster than findings about how people work.
5. **Who ran it, and why?** A study run to justify a decision already made
   reads differently from one run to make it. Vendor and analyst reports
   have a product to sell; label them.

The item's confidence is the lowest answer, not the average. Record it in
the evidence log in one line: "2025-03 usability test, 6 admins, moderated,
saw the data: high for admins, nothing for end users."

## Using a research repository

- Search by the user's job and the journey step, not by the feature
  name. Past studies were filed under the name the feature had then.
- Read the study, not the entry. A library entry is a summary written for
  reuse; it loses the caveats. Open the source before quoting it.
- Note who the past participants were. Repositories mix studies of
  different groups, and a theme that looks strong across five entries may
  be five different audiences.
- Look for what disagrees. Search for the opposite claim before concluding
  that the library agrees.
- When Magpie writes the library entry for this study (stage 8), it writes
  the one it wished it had found: the question, who took part, the
  method, the date, the caveats, and where the data lives.

## Summaries written by AI

Teams increasingly search their research with an AI tool, or get a
summary of past studies from one. Treat such a summary as a lead, not a
source.

- Ask for the source of every claim in it, and open that source.
- Check that each study it cites exists and says what the summary says.
  A summary can blend two studies, invent a number from "most", or
  attribute a quote to the wrong study.
- Count how many studies a "theme across our research" rests on, and who
  took part in each.
- Log the summary itself in the evidence log as a tool output, with the
  date and the prompt, never as a finding.

## The evidence brief (one page)

- The question and the decision.
- What the evidence says, with sources and dates.
- How confident we are, and why.
- What's still unknown.
- What the team should do: act, or run [specific study] to close [specific
  gap].

### Worked example

> **Question.** Should the mobile app get an offline mode? Decision due in
> three weeks; mobile team's planning.
>
> **What the evidence says.**
> - Support tickets, last 6 months (coded 2026-10, 312 tickets): 41
>   mention losing work with no signal; 29 of those from field
>   technicians. *Their data, coded by us: high for "it happens", says
>   nothing about how often per user.*
> - Diary study, 2025-11, 9 field technicians, 2 weeks: 7 of 9 logged at
>   least one day with no signal; 4 described re-entering a job on return.
>   *Saw the entries: high for this group; the app has changed since but
>   not the sync.*
> - Analytics, 2026-09: 6% of mobile sessions end in a failed sync.
>   *Partner data; counts sessions, not people.*
> - Sales notes, 2026: "customers ask for offline all the time."
>   *Anecdote; label indirect.*
>
> **Confidence.** High that losing work with no signal is real and painful
> for field technicians. Low on how many users beyond that group are
> affected, and none on whether an offline mode is what they'd want over,
> say, a draft that survives a failed sync.
>
> **Unknown.** Scale outside field technicians; what "offline" would need
> to cover.
>
> **Recommendation.** Act for field technicians: the problem is established.
> Before scoping the full feature, run five contextual inquiry sessions
> with technicians on a day in the field to see what work needs to
> survive (two weeks, fits the deadline). Don't run a survey; the
> question is what, not how many.

## What makes it good

- Honest dates. A 2023 finding about a flow that changed in 2025 is
  history, not evidence.
- Confidence labels on every source, and the brief's overall confidence
  no higher than its weakest load-bearing source.
- Disagreements between sources shown, not averaged.

## Pitfalls

- Treating a deck's conclusion as evidence without seeing its data.
- Stitching three weak sources into one strong claim.
- Skipping the brief and just saying "we already know this".
- Quoting a library entry or an AI summary without opening the study.

## Basis

S18 (secondary research as a standard first step; judge each source's
validity and limitations; a missing methods section is a red flag); S13
(one source's limits are offset by another); S14 (when sources disagree,
examine how each was done; quantitative data doesn't automatically
overrule qualitative); S10 (where AI tools break: blended sources,
invented specifics, confident summaries). The five judging questions, the
repository rules, the AI-summary rules, the evidence brief's shape, the
worked example and the confidence rule (no higher than the weakest
load-bearing source): practitioner judgment.

---

Part of Magpie version 2026-11-02, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
