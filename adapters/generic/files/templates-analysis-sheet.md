# Analysis sheet: [study name]

An Excel workbook Magpie offers at stage 7, laid out like the note-taking
sheet so the researcher can put the two side by side. Every cell is
Magpie's draft from the transcripts and the study record, for the
researcher to check, change or delete. Made with
`tools/export/make_sheet.py` (`operating.md`, "Files for the team").

Every sheet opens the same way: the study name as the title, the
document details block (Team, Date, Author(s), Reviewers, Status; Status
starts as Draft), then one line saying what the sheet is for. Keep that
line to one or two sentences on every sheet.

## Sheet 1: By participant

The same rows and research-question columns as the note-taking sheet.

| Participant | Who they are | RQ1: [question] | RQ2: [question] | Also noticed |
| --- | --- | --- | --- | --- |
| P1 | [role, segment] | [what they said or did, with line numbers, and the codes applied in brackets] | | |
| **Findings** | | [each finding for this question: claim, N of M with codes, strength, priority] | | |

- Each cell says what that participant said or did on that question,
  with transcript references written as in the study record ("Invited
  after locations were done (P1 06) [waits-for-setup]"). The intro line
  says once that "P1 06" means participant 1, line 6. "Not covered" where
  the session didn't reach it.
- The Findings row holds the findings for each research question, in the
  same words as the study record, with counts and the participants behind
  them.

## Sheet 2: Themes

| Theme | Finding | Research question | Count | Participants (lines) | Codes in it | Who didn't fit | Strength | Researcher decision | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [short plain name, a few words] | F[n] | RQ1 | 2 of 8 | P1 06, P3 06 | [codes] | P2, P5 | moderate | [keep, change, split or drop] | |

Sorted by research question, then by count, most shared first, so the
strongest themes are on top. Single cases go last. The theme name is a
short plain label; the finding number links it to the study record.
Counts are always "N of M". "Researcher decision" stays blank until the
researcher fills it in; Magpie never fills it. Flag the riskiest theme in
its Notes cell.

## Sheet 3: Codes

| Code | What it means | Research question | Participants |
| --- | --- | --- | --- |
| [code] | [one-line definition] | RQ1 | P1, P3 |

The coding frame, so a teammate can check the work. Merged and dropped
codes go in a second small table below it (Code, What happened, Why), not
as rows of the coding frame.

## What it is not

The sheet is a working copy for review. The study record holds the
findings; if the researcher changes a cell, Magpie updates the record to
match and says what changed.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
