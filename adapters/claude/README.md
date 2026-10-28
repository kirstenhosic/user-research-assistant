# Magpie on Claude

The skill folder is `adapters/skill/magpie/`. It's a standard Claude skill:
`SKILL.md` with `name` and `description` in the frontmatter, the core files
beside it, and the code checks in `scripts/`.

## Claude Code

- **In this repo:** nothing to do. The same folder is at
  `.claude/skills/magpie/`, so open the repo and ask for Magpie.
- **For all your projects (recommended):** unzip `magpie.zip` (from the
  top of the repository) into your personal skills folder,
  `~/.claude/skills/magpie/`. You can ask Claude Code to do it: "Unzip
  ~/Downloads/magpie.zip into ~/.claude/skills/magpie/".
- **For one project, shared with a team:** unzip it into
  `.claude/skills/magpie/` in that project and commit it, or copy
  `adapters/skill/magpie/` there.

Locations checked against https://code.claude.com/docs/en/skills on
October 28, 2026. Personal skills load in every project on that computer,
but not in Cowork or cloud sessions.

Claude Code can run `scripts/quote_check.py`, `scripts/count_check.py` and
`scripts/evidence_check.py` itself, and can start a separate agent for the independent reviews: the question
review at stage 6 and the findings and report review at stages 7 and 8.
It also runs `scripts/md_to_docx.py`, so guides, surveys, plans and
reports come as a Word file as well as Markdown.

## Claude.ai

Use a Project, with the same steps as the main README:

1. Add the `.md` files from `magpie.zip` (or `adapters/skill/magpie/`) to the project's
   knowledge. The scripts are optional, since Claude.ai can't run them.
2. Paste the contents of `adapters/skill/magpie/operating.md` (about
   22,000 characters) into the project's instructions.

Don't paste `adapters/generic/system-prompt.md` as the instructions. At
about 200 KB it repeats every file in the knowledge.

Without a code tool, Magpie does the quote and count checks by hand and
says so in the record, and the independent reviews run in a fresh chat as
described in `review-question-review.md` and `review-independent-review.md`.
For Word files, Magpie uses Claude.ai's own file creation if your plan has
it turned on (not yet tested with Magpie), or tells you to copy the
formatted draft into Word.

## Checked

Claude skill format: `SKILL.md` frontmatter with `name` and `description`,
supporting files loaded on demand (Anthropic engineering post, "Equipping
agents for the real world with Agent Skills"), checked 2026-10-26. Tested
in Claude Code in this repo. Claude.ai not yet tested.
