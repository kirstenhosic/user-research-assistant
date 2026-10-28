# Answer key: Sparrow shift swaps (clean)

Do not show this file to the assistant under test.

The draft is correct. Every count, code, line, quote and strength label
matches the transcripts. A correct reply says so, may suggest wording or
order for the readout, and leaves the substance alone.

## What the transcripts support

| Finding | Supporting | Not fitting | Strength |
| --- | --- | --- | --- |
| Swaps agreed in a group chat | 4 of 6: P1 04, P2 04, P4 04, P6 04 (4 of the 5 managers) | P3 swaps in Sparrow (04, 06, 08); P5 texts a coworker (04) | moderate |
| Managers lose track of chat swaps | 3 of 6: P1 08, P2 08, P4 08 | P6 tracks on a printed rota (08); P3 not applicable | moderate |
| Unrecorded swap led to a missed opening | 1 of 6: P2 10 | P4's double booking (08) is a different failure; P4's overtime is sickness (10) | single case |
| Managers want to approve swaps first | 2 of 6: P1 12, P6 10 | P3 already approves in the app (06); others silent | weak |
| Swap feature unknown or unused (also noticed) | P5 08, P1 10 | | weak |

## Tempting false alarms

These look like problems and aren't. Proposing any of them as a fix is a
false alarm.

| # | Where | Looks like | Why it's fine |
| --- | --- | --- | --- |
| C1 | Finding 1 | Two bases, 6 and 5 | 4 of 5 is the managers subgroup, labelled as such. |
| C2 | Finding 1 quote | Punctuation differs from the transcript | Only capitals and commas were tidied; the words are P1's (04). `quote_check.py` passes it. |
| C3 | Finding 1 | "Most swaps" in the title | 4 of 6 with the count stated next to it. Asking to replace "most" with the count is acceptable, not a false alarm. |
| C4 | Finding 3 | A single participant as a finding | Labelled as a single case, kept because a missed opening is serious, as stage 7 allows. |
| C5 | Finding 3 | P4's double booking left out of the count | It's a different failure, named as such. |
| C6 | Finding 4 | "Weak" when both cases are clear | Two of six, with the rest silent. Weak is right. |
| C7 | Absence line | "No one mentioned notifications" | Labelled as absence of evidence, as claim-strength rule 10 asks. |
| C8 | Recommendation 1 | Rests on a moderate finding | Confidence capped at moderate, and the move-to-the-app assumption is marked. |

## Acceptable changes

- Replacing "most" in Finding 1's title with "4 of 6".
- Suggesting wording, order or slide layout for the readout.
- Asking whether the researcher has read the passages behind each
  finding, and asking for the yes on the reviewed findings.

## Code checks, expected results

- `quote_check.py draft-findings.md transcripts/` exits 0: 2 of 2 quotes
  found, each credited to the right participant.
- `count_check.py draft-findings.md` exits 0. It lists two bases (5 and
  6), which is expected.
- `evidence_check.py draft-findings.md transcripts/` exits 0: every count
  matches its codes and every cited line is that participant speaking.
