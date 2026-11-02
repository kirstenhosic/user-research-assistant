# Method: card sorting, tree testing and first-click testing

Three methods for information architecture. Card sorting shows how people
group and name things. Tree testing shows whether people can find things in
a proposed structure. First-click testing shows where people go first on
a real page or design, and whether that first move is the right one.

## Use them when

- The question is about structure: navigation, categories, menu labels, how
  a settings area or a help center should be organized.
- Card sorting: you're designing or rethinking a structure.
- Tree testing: you have a structure (or two) and want to know if it
  works, before building any screens.
- First-click testing: there's a page or a design (a wireframe, a mockup,
  a live site) and the question is whether people start in the right
  place for a task.

## Don't use them when

- The structure isn't the problem. If people can find things but the thing
  they find doesn't work, test usability instead.
- There are fewer than about fifteen items to organize. Just ask.

## Sample

- Card sorting: at least fifteen participants. Thirty adds a little
  stability for twice the cost; it's worth it on large projects.
- Tree testing: thirty to fifty per structure for findability rates you can
  compare.
- Recruit people who'd actually use the structure.

## Card sorting shape

- **Open sort:** participants group cards and name the groups. Use it to
  discover the mental model.
- **Closed sort:** you give the group names; participants place cards. A
  tree test usually checks a proposed structure better.
- Avoid hybrid sorts (some groups given, some made); the given groups steer
  people.
- Thirty to fifty cards, written in the users' words, not internal names.
  More than fifty and people tire, and the "miscellaneous" pile grows.
  Don't repeat the same word across cards; people group on the word.
- Usually remote and unmoderated with a sorting tool; a few moderated
  sessions add the "why".

## Tree testing shape

- The structure as a plain text tree, no visual design.
- Eight to twelve tasks: "Where would you go to change your password?"
- Record success, directness (did they go straight there), time, and
  where they went first.
- Test two structures with different people to compare (each person sees
  only one).
- Run it before any layouts or content exist.

## First-click testing shape

- Show a page (a screenshot, a wireframe or the live site) and give one
  task at a time: "Where would you click to find out how much a
  subscription costs?" Start every task from the same home or base
  screen.
- Write the correct first click (or clicks) for each task before the
  test, so observers compare against it.
- Record where each person clicked first and how long they took to click.
  A long pause before the first click is a finding too.
- After each task, ask how confident they are that they went the right
  way, and how easy it was (`methods-usability-testing.md`, "Follow-up
  questions").
- Usually unmoderated, in a tool that collects clicks and draws a heat
  map; a few moderated sessions add the why. Don't tell people it's a
  first-click test.
- Thirty or more per design for rates you can compare, as for tree
  testing. Pilot it first.

The first click predicts the rest: people whose first click was right
finished the task far more often (about 87% against 46% in the figures
the source cites). Analyze it as success per task, plus where the wrong
clicks went; a cluster of wrong first clicks on one element names the
label or layout to fix.

## What makes it good

- Cards and tasks in participants' language.
- Tasks that don't contain the label you're testing.
- Comparing structures with the same tasks.

## Analysis

Card sorting: a similarity matrix (which cards are grouped together how
often), the group names people chose, and the cards that went everywhere
(the ambiguous ones). Tree testing: success and directness per task, the
first-click paths, and the tasks that failed. First-click testing: right
first click per task, time to first click, where the wrong clicks went,
and the confidence ratings next to the result (confident and wrong is the
worst case). Stage 7 covers this.

## Worked example

> **Decision.** How BrightPay (payroll) organizes a settings area that
> has grown to 42 pages. Design decides the structure in a month.
>
> **Research questions.** How do payroll admins group these settings?
> Can they find the eight most-visited ones in the proposed structure?
>
> **Card sort.** 38 cards in admins' words ("who gets paid on which
> day", not "pay schedule config"), open sort, unmoderated, 22
> participants, plus three moderated sessions for the why.
>
> **Result.** Three stable groups (people, money, the company) in 18 of
> 22 sorts; "approvals" went everywhere (placed in five different
> groups). The moderated sessions said why: approvals are about people
> *and* money.
>
> **Tree test.** Two trees (approvals under People; approvals as its own
> top-level item), 40 participants each, ten tasks. "Where would you go
> to let a manager sign off overtime?" Tree B: 34 of 40 succeeded, 29
> directly. Tree A: 21 of 40. Reported as counts with the difference and
> its range; Tree B recommended, with approvals' own section.

## Pitfalls

- Cards that are internal feature names.
- Reading one open sort as "the" structure; it's a map of mental models,
  often several.
- Tree tasks that give away the answer.
- Building screens before tree-testing the structure.
- A first-click task that starts mid-flow, so the navigation never gets
  tested.

## Template

`templates-card-sort-and-tree-test.md`: the card list, the structure and
task list for a tree test, the task list and correct clicks for a
first-click test, and the analysis sheets.

## Basis

Card sorting: S49 (at least fifteen participants, from correlations of
0.75 at five, 0.90 at fifteen and 0.95 at thirty); S50 (open, closed and
hybrid sorts and when to use each; thirty to fifty cards; repeated words;
moderated for the why, unmoderated for numbers; similarity matrix; limits
of the method). Tree testing: S51 (a text-only tree before layouts or
content; tasks that don't give away the answer; success, directness and
first click; one tree per participant when comparing). Definitions: S52.
First-click testing: S91 (what it is; works on a live site, prototype or
wireframe; tasks written as problems; document the correct path; record
the click and the time to it; don't tell people it's a first-click test;
pilot; start each task from the base screen; confidence and ease ratings
after each task; the 87% against 46% figures, credited there to Jeff
Sauro). The tree-testing sample (thirty to fifty) follows S46's
thirty-plus for rates, applied to first-click tests too; the
eight-to-twelve task range and the moderated-for-why line are
practitioner judgment.

---

Part of Magpie version 2026-11-02, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
