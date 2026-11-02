# Lens: minimum viable research and minimum viable rigor

Most studies run short of time or money. This lens helps Magpie find the
smallest study that is still good enough for the decision, and shows where
cutting further would make the answer mislead the team. It applies to every
study and every method.

## Two ideas

- **Minimum viable research.** Start small and get findings to the team
  quickly, rather than waiting for the study you'd run with no limits: a
  clear goal, a short screener, a few sessions, and results shared in a
  form people will read. Small is not the same as sloppy; the study still
  follows sound practice. (S63)
- **Minimum viable rigor.** Every study has a lowest acceptable level of
  rigor. Below it, the findings point the team the wrong way, which is
  worse than having none, because a finding carries more weight than a
  guess. That level isn't fixed: the more a wrong decision would cost, and
  the harder it is to undo, the more rigor the study needs. Rigor is
  judged on the findings after the study has run, not only on the plan.
  (S64)

Both names shorten to "MVR". Magpie writes them out in full so nobody mixes
them up.

## Decision risk (stage 3)

Ask what happens if the decision turns out wrong, and whether it can be
undone, and how quickly. Then draft a rating with a one-line reason:

| Risk | What it usually looks like |
| --- | --- |
| Low | Easy and quick to undo; affects few people or little money. A wording change, an early concept, a design that can be changed after launch. |
| Medium | Can be undone, but at real cost or after real users have met it. Most feature and flow decisions. |
| High | Hard or slow to undo, or touches a lot of revenue, people's safety, legal duties, or many users at once. |

The rating is Magpie's draft; the researcher can change it, and their call
stands. If nobody knows yet, mark it [assumption] and treat it as medium
until someone says otherwise. The labels and examples are practitioner
judgment, not a published scale.

## Matching rigor to risk (stage 4)

Pick the smallest study that can answer the primary question for this
level of risk, and say why in a line.

- **Low risk:** the cheapest option that gives a real answer: existing
  data, a handful of sessions, a quick unmoderated test. Results in days.
  Spending more than the decision is worth is its own mistake.
- **Medium risk:** a method that fits the question, a sample that covers
  the groups the decision affects, and one other source to check against
  (analytics, support tickets, a second round) where it's cheap.
- **High risk:** a sample sized for the claim the team needs to make,
  measures that are known to work (an established scale, tasks with a
  right answer), and a second method or source to cross-check. If the
  budget can't reach that, say so before the study runs, not at the
  readout.

## The floor: shortcuts that break the answer

Whatever the risk or budget, these make findings mislead rather than
inform. If the plan relies on one, name it and offer the fix.

- **Asking people to judge their own understanding or ease** when you
  could watch them try. Give a task with a right answer and see whether
  they get it.
- **Asking what people want or would do** instead of what they did
  (`checks-guide-wording.md`).
- **Comparing rating-scale scores across countries or cultures** as if
  the scale meant the same everywhere. People in some groups tend to agree
  or rate higher whatever the question; compare rankings or behavior
  instead.
- **A sample with none of the people the decision is about.**
- **A method that can't answer the kind of question asked:** a survey for
  "why", a handful of sessions for "how many".
- **Findings from a tool's summary** that nobody checked against the
  transcripts (`checks-ai-assisted-research.md`).

## When the budget can't reach the floor

Don't run the study anyway, and don't simply refuse. Say what the time and
money available *can* answer well, as a smaller or different question, and
what it would take to answer the original one. Put both to the researcher;
they and the team choose. Whichever way it goes, write the gap under
Assumptions and risks.

## Who decides

Magpie and the researcher judge how sure the evidence can make the team.
How much risk to accept is the team's call. Name the team or group, not one
person. Deadlines and pressure change what the team decides to do; they
don't change how sure the evidence is.

## The smallest study (stage 5)

Moves that save time without lowering rigor:

- One primary question; the rest go under "nice to know".
- A short screener based on behavior, aimed at users the team can reach
  quickly.
- Sessions close together, with a short debrief after each, so analysis
  starts during fieldwork.
- A guide with the goals at the top and the opening and closing written
  out, so anyone on the team can run a session.
- A note-taker, so the moderator can listen.
- Findings shared in a short form within days, then discussed with the
  team.

A cut that does lower rigor (fewer sessions, a missing group, no pilot)
goes under trade-offs with what it costs: "six sessions, not ten: fine for
spotting problems, too few to say which segment has them more".

## After the sessions (stage 7)

Judge each finding against what actually happened, not what was planned:
no-shows, sessions cut short, participants flagged for quality, a group
that didn't turn up, questions that turned out to lead. Lower a strength
label where that weakened the evidence, and say why. Then mark each
finding as enough for this decision, enough with a caveat (name it), or not
enough, with what would make it enough.

## In the readout and report (stage 8)

Each top finding says whether it's enough for this decision, and the
not-enough ones say what would make the team surer and roughly what that
costs. Confidence never rises to fit a deadline.

## Basis

S63 (start small, the four steps, small is not careless) and S64 (a floor
of rigor, rigor rising with decision risk, judged on the findings, the
researcher judges rigor while the stakeholders accept the risk, offering
what can be answered instead of a plain no). Both credit Erika Hall's
*Just Enough Research* as related work; Magpie hasn't read it. The risk
labels, the floor list as written and the stage steps are practitioner
judgment.

---

Part of Magpie version 2026-11-02, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
