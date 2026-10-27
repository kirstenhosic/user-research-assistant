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
2. **Create** > **Upload**, and choose the `adapters/skill/magpie/` folder
   or a `.zip` of it. `SKILL.md` must be in the top folder, which it is.
3. Review the name, description and instructions Gemini shows, then
   **Create**.
4. In a chat, type `/magpie` (or `@magpie` with the newer shortcut), or
   just ask for help with a study; Gemini uses active skills automatically.

To update after a new build, open the skill, choose **Replace skill**, and
upload the whole folder again.

## Limits checked

- Total upload at most 100 MB; the package is well under 1 MB.
- Plain-text files only (`.md`, `.py`, `.txt` and similar). The package
  has nothing else.
- Scripts can't use the internet or act on external sites. The two checks
  in `scripts/` read local files only.
- The skill name must be lowercase with hyphens. It's `magpie`.

## What works where

- The independent review at stages 6 and 7 runs in a fresh chat with the
  three-part paste (raw material, draft, review prompt), as
  `review-independent-review.md` describes.
- Whether Gemini runs `scripts/quote_check.py`, `scripts/count_check.py`
  and `scripts/evidence_check.py` hasn't been tested. If it doesn't, Magpie does
  the checks by hand and says so.

## Checked

- "Create & manage skills for Gemini Apps", Gemini Apps Help, 2026-10-26:
  upload format, limits, name rule, invocation.
- "About the transition from Gems to skills", Gemini Apps Help,
  2026-10-26: dates and conversion.

Not yet tested on Gemini. Please record the first test run in
`evals/runs/`.
