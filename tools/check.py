#!/usr/bin/env python3
"""Maintenance check for the repository. Run before opening a pull request.

Usage: python3 tools/check.py

Checks:
  1. The adapters and magpie.zip are up to date with core/ (a rebuild
     changes nothing).
  2. Every core file has a title line and a first paragraph.
  3. Every file path named in backticks in core/ exists.
  4. Every standard names an eval that exists, and every source it cites
     (S1, S2, ...) is a row in docs/PROVENANCE.md.
  5. Every eval scenario names standards that exist.
  6. The code checks pass their fixture tests, and the Word export
     writes a valid file.
  7. Size report for the generic prompts, with a rough token estimate.

Exit 1 if any check fails. The size report never fails the run.
"""

from __future__ import annotations

import filecmp
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CORE = ROOT / "core"
sys.path.insert(0, str(ROOT / "tools"))
import build  # noqa: E402

problems: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def check_build_fresh() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        saved = (build.GENERIC, build.SKILL, build.CLAUDE_LOCAL)
        build.GENERIC = tmp / "generic"
        build.SKILL = tmp / "skill"
        build.CLAUDE_LOCAL = tmp / "local"
        try:
            files = build.core_files()
            build.build_generic(files)
            build.build_skill(files)
        finally:
            build.GENERIC, build.SKILL, build.CLAUDE_LOCAL = saved
        for fresh, committed in [
            (tmp / "generic", build.GENERIC),
            (tmp / "skill", build.SKILL),
            (tmp / "local", build.CLAUDE_LOCAL),
        ]:
            diff = trees_differ(fresh, committed)
            if diff:
                fail(f"{committed.relative_to(ROOT)} is stale; run python3 tools/build.py ({diff})")
    check_zip_fresh()


def check_zip_fresh() -> None:
    """magpie.zip holds exactly the skill folder, SKILL.md at the top.

    Compares names and file contents, not the zip's own bytes, which can
    differ between zlib versions.
    """
    if not build.ZIP.exists():
        fail("magpie.zip is missing; run python3 tools/build.py")
        return
    with zipfile.ZipFile(build.ZIP) as zf:
        zipped = {name: zf.read(name) for name in zf.namelist()}
    folder = {
        p.relative_to(build.SKILL).as_posix(): p.read_bytes()
        for p in build.SKILL.rglob("*")
        if p.is_file()
    }
    if "SKILL.md" not in zipped:
        fail("magpie.zip has no SKILL.md at the top")
    if zipped != folder:
        fail("magpie.zip is stale; run python3 tools/build.py")


def trees_differ(a: Path, b: Path) -> str:
    cmp = filecmp.dircmp(a, b)
    if cmp.left_only or cmp.right_only:
        return "files added or removed: " + ", ".join(cmp.left_only + cmp.right_only)
    if cmp.diff_files:
        return "changed: " + ", ".join(cmp.diff_files)
    for sub in cmp.subdirs.values():
        d = trees_differ(Path(sub.left), Path(sub.right))
        if d:
            return d
    return ""


def check_titles() -> None:
    for path in build.core_files():
        lines = path.read_text(encoding="utf-8").splitlines()
        if not lines or not lines[0].startswith("# "):
            fail(f"{path.relative_to(ROOT)}: first line is not a '# ' title")
            continue
        if not build.first_line_after_title(path):
            fail(f"{path.relative_to(ROOT)}: no paragraph under the title")


REF = re.compile(r"`([\w./-]+\.(?:md|py))`")


def resolve_ref(ref: str) -> bool:
    candidates = [CORE / ref, ROOT / ref]
    return any(c.exists() for c in candidates)


def check_refs() -> None:
    for path in sorted(CORE.rglob("*.md")):
        for ref in REF.findall(path.read_text(encoding="utf-8")):
            if ref.startswith("findings") or ref in {"SKILL.md", "operating.md", "voice.md"}:
                continue  # examples and skill-relative names
            if not resolve_ref(ref):
                fail(f"{path.relative_to(ROOT)}: `{ref}` does not exist")


