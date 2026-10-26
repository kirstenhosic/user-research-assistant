#!/usr/bin/env python3
"""Assemble the platform adapters from the core.

Usage: python3 tools/build.py

Reads every Markdown file under core/ in a fixed order and writes:

  adapters/generic/system-prompt.md      one prompt for any assistant
  adapters/generic/files/                a flat copy of each core file
  adapters/claude/skills/magpie/         a Claude skill: SKILL.md plus the
                                         core files it points to
  .claude/skills/magpie/                 the same skill, where Claude Code
                                         finds it when this repo is open

ChatGPT and Gemini adapters are added in Phase 4 and will read the same core.
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"
GENERIC = ROOT / "adapters" / "generic"
CLAUDE = ROOT / "adapters" / "claude" / "skills" / "magpie"
CLAUDE_LOCAL = ROOT / ".claude" / "skills" / "magpie"

# Files and folders in reading order. A folder that doesn't exist yet is skipped.
ORDER = [
    "operating.md",
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

GENERIC_HEADER = """# Magpie

You are Magpie, a research companion for user researchers working in industry
with product managers, designers and engineers. Everything below is your
working knowledge. The first section, "How Magpie works", is the set of rules
you follow in every conversation. The rest is what you draw on at each stage.

"""

SKILL_FRONTMATTER = """---
name: magpie
description: Research companion for user researchers. Takes a study from "do we already know this?" through framing, method choice, the plan and the guide, to analysis and a stakeholder-ready report. Use when someone asks for help planning, designing, running or writing up user research, or asks for Magpie by name.
---
"""

SKILL_INTRO = """# Magpie

Follow `operating.md` in every conversation; it's the rules. Read `voice.md`
once for tone. Then open the file for the stage the researcher is at and the
method or template it points to. File names below are relative to this
folder.

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


def flat_name(path: Path) -> str:
    rel = path.relative_to(CORE)
    return "-".join(rel.with_suffix("").parts) + ".md"


def first_line_after_title(path: Path) -> str:
    """The first sentence of the paragraph under a core file's title."""
    lines = path.read_text(encoding="utf-8").splitlines()[1:]
    paragraph: list[str] = []
    for line in lines:
        if line.strip():
            paragraph.append(line.strip())
        elif paragraph:
            break
    text = " ".join(paragraph)
    end = text.find(". ")
    return text if end == -1 else text[: end + 1]


def reset(directory: Path) -> None:
    if directory.exists():
        shutil.rmtree(directory)
    directory.mkdir(parents=True)


def build_generic(files: list[Path]) -> None:
    reset(GENERIC)
    files_dir = GENERIC / "files"
    files_dir.mkdir()

    parts = [GENERIC_HEADER]
    for path in files:
        rel = path.relative_to(CORE)
        text = path.read_text(encoding="utf-8").strip()
        parts.append(f"<!-- core/{rel} -->\n\n{text}\n")
        shutil.copyfile(path, files_dir / flat_name(path))

    (GENERIC / "system-prompt.md").write_text("\n".join(parts), encoding="utf-8")


def build_claude(files: list[Path]) -> None:
    reset(CLAUDE)
    index = []
    for path in files:
        name = flat_name(path)
        shutil.copyfile(path, CLAUDE / name)
        index.append(f"- `{name}`: {first_line_after_title(path)}")

    skill = SKILL_FRONTMATTER + "\n" + SKILL_INTRO + "\n".join(index) + "\n"
    (CLAUDE / "SKILL.md").write_text(skill, encoding="utf-8")

    # The same skill inside the repo's own .claude/ folder, so opening this
    # repo in Claude Code makes Magpie available without copying anything.
    reset(CLAUDE_LOCAL)
    shutil.rmtree(CLAUDE_LOCAL)
    shutil.copytree(CLAUDE, CLAUDE_LOCAL)


def main() -> None:
    files = core_files()
    build_generic(files)
    build_claude(files)
    print(f"Built adapters/generic, adapters/claude and .claude/skills from {len(files)} core file(s):")
    for path in files:
        print(f"  core/{path.relative_to(CORE)}")


if __name__ == "__main__":
    main()
