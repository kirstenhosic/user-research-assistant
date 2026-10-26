#!/usr/bin/env python3
"""Assemble the platform adapters from the core.

Usage: python3 tools/build.py

Reads every Markdown file under core/ in a fixed order and writes:

  adapters/generic/system-prompt.md   one prompt for any assistant
  adapters/generic/files/             a copy of each core file, flattened

Platform-specific adapters (Claude, ChatGPT, Gemini) are added in later
phases and will read the same core.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"
OUT = ROOT / "adapters" / "generic"

# Folders in reading order. A folder that doesn't exist yet is skipped.
ORDER = [
    "voice.md",
    "stages",
    "workshops",
    "methods",
    "standards",
    "challenges",
    "checks",
    "partners",
    "templates",
    "team",
]

HEADER = """# Magpie

You are Magpie, a research companion for user researchers working in industry with
product managers, designers and engineers. You help take a study from
"do we already know this?" to a stakeholder-ready report, one stage at a time.

Everything below is your working knowledge. Follow it in this order:

1. Find out which stage the researcher is at, or start at stage 1.
2. Draft first, then offer one challenge about the draft. The researcher can
   answer it, say it's handled, or skip it. A skip goes in the study record as
   a risk.
3. Keep the study record current and say what changed in it.
4. End every reply by naming the next step and what you need for it.
5. Use plain language. Never invent sources, numbers or quotes. Label every
   claim by where it came from: the researcher's data, partner data, general
   practice, or an assumption.

"""


def core_files() -> list[Path]:
    """Return core files in build order, folders sorted by file name."""
    files: list[Path] = []
    for entry in ORDER:
        path = CORE / entry
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(sorted(p for p in path.glob("*.md")))
    return files


def build_generic(files: list[Path]) -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    files_dir = OUT / "files"
    files_dir.mkdir(parents=True)

    parts = [HEADER]
    for path in files:
        rel = path.relative_to(CORE)
        text = path.read_text(encoding="utf-8").strip()
        parts.append(f"<!-- core/{rel} -->\n\n{text}\n")
        flat_name = "-".join(rel.with_suffix("").parts) + ".md"
        shutil.copyfile(path, files_dir / flat_name)

    (OUT / "system-prompt.md").write_text("\n".join(parts), encoding="utf-8")


def main() -> None:
    files = core_files()
    build_generic(files)
    print(f"Built adapters/generic from {len(files)} core file(s):")
    for path in files:
        print(f"  core/{path.relative_to(CORE)}")


if __name__ == "__main__":
    main()
