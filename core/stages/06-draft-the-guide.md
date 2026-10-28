# Stage 6: Draft the guide or instrument

Write the thing the researcher will put in front of participants: an
interview guide, a usability test script, a survey, diary prompts, a
focus group guide or a concept test.

## Goal

An instrument that answers the research questions, asks nothing it doesn't
need, and leads nobody.

## Inputs

- The study record through stage 5.
- The method guide from `methods/`.
- The template for the instrument from `templates/`.

## Before you build

Ask for whatever on this list isn't already in the study record, the
conversation or files you can reach, in one message, before you build
(`operating.md`, "Gather context before you build").
This list is the floor: add the questions this particular study or task
raises, within the same six.

**Minimum to draft:** the research questions, and what kind of
instrument it is (interview, usability test, survey or diary).

- The format: moderated or not, remote or in person, and how long each
  session runs.
- What participants will see or use: a prototype, the live product, a
  concept, or nothing.
- Which hypotheses the sessions need to test, and which topics are the
  priority if time runs short.
- The words participants use for the product and its features, if they
  differ from the team's.
- Anything off limits: topics, unreleased features, legal or brand rules.
- Who will run the sessions: the researcher, a teammate, a PM, or an AI
  tool.

## What to do

1. **Map every question to a research question.** Each item in the guide
   should serve a research question from the record. If it doesn't, cut it
   or move it to a "nice to have" list at the end.
2. **Draft from the template.** Opening, warm-up, the main questions, probes,
   closing. For usability tests: scenario, tasks, success criteria, what to
   observe. For surveys: screener, sections, item wording, response scales.
   For diaries: the entry prompt, its required and optional formats, and
   what not to capture (`methods/diary-studies.md`, "Ways to capture
   entries").
   **Write anything the moderator says the way a person speaks:** the
   opening, the warm-up, every question, and a spoken transition each
   time the topic changes ("Thanks, that's really helpful. Now I'd like to
   shift our focus to how you set up your team."). Short sentences the
   moderator can read aloud as written, not headings or notes. Survey and
   diary intros and section openers get the same plain, friendly voice.
3. **Fit it to the product.** Base tasks and scenarios on what the
   product does and the part under study (Product section, if filled, or
   what the researcher has told you), so they match what participants can
   actually do. In anything participants hear, use
   their words, not the team's internal feature names. If it's a
   prototype, say in the moderator notes what works and what doesn't.
4. **Show the map and invite a counter** (`operating.md`, "Show the
   reasoning"). Under the draft, a short table: each question or task,
   the research question it serves, and why it sits where it does (easy
   before hard, what they did before what they think, general before
   specific, sensitive late, tasks ordered so one doesn't give away the
   next). Then one line: "If you'd order it differently or cut something,
   say why and I'll rework it." A counter is new input: rework the guide
   with their reasoning, or say in a line or two why you'd keep it. Their
   call stands.
5. **Run the wording check.** Use `checks/guide-wording.md` for interviews,
   tests, focus groups, concept tests and diary prompts, and
   `checks/survey-wording.md` for surveys. Fix what it catches and say what
   you fixed.
6. **Run the question review** (`review/question-review.md`). It's
   required. Start it in the same reply, without waiting to be asked: start
   a separate agent where you can, otherwise give the researcher the text
   to paste and say when to bring the result back. Fix what it got right
   and say why you disagree with the rest.
7. **Add the moderator notes.** What to do if a participant says "it's fine"
   to everything, runs short, runs long, or gets upset.
8. **Time it.** Estimate the length. If it runs over, say what to cut and
   why those items matter least.
9. **Suggest a pilot.** One or two pilot sessions catch most problems. Say
   what to watch for in the pilot.
10. **Check it works with assistive technology.** If participants use a
   screen reader, magnification or voice control, try the instrument or
   prototype with it before the sessions (`lenses/accessibility.md`).

## What to draft

- The instrument, from the right template, opening with the document
  details, as a Markdown file and a Word file (`operating.md`, "Files for
  the team").
- For interviews, usability tests and diary studies, a note-taking sheet
  (`templates/notes-sheet.md`) as an Excel file: one row per participant,
  one column per research question, and a summary row.
- The question map: what each item serves and why it sits where it does.
- A list of what the wording check and the question review caught and
  changed.
- An updated Instruments section in the study record.

## If an AI tool will moderate

The moderator's instructions are a guide and get the same wording check.
Add the boundaries (what's in and out of scope) and the fallback for
unclear answers ("ask them to say more; don't rephrase or interpret"), and
plan to read the first three transcripts in full before the rest run.
`checks/ai-assisted-research.md`, section 1.

## Challenge

Usually the **guide pressure test**. Example: "Question 4 asks 'how much
easier is the new flow?' That tells people the answer. What if you asked them
to walk you through the last time they used it?"

## Red flags

Always raise a leading, loaded or double-barrelled question, even at "light".

## Exit criteria

- Every item maps to a research question.
- Wording check run and fixes made.
- Question review run and each point fixed or answered, and the status
  line shows it as done. If the researcher is running it in another chat
  and hasn't brought it back, it's listed as waiting in the record and the
  status line.
- Everything the moderator says is written to be said aloud, with a spoken
  transition at each change of topic.
- Moderator notes present.
- The instrument given as a Word file as well as Markdown, or the
  researcher told how to get one, with its document details filled in or
  labelled blank.
- Note-taking sheet given, for interviews, tests and diary studies.
- Pilot planned or deliberately skipped (logged as a risk).

## Pitfalls

- Asking people to predict their future behaviour ("would you use…?") when
  you could ask about their past behaviour.
- Questions that are really the product team's hopes with a question mark.
- A guide so long the best material comes after the participant is tired.
- No probes, so every answer stays at the surface.
- Topic headings with no spoken line, so the moderator improvises the
  transition or skips it and the participant is jolted from one subject to
  the next.
