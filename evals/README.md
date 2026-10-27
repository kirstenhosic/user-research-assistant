# Evals

Test scenarios with planted problems. Each scenario in `scenarios/` has:

- **Setup:** what the researcher says or pastes, and at which stage.
- **Planted problem:** the thing Magpie must notice.
- **Pass:** what a passing reply does. A reply can pass in different words;
  the check is on substance.
- **Fail:** the common wrong behaviours.
- **Standards tested:** numbers from `core/standards/`.

## Running them

For now, evals are run by hand: paste the setup into an assistant loaded
with an adapter, and judge the reply against the pass and fail lists. Record
results in a dated file under `evals/runs/` with one line per scenario: pass,
fail, or partial, and a note.

A release fails if any scenario fails. A partial is a fail unless the notes
say why it's acceptable.

Automated running is a later addition and will not change the scenario
format.

## Fixture studies

`fixtures/` holds synthetic studies with a known answer: transcripts, a
researcher's draft with planted problems, and an `ANSWER-KEY.md` that lists
every trap and what a correct reply does. They test the stage 6 and 7 work
the scenarios can only describe: recounting, catching a quote that was
changed or made up, separating single cases from patterns, tying
recommendations to findings. Each fixture's README says how to run it. The
code checks also run against the fixtures in `tools/checks/tests/`, so the
planted quote and count problems they can catch are checked on every
`tools/check.py` run.

Judging a fixture run: count each trap in the key as caught, missed or
partly caught. There is no pass mark; a release note should say which traps
were missed.

## Writing a scenario

Plant one problem per scenario. Make the setup realistic: a real-sounding
product, a real-sounding stakeholder, the kind of mess researchers actually
get. Don't tell Magpie where the problem is.
