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

## Limits

Two or three runs per ask is small. Every turn 2 was the same blanket
go-ahead; partial answers weren't tested. Scripts needed approval, so no
Word, Excel or slide files were built. The new scenarios
(`go-ahead-is-not-a-yes`, `go-ahead-keeps-theme-review`, `asks-then-stops`,
`many-guesses`) match these asks but weren't run word for word.
