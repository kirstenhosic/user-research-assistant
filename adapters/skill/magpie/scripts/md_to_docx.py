#!/usr/bin/env python3
"""Turn a Magpie Markdown output into a Word document (.docx).

Usage: python3 md_to_docx.py <input.md> [output.docx]

For guides, scripts, surveys, plans and reports that colleagues will edit
together in Word or Google Docs. Uses only the Python standard library, so
it runs wherever Python 3.8+ does, with nothing to install.

Handles the Markdown Magpie writes: headings (# to ####), paragraphs,
bulleted and numbered lists (nested by indent; "a." under a numbered item
becomes a lettered sub-item), survey items written "Q1.", "S1.", "D1."
(kept as Q1, S1, D1 in Word's own numbering), block quotes (the spoken
lines in a guide), tables, horizontal rules, and **bold**, *italic* and
`code` inside a line. A paragraph written wholly in italics (a moderator
note or a survey routing line) gets a shaded Note style, so nobody reads
it aloud by mistake. Answer options written "- [ ]" (pick all that apply)
or "- ( )" (pick one) come out as ☐ and ○ boxes. A line that is only
bold text becomes a small heading. Anything else comes through as plain
text.

Tables get a shaded, bold header row and columns sized to their content;
a "Document details" table becomes a titled block. Every page has a footer
with the document's title, its status (from the Status row) and the page
number.

The output uses Word's built-in style names (Heading 1, List Bullet,
Quote and so on), so a team's own template can restyle it in one step.
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# --- inline text ---------------------------------------------------------

INLINE = re.compile(r"(\*\*[^*]+\*\*|\*[^*\s][^*]*\*|_[^_\s][^_]*_|`[^`]+`|\[[^\]]+\]\([^)]+\))")


def runs(text: str) -> str:
    """Inline Markdown to Word runs."""
    out = []
    for part in INLINE.split(text):
        if not part:
            continue
        props = ""
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            part, props = part[2:-2], "<w:b/>"
        elif part.startswith("`") and part.endswith("`") and len(part) > 2:
            part, props = part[1:-1], '<w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>'
        elif part.startswith("[") and "](" in part and part.endswith(")"):
            label, url = part[1:-1].split("](", 1)
            part = f"{label} ({url})"
        elif (part[0] in "*_" and part[-1] == part[0] and len(part) > 2):
            part, props = part[1:-1], "<w:i/>"
        rpr = f"<w:rPr>{props}</w:rPr>" if props else ""
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{escape(part)}</w:t></w:r>')
    return "".join(out)


def para(text: str, style: str | None = None, extra: str = "") -> str:
    ppr = f'<w:pStyle w:val="{style}"/>' if style else ""
    ppr += extra
    return f"<w:p><w:pPr>{ppr}</w:pPr>{runs(text)}</w:p>" if ppr else f"<w:p>{runs(text)}</w:p>"


# --- blocks --------------------------------------------------------------

SHADE_HEAD = '<w:shd w:val="clear" w:color="auto" w:fill="DCE9E3"/>'
SHADE_LABEL = '<w:shd w:val="clear" w:color="auto" w:fill="F2EFE8"/>'


def plain(text: str) -> str:
    return re.sub(r"[*_`]", "", text)


def table(rows: list[list[str]]) -> str:
    ncols = max(len(r) for r in rows) if rows else 1
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    head = rows[0]
    filled = [c for c in head if c.strip()]
    # "| Document details | |": the header names the whole table.
    title = filled[0] if len(filled) == 1 and head[0].strip() and ncols == 2 else None
    has_header = bool(filled) and title is None
    body_rows = rows[1:]
    label_value = ncols == 2 and not has_header
    if label_value:
        widths = [2600, 6760]
    else:
        # Size columns to their content, so a long column isn't cramped.
        longest = [max(min(len(plain(r[c])), 60) for r in rows) + 4 for c in range(ncols)]
        total = sum(longest)
        widths = [max(1100, 9360 * n // total) for n in longest]
        widths[-1] += 9360 - sum(widths)
    grid = "<w:tblGrid>" + "".join(f'<w:gridCol w:w="{w}"/>' for w in widths) + "</w:tblGrid>"

    def tc(text: str, w: int, shade: str = "", span: int = 1) -> str:
        span_xml = f'<w:gridSpan w:val="{span}"/>' if span > 1 else ""
        return (f'<w:tc><w:tcPr><w:tcW w:w="{w}" w:type="dxa"/>{span_xml}{shade}</w:tcPr>'
                f'{para(text, "TableText")}</w:tc>')

    def bold(text: str) -> str:
        return f"**{text}**" if text and not text.startswith("**") else text

    out = []
    if title is not None:
        out.append(f'<w:tr><w:trPr><w:tblHeader/></w:trPr>{tc(bold(title), sum(widths), SHADE_HEAD, ncols)}</w:tr>')
    elif has_header:
        out.append("<w:tr><w:trPr><w:tblHeader/></w:trPr>"
                   + "".join(tc(bold(c), widths[k], SHADE_HEAD) for k, c in enumerate(head)) + "</w:tr>")
    for row in body_rows:
        cells = []
        for k, c in enumerate(row):
            if k == 0 and (label_value or title is not None):
                cells.append(tc(bold(c), widths[k], SHADE_LABEL))
            else:
                cells.append(tc(c, widths[k]))
        out.append(f"<w:tr>{''.join(cells)}</w:tr>")
    return ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="5000" w:type="pct"/>'
            '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="0" '
            'w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
            f"{grid}{''.join(out)}</w:tbl>{para('', 'TableGap')}")


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


LIST = re.compile(r"^(\s*)([-*+]|\d+[.)]|[a-z][.)])\s+(.*)$")
# Survey-style items: "Q1. ...", "S2. ...", "D1. ..." at the start of a line.
PREFIXED = re.compile(r"^([A-Z])(\d+)\.\s+(.*)$")


class Numbering:
    """Real Word numbering, so the numbers colleagues see in Word match the
    Markdown: a list that carries on from the last one keeps counting, one
    that starts elsewhere restarts at its own first number."""

    def __init__(self) -> None:
        self.abstract: dict[str, int] = {"bullet": 0, "dec": 1}
        self.nums: list[tuple[int, int, int | None]] = [(1, 0, None)]  # (numId, abstractId, start)
        self.current: dict[str, int] = {}
        self.last: dict[str, int] = {}

    def _new(self, family: str, start: int | None) -> int:
        if family not in self.abstract:
            self.abstract[family] = len(self.abstract)
        num_id = len(self.nums) + 1
        self.nums.append((num_id, self.abstract[family], start))
        self.current[family] = num_id
        return num_id

    def item(self, family: str, n: int) -> int:
        if family in self.current and n == self.last[family] + 1:
            num_id = self.current[family]
        else:
            num_id = self._new(family, n)
        self.last[family] = n
        return num_id

    def sub(self) -> int:
        return self.current.get("dec") or self._new("dec", 1)

    def xml(self) -> str:
        parts = [f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:numbering xmlns:w="{W}">']
        for family, aid in sorted(self.abstract.items(), key=lambda kv: kv[1]):
            if family == "bullet":
                lv = [("bullet", "\u2022"), ("bullet", "\u2013"), ("bullet", "\u25e6")]
            elif family == "dec":
                lv = [("decimal", "%1."), ("lowerLetter", "%2."), ("lowerRoman", "%3.")]
            else:
                lv = [("decimal", f"{family}%1.")]
            parts.append(f'<w:abstractNum w:abstractNumId="{aid}"><w:multiLevelType w:val="hybridMultilevel"/>')
            for lvl, (fmt, text) in enumerate(lv):
                left = 360 * (lvl + 1) + (140 if family not in ("bullet", "dec") else 0)
                hang = 360 + (140 if family not in ("bullet", "dec") else 0)
                parts.append(f'<w:lvl w:ilvl="{lvl}"><w:start w:val="1"/><w:numFmt w:val="{fmt}"/>'
                             f'<w:lvlText w:val="{text}"/><w:lvlJc w:val="left"/>'
                             f'<w:pPr><w:ind w:left="{left}" w:hanging="{hang}"/></w:pPr></w:lvl>')
            parts.append("</w:abstractNum>")
        for num_id, aid, start in self.nums:
            over = (f'<w:lvlOverride w:ilvl="0"><w:startOverride w:val="{start}"/></w:lvlOverride>'
                    if start is not None else "")
            parts.append(f'<w:num w:numId="{num_id}"><w:abstractNumId w:val="{aid}"/>{over}</w:num>')
        parts.append("</w:numbering>")
        return "".join(parts)


def numbered(text: str, num_id: int, level: int) -> str:
    extra = f'<w:numPr><w:ilvl w:val="{level}"/><w:numId w:val="{num_id}"/></w:numPr>'
    return para(text, "ListNumber" if level == 0 else "ListNumber2", extra)


def convert(md: str, num: Numbering) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    body: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if not buf:
            return
        text = " ".join(s.strip() for s in buf)
        buf.clear()
        if re.fullmatch(r"\*[^*].*[^*]\*|_[^_].*[^_]_", text) and "*" not in text[1:-1]:
            body.append(para(text[1:-1], "Note"))  # a note for the team, never read aloud
        elif re.fullmatch(r"\*\*[^*]+\*\*", text) and len(text) < 90:
            body.append(para(text[2:-2].rstrip(".:"), "Heading3"))
        else:
            body.append(para(text))

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            flush()
            i += 1
            continue
        m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if m:
            flush()
            level = min(len(m.group(1)), 4)
            style = "Title" if level == 1 and not body else f"Heading{level}"
            body.append(para(m.group(2).strip(), style))
            i += 1
            continue
        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", stripped):
            flush()
            i += 1
            continue
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1]):
            flush()
            rows = [split_row(line)]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i]))
                i += 1
            body.append(table(rows))
            continue
        if stripped.startswith(">"):
            flush()
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            for chunk in " ".join(q if q else "\n" for q in quote).split("\n"):
                if chunk.strip():
                    body.append(para(chunk.strip(), "Quote"))
            continue
        m = PREFIXED.match(line)
        if m and buf:
            m = None  # a wrapped sentence that happens to start "Q10." stays in its paragraph
        if m:
            flush()
            text = m.group(3)
            while (i + 1 < len(lines) and lines[i + 1].strip() and lines[i + 1].startswith("  ")
                   and not LIST.match(lines[i + 1])):
                i += 1
                text += " " + lines[i].strip()
            body.append(numbered(text, num.item(m.group(1), int(m.group(2))), 0))
            i += 1
            continue
        m = LIST.match(line)
        if m and m.group(2)[0].isalpha() and not m.group(1):
            m = None  # "a. ..." at the margin is a sentence, not a list
        if m and buf and m.group(2)[0].isdigit() and int(m.group(2)[:-1]) != 1:
            m = None  # as in CommonMark, only "1." can start a list mid-paragraph
        if m:
            flush()
            indent = len(m.group(1).expandtabs(4))
            level = min(indent // 2, 2)
            marker = m.group(2)
            text = m.group(3)
            # A wrapped list item continues on the next indented line.
            while (i + 1 < len(lines) and lines[i + 1].strip()
                   and not LIST.match(lines[i + 1]) and lines[i + 1].startswith(" " * (indent + 2))):
                i += 1
                text += " " + lines[i].strip()
            if marker[0].isdigit() and level == 0:
                body.append(numbered(text, num.item("dec", int(marker[:-1])), 0))
            elif marker[0].isdigit() or marker[0].isalpha():
                body.append(numbered(text, num.sub(), 1))
            elif text.startswith(("[ ] ", "( ) ")):
                # Survey answer options: a box for "pick all", a circle for "pick one".
                box = "\u2610" if text[0] == "[" else "\u25cb"
                body.append(para(f"{box}  {text[4:]}", "Option"))
            else:
                style = ["ListBullet", "ListBullet2", "ListBullet3"][level]
                body.append(para(text, style))
            i += 1
            continue
        buf.append(line)
        i += 1
    flush()
    return "".join(body)


# --- package -------------------------------------------------------------

# List items sit close together; the list as a whole has room after it.
LIST_SPACING = '<w:contextualSpacing/><w:spacing w:after="160"/>'


def style(sid: str, name: str, ppr: str = "", rpr: str = "", based: str = "Normal", kind: str = "paragraph") -> str:
    return (f'<w:style w:type="{kind}" w:styleId="{sid}"><w:name w:val="{name}"/>'
            f'<w:basedOn w:val="{based}"/><w:qFormat/><w:pPr>{ppr}</w:pPr><w:rPr>{rpr}</w:rPr></w:style>')


STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W}">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:eastAsia="Calibri" w:cs="Calibri"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-US"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
{style("Title", "Title", '<w:spacing w:after="200"/>', '<w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:b/><w:sz w:val="40"/>')}
{style("Heading1", "heading 1", '<w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/>', '<w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:b/><w:sz w:val="32"/>')}
{style("Heading2", "heading 2", '<w:keepNext/><w:spacing w:before="300" w:after="100"/><w:outlineLvl w:val="1"/>', '<w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:b/><w:sz w:val="28"/>')}
{style("Heading3", "heading 3", '<w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="2"/>', '<w:b/><w:sz w:val="24"/>')}
{style("Heading4", "heading 4", '<w:keepNext/><w:spacing w:before="200" w:after="60"/><w:outlineLvl w:val="3"/>', '<w:b/><w:i/>')}
{style("Quote", "Quote", '<w:spacing w:before="80" w:after="120"/><w:ind w:left="567"/><w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="2F6B5A"/></w:pBdr>', '<w:sz w:val="24"/>')}
{style("ListBullet", "List Bullet", f'<w:numPr><w:numId w:val="1"/></w:numPr>{LIST_SPACING}')}
{style("ListBullet2", "List Bullet 2", f'<w:numPr><w:ilvl w:val="1"/><w:numId w:val="1"/></w:numPr>{LIST_SPACING}')}
{style("ListBullet3", "List Bullet 3", f'<w:numPr><w:ilvl w:val="2"/><w:numId w:val="1"/></w:numPr>{LIST_SPACING}')}
{style("ListNumber", "List Number", '<w:keepNext/><w:contextualSpacing/><w:spacing w:before="160" w:after="160"/>')}
{style("ListNumber2", "List Number 2", '<w:contextualSpacing/><w:spacing w:after="160"/>')}
{style("Option", "Answer Option", '<w:contextualSpacing/><w:spacing w:after="160"/><w:ind w:left="500"/>')}
{style("Note", "Note", '<w:spacing w:before="120" w:after="160"/><w:ind w:left="284" w:right="284"/><w:pBdr><w:left w:val="single" w:sz="12" w:space="6" w:color="8A8A8A"/></w:pBdr><w:shd w:val="clear" w:color="auto" w:fill="F2EFE8"/>', '<w:i/><w:color w:val="404040"/><w:sz w:val="20"/>')}
{style("TableText", "Table Text", '<w:spacing w:before="0" w:after="0"/>', '<w:sz w:val="20"/>')}
{style("TableGap", "Table Gap", '<w:spacing w:before="0" w:after="120"/>', '<w:sz w:val="12"/>')}
{style("Footer", "footer", '<w:tabs><w:tab w:val="right" w:pos="9360"/></w:tabs><w:spacing w:after="0"/>', '<w:color w:val="666666"/><w:sz w:val="16"/>')}
<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:tblPr><w:tblBorders>
<w:top w:val="single" w:sz="4" w:color="BFBFBF"/><w:left w:val="single" w:sz="4" w:color="BFBFBF"/><w:bottom w:val="single" w:sz="4" w:color="BFBFBF"/><w:right w:val="single" w:sz="4" w:color="BFBFBF"/><w:insideH w:val="single" w:sz="4" w:color="BFBFBF"/><w:insideV w:val="single" w:sz="4" w:color="BFBFBF"/>
</w:tblBorders><w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
</Types>"""

RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
</Relationships>"""

DOC_RELS = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Target="footer1.xml"/>
</Relationships>"""


def core(title: str) -> str:
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/">'
            f"<dc:title>{escape(title)}</dc:title><dc:creator>Magpie</dc:creator></cp:coreProperties>")


def footer(title: str, status: str | None) -> str:
    """Title on the left; status and page number on the right."""
    left = escape(plain(title)) + (f" \u00b7 {escape(plain(status))}" if status else "")
    page = ('<w:r><w:t xml:space="preserve">Page </w:t></w:r>'
            '<w:fldSimple w:instr=" PAGE "><w:r><w:t>1</w:t></w:r></w:fldSimple>'
            '<w:r><w:t xml:space="preserve"> of </w:t></w:r>'
            '<w:fldSimple w:instr=" NUMPAGES "><w:r><w:t>1</w:t></w:r></w:fldSimple>')
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:ftr xmlns:w="{W}">'
            f'<w:p><w:pPr><w:pStyle w:val="Footer"/></w:pPr><w:r><w:t xml:space="preserve">{left}</w:t></w:r>'
            f"<w:r><w:tab/></w:r>{page}</w:p></w:ftr>")


def write_docx(md: str, out: Path) -> None:
    first = next((l.lstrip("# ").strip() for l in md.splitlines() if l.startswith("#")), out.stem)
    status = next((m.group(1) for m in re.finditer(r"^\|\s*\**Status\**\s*\|\s*([^|]+?)\s*\|", md, re.M)), None)
    num = Numbering()
    document = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{W}" '
                f'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>'
                f"{convert(md, num)}"
                '<w:sectPr><w:footerReference w:type="default" r:id="rId3"/><w:pgSz w:w="12240" w:h="15840"/>'
                '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>'
                "</w:sectPr></w:body></w:document>")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", num.xml())
        z.writestr("word/footer1.xml", footer(first, f"Status: {status}" if status else None))
        z.writestr("docProps/core.xml", core(first))


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(__doc__.strip().splitlines()[2])
        return 2
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix(".docx")
    write_docx(src.read_text(encoding="utf-8"), out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