ROW = re.compile(r"^\|\s*([0-9A-Z]+\.\d+[a-z]?)\s*\|(.*?)\|(.*?)\|\s*(.*?)\s*\|\s*$")
SRC = re.compile(r"\bS\d+[a-z]?\b")
EVAL = re.compile(r"`(evals/scenarios/[\w-]+\.md)`")


def provenance_sources() -> set[str]:
    text = (ROOT / "docs" / "PROVENANCE.md").read_text(encoding="utf-8")
    return set(re.findall(r"^\|\s*(S\d+[a-z]?)\s*\|", text, flags=re.M))


def check_standards_and_evals() -> None:
    known = provenance_sources()
    ids: set[str] = set()
    for path in sorted((CORE / "standards").glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if not m:
                continue
            sid, _, basis, evals = m.groups()
            ids.add(sid)
            for src in SRC.findall(basis):
                if src not in known:
                    fail(f"{path.name}: standard {sid} cites {src}, not in docs/PROVENANCE.md")
            if "practitioner judgment" not in basis and not SRC.search(basis):
                fail(f"{path.name}: standard {sid} has no basis")
            for ev in EVAL.findall(evals):
                if not (ROOT / ev).exists():
                    fail(f"{path.name}: standard {sid} points to missing {ev}")
            if not EVAL.search(evals) and "all scenarios" not in evals:
                fail(f"{path.name}: standard {sid} names no eval")
    for path in sorted((ROOT / "evals" / "scenarios").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        m = re.search(r"## Standards tested\s*\n+(.+)", text)
        if not m:
            fail(f"{path.relative_to(ROOT)}: no 'Standards tested' section")
            continue
        for sid in re.findall(r"[0-9A-Z]+\.\d+[a-z]?", m.group(1)):
            if sid not in ids:
                fail(f"{path.relative_to(ROOT)}: tests unknown standard {sid}")


def check_export() -> None:
    from xml.dom import minidom
    src = ROOT / "evals" / "fixtures" / "export-sample.md"
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "sample.docx"
        run = subprocess.run([sys.executable, str(ROOT / "tools" / "export" / "md_to_docx.py"), str(src), str(out)],
                             capture_output=True, text=True)
        if run.returncode != 0 or not out.exists():
            fail("md_to_docx.py failed:\n" + run.stdout + run.stderr)
            return
        with zipfile.ZipFile(out) as z:
            for name in z.namelist():
                if name.endswith(".xml") or name.endswith(".rels"):
                    try:
                        minidom.parseString(z.read(name))
                    except Exception as e:  # noqa: BLE001
                        fail(f"md_to_docx.py wrote invalid XML in {name}: {e}")
            doc = z.read("word/document.xml").decode("utf-8")
        for needle in ('w:val="Heading2"', 'w:val="Quote"', 'w:val="ListBullet"', "<w:tbl>", "<w:b/>", "shift our focus"):
            if needle not in doc:
                fail(f"md_to_docx.py output is missing {needle}")


def check_fixtures() -> None:
    run = subprocess.run([sys.executable, str(ROOT / "tools" / "checks" / "tests" / "run_tests.py")],
                         capture_output=True, text=True)
    if run.returncode != 0:
        fail("code check fixtures failed:\n" + run.stdout + run.stderr)


def size_report() -> None:
    print("Size report (about 4 characters per token):")
    for name in ["system-prompt.md", "system-prompt-lean.md"]:
        p = build.GENERIC / name
        if p.exists():
            n = len(p.read_text(encoding="utf-8"))
            print(f"  adapters/generic/{name}: {n // 1024} KB, ~{n // 4:,} tokens")
    skill = build.SKILL / "SKILL.md"
    if skill.exists():
        n = len(skill.read_text(encoding="utf-8"))
        print(f"  adapters/skill/magpie/SKILL.md (loaded first): {n // 1024} KB, ~{n // 4:,} tokens")


def main() -> int:
    check_build_fresh()
    check_titles()
    check_refs()
    check_standards_and_evals()
    check_fixtures()
    check_export()
    size_report()
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("\nAll checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
