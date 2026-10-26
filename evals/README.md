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

## Writing a scenario

Plant one problem per scenario. Make the setup realistic: a real-sounding
product, a real-sounding stakeholder, the kind of mess researchers actually
get. Don't tell Magpie where the problem is.
