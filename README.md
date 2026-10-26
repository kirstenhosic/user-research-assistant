# Magpie

Magpie is an open-source research companion for user researchers working in
industry. It takes a study from "do we already know this?" through framing,
study design, the plan and the guide, to analysis and a stakeholder-ready
report. It works in Claude, ChatGPT and Gemini from one shared core.

Why a magpie: it collects the shiny bits of evidence that already exist, then
helps you work out which ones matter for the decision in front of you.

## Status

Early development. Phases 1 to 4 are in: Magpie covers the whole workflow,
from existing evidence through framing, method choice, the plan and the
guide, to analysis, readout and report, with stakeholder workshops as a
branch. Eleven methods, including competitive analysis. One skill package
works on Claude, ChatGPT and Gemini; it has been tested on Claude Code and
still needs a test run on the other two. Read `docs/DESIGN.md` for what
Magpie is and how it's built, and `docs/PROVENANCE.md` for how it was made.

## Using it

Magpie ships as one skill folder, `adapters/skill/magpie/`, in the
`SKILL.md` format that Claude, ChatGPT and Gemini all accept.

- **Claude Code, in this repo:** open the repo and ask for Magpie or for
  help with a study. The skill is already at `.claude/skills/magpie/`.
- **Claude Code or Claude.ai:** see `adapters/claude/README.md`.
- **ChatGPT:** see `adapters/chatgpt/README.md`.
- **Gemini:** see `adapters/gemini/README.md`.
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
docs/       design, provenance, contributing, prompt style, changelog
```

To regenerate the adapters after changing the core:

```
python3 tools/build.py
```

Licensed under the MIT License. See `LICENSE`.
