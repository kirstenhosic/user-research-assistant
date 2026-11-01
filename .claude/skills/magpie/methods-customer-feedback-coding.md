# Method: coding customer feedback

Turn the feedback the organization already collects (support tickets,
app store reviews, survey open-ends, chat logs, sales and success notes,
community posts) into counted themes the team can act on. It's evidence
review's biggest raw source, and the same coding rules as stage 7, applied
at volume.

## Use it when

- The question is what people complain about, ask for, or praise, and
  how that is changing.
- A score has moved (satisfaction, NPS, ratings) and the team wants to
  know why. The score is the smoke alarm; the comments behind it are the
  diagnosis.
- Something seen in a few sessions needs sizing, and the feedback archive
  is large enough to size it.
- The team wants to check whether a finding from interviews or tests
  shows up in what customers write unprompted.

## Don't use it when

- The question is about people who don't write in. Feedback comes from
  the people who chose to send it: the angriest, the most engaged, the
  ones with time. It describes them, not the user base.
- The question is why something happens at the level of a single
  workflow. A ticket says "export failed"; it rarely says what the person
  was trying to do. Interview or watch.
- There's no question. A pile of feedback with no question produces
  interesting charts and no decision.

## Where it comes from

Gather it into one place with its context: the date, the channel, the
product area, the customer's plan or segment where you can, and the
whole comment. "Pricing" on its own can be praise or a complaint; the
sentence around it says which. Keep the link back to the original so a
quote can be checked.

Channels differ in who writes and why. Support tickets are problems;
reviews are extremes; survey open-ends follow a question that shaped
them; sales notes are secondhand. Say in the readout which channels were
used and what each leaves out.

## How to code it

1. **Write the question first.** "What stops people finishing setup?"
   gets a different code frame from "What do people praise?"
2. **Read a sample before coding anything.** A hundred comments, or
   enough to see the shape. Build the code frame from what's there
   (inductive), not from the team's list of features. Add codes as they
   appear; merge them as the frame settles.
3. **Keep the frame small at the top and specific underneath.** Fewer
   than about twenty top-level themes ("getting data in", "billing"), each
   with specific, actionable codes under it ("import fails on files over
   10 MB"). The specific codes are what the team can fix.
4. **A comment can carry several codes.** Don't force each comment into
   one bucket; most say more than one thing, and the second thing is
   often the useful one.
5. **Note the feeling as well as the theme.** The same theme can be
   praise or a complaint. Record which, per code, not per comment.
6. **Two spreadsheets or one tool.** By hand: one sheet for the code
   frame (code, definition, an example comment), one for the comments
   with a column per code. Tools that suggest themes do the first pass
   faster; the frame still needs a person to merge and name it.
7. **Check it.** Have a colleague code a sample blind and compare. Where
   you disagree, tighten the definition. For an automated pass, compare
   its top themes with a hand-coded sample before trusting it.

## Counting and reading

- Report each theme as a count out of the base ("412 of 3,100 tickets in
  Q3 mention import"), with the period and the channels. Per comment,
  not per customer, unless you can de-duplicate; one customer can write
  ten tickets.
- Trend over time, per theme, is often the finding: a theme that doubled
  since a release matters more than the biggest theme.
- Cross by segment where the data allows (plan, platform, tenure). A
  theme that is small overall and large in one segment is a finding.
- Where a score exists (satisfaction, NPS), look at which themes the low
  scorers mention most. That's "why the score moved", as far as feedback
  can say it.
- A theme's size says how often people wrote about it, not how often it
  happens or how much it matters. Weight it with what else is known
  (analytics, sessions) before it becomes a priority.

## At scale

Pick the way that fits the volume and the stakes.

| Volume | Way | Watch for |
| --- | --- | --- |
| Hundreds | Code by hand, as above | Drift: coders apply the frame differently over time; recheck a sample monthly |
| Thousands, a few channels | A tool for the first pass (keyword or topic extraction), a person to merge and name the themes | The tool finds what it was set to look for; new themes arrive late |
| Tens of thousands, many channels | A tool that builds and updates the frame from the feedback itself | Themes nobody can define; check a sample against the raw comments each round |

Whatever the volume, the readout quotes real comments, with the channel
and date, and `checks-claim-strength.md` applies: a count of mentions is
a count of mentions.

## Worked example

> **Decision.** Why Sparrow's (team messaging) app store rating fell
> from 4.4 to 3.9 over the summer, and what to fix first.
>
> **Question and frame.** "What do people complain about since June, and
> what's new?" Read 150 reviews first; built a frame of 14 top-level
> themes with specific codes under them; coded 1,210 reviews from June
> to September by hand with a tool's suggestions for the first pass; a
> colleague coded 60 blind, agreement checked, two definitions
> tightened.
>
> **Result, as reported.** "Notifications arrive late" rose from 4% of
> reviews in June (9 of 220) to 31% in September (104 of 335), nearly
> all on Android (97 of 104), and 1-star reviews mention it most (71 of
> 118). Per review, not per customer. Reported with what it can't say:
> how many users are affected (reviews come from people who chose to
> write), and why it happens (engineering's logs and three sessions
> with affected users were the next step).

## Pitfalls

- Treating the writers as the users. Say who writes in and who doesn't.
- A code frame made from the feature list, so the data can only confirm
  the team's map of the product.
- One code per comment.
- A percentage of comments reported as a percentage of customers.
- A theme that is really the channel: "can't reach support" from support
  tickets.
- Quoting a comment without the original to check it against.
- Letting a tool's themes stand without reading a sample of what's inside
  each.

## Template

The code frame and the comment sheet above, kept with the study record.
Report counts with `templates-analysis-sheet.md`.

## Basis

S89 (gather feedback in one place with its context; a single word's
meaning depends on the comment around it; inductive coding; several
themes per comment, each with its own sentiment; a hierarchy from broad
themes to specific, actionable ones, under about twenty at the top; the
two-spreadsheet method; keyword extraction produces phrases that still
need merging; have a colleague check a coded sample and compare
automated themes with a hand-coded sample; quantify and visualize by
theme; explain the approach so stakeholders trust it). S90 (methods
ranked by volume: manual coding is flexible but drifts; scores show the
trend but not the cause, "a smoke alarm, not a diagnosis"; sentiment and
topic tools find what they were set to look for; adaptive tools for the
largest volumes. The source is a vendor's guide; its claims about its own
kind of tool were not checked). S1b (coding and themes as in stage 7).
Who writes in and who doesn't, per-customer de-duplication, trend and
segment reading, and the pitfalls: practitioner judgment.

---

Part of Magpie version 2026-11-01, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
