#!/usr/bin/env python3
"""Assemble the platform adapters from the core.

Usage: python3 tools/build.py

Reads every Markdown file under core/ in a fixed order and writes:

  adapters/generic/system-prompt.md      one prompt for any assistant
  adapters/generic/system-prompt-lean.md the rules, stages, lenses and
                                         checks only, for assistants with
                                         a short instruction limit; the
                                         rest is uploaded from files/
  adapters/generic/files/                a flat copy of each core file
  adapters/skill/magpie/                 one skill folder (SKILL.md plus the
                                         core files and scripts it points
                                         to) in the format Claude, ChatGPT
                                         and Gemini all accept
  .claude/skills/magpie/                 the same skill, where Claude Code
                                         finds it when this repo is open

The code checks in tools/checks/ are copied into the skill's scripts/
folder so the skill can run them. The per-platform setup notes in
adapters/claude, adapters/chatgpt, adapters/gemini and adapters/copilot are
written by hand and point at the skill folder.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"
GENERIC = ROOT / "adapters" / "generic"
SKILL = ROOT / "adapters" / "skill" / "magpie"
CLAUDE_LOCAL = ROOT / ".claude" / "skills" / "magpie"

# Files and folders in reading order. A folder that doesn't exist yet is skipped.
# core/standards/ is left out on purpose: the stage files already carry the
# rules, and the standards tables are for maintainers and the evals.
ORDER = [
    "operating.md",
    "voice.md",
    "stages",
    "lenses",
    "evidence",
    "workshops",
    "methods",
    "challenges",
    "checks",
    "review",
    "partners",
    "templates",
    "team",
]

# What the lean generic prompt carries inline. Everything else in ORDER is
# available as an uploaded file.
LEAN = {"operating.md", "voice.md", "stages", "lenses", "evidence", "challenges", "checks", "review"}

REPO_URL = "https://github.com/kirstenhosic/user-research-assistant"

# Who made Magpie. It goes at the top of every built prompt and SKILL.md and
# at the foot of every copied file, so the credit travels with any part of
# Magpie that someone downloads, uploads or pastes on its own.
CREDIT = (
    f"Magpie was made by Kirsten Hosic ({REPO_URL}). "
    "It is released under the MIT License: keep this notice and the license "
    "with any copy."
)

FOOTER = f"\n\n---\n\nPart of Magpie, made by Kirsten Hosic ({REPO_URL}). MIT License.\n"

GENERIC_HEADER = f"""# Magpie

{CREDIT}

You are Magpie, a research companion for user researchers working in industry
with product managers, designers and engineers. Everything below is your
working knowledge, organized by Markdown headings; each `<!-- core/... -->`
line marks the start of one file. The first section, "How Magpie works", is
the set of rules you follow in every conversation, including which of them
the researcher can override. The rest is what you draw on at each stage:
read the section for the current stage before drafting, and the method,
check or template it points to.

"""

LEAN_HEADER = f"""# Magpie

{CREDIT}

You are Magpie, a research companion for user researchers working in industry
with product managers, designers and engineers. This prompt holds your rules
and the stage-by-stage method. The method guides, templates, workshop
patterns, partner request templates and team files are uploaded as separate
files named like `methods-interviews.md` and `templates-study-record.md`;
open the one a stage points to before drafting from it. The first section,
"How Magpie works", is the set of rules you follow in every conversation,
including which of them the researcher can override.

"""

SKILL_FRONTMATTER = """---
name: magpie
description: Research companion for user researchers. Takes a study from "do we already know this?" through framing, method choice, the plan and the guide, to analysis and a stakeholder-ready report. Use when someone asks for help planning, designing, running or writing up user research, or asks for Magpie by name.
---
"""

SKILL_INTRO = f"""# Magpie

{CREDIT}

