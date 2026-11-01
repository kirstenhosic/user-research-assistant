# Note-taking sheet: [study name]

An Excel workbook that goes out with every interview guide, usability test
script and diary study, so note-takers write down what they hear under the
research question it answers. Made with `scripts/make_sheet.py`
(`operating.md`, "Files for the team").

## Sheet 1: Notes

Above the table: the study name as the title, the document details
block (below), then one line: "One row per participant. Write what you
heard under the research question it answers, with the time or question
number. Quotes in quotation marks, word for word." Note rows are tall
(about 120 points) so there's room to type.

| Participant | Session date | Who they are | Note-taker | RQ1: [question] | RQ2: [question] | Also noticed | Quotes worth keeping | Top takeaway |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | | [role, segment] | | | | | | |
| P2 | | | | | | | | |
| **Summary across participants** | | | | [what we're hearing so far] | [what we're hearing so far] | | | |

- One row per planned participant, with their code and a short
  descriptor filled in from the plan for every row, not just the first.
  No names.
- One column per research question, headed with its number and the
  question in plain words, in the order of the record.
- "Also noticed" is for things outside the research questions.
- The summary row is for the team's running read after each session or
  at the end. Every research question column gets the same placeholder. It's a note, not a finding: findings come from analysis at
  stage 7.

## Sheet 2: Research questions

| # | Research question | Priority | Decision it serves | Guide questions that cover it |
| --- | --- | --- | --- | --- |
| RQ1 | [question] | [Priority or blank] | [decision] | [question numbers from the guide] |

Priority has its own column, never folded into the number.

## Document details

A small two-column block under the title on every sheet: Team, Date,
Author(s), Reviewers and Status, as on the guide. In the JSON for
`scripts/make_sheet.py` it's the sheet's `"details"` list.

---

Part of Magpie version 2026-11-01, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
