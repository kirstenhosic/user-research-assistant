# Evals

Test scenarios with planted problems. Each scenario in `scenarios/` has:

- **Setup:** what the researcher says or pastes, and at which stage.
- **Planted problem:** the thing Magpie must notice.
- **Pass:** what a passing reply does. A reply can pass in different words;
  the check is on substance.
- **Fail:** the common wrong behaviours.
- **Standards tested:** numbers from `core/standards/`.

## Running them

For now, evals are run by hand: start a fresh session with an adapter,
paste the setup, and judge the reply against the pass and fail lists.
Copy `runs/TEMPLATE.md` to a dated file under `runs/` and fill it in.

A run counts only if it could have failed. These rules make sure it can.

1. **Make sure Magpie is running.** Start each session by calling Magpie
   explicitly (in Claude Code, begin the message with `/magpie`). A skill
   sitting in a folder isn't the same as a skill in use: in one re-test,
   sessions answered as plain Claude because the skill was never invoked.
   Then check the proof: the reply opens with the "Magpie is on" line and
   ends with the status line (`core/operating.md`, "The session"), and,
   where the platform shows a trace, the trace shows the skill files being
   read. No proof, no result: mark the run void and run it again.
2. **Check that the check works.** Once per eval run, run one scenario
   with Magpie left out on purpose. The loading check in step 1 must catch
   it. If it doesn't, the check is broken and the run's results don't
   count.
3. **Keep the answers out of the session.** The session gets the adapter
   and the setup, nothing else: no scenario file, no answer key, no fixture
   README, no project notes or memory the assistant can read. Where the
   tool loads notes or memory on its own, turn that off for the run.
4. **Run each scenario three times.** Replies vary from run to run, and an
   error can show up in one run of three. Record each run's result
   ("pass, pass, partial"). A scenario passes only if all three pass.
5. **Have a person judge.** A model judge from the same family as the
   assistant may judge kindly. For every release, a person judges at least
   ten replies, chosen to include every partial and a spread of passes,
   without seeing the model judge's verdict first. Record both verdicts
   and how often they agree. Where they differ, the person's verdict
   stands. Where you can, use a model from a different family as the model
   judge.
6. **Keep the replies.** Save every reply somewhere private, outside this
   repository (they'd leak the scenarios), so anyone can re-judge them.
   The run file says where.

A release fails if any run of any scenario fails. A partial is a fail
unless the notes say why it's acceptable.

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
were missed. Give the session only the files the fixture's README lists
under "How to run", never the README itself or the key.

One fixture, `fixtures/sparrow-clean/`, has no traps at all. Its draft is
correct, and the test is whether Magpie leaves it alone: every change
Magpie proposes is counted as a false alarm. The target is zero. Without
it, a Magpie that flagged everything would score well on the other
fixtures.

## Writing a scenario

Plant one problem per scenario. Make the setup realistic: a real-sounding
product, a real-sounding stakeholder, the kind of mess researchers actually
get. Don't tell Magpie where the problem is.
