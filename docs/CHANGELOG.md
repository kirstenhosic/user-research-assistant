# Changelog

## 2026-10-26

- Lessons from an assessment of the earlier tool (see `docs/PROVENANCE.md`,
  Disclosure): `tools/check.py` maintenance check with fixture tests for the
  code checks; the independent review capped at two passes and told to
  start with the riskiest finding; "a record is not evidence" rule for
  resumed studies; a reader test at stage 7; standards 7.7, 7.8, A.7, A.8
  with three new eval scenarios (PM first time, reader test, record as
  evidence); `core/standards/` no longer shipped in the adapters; a lean
  generic prompt (rules, stages, lenses, checks) for assistants with short
  instruction limits.
- README rewritten for a first-time user: what Magpie does, setup steps
  per tool (Claude Code, Claude.ai, ChatGPT, Gemini, anything else), a
  first conversation, the plain commands, and troubleshooting.
- Sources: nine public sources checked and recorded in `docs/PROVENANCE.md`
  (ICC/ESOMAR code 2025, Braun and Clarke, six Nielsen Norman Group
  articles); 12 standards now cite one in full or in part. The rest stay
  practitioner judgment.
- Phase 4: one skill package at `adapters/skill/magpie/` replaces the
  planned Custom GPT and Gem adapters, since both platforms now take the
  same `SKILL.md` folder format (and are retiring GPTs and Gems). Setup
  notes for Claude, ChatGPT and Gemini under `adapters/`, with the limits
  checked and the date. Scripts moved to `scripts/` inside the skill.
- Phase 3: stages 6 and 7, the independent review, the claim-strength check,
  stakeholder workshops, five more method guides (contextual inquiry, concept
  testing, diary studies, card sorting and tree testing, evidence review),
  readout, report and workshop templates, team profile, intake form and
  library entry, standards for stages 6 to 7, eleven more eval scenarios,
  and two code checks (quotes, counts). Readout and report templates
  reshaped around Kirsten's readout and report principles. A larger-system
  lens (systems thinking, company goals, jobs to be done, journeys and
  personas) added to framing, analysis and readout. Market research as
  indirect evidence, and an optional stage 0 for finding research
  opportunities with an opportunity brief template. A where-to-look guide
  for collecting evidence, with a use-what-you-can-reach rule. Competitive
  analysis added as the eleventh method, with a fit-matrix template.
  Prompts revised against the platforms' current prompt-writing guidance:
  explicit precedence (the researcher wins, two fixed points), rules with
  their reasons, draft-before-asking, specific reply sizing, the review
  prompt reordered to material first, a say-this-not-that voice table, and
  `docs/PROMPT-STYLE.md` recording the conventions and sources.
- Phase 2: operating rules, voice, stages 1 to 5, the challenge bank, three
  checks, three method guides, partner request templates, four instrument
  templates, standards for stages 1 to 5, twelve eval scenarios, and the
  Claude skill adapter.
- Phase 1: design, provenance record, contributing guide, study record
  template, build script and the generic adapter it generates.
