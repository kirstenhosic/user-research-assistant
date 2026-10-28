# Eval run, 2026-10-28 (diary capture options)

One new scenario, run live after the diary capture section was added.

## How it was run

- **Adapter and commit:** `adapters/skill/magpie/` at 7d643f2
- **Assistant and platform:** Claude Code (`claude -p`), in a cloud container
- **How Magpie was started:** `/magpie` plus the scenario setup as the first
  message; second message: "I don't have answers to those right now. Go
  ahead with your best guesses."
- **Answers kept out:** each run in a fresh empty folder holding only the
  skill; memory settings removed from the environment
- **Loading check failed on purpose:** not run this time
- **Model judge:** Claude, the same model family that wrote the change
- **Person judging:** not yet
- **Replies saved at:** the project's shared files, `eval-runs/2026-10-28-diary-capture/`

## Results

| Scenario | Run 1 | Run 2 | Run 3 | Loaded (3 of 3?) | Note |
| --- | --- | --- | --- | --- | --- |
| diary-capture-options | pass | pass | pass | yes | See notes |

**Totals:** 1 scenario passes in all three runs, 0 have a partial, 0 have a fail.

## Notes

- Every run asked six questions first (including what the PM wants to
  "really see", devices and screen readers, and data rules), then built
  with gaps marked [assumption] when told to go ahead.
- Every run turned down video for every failure, with the sums (600 to
  1,680 entries), and proposed a light required core (typed or voice
  note, word-labelled rating with "what made you pick that?") and
  optional video or screen recording. None made video the only way in.
- Every run covered what not to capture (customers, house numbers,
  parcel labels), one-to-one chats rather than a group, safety (no entries
  while driving), testing the form and WhatsApp with a screen reader in
  the pilot, and the drivers' dependent relationship with the company.
- No run asked about pasting transcripts into AI tools.
- Small wobbles, not fails: run 2 said video is "off the table" for the
  two screen-reader drivers, which assumes what they can do (the
  accessibility lens says ask); run 3 had one muddled line about WhatsApp
  group chats before getting it right.
