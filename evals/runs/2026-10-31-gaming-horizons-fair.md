# Eval run, October 31, 2026: Gaming Horizons player interviews, fair score

A test of stage 7 analysis on real, openly licensed interviews: the 13
"Play" transcripts from Gaming Horizons Stakeholder Interviews
(anonymised), Zenodo 10.5281/zenodo.1163698, CC BY 4.0 (Perrotta et al.,
2018). Magpie's analysis was scored against the project's own player
findings, cut down to what the 13 public transcripts support.

## How it was run

- **Adapter and commit:** `adapters/skill/magpie/` at 28787d3 (main),
  for the three new runs. The October 30 runs used main from before PR
  #67, and one re-run used main just after it.
- **Assistant and platform:** Claude Code, three separate sessions.
- **How Magpie was started:** `/magpie` at the start of each session.
- **Answers kept out:** the sessions saw the transcripts (renamed P01 to
  P13 in random order), a participant list (gender and country), the six
  interview questions, the goal and the audience. No reports, no
  codebook, no web access.
- **Replies:** after Magpie's first questions, every run got the same
  scripted reply (use your best judgment, you do my turns, I've
  reviewed, carry on). So the researcher's theme review didn't happen,
  and Magpie logged that as a risk.
- **Model judge:** a model from the same family as Magpie, with no
  tools, scoring each run's findings and codebook against the answer
  key, twice per run. The two passes agreed on 155 of 175 point scores
  (89%).
- **Person judging:** not yet.

## The answer key, and why it's smaller than the first one

The project's interview report (D2.3, Table 3) says its 13 coded player
interviews were 6 in Italian and 7 in English. Every quote in its player
section from the English interviews matched one of the 13 public
transcripts; none of the Italian quotes matched any. The researchers
also never coded 6 of the 13 public transcripts.

So the key keeps only what the public transcripts support: 25 points
(one dropped, 14 narrowed, 11 unchanged). A sub-point was kept if an
English quote supported it, or if it appears in the 13 transcripts.
Counts that mixed the two groups were dropped, and so were claims that
something was rare, since a third of the transcripts were never coded.
Nothing was added. Magpie gets no credit and no penalty for what the 6
uncoded transcripts say.

## Results

"Fully found" means Magpie's findings or codebook state all or nearly
all of the point. "In part" means the topic is there but a sub-point is
missing. Each number is the average of the two judge passes.

| Run | Fully found (of 25) | At least in part | Missed |
| --- | --- | --- | --- |
| October 30, run 1 | 11 | 24 | 1 |
| October 30, run 2 | 9 | 23 | 2 |
| October 30, run 3 | 9 | 24 | 1 |
| October 30, re-run after PR #67 | 12.5 | 24 | 1 |
| October 31, run 1 | 10 | 24 | 1 |
| October 31, run 2 | 12.5 | 25 | 0 |
| October 31, run 3 | 7 | 25 | 0 |

The judge here is stricter than the reading behind the first October 30
write-up, so these numbers aren't comparable with it. They are
comparable with each other.

**Point by point.** Because a row with six pieces counts as partial
when any one is missing, the 25 points were also split into 99 smaller
pieces. The judge was asked only whether each piece's substance appears
anywhere in the findings or codebook, however it is grouped or named
(two passes, agreeing on 98% of pieces). October 30 runs: 66 to 74 of 99
present, about 70%. October 31 runs: 63 to 73 of 99, about 68%. Allowing
other groupings at the row level changed little, so most of what's
missing is absent, not framed differently. Of the 16 pieces absent from
every October 31 judgment, 8 come from a single participant.

**What every October 31 run found only in part:** what drives
engagement and what breaks it; that players tie rage to competitive
play rather than to violent content; one-person points on identity and
skills; narrative as a driver of engagement; the tension between art and
gameplay; and the pattern that the three women were introduced to games
by their fathers. All three runs coded who people first played with but
didn't state the pattern.

**What looked better:** fewer outright misses, and the step that looks
for connections nobody asked about found other patterns (for example,
that the three women avoid violent play).

## Changes made after this run

Standards 7.22, 7.26, 7.30, 7.31 and 7.32 (see `docs/CHANGELOG.md`,
October 31, 2026, PR #85).

## Re-run after the changes

Three new runs on main at 4f48b67 (just after PR #85), set up the same
way as above, scored by the same judge against the same 25-point key.
The two judge passes agreed on 68 of 75 point scores (91%) and on 292
of 297 pieces (98%).

| Run | Fully found (of 25) | At least in part | Missed |
| --- | --- | --- | --- |
| After PR #85, run 1 | 6.5 | 25 | 0 |
| After PR #85, run 2 | 9.5 | 25 | 0 |
| After PR #85, run 3 | 8.5 | 24 | 1 |

Point by point: 66 to 76 of 99 pieces present, about 72% (about 68%
before the changes).

**What changed.** The fathers pattern was stated in 2 of 3 runs (0 of
3 before). The third run checked gender against who people first
played with and judged the split too small to report, which is a
defensible reading. Every run now has a Connections checked table, a
single voices list and a list of codes no finding uses.

**What didn't.** The number of points fully found stayed about the
same, and the spread between runs is as wide as the change. The rows
found only in part are mostly the same ones as before: what drives and
breaks engagement, rage tied to competitive play, narrative, and the
tension between art and gameplay. With three runs per side, a 4-point
rise in pieces present could be noise.

## Limits

- Model judging only, from the same model family as Magpie. A person
  should check the "in part" scores.
- One scripted reply, so the theme review, which Magpie is built
  around, didn't happen.
- The project is public, so the model may have read about it in
  training. No sign of that was seen in the outputs.
