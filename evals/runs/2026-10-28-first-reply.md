# Eval run, 2026-10-28 (lighter first reply)

Three scenarios, first reply only, run live after the "one ask per
number", "mark what can wait" and stage 3 fill-in rules were added.

## How it was run

- **Adapter and commit:** `adapters/skill/magpie/` as built on this
  branch, in two rounds: round 1 with the first wording of the rules,
  round 2 after tightening them (one question mark per item, the minimum
  and your-turn first, everything else "(optional)", keep "[the team or
  group]" in the decision line)
- **Assistant and platform:** Claude Code (`claude -p`), in a cloud container
- **How Magpie was started:** `/magpie` plus the scenario setup as the first
  message; only the first reply was scored
- **Answers kept out:** each run in a fresh empty folder holding only the
  skill; memory settings removed from the environment
- **Runs:** two per scenario per round, not the three `evals/README.md`
  asks for, so no scenario can count as a full pass
- **Loading check failed on purpose:** not run this time
- **Model judge:** Claude, the same model family that wrote the change
- **Person judging:** not yet
- **Replies saved at:** the project's shared files, `eval-runs/2026-10-28-first-reply/`

## Results (round 2)

| Scenario | Run 1 | Run 2 | Run 3 | Loaded | Note |
| --- | --- | --- | --- | --- | --- |
| light-first-reply | partial | partial | not run | 2 of 2 | Your-turn as one fill-in with "[the team or group]", optional questions last and labelled, no second ask for who decides. But run 1's first item asks two things (size and start of the drop), run 2's optional items each ask two, and neither offers a best guess |
| your-turn-decision | pass | pass | not run | 2 of 2 | Four parts as one fill-in item, no own guess, no separate "who decides and by when". Run 1 offered a best guess on who the study is about |
| question-message-only | partial | partial | not run | 2 of 2 | Six items, the minimum first, the optional ones labelled. Both still add lines that aren't questions (missing transcripts, the independent review), which the scenario fails |

**Totals:** 0 scenarios pass in three runs (only two were run), 1 passes
in both runs, 2 have a partial.

## Round 1, before tightening

- 3 of 4 framing replies wrote "[who] will decide" instead of "[the team
  or group]".
- Most numbered items still asked two or three things.
- Only 1 of 6 replies put all the optional questions last and labelled.
- Both stage 8 replies added a "two things I noticed" block of challenges
  to the question message.

## Notes

- Round 2 fixed the decision wording (6 of 6) and the optional labels
  (6 of 6), and the stage 8 challenge blocks were gone.
- Questions with two parts are the main thing left, mostly in optional
  items. A third round would show whether "one question mark" holds.
- The question-message-only gap (extra lines that aren't questions) was
  there before this change.
