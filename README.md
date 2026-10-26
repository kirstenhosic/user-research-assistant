# Magpie

Magpie is an open-source research companion for user researchers working in
industry. It takes a study from "do we already know this?" through framing,
study design, the plan and the guide, to analysis and a stakeholder-ready
report. It works in Claude, ChatGPT and Gemini from one shared core.

Why a magpie: it collects the shiny bits of evidence that already exist, then
helps you work out which ones matter for the decision in front of you.

## Status

Early development. Phases 1 and 2 are in: Magpie can take a study from
existing evidence through framing, method choice, the plan and the guide
(interviews, usability tests, surveys). Analysis, reporting and the other
methods come next. Read `docs/DESIGN.md` for what Magpie is and how it's
built, and `docs/PROVENANCE.md` for how it was made.

## Using it

- **Claude:** add the folder `adapters/claude/skills/magpie/` as a skill
  (in Claude Code, copy it to `.claude/skills/`). Then ask for Magpie or
  for help with a study.
- **Any other assistant:** paste `adapters/generic/system-prompt.md` as the
  system prompt or custom instructions. If it's too long for the platform,
  paste `core/operating.md` and `core/voice.md` as instructions and upload
  the files in `adapters/generic/files/`.
- Save the study record Magpie keeps for you; it's how you pick up where
  you left off, in any assistant.

## Layout

```
core/       everything Magpie knows, in plain Markdown (edit here)
adapters/   generated packages for each platform (don't edit)
tools/      the build script
evals/      test scenarios with planted problems
docs/       design, provenance, contributing, changelog
```

To regenerate the adapters after changing the core:

```
python3 tools/build.py
```

Licensed under the MIT License. See `LICENSE`.
