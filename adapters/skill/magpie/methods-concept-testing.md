# Method: concept and value testing

Show people an idea before it's built and learn whether it solves a problem
they have, how they'd fit it into their work, and what would stop them.

## Use it when

- The decision is whether to build something, or which of several
  directions to take.
- You have a concept to show: a sketch, a storyboard, a one-page
  description, a clickable mock.
- You want direction, not usability.

## Don't use it when

- You want to know whether people can use it. That's a usability test.
- You want to know how many would buy or adopt. Reactions in a session
  don't predict that; combine with behavioral data or a pricing method,
  or run a fake-door test (below).
- The concept is so vague participants would be reacting to the drawing,
  not the idea.

## What to show

Pick the lightest form that carries the idea, and show every concept at
the same level of polish so polish isn't the variable.

| Form | Shows | Good for |
| --- | --- | --- |
| One-paragraph description | The promise in words | Early, many ideas, cheap to change |
| Storyboard (four to six frames) | A person, a situation, the idea in use, the outcome | Ideas that only make sense in a situation |
| Sketch or wireframe | What it might look like | Ideas where the shape matters |
| Clickable mock | A few screens that respond | Ideas people need to try to understand |
| Fake landing page | The promise as the market would meet it | Measuring interest at scale (see fake-door tests) |

Words first where you can. A polished screen makes people react to the
screen. Leave out the brand, prices and a name unless they're part of
what's being tested.

## Sample

- Six to ten per target group. If comparing concepts, show each person all
  of them, in rotated order.

## Session shape (30 to 45 minutes)

1. Context first: how they handle the problem today, before they see
   anything. Ask for the last time, not the usual: "Tell me about the last
   time you [did the thing]. What did you do? What did it cost you?" This
   is the baseline.
2. Show the concept. Let them read or explore it. Ask what they think it
   is and who it's for, before you explain.
3. Value: "Where in your week would this fit?", "What would you stop doing?",
   "What would make you not bother?"
4. If several concepts: the same questions for each, then "If you could
   only have one…" and why.
5. Close: what's missing, what they'd want to know before using it.

## Ask about the past, not the future

"Would you use this?" gets a kind yes from almost everyone. Replace it
with questions that have a true answer:

- **Have they tried to solve it?** "What have you tried?" "What do you do
  now instead?" Someone who has never tried to solve the problem doesn't
  have it badly enough to change.
- **What has it cost them?** Time, money, workarounds, a tool they bought
  and dropped. Past spend is a better signal than stated interest.
- **What would they give up?** "What would this replace?" A concept that
  replaces nothing fits nowhere.
- **A small commitment.** "Can I show you the next version?" "Would you
  join a pilot?" "Who else here should see this?" A yes that costs
  something means more than a compliment.

Write down the compliments and set them aside. A session full of "that's
great" and no stories is a polite no.

## Fake-door and smoke tests

The behavioral check. Put the promise of the feature in front of real
users before it exists (a button, a menu entry, a landing page with a
sign-up) and count who acts on it. Those who click see a short, honest
message: it isn't ready, thanks for telling us you're interested, and an
optional "tell us why". Pair it with a few interviews of the people who
clicked.

- Use it when sessions show interest and the team needs to know how wide
  the interest is before building.
- Write the question and the bar first: how many clicks, out of how many
  who saw it, would make the feature worth building? Agree the bar before
  the number arrives.
- Keep it short and small. A dead-end button costs trust, and people who
  meet unavailable features more than once, such as beta testers, get
  frustrated; run it for a short, fixed time, to a slice of users, never
  twice on the same people, and never for something they urgently need.
- Count clicks on the call to action out of everyone who saw it, and
  time on the page. In a remote test, a short survey after the message
  adds the why; in a moderated session, agree beforehand how the
  moderator handles the moment the door turns out to be fake.
- Say what the number can't tell you. A click is curiosity; it isn't use.
  People who clicked once may not have the problem the way the team
  thinks. It isn't a method on its own; it sits next to the sessions.
- The analytics or growth team usually runs it. Magpie drafts the question,
  the bar and the message (`methods-analytics-and-ab-tests.md`, "Who does
  it") and logs the result as [their data].

## What makes it good

- Baseline before exposure.
- Asking what they'd give up for it, not whether they like it.
- Concepts shown at the same level of polish, so polish isn't the
  variable.
- Noting the questions participants ask; they reveal the gaps.

## Analysis

For each concept: how participants understood it, where they saw value and
for what, what would block adoption, and how it compares to how they cope
today. Reaction patterns, not votes. Stage 7 covers this. Keep the
baseline stories next to the reactions: someone who described a painful
workaround and then shrugged at the concept is a finding.

## Worked example

> **Decision.** Which of two directions Sparrow (team messaging) takes
> for "catch up after time away": a digest, or a per-channel summary.
>
> **Research question.** When people come back after a day or more away,
> what do they do now, and which direction fits that?
>
> **Sample.** Eight people who were away from work for two or more days
> in the last month, 40 minutes each, both concepts as four-frame
> storyboards at the same polish, order rotated.
>
> **Baseline.** "Tell me about the last time you came back after a few
> days." 6 of 8 described scrolling each channel from the top (P1, P2,
> P4, P5, P7, P8); two asked a colleague what they'd missed.
>
> **Reactions, as reported.** All eight said both ideas were "great".
> Asked what each would replace: 5 of 8 said the digest would replace
> the scroll (P1, P2, P4, P5, P8); 2 of 8 said the per-channel summary
> would replace anything. 3 of 8 asked to see the next version of the
> digest unprompted. Reported as patterns in reasons, not a vote;
> recommendation: a fake-door digest entry for two weeks to size
> interest before building.

## Pitfalls

- "Would you use this?" Everyone says yes to be kind.
- Selling the concept instead of testing it.
- Reading politeness as enthusiasm.
- Treating a preference between two mock-ups as a market signal.
- A fake door left up for weeks, or on something people need now.

## Template

`templates-concept-test.md`

## Basis

Definition: S52 (an attitudinal method that collects people's thoughts
and attitudes about a product idea). Why "would you use it?" misleads and
reactions don't predict adoption: S8 (self-reported future intentions are
unreliable; observe behavior where you can); S27 (research should not stop
at a yes or no); S5 (past experience over hypotheticals). Pairing reactions
with behavioral data: S13. The forms to show, the past-not-future
questions, the small-commitment test, sample sizes, the session shape and the
baseline-first rule: practitioner judgment. Fake-door tests: S99 (a
landing page or mockup with a call to action for a feature that doesn't
exist; judge interest by what people do; clicks and time on page; a
survey after the message in remote tests, agreed moderator guidance in
person; repeated exposure frustrates people; not a standalone method).
The honest message after the click, the fixed short run and the agreed
bar: practitioner judgment; S99 does not cover them.

---

Part of Magpie version 2026-11-01, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
