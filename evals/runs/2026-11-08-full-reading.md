# Eval run, November 8, 2026: full reading

## How it was run

- **Adapter and commit:** before: `adapters/skill/magpie/` on main at
  b0c8ddf. After: the same folder on the PR branch at 73f8544.
- **Assistant and platform:** Claude Code (`claude -p`, one session for
  each run, with Python allowed so the scripts could run). Claude.ai and
  Gemini were not tested.
- **How Magpie was started:** `/magpie` at the start of the first message.
- **Answers kept out:** each run had a fresh folder holding only the
  skill and, where needed, the transcripts. Memory was turned off.
- **Model judge:** the same model family that ran Magpie. No person has
  judged these replies yet.
- **Fixtures:** made-up Ledgerline transcripts, written by a script.
  They aren't real participants and they aren't part of the repo. The
  script gave the follow-up answers a few stock sentences. Every run
  noticed this and flagged the transcripts as looking templated, which
  is right, but it adds noise.
- **Replies saved at:** the project's eval-runs folder (private), outside
  the repo.
- **Runs:** two after and one before for each scenario, not three.

## Results

| Scenario | Before | After 1 | After 2 | Loaded | Note |
| --- | --- | --- | --- | --- | --- |
| partial-read | fail | pass | pass | 3 of 3 | Pasted transcripts, with P9 cut off mid-sentence. Before: it caught the cut-off, gave no receipt, and planned to code P9's first half and count on a base of 12. After: both runs gave a receipt table, held the coding, and asked for the rest of P9 or a go-ahead. |
| read-to-the-end | fail | pass | pass | 3 of 3 | P5 has 3,128 lines, with a story at line 3126. Before: it read the first 700 lines, then used grep to filter the rest. It found the story only because the filler was repetitive. After: both runs read P5 in three pages to the last line, ran `coverage_check.py`, and gave P5's real last line in the receipt. |
| uncoded-stretch | pass | pass | pass | 3 of 3 | Each transcript has a long aside. All three runs coded every aside, so the old rule (7.22) already covered this. After: both runs ran the coverage check and wrote the result in the receipt. |

**Totals (after):** 3 scenarios pass in both runs.

## What this doesn't show

- A cut-off the tool makes silently, on Claude.ai or Gemini. Here every
  cut-off was in the file itself, so the model could see it. The receipt
  is there so the researcher can catch the silent kind.
- Whether the results hold across three runs each, or with a person as
  the judge.
- Real transcripts, and long ones that vary from line to line, where a
  grep filter wouldn't work.
