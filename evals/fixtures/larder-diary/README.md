# Fixture study: Larder meal-planning diary

A synthetic diary study with a known answer. Six participants' two-week
diaries with exit interviews, the instructions they were given, a
researcher's draft findings with twelve planted problems, and an answer
key. Larder, the participants and the entries are invented.

**Use it for:** stage 6 analysis of a diary study. Does Magpie notice the
dropout, read entries together with the exit interviews, see that the
study's own reminder made the 6pm entries, recount the change over time,
and catch the quote lifted from the instructions?

## How to run

1. Give the assistant the skill or adapter, then the six files in
   `entries/`, `study-guide.md` and `draft-findings.md`. Don't give it
   `ANSWER-KEY.md`.
2. Paste this message:

   > Here are the diaries and exit interviews from our two-week Larder
   > study, the instructions participants got, and my draft findings.
   > Research question: how does weekly meal planning fit into people's
   > weeks, and what makes them stop? Can you check the draft before I
   > write the readout?

3. Judge the reply against the traps table in `ANSWER-KEY.md`. Count each
   trap as caught, missed, or partly caught (noticed but mis-stated).
4. Run the two code checks and compare with the expected results at the end
   of the key:

   ```
   python3 tools/checks/quote_check.py evals/fixtures/larder-diary/draft-findings.md evals/fixtures/larder-diary/entries/
   python3 tools/checks/count_check.py evals/fixtures/larder-diary/draft-findings.md
   ```
