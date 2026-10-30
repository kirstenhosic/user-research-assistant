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
  6. The code checks pass their fixture tests, and the Word and Excel
     exports write valid files.
  7. Hand-written files use American English: no British spellings and
     no day-before-month dates. Participant transcripts, docs/CHANGELOG.md
     and evals/runs/ are left as written.
  8. Every source in docs/PROVENANCE.md names a year (or n.d.) and a link
     (or is a book or journal with its title in italics); every source code
     used in core/ or docs/DESIGN.md is in the list and not retired; the
     standards count line is right; and every paragraph that mentions
     HEARTS gives the full citation.
  9. Size report for the generic prompts, with a rough token estimate.

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

    if not build.GEMINI_ZIP.exists():
        fail("magpie-gemini.zip is missing; run python3 tools/build.py")
        return
    with zipfile.ZipFile(build.GEMINI_ZIP) as zf:
        gemini = {name: zf.read(name) for name in zf.namelist()}
    if gemini != build.gemini_files():
        fail("magpie-gemini.zip is stale; run python3 tools/build.py")

    if not build.COPILOT_ZIP.exists():
        fail("magpie-copilot.zip is missing; run python3 tools/build.py")
    with zipfile.ZipFile(build.COPILOT_ZIP) as zf:
        copilot = {name: zf.read(name) for name in zf.namelist()}
    if copilot != build.copilot_files():
        fail("magpie-copilot.zip is stale; run python3 tools/build.py")


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


SOURCE_ROW = re.compile(r"^\|\s*(S\d+[a-z]?)\s*\|\s*(.*?)\s*\|", re.M)
RETIRED = "Same source as"
HEARTS_CITATION = (
    "Loosbrock, K. (2025). The HEARTS Framework: Six lenses for evaluating AI-assisted UX research. "
    "Hey Kaleb & Co. https://www.heykaleb.com/hearts-framework"
)
COUNT_LINE = re.compile(r"Current count: (\d+) of (\d+) standards cite a source")


def check_sources() -> None:
    provenance = (ROOT / "docs" / "PROVENANCE.md").read_text(encoding="utf-8")
    rows = dict(SOURCE_ROW.findall(provenance))
    for sid, source in rows.items():
        if source.startswith(RETIRED):
            continue
        if not re.search(r"\b(?:19|20)\d\d\b|n\.d\.", source):
            fail(f"docs/PROVENANCE.md: {sid} has no year (write n.d. for an undated page)")
        if not re.search(r"https?://|doi:", source) and not re.search(r"\*[^*]+\*", source):
            fail(f"docs/PROVENANCE.md: {sid} has no link")
    retired = {sid for sid, source in rows.items() if source.startswith(RETIRED)}
    for path in sorted(CORE.rglob("*.md")) + [ROOT / "docs" / "DESIGN.md"]:
        for src in sorted(set(SRC.findall(path.read_text(encoding="utf-8")))):
            if src not in rows:
                fail(f"{path.relative_to(ROOT)}: cites {src}, not in docs/PROVENANCE.md")
            elif src in retired:
                fail(f"{path.relative_to(ROOT)}: cites {src}, which is retired; cite the source it points to")

    total = cited = 0
    for path in sorted((CORE / "standards").glob("*.md")):
        for line in path.read_text(encoding="utf-8").splitlines():
            m = ROW.match(line)
            if m:
                total += 1
                cited += bool(SRC.search(m.group(3)))
    m = COUNT_LINE.search(provenance)
    if not m:
        fail("docs/PROVENANCE.md: no 'Current count' line")
    elif (int(m.group(1)), int(m.group(2))) != (cited, total):
        fail(f"docs/PROVENANCE.md: count line says {m.group(1)} of {m.group(2)}; it's {cited} of {total}")

    # Kirsten Hosic's rule: any mention of HEARTS credits it in full.
    # Headings are exempt; the paragraph under them carries the citation.
    hand_written = [ROOT / "README.md"] + sorted((ROOT / "docs").glob("*.md"))
    hand_written += sorted(CORE.rglob("*.md")) + sorted((ROOT / "evals").rglob("*.md"))
    for path in hand_written:
        for block in re.split(r"\n\s*\n", path.read_text(encoding="utf-8")):
            if "HEARTS" not in block or block.lstrip().startswith("#"):
                continue
            if HEARTS_CITATION not in re.sub(r"\s+", " ", block):
                fail(f"{path.relative_to(ROOT)}: mentions HEARTS without the full citation")


