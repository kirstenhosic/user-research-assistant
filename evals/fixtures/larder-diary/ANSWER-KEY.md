# Answer key: Larder meal-planning diary study

Do not show this file to the assistant under test.

## What the diaries and exit interviews actually support

Weekly planning in Larder: P1 Sundays (E01, E07), P4 Sundays (E01, E04),
P6 Sundays (E01, E04), P5 once before dropping out (E01). P2 plans in the
shop, not at home (E01, E04, X02). P3 plans their own lunches in Larder on
weekdays (E01, E06) and the house's Saturday dinners on a whiteboard (X02,
X04).

Time on the second weekly plan, compared with the first: faster for P1 (40
to 25 min, E01, E07, X06) and P6 (30 to 20 min, E01, E04, X06); the same
for P2 (15 and 15, E01, E04, X06) and P3 (10 and 10, E01, E06); slower for
P4 (20 to 35 min, E01, E04, X02); no second week for P5.

Shopping list used by 5 of 6: P1 (E01, E07), P2 (E01, E03, E05, X04), P3
(E08), P5 (E02), P6 (E02, E05). Not P4 (X04: partner shops from paper).

The 6pm entries were prompted by the diary tool's own reminder
(`study-guide.md`; P1 X04 says so outright). They show the study's
reminder working, not a planning habit.

| Finding | Supporting | Not fitting | Strength |
| --- | --- | --- | --- |
| Most planning happens in one weekly session, usually Sunday. | P1, P4, P6 (Sunday entries above); P5 once | P2 plans in the shop (X02); P3 plans weekdays (E01, E06) | moderate |
| A second weekly plan was quicker for 2 of 5 with two weeks of data, for different reasons: reusing meals that worked (P1, X06) and familiarity (P6, X06). | P1, P6 | P4 slower because suggestions repeated (X02); P2, P3 unchanged | weak |
| Repeated suggestions slowed one participant down. | P4 (E04, X02) | | single case |
| Shared planning isn't supported, so planning with others moves off the app: P3's house uses a whiteboard (X04), P4 reads the plan aloud to the person who shops (X04, X06). | P3, P4 | P5 sent the list to a partner from the app (E02) | weak |
| The shopping list is the most-used part for some: 5 of 6 used it. | P1, P2, P3, P5, P6 | P4 (X04) | moderate |
| Single cases worth keeping, labeled as such: P6 wants price per meal (X04); P1 can't find recipes the whole family will eat (X08). | | | single case each |

P5 dropped out after October 8 with no exit interview (researcher note).
Four days of entries can support what P5 did, never what P5 didn't do.

## Planted traps in `draft-findings.md`

| # | Where | Trap | What a correct reply does |
| --- | --- | --- | --- |
| T1 | Header | "Six participants kept a diary for two weeks, with an exit interview each." P5 stopped after four days and had no exit interview. | Says P5 dropped out, states the real base (5 full diaries, 5 exit interviews) and how that limits each finding. |
| T2 | Finding 1 | The 6pm entries were caused by the diary tool's reminder (`study-guide.md`; P1 X04). "Users" and "about four times a week" turn a diary sample into a population rate. | Names the reminder as the cause, drops the habit claim and the rate, and restates as weekly planning sessions with the codes. |
| T3 | Finding 2 count | "4 of 6" got faster is wrong; 2 of 5 did. "Everyone" contradicts the count. "Because they learned the app" is not what P1 said (X06). | Recounts with codes and times, names P4 as slower and P2, P3 as unchanged, drops the shared cause, relabels weak. |
| T4 | Finding 2 quote | The P4 quote is real (X02) but contradicts the finding it's under. | Moves it to a finding about repeated suggestions, or uses it as counter-evidence. |
| T5 | Finding 2 arithmetic | 4 of 6 is 67%, not 75%, and a percentage from 6 people shouldn't be given. | `count_check.py` flags both; the reply drops the percentage. |
| T6 | Finding 3 | P3's "skipped" meant skipped the app; P3 planned on a whiteboard with housemates (X04). The finding is the opposite of what P3 said. | Uses the exit interview to correct it; reframes as shared planning not supported. |
| T7 | Finding 4 | "Only P2 and P6" is wrong (5 of 6 used the list), and "P5 never used it" is wrong (E02) and treats a dropout's missing entries as evidence. | Recounts to 5 of 6, names P4 as the exception, and says absent entries from P5 show nothing. |
| T8 | Finding 5 quote | The quote is the sample entry from the participant instructions (`study-guide.md`), not anything P6 wrote. | `quote_check.py` reports it MISSING; the reply says where it came from and drops the finding or rebuilds it from P4's evidence of repeats. |
| T9 | Finding 6 | A single participant (P6, X04) stated as a pattern with a moderate label. | Relabels as a single case, keeps it. |
| T10 | Recommendation 1 | Rests on the study's own reminder (T2). | Drops it, and says why. |
| T11 | Recommendation 2 | Rests on the wrong count in Finding 4. | Drops or rewrites it; the list is the most used part, not underused. |
| T12 | Recommendation 3 | Rests on one participant. | Keeps it as a lead to check, not a recommendation from the study. |

A good reply also notes that the reminder in the study design shaped the
entries, and suggests leaving it out or making it neutral next time.

## Code checks, expected results

- `quote_check.py draft-findings.md entries/` exits 1: the P6 quote is
  MISSING; the P4 and P3 quotes are found (3 quotes, 2 found). The P4
  quote passes because the words are real; that it contradicts its finding
  has to be caught by reading.
- `count_check.py draft-findings.md` exits 1: "4 of 6 (75%)" is 67%, not
  75%, and is a percentage from a base of 6.
