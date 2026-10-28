# Prompt style

How the files in `core/` are written, and why. These are the conventions a
change should follow. They come from the prompt-writing guidance the three
target platforms publish, checked on 2026-10-26 (see "Sources" below); that
guidance moves with each model release, so check it again before a large
rewrite.

## Conventions

1. **One structure throughout.** Markdown headings, numbered steps where
   order matters, tables for lookups. No XML tags, no all-caps, no bold
   "IMPORTANT". All three platforms recommend one consistent delimiter
   style, and Markdown is the one a researcher can read too.
2. **The rules come first.** `operating.md` opens every adapter: role,
   what the researcher can override, what stays fixed. Platform guidance
   agrees that persona, hard constraints and output shape belong at the
   start of a system prompt.
3. **Say what to do, then why.** An instruction with its reason ("ask once;
   the log carries the point") generalizes better than a bare rule and far
   better than a bare prohibition. Prohibitions are kept for the few things
   that are genuinely off limits (inventing a source), stated once.
4. **State each instruction once.** Repeating a rule, or escalating its
   wording, makes current models over-apply it. If a rule seems to need
   repeating, make it clearer where it lives instead.
5. **Precedence is explicit.** The researcher's instructions in the
   conversation override the defaults in these files, with the two fixed
   points named in `operating.md`. Without this, a model has to guess
   whether a file or the person wins, and guesses differently each time.
6. **Say exactly what to ask before building, and when to stop asking.**
   Each stage file lists what its output can't be built without, and
   `operating.md` says how to ask for it: once, in one message, six
   questions at most, never for what's already known, and build anyway if
   the researcher says so. Platform guidance generally favors doing the
   work over asking permission. Magpie asks first on purpose, because a
   study's hypotheses, goals and audience are facts a model can't guess,
   and a plausible guess is easy to miss in review. The limits keep the
   asking from turning into a form.
7. **Tone through examples, not adjectives.** `voice.md` shows Magpie's
   voice in example lines and a say-this-not-that table rather than
   labeling it "friendly". Models copy examples; they interpret labels.
8. **Size instructions are specific.** "A reply holds the draft, the
   challenge and the next step" rather than "be concise". Current models
   are concise by default, and a bare brevity instruction can cut what the
   researcher needed.
9. **Long inputs first, questions last.** The independent review prompt
   takes the raw material, then the draft, then the questions, with each
   part labeled. Platform guidance on long context puts the documents
   above the task.
10. **Files are to be opened, scripts are to be run.** The skill intro
    says which is which, and `operating.md` asks Magpie to work from the
    file it's pointed to rather than from memory of it.
11. **No requests for visible reasoning.** The files ask for outputs
    (a draft, a list of problems), not for the model to show its thinking;
    current models reason on their own and some decline a request to
    write it out.
12. **Plain language in the files themselves.** Prompt style matches
    output style. Short sentences and everyday words in `core/` produce
    them in Magpie's replies.

## What this doesn't cover

Platform-specific settings (reasoning effort, verbosity parameters,
temperature) belong to the adapters in Phase 4, not to `core/`. The core
has to read well on all three platforms, so it carries no platform-only
syntax.

## Sources

Checked 2026-10-26. These pages change with each model release.

- Anthropic, "Prompting best practices":
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic, "Prompt engineering overview":
  https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview
- Anthropic Engineering, "Equipping agents for the real world with Agent Skills":
  https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- OpenAI, "Prompt guidance" for current GPT models:
  https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6
- OpenAI Help Center, "Best practices for prompt engineering with the OpenAI API":
  https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api
- Google, Gemini API "Prompt design strategies":
  https://ai.google.dev/gemini-api/docs/prompting-strategies
