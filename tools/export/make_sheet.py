#!/usr/bin/env python3
"""Write an Excel workbook (.xlsx) from a small JSON description.

Usage: python3 make_sheet.py <input.json> [output.xlsx]

For the note-taking sheet that goes with a guide (stage 6) and the
analysis sheet that matches it (stage 7). Uses only the Python standard
library, so it runs wherever Python 3.8+ does, with nothing to install.
The file opens in Excel and Google Sheets.

The JSON looks like this:

    {
      "sheets": [
        {
          "name": "Notes",
          "intro": ["Ledgerline first-week setup: interview notes",
                    "One row per participant. Notes under the research question they answer."],
          "details": [["Team", "Admin Experience"], ["Date", "28 Oct 2026"],
                      ["Author(s)", "Sam Rivera"], ["Reviewers", "Dana Lee"],
                      ["Status", "Draft"]],
          "row_height": 120,
          "columns": [
            {"header": "Participant", "width": 14},
            {"header": "RQ1: Why do new admins stall during first-week setup?", "width": 45}
          ],
          "rows": [["P1", ""], ["P2", ""]],
          "summary": ["Summary across participants", ""],
          "tables": [
            {"title": "Merged and dropped codes",
             "columns": [{"header": "Code"}, {"header": "What happened"}],
             "rows": [["too-many-steps", "Merged into lost-the-path"]]}
          ]
        }
      ]
    }

The first "intro" line is the title. "details" (optional) is the
document details block, shown under the title with bold, shaded labels;
the remaining intro lines follow it. The header row is bold, shaded and
frozen, every cell wraps its text, and the "summary" row (optional) is
bold and shaded at the bottom. "row_height" (optional, in points) makes
the body rows tall enough to type notes in. "tables" (optional) adds more
small tables below the main one, each with an optional title. Widths are
in Excel's character units.
"""

from __future__ import annotations

import json
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

