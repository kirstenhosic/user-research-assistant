# Analysis sheet: [study name]

An Excel workbook Magpie offers at stage 6, laid out like the note-taking
sheet so the researcher can put the two side by side. Every cell is
Magpie's draft from the transcripts and the study record, for the
researcher to check, change or delete. Made with
`scripts/make_sheet.py` (`operating.md`, "Files for the team").

## Sheet 1: By participant

The same rows and research-question columns as the note-taking sheet.

| Participant | Who they are | RQ1: [question] | RQ2: [question] | Also noticed |
| --- | --- | --- | --- | --- |
| P1 | [role, segment] | [what they said or did, with line numbers, and the codes applied in brackets] | | |
| **Findings** | | [each finding for this question: claim, N of M with codes, strength] | | |

- Each cell says what that participant said or did on that question,
  with transcript line numbers ("Invited after locations were done (06)
  [waits-for-setup]"). "Not covered" where the session didn't reach it.
- The Findings row holds the findings for each research question, in the
  same words as the study record, with counts and the participants behind
  them.

## Sheet 2: Themes

| Theme | Research question | Codes in it | Participants (lines) | Count | Who didn't fit | Strength | Researcher decision | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [theme] | RQ1 | [codes] | P1 06, P3 06 | 2 of 8 | P2, P5 | moderate | [keep, change, split or drop] | |

Riskiest theme first, as in the theme review. "Researcher decision" stays
blank until the researcher fills it in; Magpie never fills it.

## Sheet 3: Codes

| Code | What it means | Research question | Participants |
| --- | --- | --- | --- |
| [code] | [one-line definition] | RQ1 | P1, P3 |

The coding frame, so a teammate can check the work. Merged and dropped
codes are listed at the bottom with the reason.

## What it is not

The sheet is a working copy for review. The study record holds the
findings; if the researcher changes a cell, Magpie updates the record to
match and says what changed.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
