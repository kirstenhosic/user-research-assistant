#!/usr/bin/env python3
# Part of Magpie, made by Kirsten Hosic
# (https://github.com/kirstenhosic/user-research-assistant). MIT License.
"""Check that every participant count lists the people and lines behind it.

Usage: python3 tools/checks/evidence_check.py FINDINGS.md SOURCE [SOURCE ...]

FINDINGS.md is the draft findings, readout or report. Each SOURCE is a
transcript or notes file, or a folder of them. Each source file belongs to
one participant: the code comes from the file name (p3.md is P3) or, failing
that, from the first code on the title line ("# P3, 2026-09-08").

A count is written with its receipts, in either form:

  3 of 8 (P1 06, P5 06, P7 06)
  3 of 8: P1 (06, 10), P5 (06), P7 (06)

Line numbers are the numbers at the start of each transcript line. For each
"N of M" the check flags:

  - a count over the whole sample (M is the number of participants in the
    sources) with no participant codes after it
  - a list of codes whose length isn't N
  - a code that isn't one of the participants in the sources
  - a cited line that isn't in that participant's transcript
  - a cited line where the participant isn't the one speaking

It can't tell whether a line says what the finding claims; that still needs
reading and the independent review. Counts over a subgroup or a survey base
are checked only when they list codes. Exit code 1 if anything is flagged.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

N_OF_M = re.compile(r"\b(\d+)\s+(?:out\s+)?of\s+(?:the\s+)?(\d+)\b")
LINE_NO = re.compile(r"\b(\d{1,4})\b")
TITLE_CODE = re.compile(r"^#\s*([A-Za-z]{1,2}\d{1,3})\b")
STEM_CODE = re.compile(r"^[A-Za-z]{1,2}\d{1,3}$")
NUMBERED = re.compile(r"^\s*(\d{1,4})\s+(.*)$")
# How far after "N of M" to look for the codes: to the end of the sentence
# (a full stop, then a space and a capital or a quote mark), the end of the
# paragraph, or the end of a table cell. A single line break doesn't end
# it, because Markdown wraps sentences across lines.
SENTENCE_END = re.compile(r"\.\s+(?=[A-Z*>\"“])|\n\s*\n|\|")


def load_sources(paths: list[str]) -> dict[str, dict[int, str]]:
    """Map each participant code to its numbered lines."""
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
        text = f.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        code = None
        if STEM_CODE.match(f.stem):
            code = f.stem.upper()
        elif lines and TITLE_CODE.match(lines[0]):
            code = TITLE_CODE.match(lines[0]).group(1).upper()
        if not code:
            continue
        numbered: dict[int, str] = {}
        for line in lines:
            m = NUMBERED.match(line)
            if m:
                numbered[int(m.group(1))] = m.group(2)
        sources[code] = numbered
    return sources


def receipts(after: str, code_re: re.Pattern[str]) -> list[tuple[str, list[int]]]:
    """Codes and their line numbers in the text after a count, in order."""
    end = SENTENCE_END.search(after)
    span = after[: end.start()] if end else after
    found: list[tuple[str, list[int]]] = []
    matches = list(code_re.finditer(span))
    for i, m in enumerate(matches):
        stop = matches[i + 1].start() if i + 1 < len(matches) else len(span)
        tail = span[m.end():stop]
        # A following "N of M" starts a new count; stop reading lines there.
        nxt = N_OF_M.search(tail)
        if nxt:
            tail = tail[: nxt.start()]
        found.append((m.group(1), [int(n) for n in LINE_NO.findall(tail)]))
    return found


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2

    findings = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    sources = load_sources(argv[2:])
    if not sources:
        print("no participant files found (expected names like p1.md, or a '# P1' title line)")
        return 2

    sample = len(sources)
    # Only the code prefixes the sources use count as codes ("P" for P1 to
    # P8), so question numbers like Q2 or task numbers like T3 aren't read
    # as participants.
    prefixes = sorted({re.match(r"[A-Z]+", c).group(0) for c in sources})
    code_re = re.compile(r"\b((?:" + "|".join(prefixes) + r")\d{1,3})\b")
    problems: list[str] = []
    checked = 0

    counts = list(N_OF_M.finditer(findings))
    for i, m in enumerate(counts):
        n, total = int(m.group(1)), int(m.group(2))
        stop = counts[i + 1].start() if i + 1 < len(counts) else len(findings)
        refs = receipts(findings[m.end():stop], code_re)
        shown = m.group(0)
        if not refs:
            if total == sample:
                problems.append(f"{shown}: no participant codes listed")
            continue
        checked += 1
        codes = list(dict.fromkeys(code for code, _ in refs))
        if len(codes) != n:
            problems.append(f"{shown}: {len(codes)} code(s) listed ({', '.join(codes)}), not {n}")
        for code, lines in refs:
            if code not in sources:
                problems.append(f"{shown}: {code} is not a participant in the sources")
                continue
            for line in lines:
                text = sources[code].get(line)
                if text is None:
                    problems.append(f"{shown}: {code} has no line {line:02d}")
                elif not re.match(rf"\[?{code}\b", text):
                    speaker = text.split(":", 1)[0][:20]
                    problems.append(f"{shown}: {code} line {line:02d} is spoken by {speaker}, not {code}")

    print(f"Participants in the sources: {sample} ({', '.join(sorted(sources, key=lambda c: (len(c), c)))})")
    print(f"Counts with receipts checked: {checked}")
    print()
    if problems:
        print("Flagged:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("Every count matches its receipts.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
