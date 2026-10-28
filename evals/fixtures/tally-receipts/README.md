# Fixture study: Tally receipt capture

A synthetic usability test with a known answer. Six session transcripts with
task outcomes and times, a researcher's draft readout summary with twelve
planted problems, and an answer key. Tally, the participants and the quotes
are invented.

**Use it for:** the stage 7 to 8 handover. Does Magpie refuse the smoothed
summary, recount, catch the stitched quote, separate single cases from
patterns, and tie each recommendation to a real finding?

## How to run

1. Give the assistant the skill or adapter, then the six files in `sessions/`
   and `draft-readout-summary.md`. Don't give it `ANSWER-KEY.md`.
2. Paste this message:

   > Six usability sessions on Tally's receipt capture, transcripts
   > attached, plus my draft readout summary. The readout is Thursday for the
   > PM, the designer and two engineers, 30 minutes. Can you check the
   > summary and draft the readout?

3. Judge the reply against the traps table in `ANSWER-KEY.md`. Count each
   trap as caught, missed, or partly caught.
4. Run the three code checks and compare with the expected results at the end
   of the key:

   ```
   python3 tools/checks/quote_check.py evals/fixtures/tally-receipts/draft-readout-summary.md evals/fixtures/tally-receipts/sessions/
   python3 tools/checks/count_check.py evals/fixtures/tally-receipts/draft-readout-summary.md
   python3 tools/checks/evidence_check.py evals/fixtures/tally-receipts/draft-readout-summary.md evals/fixtures/tally-receipts/sessions/
   ```
