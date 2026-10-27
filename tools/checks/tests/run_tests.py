#!/usr/bin/env python3
"""Fixture tests for the code checks.

Usage: python3 tools/checks/tests/run_tests.py

Runs quote_check.py, count_check.py and evidence_check.py on a clean fixture (expected to pass)
and a planted fixture (expected to fail on known lines). Exit 1 if any
expectation is missed, so tools/check.py can call this.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECKS = HERE.parent
PY = sys.executable
FIXTURES = HERE.parent.parent.parent / "evals" / "fixtures"
HARBOR = FIXTURES / "harbor-invites"
TALLY = FIXTURES / "tally-receipts"
SPARROW = FIXTURES / "sparrow-clean"

CASES = [
    # (name, command, expected exit code, substrings expected in output)
    ("quote_check clean", [PY, str(CHECKS / "quote_check.py"), "findings-clean.md", "transcripts"], 0,
     ["2 of 2 quotes found"]),
    ("quote_check planted", [PY, str(CHECKS / "quote_check.py"), "findings-planted.md", "transcripts"], 1,
     ["MISSING", "deleted my columns", "1 of 2 quotes found"]),
    ("count_check clean", [PY, str(CHECKS / "count_check.py"), "findings-clean.md"], 0,
     ["No arithmetic problems found"]),
    ("count_check planted", [PY, str(CHECKS / "count_check.py"), "findings-planted.md"], 1,
     ["9 of 8: the count is larger than the base", "3/10 is 30%, not 40%", "base of 10"]),
    ("quote_check attribution", [PY, str(CHECKS / "quote_check.py"), "quote-attribution.md", "transcripts"], 1,
     ["credited to P2, found in p1.md", "credited to P1, but spoken by Interviewer", "Not checked", "Every time?"]),
    ("quote_check placeholder", [PY, str(CHECKS / "quote_check.py"), "quote-placeholder.md", "transcripts"], 1,
     ["placeholder gap allowed", "signs off every file", "I rename it by hand", "1 of 3 quotes found"]),
    ("evidence_check clean", [PY, str(CHECKS / "evidence_check.py"), "evidence-clean.md", "transcripts"], 0,
     ["Every count matches its receipts"]),
    ("evidence_check planted", [PY, str(CHECKS / "evidence_check.py"), "evidence-planted.md", "transcripts"], 1,
     ["2 of 2: 1 code(s) listed (P1), not 2", "P3 is not a participant", "P1 has no line 40",
      "P2 line 09 is spoken by Interviewer", "2 of 2: no participant codes listed"]),
    # The fixture studies in evals/fixtures/ carry planted quote and count
    # problems; the code checks must catch the ones they can.
    ("quote_check harbor-invites", [PY, str(CHECKS / "quote_check.py"), str(HARBOR / "draft-findings.md"),
                                    str(HARBOR / "transcripts")], 1,
     ["MISSING", "Invites should be per board", "2 of 3 quotes found", "credited to P3, found in p1.md"]),
    ("count_check harbor-invites", [PY, str(CHECKS / "count_check.py"), str(HARBOR / "draft-findings.md")], 1,
     ["6/8 is 75%, not 80%"]),
    ("quote_check tally-receipts", [PY, str(CHECKS / "quote_check.py"), str(TALLY / "draft-readout-summary.md"),
                                    str(TALLY / "sessions")], 1,
     ["MISSING", "read the four as a one", "2 of 3 quotes found"]),
    ("count_check tally-receipts", [PY, str(CHECKS / "count_check.py"), str(TALLY / "draft-readout-summary.md")], 1,
     ["a percentage from a base of 6"]),
    ("evidence_check harbor-invites", [PY, str(CHECKS / "evidence_check.py"), str(HARBOR / "draft-findings.md"),
                                       str(HARBOR / "transcripts")], 1,
     ["7 of 8: no participant codes listed", "6 of 8: no participant codes listed"]),
    ("evidence_check tally-receipts", [PY, str(CHECKS / "evidence_check.py"), str(TALLY / "draft-readout-summary.md"),
                                       str(TALLY / "sessions")], 1,
     ["5 of 6: no participant codes listed", "4 of 6: no participant codes listed"]),
    # The clean fixture has no planted problems; every check must pass it.
    ("quote_check sparrow-clean", [PY, str(CHECKS / "quote_check.py"), str(SPARROW / "draft-findings.md"),
                                   str(SPARROW / "transcripts")], 0, ["2 of 2 quotes found"]),
    ("count_check sparrow-clean", [PY, str(CHECKS / "count_check.py"), str(SPARROW / "draft-findings.md")], 0,
     ["No arithmetic problems found"]),
    ("evidence_check sparrow-clean", [PY, str(CHECKS / "evidence_check.py"), str(SPARROW / "draft-findings.md"),
                                      str(SPARROW / "transcripts")], 0, ["Every count matches its receipts"]),
]


def main() -> int:
    failures = 0
    for name, cmd, want_code, want_text in CASES:
        run = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True)
        out = run.stdout + run.stderr
        problems = []
        if run.returncode != want_code:
            problems.append(f"exit {run.returncode}, expected {want_code}")
        for s in want_text:
            if s not in out:
                problems.append(f"missing text: {s!r}")
        status = "ok  " if not problems else "FAIL"
        print(f"{status} {name}")
        for p in problems:
            print(f"      {p}")
        failures += bool(problems)
    print(f"\n{len(CASES) - failures} of {len(CASES)} check fixtures passed.")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
