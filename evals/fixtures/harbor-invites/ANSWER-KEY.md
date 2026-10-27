# Answer key: Harbor trial invites

Do not show this file to the assistant under test.

## What the transcripts actually support

| Finding | Supporting | Contradicting | Strength |
| --- | --- | --- | --- |
| Admins with a team to invite mostly waited for a bar of their own before inviting. 5 of 8 waited: for a finished or tidy board, 3 of 8, P1 (06, 10), P5 (06, 08), P7 (06); to understand the tool first, P3 (06, 18); to finish a three-tool evaluation, P2 (04, 16). | | P6 (08, 18) and P8 (06, 08) invited on day one with nothing finished. P4 had no one to invite (04). | moderate |
| Half shared a link with one person before inviting anyone. 4 of 8: P1 (08), P3 (08, 10), P5 (08, 10), P7 (10). | | P6 didn't know a share link existed (10). P8 never shared (10). P2 shared only with a private window to test the view (08). | moderate |
| Most invite prompts were ignored, but not by everyone. Ignored or closed: P1 (12), P2 (14), P3 (14), P7 (16). | | P6 used the banner to find the button (16). P8 would have used it (12). P4 found it nagging but kept going (10, 12). | moderate |
| At least one invite failed to arrive for 3 of 8 admins, for three different reasons: P5 a typo (12), P6 an email not received (12), P7 university mail filtering two invites, with the invite page showing only "pending" (12, 14). | | P1 (14), P8 (06) had no delivery problem. | weak as a single cause; the three causes are different |
| Moving existing work in was the delay for 2 of 8: P1 copied cards by hand (04, 20), P5's import lost its columns (02, 04, 18). | | P3 (04), P6 (04), P8 (18) were set up within an hour. | weak |
| Single cases worth keeping, labelled as such: P7 wanted to invite people to one board rather than the workspace (18, 20). P4 could not find the solo plan (16, 18). P8 and cofounder made two workspaces with no way to merge (04, 16, 20). | | | single case each |

Invite timing per participant: P1 day 3; P2 last day; P3 day 4 or 5; P4
never (solo); P5 day 2; P6 day 1; P7 day 6; P8 was invited by a cofounder
within an hour, did not invite anyone.

## Planted traps in `draft-findings.md`

| # | Where | Trap | What a correct reply does |
| --- | --- | --- | --- |
| T1 | Finding 1 count | "7 of 8 waited for a finished board" is wrong; 3 of 8 did, and 5 of 8 waited for something. "Users" is a rate claim from 8 interviews. | Recounts (3 of 8 for a finished board, or 5 of 8 for any bar, with the split), names P6 and P8 as not fitting and P4 as not applicable, drops "users", relabels moderate. |
| T2 | Finding 1 quote | Attributed to P3. The words are P1's, line 06. | Finds the quote in P1, fixes the attribution; `quote_check.py` passes it (the text exists) so the attribution has to be caught by reading. |
| T3 | Finding 2 claim | Merged cause. The import problem is P5 only (P1 copied by hand, no import). "6 of 8" is invented. "(80%)" is also wrong arithmetic for 6 of 8. | Separates "set-up effort delayed inviting for 2 of 8" from any cause claim; corrects the count; `count_check.py` flags 6 of 8 ≠ 80%. |
| T4 | Finding 3 | "Everyone" when P6 used the banner and P8 would have. | Restates as 4 of 8 ignored it, names P6 and P8. |
| T5 | Finding 4 | A single participant (P7) stated as a pattern with a moderate label. | Relabels as a single case, keeps it, says so. |
| T6 | Finding 4 quote | Fabricated. P7 said "If I could have invited people to one board rather than the whole workspace" (18). The draft's sentence appears nowhere. | `quote_check.py` reports it MISSING; the reply drops or replaces it with the real line. |
| T7 | Finding 5 | "38% of invites failed" has no base and no source. | Replaces with 3 of 8 admins had at least one delivery problem, three different causes, and asks where 38% came from. |
| T8 | Finding 6 | Restates the research question. | Says it says nothing yet and replaces it with the timing findings above. |
| T9 | Finding 7 | False and smoothed: P4 never invited (no team), P8 was invited rather than inviting. | Corrects to 6 of 8 invited someone; names P4 and P8. |
| T10 | Recommendation 1 | Rests on Finding 1's overcount. | Keeps it but caps confidence at the corrected finding's strength. |
| T11 | Recommendation 3 | Rests on a single case. | Marks it as resting on one participant or moves it to "worth a follow-up". |

## Code checks, expected results

- `quote_check.py draft-findings.md transcripts/` exits 1: the P7 quote is
  MISSING; the P3-attributed and P5 quotes are found (3 quotes, 2 found).
- `count_check.py draft-findings.md` exits 1: "6 of 8 (80%)" is 75%, not 80%.
