#!/usr/bin/env python3
"""Check the arithmetic of counts and percentages in a findings file.

Usage: python3 tools/checks/count_check.py FINDINGS.md

Looks for two patterns:

  "6 of 8"            flags N greater than M, and lists every M used so you
                      can spot a sample size that changes between findings
  "41 of 120 (34%)"   recomputes the percentage and flags a mismatch of more
                      than one point
  "34% (41 of 120)"   the same, written the other way round

It also flags a percentage that appears next to a base under 30, since a
rate from a sample that small usually shouldn't be reported as one. Exit
code 1 if anything is flagged.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

N_OF_M = re.compile(r"\b(\d+)\s+(?:out\s+)?of\s+(\d+)\b")
N_OF_M_PCT = re.compile(r"\b(\d+)\s+(?:out\s+)?of\s+(\d+)\b[^.\n]{0,12}?\(\s*(\d+(?:\.\d+)?)\s*%\s*\)")
PCT_N_OF_M = re.compile(r"(\d+(?:\.\d+)?)\s*%\s*\(\s*(\d+)\s+(?:out\s+)?of\s+(\d+)\s*\)")
SMALL_BASE = 30


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2

    text = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []
    bases: Counter[int] = Counter()

    for n, m in N_OF_M.findall(text):
        n, m = int(n), int(m)
        bases[m] += 1
        if n > m:
            problems.append(f"{n} of {m}: the count is larger than the base")

    def check_pct(n: int, m: int, pct: float, shown: str) -> None:
        if m == 0:
            problems.append(f"{shown}: base of zero")
            return
        actual = 100 * n / m
        if abs(actual - pct) > 1:
            problems.append(f"{shown}: {n}/{m} is {actual:.0f}%, not {pct:g}%")
        if m < SMALL_BASE:
            problems.append(
                f"{shown}: a percentage from a base of {m}; say the count instead"
            )

    for n, m, pct in N_OF_M_PCT.findall(text):
        check_pct(int(n), int(m), float(pct), f"{n} of {m} ({pct}%)")
    for pct, n, m in PCT_N_OF_M.findall(text):
        check_pct(int(n), int(m), float(pct), f"{pct}% ({n} of {m})")

    if bases:
        print("Bases used:")
        for m, count in sorted(bases.items()):
            print(f"  {m}: {count} time(s)")
        if len(bases) > 1:
            print("  More than one base. Fine if there are several groups or")
            print("  questions; worth a look if there should be one sample size.")
        print()

    if problems:
        print("Flagged:")
        for p in problems:
            print(f"  - {p}")
        return 1

    print("No arithmetic problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
