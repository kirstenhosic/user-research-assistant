# Code checks

Small scripts that check things a model shouldn't be trusted to check by
eye. Python 3, standard library only. Run them at stage 6 and again on the
readout and report.

| Script | Checks | Run |
| --- | --- | --- |
| `quote_check.py` | Every quote in the findings appears in the transcripts, and in the transcript of the participant it's credited to, in their own lines; lists short quoted text it didn't check | `python3 tools/checks/quote_check.py findings.md transcripts/` |
| `count_check.py` | "N of M" arithmetic, percentage math, percentages from small bases | `python3 tools/checks/count_check.py findings.md` |
| `evidence_check.py` | Every count lists as many participant codes as it claims, every code is a real participant, every cited line exists and is that participant speaking; a whole-sample count with no codes is flagged | `python3 tools/checks/evidence_check.py findings.md transcripts/` |

Inside the skill package they live at `scripts/`, so the same commands are
`python3 scripts/quote_check.py ...` there.

Each transcript file belongs to one participant. The code comes from the
file name (`p3.md` is P3) or from the first code on the title line
(`# P3, 2026-09-08`). Lines are numbered at the start ("06 P1: ..."), and
counts cite them as "3 of 8 (P1 06, P5 06, P7 06)".

What the scripts can't do: tell whether a line means what the finding
says. That still needs reading and the independent review.

Where Magpie can run code (Claude Code, or any assistant with a code tool),
it runs these itself and reports the result. Where it can't, it tells the
researcher to run them, or does the check by hand and says so in the record.

Survey statistics (cross-tabs, tests) are left to the researcher's survey
tool or a notebook for now; a helper may come later.
