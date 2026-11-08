#!/usr/bin/env python3
# Part of Magpie, made by Kirsten Hosic
# (https://github.com/kirstenhosic/user-research-assistant). MIT License.
"""Give a reading receipt for each transcript, and list the lines no code covers.

Usage: python3 tools/checks/coverage_check.py SOURCE [SOURCE ...] [--codes CODING_NOTES.md]

Each SOURCE is a transcript or notes file, or a folder of them. Each file
belongs to one participant: the code comes from the file name (p3.md is P3)
or from the first code on the title line ("# P3, 2026-09-08"). Lines are
numbered at the start ("06 P3: ...").

Without --codes it prints the reading receipt: for each file, how many
numbered lines it has, its last line number and the first words of that
line, and a warning when the file looks cut off (it starts after line 1,
its last line stops without an end mark such as . ? ! or a closing quote,
or its line numbers jump).
Compare the receipt with what was read; a file that ends sooner than the
session did was cut off somewhere.

With --codes it also reads the coding notes, where each code lists its
participant and lines ("P3 12-15, 40" or "P3 (12, 13)"), and lists, for
each participant, the stretches of their own lines that no code cites.
Interviewer lines aren't listed. Each stretch is to look at, not an error:
code it, or say why it's left out (only logistics, such as consent or
screen sharing, should be). Exit code 1 if anything is listed.

It can't tell whether a code fits its lines, or whether the transcript
file itself is complete; the researcher can check the receipt against
their own files.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

TITLE_CODE = re.compile(r"^#\s*([A-Za-z]{1,2}\d{1,3})\b")
STEM_CODE = re.compile(r"^[A-Za-z]{1,2}\d{1,3}$")
NUMBERED = re.compile(r"^\s*(\d{1,4})\s+(.*)$")
RANGE = re.compile(r"\b(\d{1,4})\s*(?:-|–|to)\s*(\d{1,4})\b|\b(\d{1,4})\b")
N_OF_M = re.compile(r"\b\d+\s+(?:out\s+)?of\s+(?:the\s+)?\d+\b")
END_MARK = re.compile(r"[.?!…\"”')\]]\s*$")


def load_sources(paths: list[str]) -> dict[str, tuple[Path, dict[int, str]]]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(q for q in p.rglob("*") if q.is_file()))
        elif p.is_file():
            files.append(p)
        else:
            print(f"warning: {raw} not found", file=sys.stderr)
    sources: dict[str, tuple[Path, dict[int, str]]] = {}
    for f in files:
        lines = f.read_text(encoding="utf-8", errors="replace").splitlines()
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
        sources[code] = (f, numbered)
    return sources


def first_words(text: str, n: int = 6) -> str:
    words = text.split()
    return " ".join(words[:n]) + (" ..." if len(words) > n else "")


def cited_lines(notes: str, code_re: re.Pattern[str]) -> dict[str, set[int]]:
    """Every line each participant code cites in the coding notes."""
    cited: dict[str, set[int]] = {}
    for line in notes.splitlines():
        line = N_OF_M.sub(" ", line)
        matches = list(code_re.finditer(line))
        for i, m in enumerate(matches):
            stop = matches[i + 1].start() if i + 1 < len(matches) else len(line)
            tail = line[m.end():stop]
            got = cited.setdefault(m.group(1).upper(), set())
            for r in RANGE.finditer(tail):
                if r.group(3):
                    got.add(int(r.group(3)))
                else:
                    a, b = int(r.group(1)), int(r.group(2))
                    if a <= b and b - a < 500:
                        got.update(range(a, b + 1))
    return cited


def stretches(numbers: list[int]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    for n in numbers:
        if out and n == out[-1][1] + 1:
            out[-1] = (out[-1][0], n)
        else:
            out.append((n, n))
    return out


def main(argv: list[str]) -> int:
    args = argv[1:]
    codes_file = None
    if "--codes" in args:
        i = args.index("--codes")
        if i + 1 >= len(args):
            print(__doc__)
            return 2
        codes_file = args[i + 1]
        del args[i:i + 2]
    if not args:
        print(__doc__)
        return 2
    sources = load_sources(args)
    if not sources:
        print("no participant files found (expected names like p1.md, or a '# P1' title line)")
        return 2

    order = sorted(sources, key=lambda c: (len(c), c))
    flagged = 0
    print(f"Reading receipt ({len(order)} file(s)):")
    for code in order:
        f, numbered = sources[code]
        if not numbered:
            print(f"  {code} ({f.name}): no numbered lines; number the lines to check it")
            flagged += 1
            continue
        nums = sorted(numbered)
        last = nums[-1]
        notes = []
        if nums[0] > 1:
            notes.append(f"starts at line {nums[0]:02d}; the start may be missing")
        if not END_MARK.search(numbered[last]):
            notes.append("last line stops without an end mark; it may be cut off")
        gaps = [(a, b) for a, b in zip(nums, nums[1:]) if b - a > 1]
        if gaps:
            shown = ", ".join(f"{a:02d} to {b:02d}" for a, b in gaps[:5])
            notes.append(f"line numbers jump ({shown})")
        print(f"  {code}: lines {nums[0]:02d} to {last:02d} ({len(nums)} lines), last: \"{first_words(numbered[last])}\"")
        for n in notes:
            print(f"      - {n}")
            flagged += 1

    if codes_file:
        notes_text = Path(codes_file).read_text(encoding="utf-8", errors="replace")
        prefixes = sorted({re.match(r"[A-Z]+", c).group(0) for c in sources})
        code_re = re.compile(r"\b((?:" + "|".join(prefixes) + r")\d{1,3})\b", re.IGNORECASE)
        cited = cited_lines(notes_text, code_re)
        print()
        print("Coverage (participant lines no code cites):")
        for code in order:
            _, numbered = sources[code]
            own = [n for n in sorted(numbered) if re.match(rf"\[?{code}\b", numbered[n], re.IGNORECASE)]
            if not own:
                print(f"  {code}: no lines spoken by {code} found")
                continue
            missing = [n for n in own if n not in cited.get(code, set())]
            if not missing:
                print(f"  {code}: all {len(own)} of their lines coded")
                continue
            flagged += 1
            spans = ", ".join(f"{a:02d}" if a == b else f"{a:02d}-{b:02d}" for a, b in stretches(missing))
            print(f"  {code}: {len(missing)} of {len(own)} of their lines uncoded: {spans}")
        extra = sorted(set(cited) - set(sources))
        if extra:
            flagged += 1
            print(f"  Codes cite participants with no file: {', '.join(extra)}")

    print()
    if flagged:
        print(f"{flagged} thing(s) to look at. Code each uncoded stretch or say why it's left out,")
        print("and check any file that may be cut off against the original.")
        return 1
    print("Every file ends cleanly" + (" and every participant line is coded." if codes_file else "."))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
