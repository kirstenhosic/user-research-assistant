#!/usr/bin/env python3
"""Turn a Magpie Markdown output into a Word document (.docx).

Usage: python3 md_to_docx.py <input.md> [output.docx]

For guides, scripts, surveys, plans and reports that colleagues will edit
together in Word or Google Docs. Uses only the Python standard library, so
it runs wherever Python 3.8+ does, with nothing to install.

Handles the Markdown Magpie writes: headings (# to ####), paragraphs,
bulleted and numbered lists (nested by indent), block quotes (the spoken
lines in a guide), tables, horizontal rules, and **bold**, *italic* and
`code` inside a line. Anything else comes through as plain text.

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

def table(rows: list[list[str]]) -> str:
    cells_xml = []
    for i, row in enumerate(rows):
        cells = []
        for cell in row:
            text = f"**{cell}**" if i == 0 and cell and not cell.startswith("**") else cell
            cells.append(f'<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/></w:tcPr>{para(text)}</w:tc>')
        header = "<w:trPr><w:tblHeader/></w:trPr>" if i == 0 else ""
        cells_xml.append(f"<w:tr>{header}{''.join(cells)}</w:tr>")
    return ('<w:tbl><w:tblPr><w:tblStyle w:val="TableGrid"/><w:tblW w:w="5000" w:type="pct"/>'
            '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="0" '
            'w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
            f"{''.join(cells_xml)}</w:tbl>{para('')}")


def split_row(line: str) -> list[str]:
    return [c.strip() for c in line.strip().strip("|").split("|")]


LIST = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")


def convert(md: str) -> str:
    lines = md.replace("\r\n", "\n").split("\n")
    body: list[str] = []
    buf: list[str] = []

    def flush() -> None:
        if buf:
            body.append(para(" ".join(s.strip() for s in buf)))
            buf.clear()

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
        m = LIST.match(line)
        if m:
            flush()
            indent = len(m.group(1).expandtabs(4))
            level = min(indent // 2, 2)
            numbered = m.group(2)[0].isdigit()
            text = m.group(3)
            # A wrapped list item continues on the next indented line.
            while (i + 1 < len(lines) and lines[i + 1].strip()
                   and not LIST.match(lines[i + 1]) and lines[i + 1].startswith(" " * (indent + 2))):
                i += 1
                text += " " + lines[i].strip()
            if numbered:
                body.append(para(f"{m.group(2)} {text}", "ListNumber" if level == 0 else "ListNumber2"))
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
{style("ListBullet", "List Bullet", '<w:numPr><w:numId w:val="1"/></w:numPr><w:spacing w:after="60"/>')}
{style("ListBullet2", "List Bullet 2", '<w:numPr><w:ilvl w:val="1"/><w:numId w:val="1"/></w:numPr><w:spacing w:after="60"/>')}
{style("ListBullet3", "List Bullet 3", '<w:numPr><w:ilvl w:val="2"/><w:numId w:val="1"/></w:numPr><w:spacing w:after="60"/>')}
{style("ListNumber", "List Number", '<w:spacing w:after="60"/><w:ind w:left="360" w:hanging="360"/>')}
{style("ListNumber2", "List Number 2", '<w:spacing w:after="60"/><w:ind w:left="720" w:hanging="360"/>')}
<w:style w:type="table" w:styleId="TableGrid"><w:name w:val="Table Grid"/><w:tblPr><w:tblBorders>
<w:top w:val="single" w:sz="4" w:color="BFBFBF"/><w:left w:val="single" w:sz="4" w:color="BFBFBF"/><w:bottom w:val="single" w:sz="4" w:color="BFBFBF"/><w:right w:val="single" w:sz="4" w:color="BFBFBF"/><w:insideH w:val="single" w:sz="4" w:color="BFBFBF"/><w:insideV w:val="single" w:sz="4" w:color="BFBFBF"/>
</w:tblBorders><w:tblCellMar><w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>
</w:styles>"""

NUMBERING = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="{W}">
<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="•"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="360" w:hanging="360"/></w:pPr></w:lvl>
<w:lvl w:ilvl="1"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="–"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr></w:lvl>
<w:lvl w:ilvl="2"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="◦"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="1080" w:hanging="360"/></w:pPr></w:lvl>
</w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>"""

CONTENT_TYPES = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
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
</Relationships>"""


def core(title: str) -> str:
    return ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/">'
            f"<dc:title>{escape(title)}</dc:title><dc:creator>Magpie</dc:creator></cp:coreProperties>")


def write_docx(md: str, out: Path) -> None:
    first = next((l.lstrip("# ").strip() for l in md.splitlines() if l.startswith("#")), out.stem)
    document = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:document xmlns:w="{W}"><w:body>'
                f"{convert(md)}"
                '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
                '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>'
                "</w:sectPr></w:body></w:document>")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING)
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
