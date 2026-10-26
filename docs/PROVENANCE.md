# Provenance

This file records how this project was made, so anyone can check that it was
developed independently. It is updated whenever a new source is used or a new
tool joins the work.

## Origin

- Magpie was started on 26 October 2026 by Kirsten Hosic, in a new public repository on
  a personal GitHub account.
- Built with the help of an AI coding assistant (Claude, by Anthropic). The
  design was drafted in conversation, then written into this repository as the
  first substantive commit (`docs/DESIGN.md`).
- The author has previously built a separate UX research assistant in the
  course of employment. This project is a fresh design with its own
  architecture, vocabulary, templates and test cases.

## What was not used

- No prompts, code, templates, scenarios, test cases or documentation from any
  earlier research assistant were read, copied, paraphrased or adapted while
  designing or building this project.
- No employer-internal material of any kind was used.

## Disclosure

During the design conversation, the AI assistant's working context included a
one-paragraph description of the structure of the author's earlier tool (a
named mentor persona backed by separate reviewer agents). That description was
the only exposure. No prompts, code or content from that tool were opened. The
design here differs on purpose: there is no persona, continuity comes from a
portable study record, accuracy rests on grounding rules and code checks, and
an independent review runs only on analysis and final reports.

## Public sources

Sources are listed here only after they have been checked and actually used.
Each standard in `core/standards/` links to its entry in this list or is
marked as practitioner judgment.

| Source | Used for | Checked on |
| --- | --- | --- |
| (none yet) | | |

Candidates to check before Phase 2, not yet verified or used: Braun and
Clarke (2006) on thematic analysis; Steve Portigal, *Interviewing Users*;
Erika Hall, *Just Enough Research*; Dillman, Smyth and Christian on the
tailored design method for surveys; Nielsen Norman Group articles on usability
testing; the ICC/ESOMAR code on market, opinion and social research; ISO
9241-210 on human-centred design.

## Tools used

| Tool | Role |
| --- | --- |
| Claude (Anthropic) | Drafting the design and the first build in conversation with the author |
| Git and GitHub | Version history, which is itself part of this record |
| Python 3 | The build script in `tools/` |
