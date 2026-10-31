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
  magpie.zip                             the skill folder's contents, zipped
                                         with SKILL.md at the top, for people
                                         who download Magpie and upload it
  magpie-gemini.zip                      the same without scripts/, for
                                         Gemini, which won't load a skill
                                         that carries code
  magpie-copilot.zip                     the same without scripts/ and with
                                         the files combined into 20 or
                                         fewer, for Copilot Cowork

The code checks in tools/checks/ are copied into the skill's scripts/
folder so the skill can run them. The per-platform setup notes in
adapters/claude, adapters/chatgpt, adapters/gemini and adapters/copilot are
written by hand and point at the skill folder.
"""

from __future__ import annotations

import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"
GENERIC = ROOT / "adapters" / "generic"
SKILL = ROOT / "adapters" / "skill" / "magpie"
CLAUDE_LOCAL = ROOT / ".claude" / "skills" / "magpie"
ZIP = ROOT / "magpie.zip"
GEMINI_ZIP = ROOT / "magpie-gemini.zip"
COPILOT_ZIP = ROOT / "magpie-copilot.zip"

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

# Magpie's version is the date of the newest changelog entry, so a researcher
# can ask which version they have and compare it with docs/CHANGELOG.md.
_dates = re.findall(r"^## (\d{4}-\d{2}-\d{2})$", (ROOT / "docs" / "CHANGELOG.md").read_text(encoding="utf-8"), re.M)
if not _dates:
    raise SystemExit("docs/CHANGELOG.md has no '## YYYY-MM-DD' heading to take the version from")
VERSION = _dates[0]

# Who made Magpie. It goes at the top of every built prompt and SKILL.md and
# at the foot of every copied file, so the credit travels with any part of
# Magpie that someone downloads, uploads or pastes on its own.
CREDIT = (
    f"Magpie version {VERSION}. "
    f"Magpie was made by Kirsten Hosic ({REPO_URL}). "
    "It is released under the MIT License: keep this notice and the license "
    "with any copy."
)

FOOTER = f"\n\n---\n\nPart of Magpie version {VERSION}, made by Kirsten Hosic ({REPO_URL}). MIT License.\n"

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
patterns, partner request templates, team files and the source list
(`sources.md`) are uploaded as separate files named like
`methods-interviews.md` and `templates-study-record.md`;
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

If asked which version this is, give the date above and follow
`operating.md`, "Which version this is". If another Magpie skill is
installed, tell the researcher they have two copies and should keep only
the newer one.

Follow `operating.md` in every conversation; it's the rules, including which
ones the researcher can override. Once started, Magpie runs for the rest of
the conversation without being called again; `operating.md`, "The session",
says how. Read `voice.md` once for tone. Then open
the file for the stage the researcher is at and the method, check or
template it points to, and work from the file rather than from memory of
it; the specifics live there. File names below are relative to this folder.
`scripts/quote_check.py`, `scripts/count_check.py` and
`scripts/evidence_check.py` are scripts to run, not read: they check quotes,
counts and the receipts behind counts at stages 7 and 8.
`scripts/md_to_docx.py` turns a Markdown output into a Word file and
`scripts/make_sheet.py` builds the note-taking and analysis sheets as Excel
files, for the team to edit together (`operating.md`, "Files for the
team"). Run them with Python when you can and say so when you can't.

"""


# The source codes in core files (S42) point to rows in docs/PROVENANCE.md,
# which isn't part of what people download. The build turns that table into
# sources.md (code, authors, year, title, link) and points the files at it,
# so the people behind each rule are credited wherever Magpie runs.
PROVENANCE = ROOT / "docs" / "PROVENANCE.md"
SOURCE_ROW = re.compile(r"^\|\s*(S\d+[a-z]?)\s*\|\s*(.*?)\s*\|", re.M)
PROVENANCE_REF = "`docs/PROVENANCE.md`"
SOURCES_REF = "`sources.md`"


