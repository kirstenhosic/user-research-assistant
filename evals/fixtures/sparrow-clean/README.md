# Fixture study: Sparrow shift swaps (clean)

A synthetic interview study with a known answer, and no planted problems.
Six transcripts, a researcher's draft findings that are correct, and an
answer key. Sparrow, the participants and the quotes are invented.

**Use it for:** false alarms. The other fixtures test whether Magpie finds
problems; this one tests whether it invents them. A Magpie that flags
everything would do well on the other two and badly here.

## How to run

1. Give the assistant the skill or adapter, then the six files in
   `transcripts/` and `draft-findings.md`. Don't give it this README or
   `ANSWER-KEY.md`.
2. Paste this message:

   > Here are six transcripts and my draft findings for the Sparrow shift
   > swaps study. Can you check the draft against the transcripts before I
   > write the readout?

3. Judge the reply against `ANSWER-KEY.md`. Count every change Magpie
   proposes to a count, a code, a quote, a strength label or a finding as
   a false alarm, unless the key lists it as acceptable. The target is
   zero.
4. Run the three code checks. All three should pass:

   ```
   python3 tools/checks/quote_check.py evals/fixtures/sparrow-clean/draft-findings.md evals/fixtures/sparrow-clean/transcripts/
   python3 tools/checks/count_check.py evals/fixtures/sparrow-clean/draft-findings.md
   python3 tools/checks/evidence_check.py evals/fixtures/sparrow-clean/draft-findings.md evals/fixtures/sparrow-clean/transcripts/
   ```
