# Core

Everything Magpie knows lives here, in plain Markdown. The build script
in `tools/build.py` assembles these files into the adapters for each platform.

| Folder or file | Holds | Status |
| --- | --- | --- |
| `operating.md` | The rules Magpie follows in every conversation; read first | Phase 2 |
| `stages/` | One file per workflow stage, including the optional stage 0 for finding opportunities: goal, inputs, what to draft, challenges, exit criteria | Phase 2–3 |
| `lenses/` | The larger-system lens (systems thinking, company goals, jobs to be done, journeys and personas, market research, finding opportunities) the lens for including disabled people, and the minimum viable research and rigor lens (matching the study to the decision's risk) | Phase 3 |
| `evidence/` | Where to look for each kind of evidence, what Magpie can reach itself, and the paste-in format | Phase 3 |
| `workshops/` | When to run a stakeholder workshop, how to choose its type, and the activities to build it from | Phase 3 |
| `methods/` | One guide per research method, with pitfalls | Phase 2–3 |
| `standards/` | What good looks like per stage, each with its source or marked practitioner judgment; for maintainers and the evals, not shipped in the adapters | Phase 2–3 |
| `challenges/` | The challenge bank | Phase 2 |
| `checks/` | Checklists for guide wording, survey wording, ethics and consent, claim strength, and AI-assisted research (AI moderators, AI summaries, receipts, participant quality) | Phase 2–3 |
| `review/` | The independent review: when it runs and the prompt it uses | Phase 3 |
| `partners/` | Request templates for analytics, field, support and other teams | Phase 2 |
| `templates/` | Study record, plan, interview guide, usability test script, survey, readout, report, workshop agenda and summary, opportunity brief | Phase 1–3 |
| `team/` | Team profile, intake form, research library entry | Phase 3 |
| `voice.md` | Magpie's voice, with example lines | Phase 2 |

Each file starts with a one-sentence description under its title; the build
script uses it to index the Claude skill. The build reads files in the order
above.
