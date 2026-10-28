# Stage 7: Analyze

Turn raw material into findings that say what the evidence supports, how
strongly, and what cuts against it.

## Goal

A short list of findings, each tied to a research question, each with its
evidence and its strength, and each honest about the participants who don't
fit.

## Inputs

- The study record through stage 6.
- The raw material: transcripts, notes, recordings' timestamps, observer
  sheets, survey exports, diary entries. Pasted or uploaded.
- Partner data gathered along the way.

## Before you build

Ask for whatever on this list isn't already in the study record, the
conversation or files you can reach, in one message, before you build
(`operating.md`, "Gather context before you build").
This list is the floor: add the questions this particular study or task
raises, within the same six.

**Minimum to draft:** the raw material: transcripts, notes, recordings
or responses. Without it there's nothing to analyze, only to imagine.

- The raw material for every session, or a note of which sessions are
  missing and why.
- The participant list with what matters for this study: role, segment
  or company type (such as enterprise or SMB), how long they've used the
  product, any accessibility needs. Quotes are labeled from it.
- Who the target users are, if the plan doesn't say, so each participant's
  fit can be judged: matches, partly, or stand-in (a buyer or admin
  speaking for users). Magpie drafts the fit from the screener for a yes
  (`lenses-confidence-and-priority.md`).
- Other sources on the same topic: past studies, analytics, support
  tickets. "None, this is the first study" is a full answer and counts
  against nothing.
- Sessions that went wrong or should be left out, and why.
- Observer notes or debrief notes, if the team kept them.
- Partner data that arrived since planning.
- The research questions and hypotheses, if they aren't in the record.

**Your turn** (`operating.md`, "Your turn"). If the researcher sat in or
watched the sessions, ask in the same message: "Before I code anything,
what were the two or three patterns that stood out to you?" Write their
answer in the record as the researcher's patterns. Don't use it to code;
it's compared with the themes afterwards (step 7). If they didn't see the
sessions, or say "you do it", skip it.

## What to do

1. **Anchor on the questions.** Re-read the research questions before
   reading the data. Findings answer questions; anything that met the
   evidence bar but answers none of them is tagged "also noticed". It is
   still a finding, with the same evidence, counter-evidence and strength,
   and it still reaches the readout; the tag says it was unexpected, not
   that it matters less.
2. **Screen for participant quality first.** Before coding, drop or flag
   transcripts that look fraudulent or rushed (too clean, too fast, too
   perfectly structured), following the plan's threshold, and note each
   removal in the record. `checks-ai-assisted-research.md`, section 4.
3. **Read everything once before coding.** No themes yet. Note what
   surprised you. If a tool (Magpie included) has already produced a
   summary, use it to decide which transcripts to read closely, not as a
   substitute for reading them.
4. **Code what's there.** Tag each relevant passage with a short label and
   its source: participant code plus line, timestamp or question number.
   Codes describe what people did or said, not what you think it means.
   Tag each code with the kind of evidence: **seen** (watched doing it),
   **past time** (described a real, specific time) or **opinion** (a
   general view, habit or prediction). Where participants differ in role
   (end user, buyer, admin), note each one's role and fit to the target
   users, so a theme that comes only from buyers isn't reported as what
   end users do. Where someone says one thing and does another, code both
   (`lenses-confidence-and-priority.md`).
5. **Group codes into candidate themes.** A theme needs more than one
   participant unless it's a serious single case (a safety issue, a
   blocked task). Each theme carries its receipts from the start: the
   participant codes and locations it rests on.
6. **Check each theme against the people who don't fit.** For every theme,
   list the participants who said or did something different. If you can't
   find any, look harder. Write them into the finding.
7. **Compare with the researcher's patterns.** If they named patterns
   before coding, put them next to the candidate themes: which match,
   which of theirs the coding didn't find, and which themes they didn't
   mention. Say what each gap might mean in a line. A pattern they saw
   that the transcripts don't show may live in what wasn't said; a theme
   they missed may be one they'd want to check. Neither side wins by
   default.
