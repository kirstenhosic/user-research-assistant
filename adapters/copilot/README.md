# Magpie on Microsoft 365 Copilot

## Which Copilot

This is for **Cowork** in Microsoft 365 Copilot. Cowork takes a skill
file in the same format as `adapters/skill/magpie/`, so Magpie works
there without changes.

Other Copilot options were checked on 2026-10-27 and not used:

- **Agent Builder agents.** Instructions are limited to 8,000
  characters. `operating.md` alone is about 21,600. You can upload up to
  20 knowledge files, and `.md` isn't on the list of supported types.
  Uploading a skill package is a preview feature for organizations in
  Microsoft's Frontier program only. Getting Magpie to fit would mean
  cutting it down.
- **GitHub Copilot** reads the same `SKILL.md` format, but it's a coding
  tool.
- **The free Copilot app** dropped its GPT Builder in 2024. We found no
  current way there to add instructions this large (checked again
  2026-10-30).
- **Copilot Notebooks** (on Microsoft 365 Personal and Family too) take
  instructions and up to 300 reference files, but not `.md` files, and
  Microsoft doesn't give an instruction length limit. Not set up for
  Magpie yet.

## Who can use Cowork

- **Work or school accounts:** generally available. You need a Microsoft
  Copilot license, and your admin has to turn on Cowork and usage-based
  billing. If you can't find Cowork, ask your IT team.
- **Personal Microsoft accounts:** in preview, on Microsoft 365 Premium or
  Pro only, and only in the US and Canada. Microsoft lists Cowork as "Not
  available" on Microsoft 365 Personal and Family, and says people on those
  plans "will lose access to Cowork".
- **The free Copilot app:** no Cowork and no skills. We found no way there
  to add Magpie (checked 2026-10-30).

At work, check that your employer has approved Copilot for research
material first. See "Using Magpie at work" in the main README.

## Setup

1. Download `magpie-copilot.zip` from the top of the repository, not
   `magpie.zip`. It's the same Magpie with no scripts and with its files
   combined into 18 plus `SKILL.md`, to fit Copilot's file limit (see
   "Limits checked"). `SKILL.md` is at the top level, not inside a folder,
   as Cowork needs.
2. In Cowork, open **Customize**, then the **Skills** tab. Choose the
   arrow next to **Add**, then **Upload skill**, and pick the zip.
3. Cowork checks the file and saves the skill to your OneDrive. When it
   has synced, it shows up under **Your skills**. That can take a few
   moments. Custom skills don't work in Cowork's mobile app, so use the
   web or desktop app.
4. Start a Cowork chat and describe your study, or ask for Magpie by name.

The first time you upload a skill, Cowork reminds you that skills run as
instructions to the AI. `magpie-copilot.zip` holds only text files.

To update after a new build, upload the new zip. If a skill with the same
name is already there, Cowork keeps both and adds a number to the new
one's name. Delete the old one so Copilot doesn't pick it up.

## Limits checked

- Microsoft's two Cowork pages give different limits. "Use Cowork" says a
  skill can include "up to 20 companion files (such as reference documents
  and scripts), with a total of 10 MB per skill". "Customize Copilot
  Cowork" says an archive "can contain up to 100 files", up to 10 MB
  compressed and 50 MB uncompressed. Both say `SKILL.md` can be up to
  1 MB.
- `magpie.zip` now has more than 70 files, so it breaks the 20-file limit
  if that one applies. `magpie-copilot.zip` fits both: 19 files in all,
  `SKILL.md` included. Each original file keeps its name on a
  `<!-- file: name.md -->` line inside the combined file, and `SKILL.md`
  says which combined file holds it.
- The frontmatter needs a `name` and a `description`. Magpie's
  `SKILL.md` has both.

## What works where

- The independent reviews (questions at stage 6, findings and report at
  stages 7 and 8) run in a fresh chat with a three-part paste. The steps
  are in `review-question-review.md` and `review-independent-review.md`,
  which stay as separate files in the Copilot zip.
- No scripts, so Magpie does the quote, count and evidence checks by hand
  and says so in the record.
- Word files: Magpie uses Cowork's own way to make a Word file if it has
  one, or tells you to copy the formatted draft into Word.
- Not yet tested: whether Cowork accepts the upload, and whether Magpie
  follows its rules when its files are combined.

## Checked

- "Get started with Microsoft Copilot Cowork for personal accounts
  (Preview)", Microsoft Support, last updated 2026-10-21; "How AI usage
  works across Microsoft 365 subscriptions for individuals", Microsoft
  Support, last updated October 2026; "Copilot app updates for personal,
  work, and school accounts", Microsoft Support, updated 2026-10-28; all
  checked 2026-10-30: personal-account plans, regions, and Personal and
  Family losing Cowork.
- "Use Copilot Cowork" and "Customize Copilot Cowork", Microsoft Learn,
  both last updated 2026-10-21, checked 2026-10-30: the two different file
  limits, the 1 MB `SKILL.md` limit, and no custom skills on mobile.

- "Customize Copilot Cowork", Microsoft Learn, last updated 2026-09-15,
  checked 2026-10-27: upload path, accepted formats, size limits, the
  duplicate-name rule and the trust reminder.
- "Get started with Cowork", Microsoft Support, last updated 2026-10-21,
  checked 2026-10-27: work and personal availability, license and admin
  requirements.
- "Build agents with Agent Builder" and "Add knowledge sources to an agent
  in Agent Builder", Microsoft Learn, both last updated 2026-09-30,
  checked 2026-10-27: the 8,000-character instruction limit, 20-file
  knowledge limit, supported file types and Frontier-only skills preview.

Not yet tested in Copilot. Please record the first test run in
`evals/runs/`.
