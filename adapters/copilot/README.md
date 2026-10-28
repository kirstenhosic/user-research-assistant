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
  current way there to add instructions this large.

## Who can use Cowork

- **Work or school accounts:** generally available. You need a Microsoft
  Copilot license, and your admin has to turn on Cowork and usage-based
  billing. If you can't find Cowork, ask your IT team.
- **Personal Microsoft accounts:** in preview. You need an eligible
  Microsoft 365 subscription.

At work, check that your employer has approved Copilot for research
material first. See "Using Magpie at work" in the main README.

## Setup

1. Download `magpie.zip` from the top of the repository. It has
   `SKILL.md` at the top level, not inside a folder, as Cowork needs.
   To make your own instead, open `adapters/skill/magpie/`, select
   everything inside it, and compress that selection. Don't zip the
   `magpie` folder itself.
2. In Cowork, open **Customize**, then the **Skills** tab. Choose the
   arrow next to **Add**, then **Upload skill**, and pick the zip.
3. Cowork checks the file and saves the skill to your OneDrive. When it
   has synced, it shows up under **Your skills**. That can take a few
   moments.
4. Start a Cowork chat and describe your study, or ask for Magpie by name.

The first time you upload a skill, Cowork reminds you that skills run as
instructions to the AI. Magpie's only code is three scripts in `scripts/`.
They read files you give them and don't connect to the internet.

To update after a new build, upload the new zip. If a skill with the same
name is already there, Cowork keeps both and adds a number to the new
one's name. Delete the old one so Copilot doesn't pick it up.

## Limits checked

- Archive: up to 10 MB compressed, 50 MB uncompressed and 100 files.
  Magpie is about 110 KB zipped, about 220 KB unzipped, and 52 files
  (measured 2026-10-27).
- The frontmatter needs a `name` and a `description`. Magpie's
  `SKILL.md` has both.

## What works where

- The independent reviews (questions at stage 5, findings and report at
  stages 6 and 7) run in a fresh chat with a three-part paste. The steps
  are in `review-question-review.md` and `review-independent-review.md`.
- We haven't tested whether Cowork runs `scripts/quote_check.py`,
  `scripts/count_check.py` and `scripts/evidence_check.py`. If it doesn't,
  Magpie does the checks by hand and says so.
- Word files: `scripts/md_to_docx.py` turns a guide, survey, plan or
  report into a .docx using only Python. Whether Cowork runs it hasn't been
  tested. If it doesn't, Magpie uses Cowork's own way to make a Word file if
  it has one, or tells you to copy the formatted draft into Word.

## Checked

- "Customize Copilot Cowork", Microsoft Learn, last updated 2026-09-15,
  checked 2026-10-27: upload path, accepted formats, size limits, the
  duplicate-name rule and the trust reminder.
- "Get started with Cowork", Microsoft Support, last updated 2026-10-21,
  checked 2026-10-27: work and personal availability, licence and admin
  requirements.
- "Build agents with Agent Builder" and "Add knowledge sources to an agent
  in Agent Builder", Microsoft Learn, both last updated 2026-09-30,
  checked 2026-10-27: the 8,000-character instruction limit, 20-file
  knowledge limit, supported file types and Frontier-only skills preview.

Not yet tested in Copilot. Please record the first test run in
`evals/runs/`.
