# Core

Everything Magpie knows lives here, in plain Markdown. The build script
in `tools/build.py` assembles these files into the adapters for each platform.

| Folder or file | Holds | Status |
| --- | --- | --- |
| `stages/` | One file per workflow stage: goal, inputs, what to draft, challenges, exit criteria | Phase 2 |
| `workshops/` | Agenda patterns and activities for stakeholder workshops | Phase 3 |
| `methods/` | One guide per research method, with pitfalls | Phase 2–3 |
| `standards/` | What good looks like per stage, each with its source | Phase 2 |
| `challenges/` | The challenge bank | Phase 2 |
| `checks/` | Checklists for guide wording, survey wording, claim strength, ethics and consent | Phase 2 |
| `partners/` | Request templates for analytics, field, support and other teams | Phase 2 |
| `templates/` | Study record, plan, guides, survey, readout, report, workshop agenda | Phase 1 onward |
| `team/` | Team profile, intake form, research library entry | Phase 3 |
| `voice.md` | The assistant's voice, with example lines | Phase 2 |

Each file starts with a one-line description under its title. The build
script reads folders in the order above.
