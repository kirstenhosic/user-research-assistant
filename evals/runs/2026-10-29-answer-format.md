# Run: answering in any format (2026-10-29)

Claude Code, one session per case, judged by a model (not yet by a
person). Raw transcripts are kept outside the repo.

## Before the change (main c92a5dc)

Four sessions opened with "Hi Magpie, can you help me with a study? I'm
starting from scratch and want help understanding market needs." The
second message gave the same Vault facts four ways: numbered to match,
one paragraph, labeled lines, and wrong, nested numbers. The third was
"All looks good". Three earlier sessions from the asks re-run were
re-read for the same blanket reply.

- All four answer formats were understood (4 of 4). With wrong numbers,
  Magpie matched by meaning but didn't say so.
- "All looks good" was handled differently each time. Only 1 of the 6
  runs where it applied asked what it covered. The others counted it as
  yes to guesses and the review, dropped optional questions, and once
  counted it as answering an open "which should I add or drop?"
  question.
- Required and optional were marked three different ways. One number held
  two asks, and in one run the challenge and the review ask sat below
  the list.

## After the change (this branch)

Six sessions, the same opener; turn 2 in the four formats plus two runs
with nested numbering; turn 3 "All looks good"; turn 4, for three
sessions, a normal answer.

| Check | Result |
| --- | --- |
| "Answer in any order..." line in the first questions section | 6 of 6 |
| Every item ends "(required)" or "(optional)" | 6 of 6 sessions, every reply |
| Reply opens with what Magpie took the last reply to mean | 6 of 6 at turn 2, 6 of 6 at turn 3, 3 of 3 at turn 4 |
| Re-matched numbers named | 2 of 2 nested-number runs; one matched "3. yes please" to the wrong item, but said so and asked to be corrected |
| "All looks good": open questions and challenge stay open | 6 of 6 |
| "All looks good": skipped optional questions named | 6 of 6 where one was open |
| Your-turn ask uses labeled lines, no sub-list | 5 of 5 where it appeared |
| "Answer in any order..." line not repeated in an ordinary reply | 0 of 4 on the first wording; 3 of 3 after the rule was tightened |

Still seen: a few items pair two asks in one number (rule A.10 and
"One ask per number" were already there), one reply explained the
blanket-reply rule inside the how-to-answer line, and one reply kept
"Reviews: none needed yet" in the status line before stage 6.