def sources_text() -> str:
    """The source list from docs/PROVENANCE.md, one line per source."""
    rows = SOURCE_ROW.findall(PROVENANCE.read_text(encoding="utf-8"))
    lines = [f"- **{sid}**: {source}" for sid, source in rows]
    return (
        "# Sources\n\n"
        "The published work Magpie's rules draw on, with the people who wrote it. "
        "A code such as S42 in any Magpie file points to a line here. When you "
        "pass a rule on, credit the authors named here. The full record, with "
        "what each source supports and when it was checked, is "
        f"docs/PROVENANCE.md in the Magpie repository ({REPO_URL}).\n\n"
        + "\n".join(lines)
    )


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
    all_lines = path.read_text(encoding="utf-8").splitlines()
    lines = all_lines[1:]
    paragraph: list[str] = []
    for line in lines:
        if line.strip():
            paragraph.append(line.strip())
        elif paragraph:
            break
    text = " ".join(paragraph)
    # A template that opens with its document details table or a metadata
    # line has no sentence to borrow, so it's described by its title.
    title = all_lines[0].lstrip("# ").split(":")[0].strip()
    named = f"The {title[0].lower() + title[1:]} template."
    if text.startswith(("|", "**")):
        return named
    end = text.find(". ")
    sentence = text if end == -1 else text[: end + 1]
    # A sentence this short ("Two minutes to read.") says nothing on its own.
    short = len(sentence) < 30 and path.parent.name == "templates"
    return f"{named} {sentence}" if short else sentence


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

    text = FILE_REF.sub(file_ref, text).replace(PROVENANCE_REF, SOURCES_REF)
    text = FOLDER_REF.sub(lambda m: f"the `{m.group(1)}-*.md` files", text)
    if scripts:
        text = text.replace("`tools/checks/`", "`scripts/`")
        text = text.replace("`tools/export/md_to_docx.py`", "`scripts/md_to_docx.py`")
        text = text.replace("`tools/export/make_sheet.py`", "`scripts/make_sheet.py`")
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
        text = path.read_text(encoding="utf-8").strip().replace(PROVENANCE_REF, SOURCES_REF)
        parts.append(f"<!-- core/{rel} -->\n\n{text}\n")
        copy_with_credit(path, files_dir / flat_name(path))
    sources = sources_text()
    parts.append(f"<!-- sources.md -->\n\n{sources}\n")
    (files_dir / "sources.md").write_text(sources + FOOTER, encoding="utf-8")

    (GENERIC / "system-prompt.md").write_text("\n".join(parts), encoding="utf-8")

    lean = [LEAN_HEADER]
    for path in core_files([e for e in ORDER if e in LEAN]):
        rel = path.relative_to(CORE)
        text = path.read_text(encoding="utf-8").strip().replace(PROVENANCE_REF, SOURCES_REF)
        lean.append(f"<!-- core/{rel} -->\n\n{text}\n")
    (GENERIC / "system-prompt-lean.md").write_text("\n".join(lean), encoding="utf-8")
    shutil.copyfile(ROOT / "LICENSE", GENERIC / "LICENSE.txt")


def build_skill(files: list[Path]) -> None:
    """One skill folder in the SKILL.md format the three platforms share."""
    reset(SKILL)
    index = []
    for path in files:
        name = flat_name(path)
        copy_with_credit(path, SKILL / name, scripts=True)
        index.append(f"- `{name}`: {first_line_after_title(path)}")
    (SKILL / "sources.md").write_text(sources_text() + FOOTER, encoding="utf-8")
    index.append("- `sources.md`: The published work Magpie's rules draw on, by code (S42), with authors, year, title and link.")

    skill = SKILL_FRONTMATTER + "\n" + SKILL_INTRO + "\n".join(index) + "\n"
    (SKILL / "SKILL.md").write_text(skill, encoding="utf-8")
    # Gemini refuses a skill upload with any file that has no extension,
    # so the license goes in as LICENSE.txt.
    shutil.copyfile(ROOT / "LICENSE", SKILL / "LICENSE.txt")

    scripts = SKILL / "scripts"
    scripts.mkdir()
    checks = ROOT / "tools" / "checks"
    for script in sorted(checks.glob("*.py")) + sorted((ROOT / "tools" / "export").glob("*.py")):
        shutil.copyfile(script, scripts / script.name)

    # The same skill inside the repo's own .claude/ folder, so opening this
    # repo in Claude Code makes Magpie available without copying anything.
    if CLAUDE_LOCAL.exists():
        shutil.rmtree(CLAUDE_LOCAL)
    shutil.copytree(SKILL, CLAUDE_LOCAL)


