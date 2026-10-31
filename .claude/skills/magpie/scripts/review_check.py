#!/usr/bin/env python3
# Part of Magpie, made by Kirsten Hosic
# (https://github.com/kirstenhosic/user-research-assistant). MIT License.
"""Label each point of a reviewer's list by whether what it cites exists.

Usage: python3 tools/checks/review_check.py REVIEW.md SOURCE [SOURCE ...]

REVIEW.md is the reviewer's numbered list (the independent review). Each
SOURCE is a transcript or notes file, or a folder of them, named and
numbered the same way as for evidence_check.py: p3.md is P3, and lines start
with their number ("06 P3: ...").

Each point should end with a source line naming what it rests on:

  Source: P3 12, P5 06 and 08
  Source: none (about the draft's wording)

Without a source line, the participant codes and line numbers anywhere in
the point are read instead ("P3 12", "P3 line 12", "P3, lines 12 and 14").

Each point gets one label:

  found      every participant and line it cites is in the material
  lead       it cites no participant, so there's nothing to look up; the
             point may still be right, and needs checking by reading
  not found  it cites a participant or a line that isn't in the material

"found" means the cited lines exist. It doesn't mean the point is right:
whether a line says what the reviewer says it does still needs reading. The
idea of labeling a model's critique by whether its references exist in the
input comes from claim-stress-tester (Kazakos, 2026, MIT License); this is
Magpie's own code. Exit code 1 if any point is "not found".
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TITLE_CODE = re.compile(r"^#\s*([A-Za-z]{1,2}\d{1,3})\b")
STEM_CODE = re.compile(r"^[A-Za-z]{1,2}\d{1,3}$")
NUMBERED = re.compile(r"^\s*(\d{1,4})\s+(.*)$")

# A top-level numbered point: "1. ...", "1) ...", "**1.** ..." at the start of a line.
POINT = re.compile(r"^\s{0,3}(?:\*\*)?(\d{1,3})[.)](?:\*\*)?\s+", re.MULTILINE)
SOURCE_LINE = re.compile(r"(?:\*\*)?\bSources?(?:\*\*)?\s*:(?:\*\*)?\s*(.*)", re.IGNORECASE)
# Line numbers after a code: "12", "line 12", "lines 12 and 14", "12, 14", "12-14".
LINES_AFTER = re.compile(
    r"^[\s,(]*(?:lines?\s+)?(\d{1,4}(?:\s*(?:,|and|&|-|–|to)\s*(?:lines?\s+)?\d{1,4})*)",
    re.IGNORECASE,
)


def load_sources(paths: list[str]) -> dict[str, dict[int, str]]:
    """Map each participant code to its numbered lines (same rules as evidence_check.py)."""
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(q for q in p.rglob("*") if q.is_file()))
        elif p.is_file():
            files.append(p)
        else:
            print(f"warning: {raw} not found", file=sys.stderr)
    sources: dict[str, dict[int, str]] = {}
    for f in files:
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
        code = None
        if STEM_CODE.match(f.stem):
            code = f.stem.upper()
        elif lines and TITLE_CODE.match(lines[0]):
            code = TITLE_CODE.match(lines[0]).group(1).upper()
        if not code:
            continue
        sources[code] = {int(m.group(1)): m.group(2) for line in lines if (m := NUMBERED.match(line))}
    return sources


def split_points(text: str) -> list[tuple[str, str]]:
    """The review's numbered points as (number, text)."""
    marks = list(POINT.finditer(text))
    points = []
    for i, m in enumerate(marks):
        stop = marks[i + 1].start() if i + 1 < len(marks) else len(text)
        points.append((m.group(1), text[m.end():stop].strip()))
    return points


def citations(text: str, code_re: re.Pattern[str]) -> list[tuple[str, list[int]]]:
    """Participant codes in the text, each with the line numbers right after it."""
    found = []
    for m in code_re.finditer(text):
        tail = LINES_AFTER.match(text[m.end():])
        lines: list[int] = []
        if tail:
            # A range ("12-14") checks both ends.
            lines = [int(n) for n in re.findall(r"\d{1,4}", tail.group(1))]
        found.append((m.group(1).upper(), lines))
    return found


def label(point: str, sources: dict[str, dict[int, str]], code_re: re.Pattern[str]) -> tuple[str, list[str]]:
    src = SOURCE_LINE.findall(point)
    scope = src[-1] if src else point
    cited = citations(scope, code_re)
    if not cited:
        return "lead", ["cites no participant"]
    notes, missing = [], False
    for code, lines in cited:
        if code not in sources:
            notes.append(f"{code} is not a participant in the material")
            missing = True
            continue
        if not lines:
            notes.append(f"{code} (person only, no line given)")
            continue
        for line in lines:
            if line in sources[code]:
                notes.append(f"{code} {line:02d}")
            else:
                notes.append(f"{code} has no line {line:02d}")
                missing = True
    return ("not found" if missing else "found"), list(dict.fromkeys(notes))


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2

    review = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    sources = load_sources(argv[2:])
    if not sources:
        print("no participant files found (expected names like p1.md, or a '# P1' title line)")
        return 2
    points = split_points(review)
    if not points:
        print("no numbered points found in the review")
        return 2

    prefixes = sorted({re.match(r"[A-Z]+", c).group(0) for c in sources})
    code_re = re.compile(r"\b((?:" + "|".join(prefixes) + r")\d{1,3})\b", re.IGNORECASE)

    results = [(num, *label(text, sources, code_re)) for num, text in points]
    tally = {k: sum(1 for _, lab, _ in results if lab == k) for k in ("found", "lead", "not found")}
    print(f"Participants in the material: {len(sources)} ({', '.join(sorted(sources, key=lambda c: (len(c), c)))})")
    print(f"Review points: {len(results)} (found {tally['found']}, lead {tally['lead']}, not found {tally['not found']})")
    print()
    for num, lab, notes in results:
        print(f"{num}. {lab}: {'; '.join(notes)}")
    print()
    print("found = the cited lines exist; read them to judge the point. "
          "lead = nothing cited to look up; check it by reading. "
          "not found = a citation isn't in the material; don't act on the point as stated.")
    return 1 if tally["not found"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