# American English. Each pattern is a British form; the generated adapters
# are rebuilt from core/ and are covered through it.
BRITISH = re.compile(
    r"\b(?:"
    r"(?:behavio|colo|favo|flavo|hono|humo|labo|neighbo|rumo|harbo|savo|endeavo|armo|odo|rigo|vigo|clamo)ur\w*"
    r"|\w+isations?"
    r"|(?:organ|recogn|real|summar|priorit|critic|emphas|minim|maxim|optim|categor|anonym|visual|standard"
    r"|apolog|custom|personal|synthes|final|util|familiar|general|character|special|author|memor|normal"
    r"|contextual|verbal|scrutin|stabil|central|capital|local|initial|incentiv|harmon|item|summar|theor)is(?:e|ed|es|ing)"
    r"|analys(?:e|ed|ing)"
    r"|(?:label|travel|cancel|model|signal|level|fuel|counsel|total|channel|funnel|tunnel|marshal|barrel)l(?:ed|ing|er|ers)"
    r"|jewellery|enrolment|fulfilment|skilful|wilful|instalments?"
    r"|(?:cent|theat|met|lit|fib|calib|somb|spect|lust|meag)re[sd]?"
    r"|grey|licence|defence|offence|pretence|practis(?:e|ed|es|ing)|artefacts?|catalogue[sd]?|programmes?"
    r"|judgements?|ageing|cheques?|tyres?|aluminium|ploughs?|moulds?|whilst|amongst|learnt|spelt"
    r"|sceptic\w*|manoeuvre\w*|paediatric\w*|analogue|full stops?|tick box(?:es)?"
    r")\b",
    re.IGNORECASE,
)
DAY_MONTH = re.compile(
    r"\b\d{1,2}\s+(?:January|February|March|April|May|June|July|August|September|October|November|December)\b"
)
# Titles and names kept as published, and the examples of other varieties
# in the rule that lets a researcher choose one.
KEEP_AS_PUBLISHED = ['"Analyse a research session"', "(analyse,", "behaviour, colour, 27 October 2026)",
                     '"27 October 2026" in British English']
# The scenario that tests this rule plants British spelling on purpose.
SPELLING_EXEMPT = {"evals/scenarios/spelling-and-dates.md"}


def english_files() -> list[Path]:
    paths = [ROOT / "README.md", ROOT / "evals" / "README.md"]
    paths += sorted(CORE.rglob("*.md"))
    paths += sorted(p for p in (ROOT / "docs").rglob("*.md") if p.name != "CHANGELOG.md")
    paths += sorted((ROOT / "evals" / "scenarios").glob("*.md"))
    paths += sorted(p for p in (ROOT / "evals" / "fixtures").rglob("*.md")
                    if not {"transcripts", "sessions"} & set(p.parts))
    paths += sorted((ROOT / "adapters").glob("*/README.md"))
    paths += sorted((ROOT / "tools").rglob("*.py"))
    return [p for p in paths if p.exists() and p != Path(__file__).resolve()
            and p.relative_to(ROOT).as_posix() not in SPELLING_EXEMPT]


def check_american_english() -> None:
    for path in english_files():
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for keep in KEEP_AS_PUBLISHED:
                line = line.replace(keep, "")
            for m in list(BRITISH.finditer(line)) + list(DAY_MONTH.finditer(line)):
                fail(f"{path.relative_to(ROOT)}:{n}: \"{m.group(0)}\" is not American English")


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
            numbering = z.read("word/numbering.xml").decode("utf-8")
            footer = z.read("word/footer1.xml").decode("utf-8")
        for needle in ('w:val="Heading2"', 'w:val="Quote"', 'w:val="ListBullet"', 'w:val="ListNumber"',
                       "<w:tbl>", "<w:b/>", "shift our focus"):
            if needle not in doc:
                fail(f"md_to_docx.py output is missing {needle}")
        if "ask question 10. This wrapped line" not in doc.replace("</w:t></w:r><w:r><w:t xml:space=\"preserve\">", ""):
            fail("md_to_docx.py split a paragraph at a wrapped line starting with a number")
        for needle in ('w:val="lowerLetter"', 'w:val="Q%1."'):
            if needle not in numbering:
                fail(f"md_to_docx.py numbering is missing {needle}")
        for needle in ('w:val="Note"', 'w:val="Option"', "\u2610", "\u25cb", "<w:gridSpan", 'w:fill="DCE9E3"',
                       'w:val="Heading3"', "footerReference"):
            if needle not in doc:
                fail(f"md_to_docx.py output is missing {needle}")
        if "Status: Draft" not in footer or "PAGE" not in footer:
            fail("md_to_docx.py footer is missing the status or page number")
        sheet = Path(tmp) / "sample.xlsx"
        run = subprocess.run([sys.executable, str(ROOT / "tools" / "export" / "make_sheet.py"),
                              str(ROOT / "evals" / "fixtures" / "export-sample.json"), str(sheet)],
                             capture_output=True, text=True)
        if run.returncode != 0 or not sheet.exists():
            fail("make_sheet.py failed:\n" + run.stdout + run.stderr)
            return
        with zipfile.ZipFile(sheet) as z:
            for name in z.namelist():
                try:
                    minidom.parseString(z.read(name))
                except Exception as e:  # noqa: BLE001
                    fail(f"make_sheet.py wrote invalid XML in {name}: {e}")
            first = z.read("xl/worksheets/sheet1.xml").decode("utf-8")
            if "RQ1" not in first or 'state="frozen"' not in first or "xl/worksheets/sheet2.xml" not in z.namelist():
                fail("make_sheet.py output is missing its header row, frozen pane or second sheet")
            if 'customHeight="1"' not in first or "Merged and dropped codes" not in first or ">Team<" not in first:
                fail("make_sheet.py output is missing its row height, details block or extra table")


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
    check_sources()
    check_fixtures()
    check_export()
    check_american_english()
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
