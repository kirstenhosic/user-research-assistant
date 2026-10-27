# Fixture study: Dockside returns desk

A synthetic contextual inquiry with a known answer. Observation notes from
five sessions at five sites, a researcher's draft findings with eleven
planted problems, and an answer key. Dockside, the sites, the participants
and the quotes are invented.

**Use it for:** stage 6 analysis of observation data. Does Magpie read a
workaround as a workaround rather than a preference, use the participant's
correction over the researcher's first guess, keep a bystander's words out
of the findings, set aside the atypical session, and tie each
recommendation to a finding?

## How to run

1. Give the assistant the skill or adapter, then the five files in
   `sessions/` and `draft-findings.md`. Don't give it `ANSWER-KEY.md`.
2. Paste this message:

   > Here are my notes from five contextual inquiry sessions at our returns
   > desks and my draft findings. Research question: how does returns
   > processing actually work at the desk, and where does it break down?
   > Can you check the draft before I share it with the product team?

3. Judge the reply against the traps table in `ANSWER-KEY.md`. Count each
   trap as caught, missed, or partly caught (noticed but mis-stated).
4. Run the two code checks and compare with the expected results at the end
   of the key:

   ```
   python3 tools/checks/quote_check.py evals/fixtures/dockside-returns/draft-findings.md evals/fixtures/dockside-returns/sessions/
   python3 tools/checks/count_check.py evals/fixtures/dockside-returns/draft-findings.md
   ```
