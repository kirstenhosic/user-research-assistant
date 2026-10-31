# Magpie on Gemini

## What changed

Phase 4 was going to produce a Gem. When the platform docs were checked on
2026-10-26, Google's help center said Gems are being replaced by skills:
November 2026 for personal Google accounts, March 2027 for Workspace
business accounts, June 2027 for education accounts. Existing Gems are
converted automatically when they're removed. A Gemini skill is a folder
with a `SKILL.md` file plus reference files: the same shape as
`adapters/skill/magpie/`.

## Setup

Skills are available in the Gemini web app, the Mac app and the mobile
apps to signed-in users over 18 with Keep Activity on. Uploading a skill
is web and Mac only. No paid plan is needed for chats.

1. At gemini.google.com, open **Customize** in the sidebar (under **More**
   if you don't see it), then **Skills**.
2. **Create** > **Upload**, and choose `magpie-gemini.zip` from the top of
   the repository. It's the skill folder without `scripts/`. `SKILL.md`
   is in the top folder.
3. Review the name, description and instructions Gemini shows, then
   **Create**.
4. In a chat, type `/magpie` (or `@magpie` with the newer shortcut), or
   just ask for help with a study; Gemini uses active skills automatically.

To update after a new build, open the skill, choose **Replace skill**, and
upload the whole folder again.

## Limits checked

- Total upload at most 100 MB; the package is well under 1 MB.
- Plain-text files only (`.md`, `.py`, `.txt` and similar), and every file
  needs an extension. A file named just `LICENSE` is refused with "The
  skill folder contains a file with an unsupported file type", so the
  build names it `LICENSE.txt`. Found on 2026-10-30.
- Scripts can't use the internet or act on external sites. The three
  checks in `scripts/` read local files only.
- The skill name must be lowercase with hyphens. It's `magpie`.

## What works where

- The independent reviews (questions at stage 6, findings and report at
  stages 7 and 8) run in a fresh chat with a three-part paste, as
  `review-question-review.md` and `review-independent-review.md` describe.
- Gemini won't load a skill that carries code. On a free account on
  2026-10-30, uploading `magpie.zip` (which has `scripts/`) worked, but in
  chat Gemini said the skill "couldn't be loaded because it contains custom
  code scripts" and answered without Magpie's rules. So `magpie-gemini.zip`
  leaves `scripts/` out, and its `SKILL.md` tells Magpie to do the quote,
  count, evidence, review-point and wording checks by hand and say so.
- Word files: with no scripts, Magpie uses Gemini's own way to make a Word
  file if it has one, or tells you to copy the formatted draft into Word.
- Not yet tested: whether Gemini follows Magpie's rules once
  `magpie-gemini.zip` is loaded.

## Checked

- "Create & manage skills for Gemini Apps", Gemini Apps Help, 2026-10-26:
  upload format, limits, name rule, invocation.
- "About the transition from Gems to skills", Gemini Apps Help,
  2026-10-26: dates and conversion.

Not yet tested on Gemini. Please record the first test run in
`evals/runs/`.