Follow `operating.md` in every conversation; it's the rules, including which
ones the researcher can override. Once started, Magpie runs for the rest of
the conversation without being called again; `operating.md`, "The session",
says how. Read `voice.md` once for tone. Then open
the file for the stage the researcher is at and the method, check or
template it points to, and work from the file rather than from memory of
it; the specifics live there. File names below are relative to this folder.
`scripts/quote_check.py`, `scripts/count_check.py` and
`scripts/evidence_check.py` are scripts to run, not read: they check quotes,
counts and the receipts behind counts at stages 6 and 7. Run them with
Python when you can and say so when you can't.

"""


def core_files(order: list[str] | None = None) -> list[Path]:
    """Return core files in build order, folders sorted by file name."""
    files: list[Path] = []
    for entry in order or ORDER:
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


# Core files point to each other by their core paths (`methods/interviews.md`).
# In the flat copies those files are named `methods-interviews.md`, so the
# references are rewritten to match, and the code checks live in `scripts/`.
FILE_REF = re.compile(r"`([a-z]+)/([\w.-]+\.md)`")
FOLDER_REF = re.compile(r"`(" + "|".join(e for e in ORDER if not e.endswith(".md")) + r")/`")


def flatten_refs(text: str, scripts: bool) -> str:
    """Rewrite core paths in backticks to the flat names beside them."""

    def file_ref(match: re.Match[str]) -> str:
        folder, name = match.groups()
        if (CORE / folder / name).is_file():
            return f"`{folder}-{name}`"
        return match.group(0)

    text = FILE_REF.sub(file_ref, text)
    text = FOLDER_REF.sub(lambda m: f"the `{m.group(1)}-*.md` files", text)
    if scripts:
        text = text.replace("`tools/checks/`", "`scripts/`")
    return text


def copy_with_credit(path: Path, target: Path, scripts: bool = False) -> None:
    """Copy a core file with flat references, adding the credit footer."""
    text = flatten_refs(path.read_text(encoding="utf-8").rstrip("\n"), scripts)
    target.write_text(text + FOOTER, encoding="utf-8")


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
        copy_with_credit(path, files_dir / flat_name(path))

    (GENERIC / "system-prompt.md").write_text("\n".join(parts), encoding="utf-8")

    lean = [LEAN_HEADER]
    for path in core_files([e for e in ORDER if e in LEAN]):
        rel = path.relative_to(CORE)
        text = path.read_text(encoding="utf-8").strip()
        lean.append(f"<!-- core/{rel} -->\n\n{text}\n")
    (GENERIC / "system-prompt-lean.md").write_text("\n".join(lean), encoding="utf-8")
    shutil.copyfile(ROOT / "LICENSE", GENERIC / "LICENSE")


def build_skill(files: list[Path]) -> None:
    """One skill folder in the SKILL.md format the three platforms share."""
    reset(SKILL)
    index = []
    for path in files:
        name = flat_name(path)
        copy_with_credit(path, SKILL / name, scripts=True)
        index.append(f"- `{name}`: {first_line_after_title(path)}")

    skill = SKILL_FRONTMATTER + "\n" + SKILL_INTRO + "\n".join(index) + "\n"
    (SKILL / "SKILL.md").write_text(skill, encoding="utf-8")
    shutil.copyfile(ROOT / "LICENSE", SKILL / "LICENSE")

    scripts = SKILL / "scripts"
    scripts.mkdir()
    checks = ROOT / "tools" / "checks"
    for script in sorted(checks.glob("*.py")):
        shutil.copyfile(script, scripts / script.name)

    # The same skill inside the repo's own .claude/ folder, so opening this
    # repo in Claude Code makes Magpie available without copying anything.
    if CLAUDE_LOCAL.exists():
        shutil.rmtree(CLAUDE_LOCAL)
    shutil.copytree(SKILL, CLAUDE_LOCAL)


def main() -> None:
    files = core_files()
    build_generic(files)
    build_skill(files)
    print(f"Built adapters/generic, adapters/skill and .claude/skills from {len(files)} core file(s):")
    for path in files:
        print(f"  core/{path.relative_to(CORE)}")


if __name__ == "__main__":
    main()
