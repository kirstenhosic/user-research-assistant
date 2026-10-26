# Core

Everything Magpie knows lives here, in plain Markdown. The build script
in `tools/build.py` assembles these files into the adapters for each platform.

| Folder or file | Holds | Status |
| --- | --- | --- |
| `operating.md` | The rules Magpie follows in every conversation; read first | Phase 2 |
| `stages/` | One file per workflow stage: goal, inputs, what to draft, challenges, exit criteria | Stages 1–5 in Phase 2; 6–7 in Phase 3 |
| `workshops/` | Agenda patterns and activities for stakeholder workshops | Phase 3 |
| `methods/` | One guide per research method, with pitfalls | Interviews, usability testing, surveys in Phase 2; the rest in Phase 3 |
| `standards/` | What good looks like per stage, each with its source or marked practitioner judgment | Stages 1–5 in Phase 2 |
| `challenges/` | The challenge bank | Phase 2 |
| `checks/` | Checklists for guide wording, survey wording, ethics and consent; claim strength in Phase 3 | Phase 2 |
| `partners/` | Request templates for analytics, field, support and other teams | Phase 2 |
| `templates/` | Study record, plan, interview guide, usability test script, survey; readout, report and workshop agenda in Phase 3 | Phase 1–2 |
| `team/` | Team profile, intake form, research library entry | Phase 3 |
| `voice.md` | Magpie's voice, with example lines | Phase 2 |

Each file starts with a one-sentence description under its title; the build
script uses it to index the Claude skill. The build reads files in the order
above.
