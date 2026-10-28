# Magpie on ChatGPT

## What changed

Phase 4 was going to produce a Custom GPT. When the platform docs were
checked on 2026-10-26, OpenAI's help center said personal accounts (Free,
Go, Plus, Pro) can no longer create or publish GPTs, and that Custom GPTs
are being retired (December 11, 2026 for affected Enterprise workspaces,
other plans "expected to follow"). The replacement is skills and plugins.
A ChatGPT skill is a folder with a `SKILL.md` file plus supporting files
and scripts: the same shape as `adapters/skill/magpie/`.

## Business, Enterprise, Healthcare and Edu workspaces

These are the accounts OpenAI's "Skills in ChatGPT" page lists as having
skills, subject to workspace settings.

1. In the ChatGPT sidebar, open **Plugins**, then the **Skills** tab.
2. **Create** > **Upload from your computer** and upload
   `magpie.zip` from the top of the repository, or the
   `adapters/skill/magpie/` folder if the zip is refused (the help page
   doesn't say which it takes).
3. ChatGPT scans the upload. If it's marked **Needs Review**, read what it
   flags; the only code in the package is the three checks in `scripts/`,
   which read local files and use no network.
4. Install it. ChatGPT uses it automatically when a request matches the
   description, or you can @-mention `magpie`.
5. Share from the skill's menu if your workspace allows it.

## Personal accounts

OpenAI's skills page doesn't mention personal plans, so as of the check
date it's unverified whether a Plus or Pro account can upload a skill. If
yours can't, use a Project, the same way as the main README's fallback:
paste `adapters/skill/magpie/operating.md` as the project instructions
and add the other `.md` files from `adapters/skill/magpie/` as project
files. (The Projects help page couldn't be read during the check, so its
instruction and file limits are unverified.)

## What works where

- The independent reviews (questions at stage 5, findings and report at
  stages 6 and 7): ChatGPT has no separate-agent step in a skill, so
  Magpie gives you the three-part paste for a fresh chat, as
  `review-question-review.md` and `review-independent-review.md` describe.
- The quote and count checks: OpenAI's skill docs allow scripts in
  `scripts/`. Whether ChatGPT runs these two hasn't been tested; if it
  doesn't, Magpie does the checks by hand and says so.

## Checked

- "Creating and editing GPTs" and "GPTs in ChatGPT", OpenAI Help Center,
  2026-10-26: GPT creation closed to personal plans; retirement dates.
- "Skills in ChatGPT", OpenAI Help Center, 2026-10-26: eligible plans,
  upload path, scanning, sharing.
- "Build skills" and "Skills" (plugins concepts), OpenAI developer docs,
  2026-10-26: `SKILL.md` with `name` and `description`; optional
  `references/`, `scripts/`, `assets/`.

Not yet tested on ChatGPT. Please record the first test run in
`evals/runs/`.