8. **The researcher reviews each theme.** Before you write findings, show
   the candidate themes riskiest first, so the shaky ones get the closest
   look: single-participant themes first, then themes where one person
   supplies most of the evidence, then themes with no one who doesn't fit,
   then themes that confirm a hypothesis. For each theme give the
   statement, the count with the participants behind it, one quote with
   its location, and its risk in a few words. Then list the codes you
   merged and dropped, with why, because that's where an experienced
   researcher will disagree. Ask for a decision on each: "Keep, change,
   split or drop? 'Keep 1 and 3, drop 2, split 4 into...' is a fine
   answer." Every theme needs its own answer. If the reply is a blanket
   "looks good", ask which, if any, they'd change. Write each decision in
   the record's Theme review table. Don't carry a dropped theme into the
   findings, and re-check the evidence for a split one. The review is
   skipped only when the researcher says so about the themes themselves,
   after seeing them ("skip the review", "just write the findings"). A
   "go ahead" or "just draft it" given earlier, to the context questions,
   doesn't skip it. When they do skip it, build the findings, log "themes
   not reviewed by the researcher" under Assumptions and risks, and say so
   in the findings.
9. **Rate strength.** Strong: consistent across most participants or
   statistically reliable. Moderate: a clear pattern with exceptions. Weak:
   few participants or mixed signals. Say the numbers: "6 of 8", never
   "most". Write each count with the people and lines behind it, "3 of 8
   (P1 06, P5 06, P7 06)", so the count can be checked by code instead of
   by trust.
   Then write the confidence line: the count and segments, the fit of the
   people behind it, the kind of evidence, whether other sources agree,
   disagree or there are none yet, and who didn't fit. Opinion-only
   behavior and stand-in-only findings are moderate at most; a source
   that disagrees lowers the label; no other source is neutral
   (`lenses-confidence-and-priority.md`). A gap between what people said
   and what they did is a finding of its own.
10. **Re-judge the rigor.** Look at what actually happened in the
   sessions (no-shows, sessions cut short, flagged participants, a missing
   group, a question that turned out to lead) and lower a strength where
   it weakened the evidence, saying why. Then mark each finding enough for
   this decision, enough with a caveat, or not enough, using the decision
   risk in the record (`lenses-minimum-viable-rigor.md`).
11. **Set the priority.** For each finding, rate impact (on the users who
   hit it and on the decision) and reach (how many target users, how
   often), each with a reason, and read the priority off the grid in
   `lenses-confidence-and-priority.md`. Confidence never moves priority.
   A high-priority finding with weak confidence, or not enough for the
   decision, is marked "check next". Show the findings in priority order
   and ask whether the order matches the researcher's; their order
   stands.
12. **Check the hypotheses.** Once the findings are drafted, say for each
   hypothesis in the record whether the evidence supports it, contradicts
   it or doesn't speak to it, with the findings behind each, and update its
   status. Do this after coding, not before, so the hypotheses don't steer
   what you see.
13. **Look outside the frame.** Some findings point upstream or downstream
   of what was studied, or at another team's piece. Keep them, label the
   cause's location ("starts at import, not export"), and map each finding
   to the journey step and persona it affects, in the team's names
   (`lenses-systems-and-journeys.md`).
14. **Bring in partner data where it applies.** Say whether it agrees,
   disagrees or is silent. Don't merge a telemetry number and an interview
   theme into one claim.
15. **Run the claim-strength check** (`checks-claim-strength.md`) over the
   draft findings.
16. **Run the code checks if you can** (`scripts/`): every quote matches
   its transcript and the person it's credited to; every count's
   arithmetic holds; every count lists as many participants as it claims,
   and each cited line exists and is that participant speaking. Where you
   can't run code, do it by hand and say so.
17. **Run the independent review** (`review-independent-review.md`) once
    the findings are drafted. It's required at this stage. Start it in the
    same reply, without waiting to be asked: where you can start a separate
    agent, start it; where you can't, give the researcher the text to paste
    and say when to bring the result back.
