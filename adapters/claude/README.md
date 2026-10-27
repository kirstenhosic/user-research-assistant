# Magpie on Claude

The skill folder is `adapters/skill/magpie/`. It's a standard Claude skill:
`SKILL.md` with `name` and `description` in the frontmatter, the core files
beside it, and the code checks in `scripts/`.

## Claude Code

- **In this repo:** nothing to do. The same folder is at
  `.claude/skills/magpie/`, so open the repo and ask for Magpie.
- **In your own project:** copy `adapters/skill/magpie/` into your
  project's `.claude/skills/` folder.

Claude Code can run `scripts/quote_check.py`, `scripts/count_check.py` and
`scripts/evidence_check.py` itself, and can start a separate agent for the independent review at stages
6 and 7.

## Claude.ai

Upload the files in `adapters/skill/magpie/` to a project, or paste
`adapters/generic/system-prompt.md` as the project's instructions. Without a
code tool, Magpie does the quote and count checks by hand and says so in the
record, and the independent review runs in a fresh chat as described in
`review-independent-review.md`.

## Checked

Claude skill format: `SKILL.md` frontmatter with `name` and `description`,
supporting files loaded on demand (Anthropic engineering post, "Equipping
agents for the real world with Agent Skills"), checked 2026-10-26. Tested
in Claude Code in this repo.
