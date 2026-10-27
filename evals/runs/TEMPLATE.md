# Eval run, [date]

Copy this file to `evals/runs/YYYY-MM-DD.md` and fill it in. The rules
behind each section are in `evals/README.md`, "Running them".

## How it was run

- **Adapter and commit:** [for example, `adapters/skill/magpie/` at abc1234]
- **Assistant and platform:** [for example, Claude Code; Claude.ai; Gemini]
- **How Magpie was started:** [for example, `/magpie` at the start of each session]
- **Answers kept out:** [what the session could not see; how notes or memory were turned off]
- **Loading check failed on purpose:** [which scenario was run without Magpie, and how the check caught it]
- **Model judge:** [model and family]
- **Person judging:** [name or role]
- **Replies saved at:** [private location outside the repo]

## Results

A scenario passes only if all three runs pass. "Loaded" means the reply
opened with the "Magpie is on" line and ended with the status line (and
the trace showed the skill being read, where there is one). A run that
didn't load is void and is run again, not scored.

| Scenario | Run 1 | Run 2 | Run 3 | Loaded (3 of 3?) | Note |
| --- | --- | --- | --- | --- | --- |
| | | | | | |

**Totals:** [N] scenarios pass in all three runs, [N] have a partial, [N] have a fail.

## Person and model judge

| Scenario and run | Model judge | Person | Agree? | Note |
| --- | --- | --- | --- | --- |
| | | | | |

**Agreement:** [N of M]. Replies the model passed and the person failed: [list].

## Fixture studies

| Fixture | Run 1 | Run 2 | Run 3 | Note |
| --- | --- | --- | --- | --- |
| harbor-invites | [traps caught of 11] | | | |
| tally-receipts | [traps caught of 12] | | | |
| sparrow-clean | [false alarms; target 0] | | | |

## What this run does not show

- [Platforms, long conversations, anything else not covered]
