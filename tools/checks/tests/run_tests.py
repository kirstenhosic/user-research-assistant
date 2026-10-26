#!/usr/bin/env python3
"""Fixture tests for the code checks.

Usage: python3 tools/checks/tests/run_tests.py

Runs quote_check.py and count_check.py on a clean fixture (expected to pass)
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
