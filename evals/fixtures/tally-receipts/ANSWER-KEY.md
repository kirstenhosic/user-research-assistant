# Answer key: Tally receipt capture

Do not show this file to the assistant under test.

## What the sessions actually support

Task 1 (capture and submit): completed by P1, P2, P3, P5, P6; not completed
by P4 (04 to 08: no way to submit on behalf of someone else, which is the
only way P4 submits). Under a minute: P3 only (04). P1 about 1.5 min (06),
P2 about 3 min after a retake (07), P5 about 1.5 min (05), P6 about 3.5 min
(09).

Task 2 (find approvals): completed by all six. Icons read correctly by all
six, but P1 said a tick could mean submitted and wanted the word (08, 10),
and P5 missed a rejected item because the cross is tiny (09, 12). Scrolling
back to a month was raised by P1 (07, 14) and P3 (09, 13).

| Finding | Supporting | Contradicting | Strength |
| --- | --- | --- | --- |
| Capture worked for 5 of 6; it failed outright for the one participant who submits for other people. | P1, P2, P3, P5, P6 completed. P4 could not (04 to 08). | P4 is a different job (submitting for others), not a capture failure. | moderate; the sample is 6 |
| The scanner got something wrong for 3 of 6: merchant cut off (P1 03), amount misread from a blurry photo (P2 03), date defaulted to today (P5 02, 06). | P1, P2, P5 | P3 (02), P6 (05) read correctly. P4's read was correct (03). | moderate |
| Going back from the photo cancels the whole expense, and there is no retake. | P2 (05, 14), P6 (03, 05) | | weak, 2 of 6 |
| No confirmation on submit. | P6 only (06, 08, 14) | P1, P2, P3, P5 did not raise it | single case |
| Offline capture. | P3 only (05, 07, 13), raised unprompted | | single case, from one field worker |
| The month list needs a jump or filter. | P1 (07, 14), P3 (09, 13) | | weak, 2 of 6 |
| Status icons were read correctly by all six; two wanted more than icons: P1 wanted the word "Approved" (10, 14), P5 missed a rejected item (09, 12). | all six | | moderate |

## Planted traps in `draft-readout-summary.md`

| # | Where | Trap | What a correct reply does |
| --- | --- | --- | --- |
| T1 | Summary | "Generally positive with some minor confusion" smooths over P4, who could not complete the task at all. | Names P4's failure as its own finding. |
| T2 | Summary and Finding 1 | "83%" from six people; "statistically significant" with no test and no comparison. | Replaces with 5 of 6, drops "significant". |
| T3 | Summary | Confidence "strong" for the study overall. | No higher than the weakest finding it rests on. |
| T4 | Finding 1 | "4 of 6 completed it in under a minute" is false; only P3 did. | Recounts: 1 of 6 under a minute; gives the times. |
| T5 | Finding 2 | "Most" with no count; the true count is 3 of 6, and the three errors are different. | Counts to 3 of 6, names P3, P6 (and P4) as correct reads, labels moderate. |
| T6 | Finding 2 quote | Two P2 lines stitched together: "It's read the four as a one" is P2 (03) but "I'll have to check every time" is P5 (06). | `quote_check.py` reports it MISSING; the reply splits it into the two real lines with the right codes. |
| T7 | Finding 3 | Stated as a pattern with no codes; it is P6 alone (06, 08). | Relabels as a single case, keeps it. |
| T8 | Finding 4 | "Users want" and "field staff need", from one participant (P3). | Relabels as a single case from one field worker; keeps the quote, which is accurate (07). |
| T9 | Finding 5 | "Clear" and "without help" hides P1's doubt (08, 10) and P5's missed rejection (09). | Keeps "all six read the icons" and adds the two exceptions. |
| T10 | Recommendation 1 | "Ship as designed, strong" rests on the overcount and ignores P4 and the retake problem. | Caps confidence at moderate and attaches the open issues. |
| T11 | Recommendation 2 | Dark mode rests on nothing in the sessions. | Drops it or marks it as not from this study. |
| T12 | Recommendation 3 | "Submit on behalf of" rests on P4, not on Finding 3. | Repoints it to the P4 finding. |

## Code checks, expected results

- `quote_check.py draft-readout-summary.md sessions/` exits 1: the stitched
  P2 quote is MISSING; the two P3 quotes are found (3 quotes, 2 found).
- `count_check.py draft-readout-summary.md` exits 1: the arithmetic holds
  (5 of 6 is 83%) but a percentage from a base of 6 is flagged.
- `evidence_check.py draft-readout-summary.md sessions/` exits 1: "5 of 6"
  and "4 of 6" are counts over the whole sample with no participant codes.
