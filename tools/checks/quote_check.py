#!/usr/bin/env python3
"""Check that every quote in a findings file appears in the source material.

Usage: python3 tools/checks/quote_check.py FINDINGS.md SOURCE [SOURCE ...]

FINDINGS.md is the draft findings, readout or report. Each SOURCE is a
transcript or notes file, or a folder of them. A quote is any run of text
inside double quotes (straight or curly) of four or more words and twenty
or more characters.

Matching ignores case, punctuation and whitespace differences, so a quote
that was tidied for readability still matches. A quote that was changed in
substance does not.

Where a quote is credited to a participant on the same line ("..." — P3,
or P3: "..."), the check also confirms the words are that participant's.
Each source file belongs to one participant: the code comes from the file
name (p3.md is P3) or from the first code on its title line. A quote found
only in someone else's transcript, or only in the interviewer's lines, is
flagged as misattributed.

Shorter quoted text is listed as not checked, so a short quote isn't taken
as verified. Exit code 1 if any quote is missing or misattributed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

QUOTE = re.compile(r'["“]([^"“”]+?)["”]')
MIN_CHARS = 20
MIN_WORDS = 4
TITLE_CODE = re.compile(r"^#\s*([A-Za-z]{1,2}\d{1,3})\b")
STEM_CODE = re.compile(r"^[A-Za-z]{1,2}\d{1,3}$")
NUMBERED = re.compile(r"^\s*\d{1,4}\s+(.*)$")


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


def participant_code(path: Path, text: str) -> str | None:
    if STEM_CODE.match(path.stem):
        return path.stem.upper()
    first = text.splitlines()[:1]
    m = TITLE_CODE.match(first[0]) if first else None
    return m.group(1).upper() if m else None


def attribution(findings: str, start: int, end: int, code_re: re.Pattern[str] | None) -> str | None:
    """The participant a quote is credited to on its own line, if any."""
    if code_re is None:
        return None
    line_start = findings.rfind("\n", 0, start) + 1
    line_end = findings.find("\n", end)
    line_end = len(findings) if line_end == -1 else line_end
    rest = findings[end:line_end]
    rest = re.split(r'["“]', rest, maxsplit=1)[0]  # stop at the next quote
    after = code_re.search(rest)
    if after:
        return after.group(1)
    before = code_re.findall(findings[line_start:start])
    return before[-1] if before else None


def speakers(text: str, key: str) -> set[str]:
    """Who speaks the numbered lines that hold the quote on their own."""
    who = set()
    for line in text.splitlines():
        m = NUMBERED.match(line)
        if m and key in normalize(m.group(1)):
            who.add(m.group(1).split(":", 1)[0].strip().lstrip("[").split()[0])
    return who


def source_files(paths: list[str]) -> list[Path]:
    files: list[Path] = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(q for q in p.rglob("*") if q.is_file()))
        elif p.is_file():
            files.append(p)
        else:
            print(f"warning: {raw} not found", file=sys.stderr)
    return files


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print(__doc__)
        return 2

    findings = Path(argv[1]).read_text(encoding="utf-8", errors="replace")
    sources = source_files(argv[2:])
    if not sources:
        print("no source files found")
        return 2

    raw = {s: s.read_text(encoding="utf-8", errors="replace") for s in sources}
    corpus = {s: normalize(text) for s, text in raw.items()}
    owners = {s: participant_code(s, text) for s, text in raw.items()}
    prefixes = sorted({re.match(r"[A-Z]+", c).group(0) for c in owners.values() if c})
    code_re = re.compile(r"\b((?:" + "|".join(prefixes) + r")\d{1,3})\b") if prefixes else None

    quotes = []
    short = []
    for m in QUOTE.finditer(findings):
        text = " ".join(m.group(1).split())
        if len(text.split()) >= MIN_WORDS and len(text) >= MIN_CHARS:
            quotes.append((text, attribution(findings, m.start(), m.end(), code_re)))
        elif text not in short:
            short.append(text)

    if not quotes:
        print("no quotes of four or more words found in the findings")
        report_short(short)
        return 0

    missing = []
    misattributed = []
    for quote, credited in quotes:
        key = normalize(quote)
        found = [s for s, text in corpus.items() if key in text]
        names = ", ".join(s.name for s in found)
        if not found:
            print(f"MISSING  {quote[:60]!r}")
            missing.append(quote)
            continue
        problem = None
        if credited:
            theirs = [s for s in found if owners[s] == credited]
            if not theirs:
                problem = f"credited to {credited}, found in {names}"
            else:
                who = set().union(*(speakers(raw[s], key) for s in theirs))
                if who and credited not in {w.upper() for w in who}:
                    problem = f"credited to {credited}, but spoken by {', '.join(sorted(who))}"
        if problem:
            print(f"WRONG    {quote[:60]!r}  {problem}")
            misattributed.append((quote, problem))
        else:
            print(f"ok       {quote[:60]!r}  in {names}")

    print()
    found_count = len(quotes) - len(missing)
    print(f"{found_count} of {len(quotes)} quotes found in the sources.")
    failed = False
    if missing:
        print("Quotes not found. Check each against the transcript before it goes out:")
        for q in missing:
            print(f"  - {q}")
        failed = True
    if misattributed:
        print("Quotes credited to the wrong person. Fix the code before it goes out:")
        for q, problem in misattributed:
            print(f"  - {q} ({problem})")
        failed = True
    report_short(short)
    return 1 if failed else 0


def report_short(short: list[str]) -> None:
    if short:
        print()
        print("Not checked (under four words or twenty characters). Check any that are quotes by hand:")
        for q in short:
            print(f"  - {q}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
