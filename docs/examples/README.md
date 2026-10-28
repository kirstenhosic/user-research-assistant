# Examples

What Magpie's two stakeholder outputs look like, empty and filled in.

The study in the filled examples is fictional. Ledgerline, its customers,
its participants and the people named in them are made up to show the
shape of a finished report and readout; nothing in them is real evidence.

| File | What it is |
| --- | --- |
| `template-report.docx` | The research report template as a Word file. Source: `core/templates/report.md` |
| `template-readout.docx` | The readout outline (slide by slide) as a Word file. Source: `core/templates/readout.md` |
| `example-report.md`, `example-report.docx` | A filled-in report: eight usability sessions on an export feature |
| `example-readout.md`, `example-readout.pptx` | The same study as a 16-slide readout, in Markdown and as a PowerPoint deck |

The Word and PowerPoint files open in Google Docs and Google Slides too:
upload to Drive and open with the matching app.

The deck is deliberately unbranded so any team can drop in its own logo and
colors, or paste its content into the team's own template. It uses only
Office fonts (Cambria and Calibri), which Google Slides also has. Its
design rules, in case you restyle it:

- It opens with the answer, then a short summary drawn from the study's
  own focus and findings, then tells the story: the
  decision, what we did, what we expected, where it actually goes wrong,
  and one slide per finding.
- Every title states the slide's message in plain words and fits on one
  line.
- One message per slide, with large type and room around it.
- Each finding slide has a stat card, one quote, who didn't fit and what it
  means, with the evidence strength in words.
- Color never carries meaning alone: strength and the "serious" flag are
  written out.
- The recommendations are cards in priority order. They name the teams
  involved, not a person; who takes each one is for the teams to agree.
- No single named person carries the decision. The deck says "the team".

The Markdown files are what Magpie actually writes; the Word and PowerPoint
versions were converted from them. They follow the house style
(`core/templates/house-style.md`): headings and slide titles that state the
finding, numerals for every count, quotes labeled with the participant's
role and company size ("P3, operations analyst, 120 seats"), a bracketed
placeholder where a quote named someone, and a "How AI was used" section
in the appendix.
