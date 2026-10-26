#!/usr/bin/env python3
"""Check that every quote in a findings file appears in the source material.

Usage: python3 tools/checks/quote_check.py FINDINGS.md SOURCE [SOURCE ...]

FINDINGS.md is the draft findings, readout or report. Each SOURCE is a
transcript or notes file, or a folder of them. A quote is any run of text
inside double quotes (straight or curly) of twenty or more characters.

Matching ignores case, punctuation and whitespace differences, so a quote
that was tidied for readability still matches. A quote that was changed in
substance does not. Exit code 1 if any quote is missing.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

QUOTE = re.compile(r'["“]([^"“”]{20,}?)["”]')
MIN_WORDS = 4


def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    return " ".join(text.split())


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

    corpus = {
        s: normalize(s.read_text(encoding="utf-8", errors="replace")) for s in sources
    }

    quotes = [q.strip() for q in QUOTE.findall(findings)]
    quotes = [q for q in quotes if len(q.split()) >= MIN_WORDS]
    if not quotes:
        print("no quotes of four or more words found in the findings")
        return 0

    missing = []
    for quote in quotes:
        key = normalize(quote)
        found = [s.name for s, text in corpus.items() if key in text]
        if found:
            print(f"ok       {quote[:60]!r}  in {', '.join(found)}")
        else:
            print(f"MISSING  {quote[:60]!r}")
            missing.append(quote)

    print()
    print(f"{len(quotes) - len(missing)} of {len(quotes)} quotes found in the sources.")
    if missing:
        print("Quotes not found. Check each against the transcript before it goes out:")
        for q in missing:
            print(f"  - {q}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
