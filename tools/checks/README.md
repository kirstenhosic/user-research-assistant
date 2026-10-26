# Code checks

Small scripts that check things a model shouldn't be trusted to check by
eye. Python 3, standard library only. Run them at stage 6 and again on the
readout and report.

| Script | Checks | Run |
| --- | --- | --- |
| `quote_check.py` | Every quote in the findings appears in the transcripts | `python3 tools/checks/quote_check.py findings.md transcripts/` |
| `count_check.py` | "N of M" arithmetic, percentage math, percentages from small bases | `python3 tools/checks/count_check.py findings.md` |

Where Magpie can run code (Claude Code, or any assistant with a code tool),
it runs these itself and reports the result. Where it can't, it tells the
researcher to run them, or does the check by hand and says so in the record.

Survey statistics (cross-tabs, tests) are left to the researcher's survey
tool or a notebook for now; a helper may come later.