18. **Offer the analysis sheet** (`templates-analysis-sheet.md`) in one
    line once the findings are drafted: an Excel file laid out like the
    note-taking sheet, filled with what each participant said on each
    research question, the findings, the themes and the codes, for the
    researcher to review. Word the offer so a "yes" can't be mistaken for
    the review yes: "Say 'make the sheet' and I'll build it." Every cell
    is a draft; the researcher's decisions on themes stay theirs to fill
    in.

## Survey data

Counts and percentages with the base shown ("41 of 120 respondents, 34%").
Cross-tabs only where each group has enough people. Open-ends coded like
interview data. No significance claims without a test, and even with one, say
what it means in plain words. Say who answered and how that limits the
finding.

When you give a test result, a margin of error or a sample size:

- **Compute it, don't estimate it.** Run the numbers in code where you can,
  and show the inputs (each group's count and base) so the researcher can
  check them. If the group sizes aren't known, say the result is an
  illustration for an assumed split, and ask for the real counts.
- **Compare groups with the margin on the difference.** The margin of error
  on each group's percentage is not the test. With two groups of 100 and
  results near 50%, each group carries about ±10 points, but the gap
  between them carries about ±14.
- **Say what a non-significant result means.** "We can't tell these groups
  apart with this sample", not "it's noise" or "they're the same". A p value
  is not the chance the difference is real.
- **State the assumption behind a sample size.** "To detect a 10-point gap"
  needs a power level (usually 80%) and a significance level (usually 0.05).
  Put both in the same sentence as the number, or leave the number out.
  Don't say "reliably" without them. A sample that only just reaches
  significance for the observed gap has about a 50% chance of detecting it,
  which isn't reliable.

## Usability data

An issue list: task, how many hit it, severity (blocked, slowed, noticed),
how often it would happen in real use, what happened, a quote or clip
reference. Severity is the issue's impact (blocked is high, slowed medium,
noticed low) and sets its priority with reach
(`lenses-confidence-and-priority.md`). Then the patterns across issues.
Five participants are five people, not percentages.

## What to draft

- The Findings section of the study record: claim, supporting evidence
  tagged seen, past time or opinion, contradicting evidence, strength with
  its confidence line, and whether it's enough for the decision.
- The Priority table: impact, reach and priority for each finding, with
  reasons, in the order the researcher agreed or marked as Magpie's draft.
- The "also noticed" findings, for things outside the questions, held to
  the same evidence bar.
- A coding frame (the list of codes with one-line definitions) so a
  teammate could check the work.
- The analysis sheet, if the researcher wants it.
- The theme review: the themes riskiest first, the merged and dropped
  codes, and the researcher's decision on each theme, in the record.

## Challenge

Usually **claim strength**. Example: "Theme 2 is 'people want faster
exports'. P3 and P7 said they never export. Is the theme 'people want faster
exports' or 'the people who export want it faster'?"

## Red flag

A finding stated with more confidence than its evidence carries. Always raise
it.

## Exit criteria

- Every finding answers a research question or is listed as "also noticed".
- Every finding has its evidence, its counter-evidence, a strength label
  and a confidence line.
- Every finding has an impact, a reach and a priority, and the order has
  been shown to the researcher.
- Each finding is marked enough, enough with a caveat, or not enough for
  this decision, judged on what happened in the sessions.
- The researcher kept, changed, split or dropped each theme, or the skip
  is logged as a risk.
- Claim-strength check run.
- Quote and count checks run, by code or by hand.
- Independent review run and each point fixed or answered, and the status
  line shows it as done. If the researcher is running it in another chat
  and hasn't brought it back, it's listed as waiting in the record and the
  status line.

## Pitfalls

- Coding for the themes you expected before reading.
- Dropping the participants who didn't fit.
- "Users want" when three people mentioned it.
- Letting a vivid quote stand in for a pattern.
- Reporting what people said they do as what they do.
- Marking a finding down because no other study exists yet.
- Ranking findings by how sure we are instead of how much they matter.
- A theme that is really the research question restated.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
