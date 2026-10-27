# Magpie on Claude

The skill folder is `adapters/skill/magpie/`. It's a standard Claude skill:
`SKILL.md` with `name` and `description` in the frontmatter, the core files
beside it, and the code checks in `scripts/`.

## Claude Code

- **In this repo:** nothing to do. The same folder is at
  `.claude/skills/magpie/`, so open the repo and ask for Magpie.
- **In your own project:** unzip `magpie.zip` (from the top of the
  repository) into `.claude/skills/magpie/` in your project, or copy
  `adapters/skill/magpie/` there.

Claude Code can run `scripts/quote_check.py`, `scripts/count_check.py` and
`scripts/evidence_check.py` itself, and can start a separate agent for the independent review at stages
6 and 7.

## Claude.ai

Use a Project, with the same steps as the main README:

1. Add the `.md` files from `magpie.zip` (or `adapters/skill/magpie/`) to the project's
   knowledge. The scripts are optional, since Claude.ai can't run them.
2. Paste the contents of `adapters/skill/magpie/operating.md` (about
   22,000 characters) into the project's instructions.

Don't paste `adapters/generic/system-prompt.md` as the instructions. At
about 200 KB it repeats every file in the knowledge.

Without a code tool, Magpie does the quote and count checks by hand and
says so in the record, and the independent review runs in a fresh chat as
described in `review-independent-review.md`.

## Checked

Claude skill format: `SKILL.md` frontmatter with `name` and `description`,
supporting files loaded on demand (Anthropic engineering post, "Equipping
agents for the real world with Agent Skills"), checked 2026-10-26. Tested
in Claude Code in this repo. Claude.ai not yet tested.
