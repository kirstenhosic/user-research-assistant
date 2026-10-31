#!/usr/bin/env python3
# Part of Magpie, made by Kirsten Hosic
# (https://github.com/kirstenhosic/user-research-assistant). MIT License.
"""Flag words in findings that claim more than a count can show.

Usage: python3 tools/checks/wording_check.py FILE [FILE ...]

FILE is the draft findings, the report or the readout deck as Markdown. The
check reads every sentence outside quotes and flags:

  - every-or-none words ("all", "always", "never", "everyone", "no one"),
    unless the sentence gives a count
  - cause words ("causes", "drives", "leads to", "because of", "due to",
    "results in"), which need more than interviews or a correlation
  - vague amounts ("most", "many", "some", "a few", "the majority",
    "users want"), unless the sentence gives a count
  - overclaiming words ("proves", "clearly", "obviously", "it's clear
    that"), and "significant" with no test named

Participants' own words are left alone: text inside quote marks and lines
starting with ">" aren't checked. A flag is a prompt to reread the
sentence, not a verdict: "because" in "P3 said it was because of the
deadline" reports a reason someone gave, and that's fine. The word lists
are the ones in core/checks/claim-strength.md, "Words to look for", so a
copy of Magpie with no scripts can do the same check by hand. The idea of
running wording rules as code, not by eye, comes from claim-stress-tester
(Kazakos, 2026, MIT License); this is Magpie's own code. Exit code 1 if
anything is flagged.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RULES = [
    ("every-or-none word", re.compile(
        r"\b(all|always|never|every|everyone|everybody|nobody|no one|none|without exception)\b", re.I),
     True, "give the count, and name who didn't fit"),
    ("cause word", re.compile(
        r"\b(causes?|caused|causing|drives?|drove|driven by|leads? to|led to|results? in|"
        r"resulted in|because of|due to)\b", re.I),
     False, "say what's known (a pattern, what people said) unless a test showed the cause"),
    ("vague amount", re.compile(
        r"\b(most|many|some|a few|several|the majority|majority of|the vast majority|nearly all|"
        r"almost all|almost everyone|users want|customers want|people want)\b", re.I),
     True, "replace with the count"),
    ("overclaiming word", re.compile(
        r"\b(proves?|proven|clearly|obviously|definitely|undeniably|it'?s clear that|it is clear that)\b", re.I),
     False, "use 'suggests', 'supports' or 'is consistent with', or delete"),
]
SIGNIFICANT = re.compile(r"\bsignificant(ly)?\b", re.I)
TEST_NAMED = re.compile(r"(\bp\s*[<=>]|\bt-test|\bchi-square|\bchi square|\banova\b|\bregression\b|"
                        r"\bconfidence interval|\bCI\b|\bstatistical(ly)? test|\bstatistically\b)", re.I)
COUNT = re.compile(r"\b\d+\s+(?:out\s+)?of\s+(?:the\s+)?\d+\b|\b\d+(\.\d+)?\s*%|\bn\s*=\s*\d+", re.I)
QUOTED = re.compile(r"\"(?:[^\"\n]|\n(?![ \t]*\n))*\"|“[^”]*”|‘[^’]*’(?!\w)")
SENTENCE = re.compile(r"(?:[^.!?|\n]|[.!?](?=[^\s|])|\n(?![ \t]*\n))+[.!?]?")


def unquoted(text: str) -> str:
    """The text with quotes and blockquote lines blanked out, keeping line breaks."""
    lines = [("" if line.lstrip().startswith(">") else line) for line in text.split("\n")]
    text = "\n".join(lines)
    return QUOTED.sub(lambda m: " " * len(m.group(0)), text)


def check(path: Path) -> list[str]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    text = unquoted(raw)
    flags = []
    # A sentence may wrap across lines; it ends at . ! ?, a blank line or a table cell edge.
    for sent in SENTENCE.finditer(text):
        s = " ".join(sent.group(0).split())
        if not s or s.startswith("#"):
            continue
        line = raw.count("\n", 0, sent.start() + len(sent.group(0)) - len(sent.group(0).lstrip())) + 1
        has_count = bool(COUNT.search(s))
        for name, rx, count_clears, fix in RULES:
            m = rx.search(s)
            if m and not (count_clears and has_count):
                flags.append(f"line {line}: {name} '{m.group(0)}': {fix}\n    {s[:160]}")
        m = SIGNIFICANT.search(s)
        if m and not TEST_NAMED.search(s):
            flags.append(f"line {line}: '{m.group(0)}' with no test named: name the test, "
                         f"or use 'large', 'clear' or the number\n    {s[:160]}")
    return flags


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 2
    total = 0
    for name in argv[1:]:
        path = Path(name)
        if not path.is_file():
            print(f"warning: {name} not found", file=sys.stderr)
            continue
        flags = check(path)
        total += len(flags)
        print(f"{name}: {len(flags)} to reread")
        for f in flags:
            print(f"  - {f}")
    print()
    if total:
        print("Each flag is a sentence to reread, not an error: keep it if it reports what "
              "someone said or a tested result, and say so in the record.")
        return 1
    print("No wording flags.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
