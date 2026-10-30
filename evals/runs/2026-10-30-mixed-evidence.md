# Run: mixed evidence (October 30, 2026)

Scenario `evals/scenarios/mixed-evidence.md`, standard 7.27. Claude Code
(`claude -p`), the skill folder from the PR #72 branch at commit d6b6f4c,
copied into a fresh folder per run. 3 runs, 2 turns each: the setup, then
"use your best judgement, go ahead". Each trace shows Magpie read its
skill files, including the stage 7 file. Judged by a model against the
scenario's Pass and Fail lists, not yet by a person.

## Results

| Pass item | Run 1 | Run 2 | Run 3 |
| --- | --- | --- | --- |
| Two findings, one per group (3 of 3 admins needed help; 5 of 5 team leads cleared alone) | pass | pass | pass |
| Says a few people per group show the groups may differ, not how often | pass (0% to 62% range) | pass ("covers only the three admins tested") | pass (ranges for both groups) |
| Receipt preview: the evidence doesn't settle it, and what would | pass (load time on the shipping build) | pass (load times, the admins' sessions) | pass (load time, asking the admins) |
| Email approvals: people are divided, with each side's reasons | pass | pass | pass |
| Doesn't rate the whole result weak or "mixed" with no reason | pass | pass | pass |

Totals: 3 of 3 pass. No run hit a Fail item.

## Notes

- All three runs added something the scenario didn't ask for: role, team
  size and use of bulk-approve always go together in this sample, so the
  study can't tell which one causes the problem. Each run asked the
  researcher about it.
- Run 2 named all three readings in turn 1, before any drafting.
- The setup gives a summary of the notes, not the notes themselves, so
  every run asked for them first and then worked from the summary, marked
  as an assumption. The evidence check couldn't run without the notes.
- Not tested: real transcripts, Claude.ai or Gemini, a person judging.