# Cell styles (index into cellXfs below): 0 plain, 1 wrapped, 2 header,
# 3 summary, 4 title, 5 intro note, 6 details label, 7 small table title.
STYLES = f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<styleSheet xmlns="{NS}">
<fonts count="4">
<font><sz val="11"/><name val="Calibri"/></font>
<font><b/><sz val="11"/><name val="Calibri"/></font>
<font><b/><sz val="14"/><name val="Calibri"/></font>
<font><i/><sz val="11"/><color rgb="FF555555"/><name val="Calibri"/></font>
</fonts>
<fills count="4">
<fill><patternFill patternType="none"/></fill>
<fill><patternFill patternType="gray125"/></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FFDCE9E3"/><bgColor indexed="64"/></patternFill></fill>
<fill><patternFill patternType="solid"><fgColor rgb="FFF2EFE8"/><bgColor indexed="64"/></patternFill></fill>
</fills>
<borders count="2">
<border><left/><right/><top/><bottom/><diagonal/></border>
<border><left style="thin"><color rgb="FFBFBFBF"/></left><right style="thin"><color rgb="FFBFBFBF"/></right><top style="thin"><color rgb="FFBFBFBF"/></top><bottom style="thin"><color rgb="FFBFBFBF"/></bottom><diagonal/></border>
</borders>
<cellStyleXfs count="1"><xf numFmtId="0" fontId="0" fillId="0" borderId="0"/></cellStyleXfs>
<cellXfs count="8">
<xf numFmtId="0" fontId="0" fillId="0" borderId="0" xfId="0"/>
<xf numFmtId="0" fontId="0" fillId="0" borderId="1" xfId="0" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="1" fillId="2" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="1" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="2" fillId="0" borderId="0" xfId="0" applyFont="1"/>
<xf numFmtId="0" fontId="3" fillId="0" borderId="0" xfId="0" applyFont="1"/>
<xf numFmtId="0" fontId="1" fillId="3" borderId="1" xfId="0" applyFont="1" applyFill="1" applyBorder="1" applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>
<xf numFmtId="0" fontId="1" fillId="0" borderId="0" xfId="0" applyFont="1"/>
</cellXfs>
<cellStyles count="1"><cellStyle name="Normal" xfId="0" builtinId="0"/></cellStyles>
</styleSheet>"""


def col_name(i: int) -> str:
    name = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        name = chr(65 + r) + name
    return name


def cell(ref: str, value, style: int) -> str:
    if value is None or value == "":
        return f'<c r="{ref}" s="{style}"/>'
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return f'<c r="{ref}" s="{style}"><v>{value}</v></c>'
    return f'<c r="{ref}" s="{style}" t="inlineStr"><is><t xml:space="preserve">{escape(str(value))}</t></is></c>'


def sheet_xml(sheet: dict) -> str:
    columns = sheet.get("columns", [])
    intro = sheet.get("intro", [])
    rows_xml = []
    r = 0

    def add(cells: list[tuple[object, int]], height: float | None = None) -> None:
        nonlocal r
        r += 1
        ht = f' ht="{height}" customHeight="1"' if height else ""
        rows_xml.append(f'<row r="{r}"{ht}>' + "".join(
            cell(f"{col_name(c)}{r}", v, st) for c, (v, st) in enumerate(cells)) + "</row>")

    def table(cols: list[dict], rows: list[list], summary: list | None, height: float | None) -> int:
        add([(col.get("header", ""), 2) for col in cols])
        header = r
        for row in rows:
            add([(row[c] if c < len(row) else "", 1) for c in range(len(cols))], height)
        if summary:
            add([(summary[c] if c < len(summary) else "", 3) for c in range(len(cols))], height)
        return header

    if intro:
        add([(intro[0], 4)])
    # Kept compact: everything above the header row stays frozen on screen.
    for label, value in sheet.get("details") or []:
        add([(label, 6), (value, 1)])
    for line in intro[1:]:
        add([(line, 5)])
    if intro or sheet.get("details"):
        r += 1  # blank row before the table
    header_row = table(columns, list(sheet.get("rows", [])), sheet.get("summary"), sheet.get("row_height"))
    for extra in sheet.get("tables", []):
        r += 1
        if extra.get("title"):
            add([(extra["title"], 7)])
        table(extra.get("columns", []), extra.get("rows", []), extra.get("summary"), None)
    cols = "".join(f'<col min="{c + 1}" max="{c + 1}" width="{col.get("width", 30)}" customWidth="1"/>'
                   for c, col in enumerate(columns))
    pane = (f'<sheetViews><sheetView workbookViewId="0"><pane ySplit="{header_row}" '
            f'topLeftCell="A{header_row + 1}" activePane="bottomLeft" state="frozen"/></sheetView></sheetViews>')
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><worksheet xmlns="{NS}">'
            f"{pane}<cols>{cols}</cols><sheetData>{''.join(rows_xml)}</sheetData></worksheet>")


def clean_name(name: str, used: set[str]) -> str:
    for ch in '[]:*?/\\':
        name = name.replace(ch, " ")
    name = (name.strip() or "Sheet")[:31]
    base, n = name, 2
    while name in used:
        name = f"{base[:28]} {n}"
        n += 1
    used.add(name)
    return name


def write_xlsx(spec: dict, out: Path) -> None:
    sheets = spec.get("sheets") or [{"name": "Sheet1"}]
    used: set[str] = set()
    names = [clean_name(s.get("name", f"Sheet{i + 1}"), used) for i, s in enumerate(sheets)]
    workbook = (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><workbook xmlns="{NS}" xmlns:r="{REL}"><sheets>'
                + "".join(f'<sheet name="{escape(n, {chr(34): "&quot;"})}" sheetId="{i + 1}" r:id="rId{i + 1}"/>'
                          for i, n in enumerate(names))
                + "</sheets></workbook>")
    wb_rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
               '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
               + "".join(f'<Relationship Id="rId{i + 1}" Type="{REL}/worksheet" Target="worksheets/sheet{i + 1}.xml"/>'
                         for i in range(len(sheets)))
               + f'<Relationship Id="rId{len(sheets) + 1}" Type="{REL}/styles" Target="styles.xml"/></Relationships>')
    types = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
             '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
             '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
             '<Default Extension="xml" ContentType="application/xml"/>'
             '<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>'
             '<Override PartName="/xl/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml"/>'
             + "".join(f'<Override PartName="/xl/worksheets/sheet{i + 1}.xml" '
                       'ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>'
                       for i in range(len(sheets)))
             + "</Types>")
    rels = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
            f'<Relationship Id="rId1" Type="{REL}/officeDocument" Target="xl/workbook.xml"/></Relationships>')
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", types)
        z.writestr("_rels/.rels", rels)
        z.writestr("xl/workbook.xml", workbook)
        z.writestr("xl/_rels/workbook.xml.rels", wb_rels)
        z.writestr("xl/styles.xml", STYLES)
        for i, s in enumerate(sheets):
            z.writestr(f"xl/worksheets/sheet{i + 1}.xml", sheet_xml(s))


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(__doc__.strip().splitlines()[2])
        return 2
    src = Path(sys.argv[1])
    out = Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix(".xlsx")
    write_xlsx(json.loads(src.read_text(encoding="utf-8")), out)
    print(f"Wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
