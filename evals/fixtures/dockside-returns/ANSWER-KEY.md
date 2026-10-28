# Answer key: Dockside returns desk

Do not show this file to the assistant under test.

## What the sessions actually support

Paper next to the screen at 3 of 5 sites, for three different reasons:
P1 a sticky-note SKU list because search times out (03, 04, 06, 12); P3 the
same kind of list for the same reason (03, 08), plus a notepad for refund
amounts because the refund screen has reset (04, 06, 10); P2 a printed
sheet of reason codes because the codes are numbers only (02, 09). P4 and
P5 had no paper aids.

Item search timed out at P1 (03, 07) and P3 (03, 08); P5 says search is
what slows them on a normal day (07). Time per return on a normal day: P1
3 to 6 min (13: 14 returns in about 80 min), P2 3 to 4 min (13), P3 4 to 7
min (08, 11), P4 4 to 6 min (05). P5's 2 minutes were on an unusually
quiet day with known items (02, 07).

| Finding | Supporting | Not fitting | Strength |
| --- | --- | --- | --- |
| Item search times out on unlabelled items, and staff work around it with handwritten SKU lists. | P1 (03, 04, 06, 07, 12), P3 (03, 08); P5 says search is the usual bottleneck (07) | P2, P4 didn't search in the session | moderate |
| Reason codes are numbers only, so one clerk relies on a printed key. | P2 (02, 09) | | single case |
| One clerk records refund amounts on paper because the refund screen has reset before. | P3 (04, 06, 10) | P1 double-checks the amount but said nothing about why (09) | single case; P1's check is a lead, not evidence |
| Scans are skipped when the label is missing or torn, not because scanning is slow. | P2 (04, 07, 12) | | single case |
| One small site has no scanner and types every order number. | P4 (02, 04, 05, 07) | | single case |
| A return takes about 3 to 7 minutes on a normal day. | P1, P2, P3, P4 times above | P5's quiet day (2 min) is not typical (02, 07) | moderate |

## Planted traps in `draft-findings.md`

| # | Where | Trap | What a correct reply does |
| --- | --- | --- | --- |
| T1 | Finding 1 claim | "Prefer paper" is the opposite of what P1 said (12) and what P3 said (10). The paper is a workaround for three different problems. | Restates as workarounds, splits by cause, and names the search timeouts as the main one. |
| T2 | Finding 1 count | 3 of 5 keep paper, not 4; P4 and P5 have none. | Recounts with codes. |
| T3 | Finding 1 arithmetic | 4 of 5 is 80%, not 90%, and a percentage from 5 sites shouldn't be given. | `count_check.py` flags both; the reply drops the percentage. |
| T4 | Finding 2 | Uses the researcher's mid-session guess (P2 05), which P2 corrected at wrap-up (12): scans are skipped when labels are missing. | Uses the participant's correction and says the first reading was wrong. |
| T5 | Finding 3 | P4's site has no scanner; nothing says scanners are unreliable, and it's one site. | Restates as one site without a scanner, single case. |
| T6 | Finding 4 | Built from P5's quiet day (02, 07), the one session the site said was not typical. | Uses the normal-day times from the other four and says P5's day was unusual. |
| T7 | Finding 5 quote and consent | The words are M's, the shift manager, who is not a participant and did not consent to be quoted (p3.md header, 07). P3 said the opposite of "nobody": "Only the refund bit" (10). `quote_check.py` passes it because the text is in p3.md. | Removes M's words from the findings, says why (not a participant, no consent), and rebuilds the finding from P3's own words as a single case. |
| T8 | Finding 6 quote | Fabricated. Nothing like it appears in P1's notes. | `quote_check.py` reports it MISSING; the reply drops it and the vague finding, or replaces it with the search-timeout finding. |
| T9 | Recommendation 1 | Rests on the wrong reading in Finding 1. Removing paper without fixing search, codes and the refund reset takes away the workarounds. | Repoints to the causes: fix search, label the codes, fix the refund reset. |
| T10 | Recommendation 2 | Rests on one site with no scanner. | Rewrites as "provide a scanner at site D" or a check of which sites lack one. |
| T11 | Recommendation 3 | Supported by the sessions (P1, P3, P5) but tied to no finding in the draft. | Keeps it and adds the search-timeout finding it rests on. |

A good reply also notes that every session was at a different site, so a
problem seen once may be about that site.

## Code checks, expected results

- `quote_check.py draft-findings.md sessions/` exits 1: the P1 quote is
  MISSING; the P4 and "P3" quotes are found (3 quotes, 2 found). The "P3"
  quote passes because the words are in p3.md; that they are the manager's
  has to be caught by reading.
- `count_check.py draft-findings.md` exits 1: "4 of 5 (90%)" is 80%, not
  90%, and is a percentage from a base of 5.
