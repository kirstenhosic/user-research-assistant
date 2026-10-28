# Method: journey maps and personas from research

Two ways to turn findings into something the team keeps using after the
readout. A journey map shows the steps one kind of person takes to reach
a goal, with what they do, think and feel at each step, and where it goes
wrong. A persona describes one kind of user: their goals, how they work,
what gets in their way. Both are outputs of research, built from
findings; neither is research.

## Use them when

- The study covered a whole journey (a diary study, field work, a round
  of interviews about a process) and the findings are a sequence, not a
  list.
- The team keeps arguing about "the user" and the research found two or
  three distinct kinds.
- The team already has journeys or personas and the study contradicts or
  extends them (`lenses-systems-and-journeys.md`).
- A map would show where the problems cluster better than a findings list
  would.

## Don't use them when

- The research didn't cover the journey. A map drawn from one touchpoint
  is a guess about the rest; label the guessed parts.
- The team wants a persona to settle an argument, with no research
  behind it. That's a proto persona: a written-down assumption. It can be
  useful for aligning a team, as long as it says so on its face.
- The deliverable would be the end of the work. A map or a persona is a
  tool for the next decision, not a poster.

## Journey maps

A map has five parts. Leave out what the research can't fill, and mark
what's inferred.

1. **The actor.** One persona or one kind of user. A map with two actors
   is two maps.
2. **The scenario and the expectation.** What they're trying to do, and
   what they expect it to be like. From the baseline questions in
   sessions.
3. **The phases.** Three to seven, in the user's words, from what people
   did, not from the product's screens.
4. **In each phase: actions, thoughts, feelings.** What they did; what
   they said they were thinking; how it felt, from what they said and
   did. Each cell carries a participant count or a code ("P2, P5, P7"),
   as any finding does.
5. **Opportunities.** Where it stalled, where they improvised, where
   they gave up. Each one points to a finding, and from there to a
   recommendation (stage 8).

How to build it from findings:

- Lay the sessions side by side (the sequences from contextual inquiry,
  the entries from a diary, the "last time" stories from interviews).
  Where did each person start, and what happened next?
- Name the phases from the steps most people had. Steps only some had
  go in as branches or notes.
- Fill each cell from coded findings, with the counts. A cell with one
  participant behind it says so.
- Mark the breakdowns, and how many hit each.
- Mark the parts the study didn't cover, so the map doesn't claim them.
- Draft it, then check it with two or three participants, or against two
  sessions you held back. A map nobody who lived it recognizes is wrong.

Related things the team may ask for: an experience map (the same, for a
whole activity, not tied to a product), a service blueprint (the same
journey from the organization's side: the people, systems and steps
behind each phase), and a user story map (the journey as a backlog, for
planning). The journey map is for understanding; the others come after.

## Personas

Three kinds, by what they rest on. Say which kind any persona is.

| Kind | Built from | Good for | Can't say |
| --- | --- | --- | --- |
| Proto persona | The team's assumptions, written down in a workshop | Aligning a team quickly; naming assumptions to test | Anything about real users; label it [assumption] |
| Qualitative persona | Interviews, field work, tests: a small sample, grouped by shared goals, attitudes and pain points | Most teams, most decisions; design and prioritization | How many users each one stands for |
| Statistical persona | A survey of a large sample (hundreds, often 500 or more) clustered by attitudes and behaviors, with qualitative research first | Sizing each group; big investment decisions | Much, without the qualitative work behind it |

How to build qualitative personas from findings:

- Group participants by what they're trying to do and how, not by who
  they are. Two people with the same job title can be different personas;
  two with different titles can be the same one.
- Look for the differences that changed the findings: the goal, the
  frequency, the setting, what they're measured on, what they fear.
  Those are the dividing lines. Demographics go in only where they
  changed behavior.
- Two to four personas. More than that and nobody remembers them.
- Each persona gets: a name and a one-line description; what they're
  trying to do; how they do it now, including the workarounds; what gets
  in the way; what they'd never do; a quote from a real participant; and
  the participant codes it's built from ("P1, P4, P6, P8").
- Say what the study can't say: how many users are each persona, and
  whether the groups hold outside the sample.
- Every persona is memorable, actionable and different from the others.
  If two personas would make the same decision in every scenario the team
  cares about, merge them.

## What makes it good

- Every cell and every trait traceable to findings, with counts or codes.
- Gaps marked, not filled in.
- Checked against people who lived it.
- Dated, and owned by someone who'll update it after the next study.
- Used: it appears in the next stage 3, when the team places a new
  question on the journey and names the persona it's about.

## Analysis

They are analysis outputs. Build them in stage 7 after the themes are
settled, and present them in stage 8 next to the findings they rest on,
never instead of them. The readout says what kind of persona it is and
how many sessions the map rests on.

## Worked example

> **Study.** Dockside (warehouse returns): five contextual inquiry
> sessions and a two-week diary with six clerks.
>
> **Journey map.** Actor: a returns clerk at a multi-person site.
> Scenario: "get a return off the floor and refunded." Five phases from
> the sequences laid side by side: receive, sort, find the order,
> refund, close. "Where it breaks" cells: search times out on unlabelled
> items (receive, 3 of 5 sessions); refund screen resets (refund, 2 of
> 5 sessions, 9 diary entries). The "close" phase was seen in only two
> sessions and is marked so. Checked with two clerks, who moved "sort"
> before "receive" for bulk deliveries; the map now shows that branch.
>
> **Personas.** Qualitative, two: the desk clerk (P1, P2, P3, P5; works
> the screen, keeps paper for the two failures) and the all-in-one clerk
> at a small site (P4; does bay, sort and desk alone, scanner-less).
> Each carries its codes, a real quote, and "can't say how many sites
> are like this". The team's existing persona, "warehouse operative",
> covered both; a library entry says why they're now two.

## Pitfalls

- A map drawn from the product's screens, not from what people did.
- A persona built from a demographic, a role or a plan tier.
- Filling the gaps with plausible guesses, unmarked.
- One participant's journey presented as the journey.
- Personas that live in a slide and never appear in a decision.
- Updating the poster, not the persona, after new research.

## Template

`templates-journey-map.md` for the map and `templates-persona.md` for
each persona. Both carry the participant codes column.

## Basis

S93 (a journey map as a visualization of the process a person goes
through to accomplish a goal; the five parts: actor, scenario and
expectations, phases, actions, mindsets and emotions, opportunities; how
it differs from experience maps, service blueprints and user story maps).
S94 (the three persona kinds: proto personas from assumptions, qualitative
personas from small-sample research grouped by attitudes, goals and pain
points, statistical personas from a large survey, ideally 500 or more,
with clustering and prior qualitative work; qualitative as the best fit
for most teams; personas rest on qualitative understanding, not
demographics or analytics correlations alone; good personas are
memorable, actionable and distinct). Building from coded findings with
counts, the two-to-four range, checking with participants, and the
pitfalls: practitioner judgment.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