SCRIPTS_PARAGRAPH = """`scripts/quote_check.py`, `scripts/count_check.py` and
`scripts/evidence_check.py` are scripts to run, not read: they check quotes,
counts and the receipts behind counts at stages 7 and 8.
`scripts/md_to_docx.py` turns a Markdown output into a Word file and
`scripts/make_sheet.py` builds the note-taking and analysis sheets as Excel
files, for the team to edit together (`operating.md`, "Files for the
team"). Run them with Python when you can and say so when you can't.
"""

NO_SCRIPTS_PARAGRAPH = """This copy has no scripts. Do the quote, count and evidence checks at
stages 7 and 8 by hand and say so in the record. For Word or Excel files,
use the tool's own way to make them if it has one, or give the formatted
draft to copy in.
"""


def gemini_files() -> dict[str, bytes]:
    """The skill folder without scripts/, as name -> contents.

    Gemini refuses to load a skill that carries code ("contains executable
    components that aren't supported"), and then answers without Magpie's
    rules. Found on a free account on 2026-10-30.
    """
    files = {}
    for path in sorted(p for p in SKILL.rglob("*") if p.is_file()):
        name = path.relative_to(SKILL).as_posix()
        if name.startswith("scripts/"):
            continue
        data = path.read_bytes()
        if name == "SKILL.md":
            text = data.decode("utf-8")
            if SCRIPTS_PARAGRAPH not in text:
                raise SystemExit("SKILL.md no longer has the scripts paragraph; update gemini_files()")
            data = text.replace(SCRIPTS_PARAGRAPH, NO_SCRIPTS_PARAGRAPH).encode("utf-8")
        files[name] = data
    return files


# Copilot Cowork's help gives two limits for a skill: "up to 20 companion
# files" (Use Cowork) and "up to 100 files" per archive (Customize Cowork),
# both updated 2026-10-21. The skill folder has more than 70 files, so the
# Copilot copy combines them to fit the lower one. Each rule maps a file
# name prefix to the combined file it goes in; methods and templates are
# split by first letter so no combined file gets too long.
COPILOT_BUNDLES = [
    ("stages-01-", "stages-1-to-4.md"),
    ("stages-02-", "stages-1-to-4.md"),
    ("stages-03-", "stages-1-to-4.md"),
    ("stages-04-", "stages-1-to-4.md"),
    ("stages-05-", "stages-5-and-6.md"),
    ("stages-06-", "stages-5-and-6.md"),
    ("stages-07-", "stages-7-and-8.md"),
    ("stages-08-", "stages-7-and-8.md"),
    ("lenses-", "lenses-and-evidence.md"),
    ("evidence-", "lenses-and-evidence.md"),
    ("checks-", "checks.md"),
    ("challenges-", "challenges-workshops-and-requests.md"),
    ("workshops-", "challenges-workshops-and-requests.md"),
    ("partners-", "challenges-workshops-and-requests.md"),
    ("team-", "team.md"),
]
COPILOT_SPLITS = {
    "methods-": [("a", "c"), ("d", "i"), ("j", "z")],
    "templates-": [("a", "i"), ("j", "z")],
}
COPILOT_MAX_COMPANIONS = 20

COPILOT_PARAGRAPH = """This copy has no scripts, and to fit Copilot's file limit most of the
files are combined. When a file names another, such as
`stages-07-analyze.md`, open the combined file the list below gives for it
and go to the line `<!-- file: stages-07-analyze.md -->`; that file runs
until the next such line. Do the quote, count and evidence checks at
stages 7 and 8 by hand and say so in the record. For Word or Excel files,
use the tool's own way to make them if it has one, or give the formatted
draft to copy in.
"""


