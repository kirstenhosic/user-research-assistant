#!/usr/bin/env python3
# Part of Magpie, made by Kirsten Hosic
# (https://github.com/kirstenhosic/user-research-assistant). MIT License.
"""Flag personal details left in an output before it's shared.

Usage: python3 tools/checks/personal_details_check.py FILE [FILE ...] [--names "Name, Name"]

FILE is any output meant for other people (a report, a readout deck, a
findings summary, a workshop summary, a persona) as Markdown. The check
flags:

  - email addresses
  - phone numbers (9 to 15 digits, with or without spaces, dots, dashes
    or brackets)
  - social media handles (@name)
  - every name passed with --names: the participants', colleagues' and
    companies' names that Magpie noted in the material, comma-separated

Placeholders such as [name], [company] or [email] are fine. A pass means
none of these were found, not that nobody can be identified: a job title,
a city and a company size together can still point to one person, which
only a reading can catch (core/checks/release.md). Magpie keeps names out
of saved files, so pass them on the command line, never in a file.
Exit code 1 if anything is flagged.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE = re.compile(r"(?<![\w-])\+?\(?\d[\d\s().-]{7,}\d(?![\w-])")
HANDLE = re.compile(r"(?<![\w@])@[A-Za-z0-9_]{2,}")


def digits(s: str) -> int:
    return sum(c.isdigit() for c in s)


def check_line(line: str, names: list[str]) -> list[tuple[str, str]]:
    found = []
    emails = list(EMAIL.finditer(line))
    for m in emails:
        found.append(("email", m.group()))
    blank = EMAIL.sub(" ", line)
    for m in PHONE.finditer(blank):
        if 9 <= digits(m.group()) <= 15:
            found.append(("phone number", m.group().strip()))
    for m in HANDLE.finditer(blank):
        found.append(("handle", m.group()))
    for name in names:
        if re.search(r"(?<!\w)" + re.escape(name) + r"(?!\w)", line, re.I):
            found.append(("name", name))
    return found


def main() -> int:
    ap = argparse.ArgumentParser(description="Flag personal details left in an output.")
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--names", default="", help="comma-separated names to look for")
    args = ap.parse_args()
    names = [n.strip() for n in args.names.split(",") if n.strip()]
    flags = 0
    for path in args.files:
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for kind, text in check_line(line, names):
                flags += 1
                print(f"{path.name} line {i}: {kind} '{text}': replace it with a placeholder such as "
                      f"[{'name' if kind == 'name' else kind.split()[0]}]")
    checked = f"emails, phone numbers, handles and {len(names)} name(s)"
    if flags:
        print(f"\n{flags} personal detail(s) to remove. Checked: {checked}.")
        return 1
    print(f"No personal details found. Checked: {checked}. "
          "A reading is still needed for details that point to one person.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
