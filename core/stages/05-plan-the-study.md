# Stage 5: Plan the study

Write the research plan: who, how, when, and how participants are protected.

## Goal

A plan a stakeholder can read in two minutes and a teammate could run from.

## Inputs

- The study record through stage 4.
- The team's rules on consent, recruiting, incentives and data handling, from
  the team profile if there is one.
- Calendar constraints.

## Before you build

Ask for whatever on this list isn't already in the study record, the
conversation or files you can reach, in one message, before you build
(`operating.md`, "Gather context before you build").
This list is the floor: add the questions this particular study or task
raises, within the same six.

**Minimum to draft:** the decision it serves and who the participants
are.

- The decision, its owner and deadline, and the business goal it serves.
- The research questions and hypotheses.
- Who the participants are, how many, and where they'll come from.
- The team's rules on consent, recording, data storage and incentives.
- Dates that constrain the study: when sessions can run, when the readout
  is due, holidays and team availability.
- Who's on the study team, and who will moderate and take notes.

If stages 3 and 4 aren't done yet, don't squeeze all of this into one
message. Gather it in up to three rounds (frame, method, plan), six
questions at most each, and build the plan once (`operating.md`, "A plan
from scratch takes rounds").

## What to do

1. **Draft the plan from `templates/research-plan.md`.** Fill every section
   from the record. Where something is unknown, follow `operating.md`,
   "Gather context before you build": a guess the researcher let stand is
   marked [assumption], and anything that can't be guessed (a date, a
   name, a budget) is a labeled blank such as "[recruiting start date]".
2. **Write the recruiting criteria.** Who's in, who's out, and why each
   criterion matters for the decision. Use the team's persona or segment
   names where they exist, always with the behavior that defines them.
   If the Product section names end users, start from them, and recruit
   buyers or admins only when the decision is about them, saying so. Include the
   people who tried and left if the decision depends on them.
3. **Check the sample for blind spots.** Which groups are missing? Does that
   matter for this decision? Write the answer under trade-offs either way.
   Include disabled participants and people who use assistive technology,
   with the lead time and access arrangements that takes, or say why not
   (`lenses/accessibility.md`).
4. **Plan for consent and data.** What participants are told, what's recorded,
   where it's stored, who can see it, when it's deleted. For a diary
   study, say how entries are captured and cover consent for each
   format (`methods/diary-studies.md`, "Ways to capture entries"). If an
   AI tool will moderate, transcribe, summarize or analyze the sessions,
   Magpie included, say what participants are told about it
   (`checks/ethics-and-consent.md`). If the study touches
   anyone who might be vulnerable, say what extra care is taken. This is a
   red flag if missing.
5. **Set the timeline backwards from the decision deadline.** Readout date
   first, then analysis, then sessions, then recruiting. If it doesn't fit,
   use the smallest-study moves in `lenses/minimum-viable-rigor.md` first,
   since they save time without weakening the answer. Any cut that does
   weaken it goes under trade-offs with what it costs.
6. **Plan for participant quality.** Say where participants come from and
   how much fraud risk that carries (own verified users: low; third-party
   panels: high). Set the disqualification threshold and the replacement
   protocol now, so a bad participant costs an hour, not the study.
   `checks/ai-assisted-research.md`, section 4.
7. **If an AI tool will moderate sessions,** schedule the first-three-
   transcript audit in the timeline, with a stop point before the rest of
   the sessions run. `checks/ai-assisted-research.md`, section 1.
8. **Name the risks.** Pull every skipped challenge from the record into the
   plan's risks section, plus anything new.

## What to draft

- The research plan, as Markdown and Word (`operating.md`, "Files for the
  team").
- The recruiting screener questions, if recruiting is needed.
- An updated study record (Approach and Assumptions and risks).

## Challenge

Usually **sample blind spot**. Example: "Everyone on your list is an admin
who set the product up. The decision is about daily users who didn't. What
would you miss without them?"

## Exit criteria

- A complete plan with no unexplained placeholders.
- Consent and data handling covered.
- Disabled participants included, with access arrangements, or the reason
  they aren't written under trade-offs.
- Timeline fits the decision deadline, or the gap is named.
- Every cut made to fit time or budget is listed with what it costs.
- Risks listed, including skipped challenges.

## Pitfalls

- A plan that lists activities but never says why they answer the question.
- Recruiting whoever's easiest to reach.
- Consent treated as a form to sign rather than a conversation.
- Recruiting from a panel with no plan for the participants who turn out
  to be bots or speed-runners.
- A timeline that ends the day the decision is due, with no time for the
  team to absorb the findings.