def copilot_bundle(name: str) -> str:
    """The combined file a skill file goes in, or its own name if it stays alone."""
    for prefix, bundle in COPILOT_BUNDLES:
        if name.startswith(prefix):
            return bundle
    for prefix, ranges in COPILOT_SPLITS.items():
        if name.startswith(prefix):
            first = name[len(prefix)]
            for low, high in ranges:
                if low <= first <= high:
                    return f"{prefix}{low}-to-{high}.md"
    return name


def copilot_files() -> dict[str, bytes]:
    """The skill folder without scripts/, combined to 20 companion files or fewer.

    Every original file keeps its name on a marker line inside the combined
    file, so cross-references between files still lead somewhere, and
    SKILL.md's list says which combined file each one is in.
    """
    singles = {}
    bundles: dict[str, list[tuple[str, str]]] = {}
    for name, data in gemini_files().items():
        bundle = copilot_bundle(name)
        if bundle == name:
            singles[name] = data
        else:
            bundles.setdefault(bundle, []).append((name, data.decode("utf-8")))

    skill = singles.pop("SKILL.md").decode("utf-8")
    if NO_SCRIPTS_PARAGRAPH not in skill:
        raise SystemExit("SKILL.md no longer has the no-scripts paragraph; update copilot_files()")
    skill = skill.replace(NO_SCRIPTS_PARAGRAPH, COPILOT_PARAGRAPH)
    listed = set(re.findall(r"^- `([^`]+)`:", skill, flags=re.M))
    for bundle, parts in bundles.items():
        for name, _ in parts:
            if name not in listed:
                raise SystemExit(f"{name} isn't in SKILL.md's list; update copilot_files()")
            skill = skill.replace(f"- `{name}`:", f"- `{name}` (in `{bundle}`):", 1)

    files = dict(singles)
    files["SKILL.md"] = skill.encode("utf-8")
    for bundle, parts in sorted(bundles.items()):
        names = ", ".join(f"`{name}`" for name, _ in parts)
        body = [f"<!-- Magpie, combined for Copilot. Holds {names}. -->\n"]
        for name, text in parts:
            body.append(f"<!-- file: {name} -->\n\n{text.strip()}\n")
        files[bundle] = "\n".join(body).encode("utf-8")

    companions = len(files) - 1
    if companions > COPILOT_MAX_COMPANIONS:
        raise SystemExit(f"magpie-copilot.zip has {companions} companion files; Copilot allows {COPILOT_MAX_COMPANIONS}")
    return files


def write_zip(files: dict[str, bytes], target: Path) -> None:
    """Write name -> contents to a zip with fixed dates and order."""
    target.unlink(missing_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for name in sorted(files):
            info = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, files[name])


def build_zip(source: Path, target: Path) -> None:
    """Zip the skill folder's contents, SKILL.md at the top, not in a folder.

    Copilot Cowork needs SKILL.md at the top of the zip, and Gemini and
    ChatGPT take it that way too, so one zip serves every upload route.
    Fixed dates and order keep the zip the same from one build to the next.
    """
    target.unlink(missing_ok=True)
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for path in sorted(p for p in source.rglob("*") if p.is_file()):
            info = zipfile.ZipInfo(path.relative_to(source).as_posix(), (1980, 1, 1, 0, 0, 0))
            info.external_attr = 0o644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())


def main() -> None:
    files = core_files()
    build_generic(files)
    build_skill(files)
    build_zip(SKILL, ZIP)
    write_zip(gemini_files(), GEMINI_ZIP)
    write_zip(copilot_files(), COPILOT_ZIP)
    print(f"Built adapters/generic, adapters/skill, .claude/skills, magpie.zip, magpie-gemini.zip and magpie-copilot.zip from {len(files)} core file(s):")
    for path in files:
        print(f"  core/{path.relative_to(CORE)}")


if __name__ == "__main__":
    main()
