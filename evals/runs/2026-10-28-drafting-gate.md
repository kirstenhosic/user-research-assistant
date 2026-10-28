# Eval run, 2026-10-28 (does Magpie draft too early?)

Kirsten asked whether Magpie drafts too much while knowing too little. Ten
asks, before and after the fix: a plan, an interview guide, a survey,
analysis and a readout, each as a bare one-line ask and as a fuller one.

## How it was run

- **Adapter and commit:** `adapters/skill/magpie/` at main 1197414 (after
  PR #50), at 12b47bb (before PR #50), and as built on this branch
- **Assistant and platform:** Claude Code (`claude -p`), in a cloud container
- **How Magpie was started:** `/magpie` plus the ask. Turn 2 was always "I
  don't have answers to those right now. Go ahead with your best
  guesses." On this branch, turn 3 was "yes".
- **Answers kept out:** each run in a fresh folder holding only the skill
  and the input file; memory settings removed; a new session id per run
- **Runs:** two per ask per version (40 before the fix, 20 on the first
  fix), then three each of the four riskiest asks after the "no unseen
  guesses" rule (12)
- **Loading check:** every run read the skill files
- **Model judge:** Claude, the same model family that wrote the change
- **Person judging:** not yet
- **Replies saved at:** the project's shared files, `eval-runs/2026-10-28-drafting-gate/`

## Results

| Version | Runs | Drafted in the reply that asked | Drafted after "go ahead" with a required answer missing | Skipped the theme review |
| --- | --- | --- | --- | --- |
| before PR #50 | 20 | 0 | 6 | 3 of 4 analysis runs |
| main (after PR #50) | 20 | 1 (guide, fuller ask) | 4 (readout and survey, 2 each) | 1 of 4 |
| first fix | 20 | 1 (guide, fuller ask) | 1 (analysis: themes on guessed research questions) | 0 of 4 |
| final fix | 12 | 0 | 0 | 0 of 3 |

On the final fix, every turn 2 was a list of guesses ending "Reply yes, or
fix any line", and every turn 3 built the output (or, at analysis, showed
candidate themes for review, not findings). One first reply had 7
numbered items, over the cap of six.

## Plan in rounds (added after Kirsten chose rounds)

Five more runs on this branch with A.25. A bare plan ask ("Can you make me
a research plan for our new onboarding flow?") was answered round by
round with scripted answers (3 runs). A fuller brief got one scripted
answer and then "yes" (2 runs).

- **Bare ask:** all 3 runs asked in three rounds of six numbered items,
  labelled round 1, 2 and 3 of 3, with no draft before the last round.
  Run 2 built the plan after round 3. Runs 1 and 3 first showed a short
  guess list for two or three answers still missing (who the 8 should
  be, how reversible the decision is, the goal metric), then built on
  "yes". So a plan from a bare ask took four or five replies.
- **Fuller brief:** both runs skipped the framing questions already
  answered and went straight to the gaps, then a "round 2". The scripted
  answers didn't cover the primary question, so Magpie asked again and
  didn't build. That is the gate working; the script, not Magpie, stalled.

## Documents, hypothesis check and before-and-after

Six more runs with A.26, A.27 and 3.10. Three bare plan asks (first reply
only), and three where the researcher shared a one-page PRD plus four
rough research questions and a vague hypothesis, answered round by round.

- **Asking for documents:** all 3 bare first replies had one optional
  item asking for a PRD, brief, past research or analytics, with "I'll
  read it and ask only what it doesn't answer".
- **Reading the PRD:** all 3 PRD runs read it before asking, said what
  they took from it (the decision, the goal, the users) and didn't ask for
  those.
- **Before-and-after:** all 3 showed one table in the round 2 summary,
  three rows in full (questions 1 to 3), the unchanged question 4 named
  as fine, the rest behind "say more". The hypotheses were split into one
  idea each.
- **Length:** round 2 messages ran about 460 to 640 words with the table.
  One run folded round 3's questions into the round 2 message.



Two or three runs per ask is small. Every turn 2 was the same blanket
go-ahead; partial answers weren't tested. Scripts needed approval, so no
Word, Excel or slide files were built. The new scenarios
(`go-ahead-is-not-a-yes`, `go-ahead-keeps-theme-review`, `asks-then-stops`,
`many-guesses`) match these asks but weren't run word for word.
