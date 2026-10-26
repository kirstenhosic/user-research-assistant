# Magpie

Magpie is an open-source research companion for user researchers working in
industry. It takes a study from "do we already know this?" through framing,
study design, the plan and the guide, to analysis and a stakeholder-ready
report. It works in Claude, ChatGPT and Gemini from one shared core.

Why a magpie: it collects the shiny bits of evidence that already exist, then
helps you work out which ones matter for the decision in front of you.

## Status

Early development. Phase 1 (the foundation) is in. Read `docs/DESIGN.md` for
what Magpie is and how it's built, and `docs/PROVENANCE.md` for how it was
made.

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
