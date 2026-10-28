# Stage 4: Choose the approach

Pick the cheapest method that can answer the primary question well enough
for the decision.

## Goal

A method, a rough sample, and the trade-offs accepted, written so the
decision owner could understand why.

## Inputs

- The study record through stage 3.
- Constraints: deadline, budget, access to participants, tools available.
- Anything partner teams can provide (analytics, support data).

## Before you build

Ask for whatever on this list isn't already in the study record, the
conversation or files you can reach, in one message, before you build
(`operating.md`, "Gather context before you build").
This list is the floor: add the questions this particular study or task
raises, within the same six.

**Minimum to draft:** the primary research question, and roughly how
long the study can take.

- The deadline for the decision, and how much time the study can take.
- Budget, including incentives and tools.
- Access to participants: who the team can reach, and how.
- Tools available for sessions, surveys or analysis.
- Any method a stakeholder expects or has ruled out, and why.
- Partner data the team can get (analytics, support, sales), and how fast.
- Where the product stands (an idea, being designed, or live) and where
  people use it, if the Product section doesn't already say.

## What to do

1. **Start from the question, not the method.** Answer four things about
   the primary question before naming a method. Together they narrow the
   list; none of them picks the method on its own.
   - **What kind of question.** *Why* and *how* (go qualitative), *how
     many* and *how often* (go quantitative), or *whether this design
     works* (test it).
   - **What people say, or what they do.** Does the decision rest on what
     people think, want and say (attitudes), or on what they actually do
     (behavior)? Lean on what they do: people can only report what they
     notice and remember, and what they say often differs from what they
     do. Methods that listen (interviews, surveys, focus groups) suit
     opinions, wants and the words people use. Methods that watch
     (usability tests, field studies, analytics) suit what happens. When
     the decision needs both, plan to compare them; a gap between what
     people say and what they do is often a finding in itself.
   - **Where the product stands.** Before anything is built, the job is to
     explore: interviews, field studies, diary studies, concept testing,
     participatory design. While it's being designed, the job is to test
     and improve it: usability testing, card sorting and tree testing,
     preference testing (`methods-preference-and-desirability.md`). Once
     it's live, the job is to measure it against something: benchmarking
     (`methods-benchmarking.md`), analytics and A/B tests
     (`methods-analytics-and-ab-tests.md`), surveys, unmoderated testing
     at scale. These are starting lists, not rules; a live product can
     still need exploring.
   - **Where and how people use it in the study.** Real use, in their own
     setting with their own data, shows the truest behavior but gives
     less control over what you see. Scripted tasks give results you can
     compare, with a narrower view. Some studies use only part of the
     product (a concept, a menu structure) or none of it (how people see
     a brand). Decide too whether sessions are in person or remote
     (remote reaches more people in less time; in person suits long
     sessions and physical tasks), and whether the study has to happen
     somewhere specific or away from a screen (at the gym, in a shop, on
     a warehouse floor). If the setting changes what people do, go to it
     (`methods-field-studies.md`).
2. **Check the cheap options first.** Could analytics, support tickets, a
   quick look at existing recordings, or five conversations answer it? Say so
   if yes, even if the researcher wanted something bigger. What's
   available depends on where the product stands (Product section, if
   filled): a live
   product has analytics, support tickets and real use to watch; an idea
   or a prototype has none of those, so concept testing or interviews
   about what people do today fit better. If there's a
   design to evaluate, an expert review (`methods-expert-review.md`) can
   clear obvious problems before users see it; it predicts problems, so it
   comes before testing, never instead of it.
3. **Consider how others solve it.** If the decision is about building
   something other tools already offer, or users will arrive with
   expectations from elsewhere, suggest a competitive analysis
   (`methods-competitive-analysis.md`) as a cheap first step or a companion
   to the main method. It works from public sources when nobody can get
   into the tools. It shows options and expectations; it doesn't replace
   hearing from users.
4. **Recommend one method and one backup.** Use the `methods-*.md` files for the fit, the
   sample guidance and the pitfalls. Give the reason in two sentences. If
   the ask names a method, check it against the question the same way. A
   focus group asked for to judge usability or predict behavior is the
   common case (`methods-focus-groups.md`).
5. **Pair methods when the question has two halves.** If the decision
   needs both *how many* and *why*, or both what people say and what they
   do, suggest a companion method for the other half and say in a line
   what it adds. For example: analytics or a short survey to find where
   people drop off, then sessions to learn why; or interviews about what
   people want, checked against what they did in a usability test. Only
   suggest a companion the time and the rigor allow (step 9); one method
   done well beats two done thinly. The researcher decides.
6. **Name what it can't tell you.** Every method has a blind spot. Write it
   under trade-offs so nobody is surprised at the readout.
7. **Show the reasoning and invite a counter** (`operating.md`, "Show the
   reasoning"). Under the recommendation, in a few plain lines: how the
   four answers from step 1 point to this method; the cheaper options you
   ruled out and why; what the method can't tell them; why the backup is
   second. Add one line on what the team will have at the end, in words
   they could repeat to someone else (for example, "the four or five
   places people get stuck and why, with clips", not "insights about the
   flow"). If someone outside the study asked for a different method,
   these lines are what to share with them. Then one line: "If
   you'd pick differently, say why and I'll rework it." A counter is new
   input: rework the choice with their reasoning, or say in a line or two
   why you'd keep it. Their call stands.
8. **Size the sample roughly.** Enough to see a pattern for the decision at
   hand, not a magic number. For qualitative work, say what "enough" looks
   like (for example, "when the last three sessions add nothing new").
9. **Match the rigor to the decision risk** (`lenses-minimum-viable-rigor.md`).
   Low risk gets the smallest study that gives a real answer; high risk
   gets a sample sized for the claim and a second source to check against.
   Say in a line how the recommendation fits the risk from stage 3. Check
   the plan against the floor in the lens, whatever the budget. If the
   time and money can't reach the floor, say so now: offer the smaller
   question they can answer well and what the original would take, and
   let the researcher and the team choose.
10. **Ask about partner data.** Would telemetry help choose who to recruit, or
   size the problem before you go qualitative? Draft the request if so.

## What to draft

- The Approach section of the study record: method, why, what the team
  will get, sample, trade-offs, partner data requested.
- The reasoning behind the choice, shown with the recommendation, and the
  line inviting a counter.
- A short comparison of the recommended method against the backup, if the
  researcher is weighing them.

## Challenge

Usually **method fit**. Example: "You've gone straight to a survey, but the
question is 'why do people stop after step 3?' What would eight sessions
watching them do step 3 tell you that the survey can't?"

## Exit criteria

- The question is placed: what kind, say or do, where the product
  stands, and the setting.
- One method chosen, with the reason written down, and a companion
  suggested or not needed.
- What the team will get is written in a line.
- Sample sized and described.
- The rigor fits the decision risk and stays above the floor, or the gap
  is named with a smaller question offered.
- Trade-offs written.
- Partner data requests drafted or marked not needed.

## Pitfalls

- Choosing the method the team is used to, not the one the question needs.
- A survey to answer a "why" question.
- A focus group to answer "can they use it?".
- Asking people what they would do when you could watch what they do.
- Asking which design people prefer and reporting it as which one works.
- An A/B test on a page with too little traffic to give an answer.
- An expert review reported as what users do.
- Treating a sample of five as proof of "how many".
- Skipping the cheap check because it feels like not doing research.
- A large study for a decision that's cheap to undo.
- Cutting below the floor to hit a deadline, and finding out at the
  readout.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
