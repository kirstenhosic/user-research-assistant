# Fixture study: Harbor trial invites

A synthetic interview study with a known answer. Eight transcripts, a
researcher's draft findings with eleven planted problems, and an answer key.
Harbor, the participants and the quotes are invented.

**Use it for:** stage 6 analysis. Does Magpie recount, catch the misattributed
and fabricated quotes, separate the single cases from the patterns, and refuse
the merged cause?

## How to run

1. Give the assistant the skill or adapter, then the eight files in
   `transcripts/` and `draft-findings.md`. Don't give it `ANSWER-KEY.md`.
2. Paste this message:

   > Here are the eight transcripts and my draft findings for the Harbor
   > trial invites study. Research question: why don't trial users invite
   > teammates? Can you check the draft against the transcripts before I
   > write the readout?

3. Judge the reply against the traps table in `ANSWER-KEY.md`. Count each
   trap as caught, missed, or partly caught (noticed but mis-stated).
4. Run the three code checks and compare with the expected results at the end
   of the key:

   ```
   python3 tools/checks/quote_check.py evals/fixtures/harbor-invites/draft-findings.md evals/fixtures/harbor-invites/transcripts/
   python3 tools/checks/count_check.py evals/fixtures/harbor-invites/draft-findings.md
   python3 tools/checks/evidence_check.py evals/fixtures/harbor-invites/draft-findings.md evals/fixtures/harbor-invites/transcripts/
   ```
