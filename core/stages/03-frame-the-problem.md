# Stage 3: Frame the problem

Turn the ask into a decision, a business reason and research questions. This
stage is the anchor for everything after it.

## Goal

A decision statement the owner would recognize, a business reason leadership
would recognize, and research questions that each serve the decision.

## Inputs

- The ask, in whatever form it arrived.
- The gap summary from stage 2.
- The team profile, if there is one (products and users, company goals,
  metrics, stakeholders).
- The intake form, if a PM or designer filled one in.
- Any PRD, brief, past research or other background the researcher
  shares. Read it before you ask anything.

## Before you build

Ask for whatever on this list isn't already in the study record, the
conversation or files you can reach, in one message, before you build
(`operating.md`, "Gather context before you build").
This list is the floor: add the questions this particular study or task
raises, within the same six.

**Minimum to draft:** what prompted this (who asked, and for what) and
who the study is about.

- Any PRD, brief, past research or background they can share (one
  optional ask; `operating.md`, "Ask for documents first").
- What prompted this: who asked, and what they asked for, in their words.
- Who makes the decision, and by when, only if the your-turn answer
  below leaves it out. (The decision itself is the researcher's turn.)
- The business goal or metric it's meant to move, and what a wrong call
  would cost: can it be undone, and how quickly?
- The hypotheses: what the team believes now, and what would change its
  mind.
- Who the study is about: which users or customers.
- Anything already known or tried, if stage 2 didn't cover it.

**Your turn** (`operating.md`, "Your turn"). In the same message, ask the
researcher to write four things in their own words before you draft them.
Give them as one numbered item, a fill-in line each, so they read as one
thing to fill in. Together they count as one of the six questions. For
example:

> Your turn, a line each is fine:
> - **The decision:** [the team or group] will decide [what] by [when],
>   choosing between [options].
> - **The one question** that would make that decision easier: ...
> - **Questions people already have** (rough is fine, or "none"): ...
> - **What the team is taking for granted** (or "none"): ...

Keep "[the team or group]" in the decision line, not "[who]" or a
person's name: who decides is often a team, and naming one person can
close a conversation the team should have.

What each line is for:

- The decision: what will someone decide differently once they know the
  answer?
- The primary research question: the one question that would make that
  decision easier.
- Research questions the team already has: any written already, or ones
  stakeholders keep asking, as they are.
- The assumptions: anything the team takes for granted that, if wrong,
  would change the study or the decision.

Don't offer your guess at any of them. If they say "not sure" or "you do
it", draft them yourself. "None" is a fine answer for the last two; write
it in the record.

## What to do

1. **Offer the product context.** Optional. If it hasn't been offered
   yet, offer to fill the record's Product section: what the product is,
   what it does, the part under study, who its end users are, and who
   buys or sets it up if that's someone else. Draft it from the team
   profile, product docs, a public site you can reach and what the
   researcher has said, or ask in one line if you have nothing. If they
   decline, write "not added" and move on (`operating.md`, "Know the
   product").
2. **Find the decision.** Most asks arrive as a topic ("look into onboarding")
   or a feeling ("it's confusing"). Start from the researcher's own
   version (the your-turn ask above). Keep their words, and fill in what's
   missing from the format: *[The team or group] will decide [what] by [when], choosing
   between [options].* If you sharpen it, say what you changed and why in
   one sentence: a decision without options can't be ruled in or out by
   the evidence. If they handed this back, draft it from what you've been
   told and ask them to correct it.
3. **Tie it to the business.** Which goal or metric does it move? What does it
   cost to get it wrong? Use the team profile's goals and current bets if
   you have them, and note any market signal that bears on it (a competitor
   move, a segment the company is chasing), labelled as partner data. If
   the researcher doesn't know, that's fine: write "[assumption]" and move
   on. Don't invent a metric or a market claim. From the cost and whether
   the decision can be undone, draft the decision risk (low, medium or
   high) with a one-line reason (`lenses/minimum-viable-rigor.md`). It
   sets how much rigor the study needs at stage 4.
4. **Write the research questions.** One primary question that most changes
   the decision, starting from the researcher's version if they gave one.
   Fold in the questions the team already had: keep the ones that serve
   the decision, rewrite the ones that are really survey questions or are
   about the product rather than users (say what you changed and why in a
   line), and list the rest under "nice to know" so nothing the team asked
   for disappears without a word. Up to three secondary questions. Each one names the decision
   it serves. Questions are about users, not about the product ("how do
   people currently track X?" not "do users like our tracker?"). Where
   you know the product has buyers or admins apart from its end users,
   say which group each question is about. Run
   `checks/research-questions.md` over them, the researcher's own
   included, and show what you changed (`operating.md`, "Show what you
   changed").
5. **Write down the hypotheses.** What does the team already believe, and
   what would change its mind? Run `checks/hypotheses.md` over each one
   and show any you sharpened in the same before-and-after table as the
   research questions. Write each one in the record's Hypotheses
   section, with who holds it. The study tests them; it doesn't set out to
   prove them. The assumptions the researcher named go under Assumptions
   and risks, in their words, plus any you see that they didn't; mark
   yours as Magpie's. An assumption that would change the decision if
   wrong is a candidate for a hypothesis; say so.
6. **Place it in the larger system.** Use `lenses/systems-and-journeys.md`,
   briefly: what's upstream and downstream of this piece, which other
   teams touch it, what job the user is doing when they meet it, which of
   the team's journeys or CUJs and which persona it sits on. If the team
   profile has these, use its names. If not, draft a guess, mark it
   [assumption], and move on. Add the job, journey step and persona lines
   to the record's Business context.
7. **Check for a design question hiding inside.** Many asks mix a strategic
   question (should we build this?) with a design question (does this screen
   work?). Separate them. They usually need different methods.

## What to draft

- Decision, business context, hypotheses, research questions and
  assumptions, all in the study record, plus the Product section if the researcher wants it.
- A one-paragraph framing summary the researcher can send to the decision
  owner to confirm. With it, say in one line that they don't have to wait
  for the reply: "go on" moves to choosing the approach, and the
  unconfirmed framing is logged as a risk until the owner answers.

## Challenge

Usually the **decision test** or the **riskiest assumption**. Example: "If
the answer comes back 'users don't want this', what would the PM do, given
it's on the roadmap? If they'd ship it anyway, what is the research for?"

## Exit criteria

- The researcher was asked to write the decision, the primary question,
  the team's existing questions and the assumptions first, or these came
  with the brief, or they handed it back.
- Product context offered once: filled, or "not added" by the
  researcher's choice.
- A decision statement with owner, deadline and options.
- A business reason, or an honest "[assumption]" placeholder.
- Decision risk rated low, medium or high with a reason, or marked
  [assumption].
- A primary research question tied to the decision.
- Research-question check run.
- Hypotheses and assumptions listed, or a note that the team has none.
- Job, journey step and persona filled in or marked as assumptions.
- The decision owner has seen the framing, or the researcher has chosen to
  proceed without that (logged as a risk).

## When stakeholder interviews would help

If the brief is thin or came from one person, or the success measure and
the constraints aren't agreed, offer stakeholder interviews in one line
(`methods/stakeholder-interviews.md`): one-to-one, 30 to 45 minutes,
before the plan is written. What stakeholders say about users goes into
the record as hypotheses with who holds them (3.7), never as findings.

## When a workshop would help

If the team disagrees about the decision, or about what users do, offer
an "align on the problem" workshop in one line
(`workshops/stakeholder-workshops.md`). It's the researcher's
call; don't hold the stage for it.

## When to stop here

If no decision depends on the answer, say so. Curiosity is a fine reason to
read, not usually a reason to run a study. Suggest the cheapest way to
satisfy it.

## Pitfalls

- Treating buyers or admins as if they were the end users.
- A decision so broad it can't be wrong ("improve the experience").
- Research questions that are really survey questions.
- Studying one step as if nothing came before or after it.
- Leaving the business reason blank because it feels awkward to ask. It's the
  sentence that gets the study funded and the findings acted on.
