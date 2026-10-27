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

On 26 October 2026, at the author's request, a short qualitative assessment
of the earlier tool's strengths and weaknesses was shared with the assistant
building Magpie and used as design input. It was a list of abstract points
prepared in a separate review of that tool (for example, "checks run in a
fresh context", "too many questions before any work", "prompts are heavy"),
not its source, prompts, templates or structure, and nothing from the
earlier tool was read. The changes it led to are listed in
`docs/CHANGELOG.md` under that date as "Lessons from an assessment of the
earlier tool".

## Public sources

Sources are listed here only after they have been checked and actually used.
Each standard in `core/standards/` links to its entry in this list or is
marked as practitioner judgment.

"Checked" means the text was read on that date and the standard's claim was
found in it, not that the source was merely located. Where only the citation
could be confirmed, the row says so. Where a passage was supplied by the
author from a copy the assistant can't open (a Kindle book), the row says
that too, and only the supplied passage counts as read. Supplied passages
are paraphrased in the core, never reproduced.

| # | Source | Used for | Checked on |
| --- | --- | --- | --- |
| S1 | Braun, V. and Clarke, V. (2006). "Using thematic analysis in psychology." *Qualitative Research in Psychology*, 3(2), 77–101. doi:10.1191/1478088706qp063oa | Citation confirmed from the publisher record; full text not read. Not yet cited by a standard. | 2026-10-26 |
| S1b | Braun, V. and Clarke, V. (2022). "Everything changes… well some things do: Reflections on, and resources for, reflexive thematic analysis." *QMiP Bulletin* (British Psychological Society). Open copy in the UWE repository. | 6.1: the six phases; a theme is a shared meaning, not a topic summary | 2026-10-26 |
| S2 | ICC/ESOMAR *International Code on Market, Opinion and Social Research and Data Analytics*, 2025 revision. https://standards.esomar.org/resources/international-codes | 4.3 (Art. 4(a)(iii) consent, 4(a)(v) retention, 6(d) security, 6(e) deletion); 6.2 (Art. 9(d)); 6.3 and 6.5 (Art. 9(c)); 7.4 (Art. 9(a)); the vulnerable-participant red flag (Art. 1(b), 2(a), 2(b), 2(d)) | 2026-10-26 |
| S3 | McCloskey, M. (2014). "Turn User Goals into Task Scenarios for Usability Testing." Nielsen Norman Group. https://www.nngroup.com/articles/task-scenarios-usability-testing/ | 5.4: tasks as realistic, actionable scenarios free of clues | 2026-10-26 |
| S4 | Schade, A. (2017). "Avoid Leading Questions to Get Better Insights from Participants." Nielsen Norman Group. https://www.nngroup.com/articles/leading-questions/ | 5.2: what a leading question is and how to neutralize it | 2026-10-26 |
| S5 | Rosala, M. (2022). "6 Mistakes When Crafting Interview Questions." Nielsen Norman Group. https://www.nngroup.com/articles/interview-questions-mistakes/ | 5.2 (leading clarifiers, compound questions); 5.3 (hypotheticals vs past experience) | 2026-10-26 |
| S6 | Brown, M. (2023). "Writing Good Survey Questions: 10 Best Practices." Nielsen Norman Group. https://www.nngroup.com/articles/survey-best-practices/ | 5.1 (ask only what the research questions need); 5.2 (neutral wording, no double-barrelled items); 5.3 (past behaviour, not predictions); 5.5 (balanced scales) | 2026-10-26 |
| S7 | Nielsen, J. (2001). "First Rule of Usability? Don't Listen to Users." Nielsen Norman Group. https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/ | Background for the behavioural emphasis in `methods/usability-testing.md`; not cited by a standard | 2026-10-26 |
| S8 | Laubheimer, P. (2024). "Attitudinal vs. Behavioral Research in UX." Nielsen Norman Group. https://www.nngroup.com/articles/attitudinal-behavioral/ | 5.3: self-reports of past habits and future intentions are unreliable; observe actions | 2026-10-26 |
| S9 | Brown, M. (2024). "Screening Participants for User-Research Studies." Nielsen Norman Group. https://www.nngroup.com/articles/screening-participants/ | 4.1: criteria tied to the research questions, behavioural over demographic, past behaviour not predicted | 2026-10-26 |
| S10 | Papas, C. (2026). *AI-Powered UX Research*. The Voice of User (Kindle edition, 15 July 2026; print edition, 27 August 2026). Chapter 3, "Where the tools break", pp. 57–63 (page numbers as given by the supplier of the passage; they may differ between editions). Publication details were supplied by Kirsten Hosic from the retailer listing, not checked against the book's copyright page. The passage on five failure modes of AI research tools (AI moderators shaping answers, overclaiming from AI summaries, a thin evidence trail, moderation going off-script, participant quality) with their mitigations was supplied by Kirsten Hosic from her copy on 2026-10-27; the text of the passage was read, the rest of the book was not. | 4.5, 5.6, 6.10, 7.9; `core/checks/ai-assisted-research.md` | 2026-10-27 |
| S11 | Rohrer, C. (2022, reviewed 2026). "When to Use Which User-Experience Research Methods." Nielsen Norman Group. https://www.nngroup.com/articles/which-ux-research-methods/ | 3.2 (qualitative for why and how to fix, quantitative for how many and how much); 3.3 in part (attitudinal methods limited to what people are aware of and will report) | 2026-10-27 |
| S12 | Budiu, R. (2021). "Why You Cannot Trust Numbers from Qualitative Usability Studies." Nielsen Norman Group. https://www.nngroup.com/articles/true-score/ | 6.8: report the sample size, compute the interval, test before claiming a difference; small samples give large error | 2026-10-27 |
| S13 | Whitenton, K. (2021). "Triangulation: Get Better Research Results by Using Multiple UX Methods." Nielsen Norman Group. https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/ | 3.3 in part (one method's limits are mitigated by another source); 6.6 in part (check whether other data supports a result) | 2026-10-27 |
| S14 | Moran, K. (2019). "Interpreting Contradictory UX Research Findings." Nielsen Norman Group. https://www.nngroup.com/articles/interpreting-research-findings/ | 6.6 in part: quantitative data should never automatically overrule qualitative; examine how each study was conducted | 2026-10-27 |
| S15 | Harley, A. (2017). "Ideation in Practice: How Effective UX Teams Generate Ideas." Nielsen Norman Group. https://www.nngroup.com/articles/ideation-in-practice/ | W.2: written ideation, in which people document ideas individually before the group, avoids groupthink and unbalanced contributions (survey evidence, correlational) | 2026-10-27 |
| S16 | Kaplan, K. (2021). "How to Handle Dominating Participants in UX Workshops: 3 Tactics." Nielsen Norman Group. https://www.nngroup.com/articles/dominating-workshop-participants/ | W.2: silent post-up and brainwriting so contributions come from the whole group | 2026-10-27 |
| S17 | Kaplan, K. (2017). "Planning Effective UX Workshop Agendas." Nielsen Norman Group. https://www.nngroup.com/articles/ux-workshop-agendas/ | W.1: articulate the goal as a short description of the ideal end state before anything else | 2026-10-27 |
| S18 | Azarova, M. (2022). "Secondary Research in UX." Nielsen Norman Group. https://www.nngroup.com/articles/secondary-research-in-ux/ | 1.1 in part (identify each source's validity and limitations; a missing methods section is a red flag); 3.1 in part (secondary research as a standard first step) | 2026-10-27 |
| S19 | Government Digital Service. "Plan user research for your service." GOV.UK Service Manual, updated 15 October 2026. https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service | 2.3 (be clear what questions each round answers and how it helps the team decide); 2.1 in part | 2026-10-27 |
| S20 | Government Digital Service. "Sharing user research findings." GOV.UK Service Manual, updated 9 September 2026. https://www.gov.uk/service-manual/user-research/sharing-user-research-findings | 7.1 in part: one or two slides on the research done, five to ten findings slides each with a headline and evidence, one or two on next steps | 2026-10-27 |
| S21 | Krause, R. (2022). "Creating Engaging Reports & Asynchronous Presentations." Nielsen Norman Group. https://www.nngroup.com/articles/engaging-reports-presentations/ | 7.3a in part: structure for three kinds of reader (headlines, themes, in-depth detail) | 2026-10-27 |
| S22 | Klein, L. (2026). "How to Get Research Recommendations on the Roadmap." Nielsen Norman Group. https://www.nngroup.com/articles/research-recommendations-roadmap/ | 7.2 in part (start from the finding, connect to what the PM is measured on, suggest something concrete); 2.2 in part | 2026-10-27 |
| S23 | Schade, A. (2013). "Making Usability Findings Actionable." Nielsen Norman Group. https://www.nngroup.com/articles/actionable-usability-findings/ | 7.2 in part: findings specific to the design element, ranked by severity, recommendations labelled as such | 2026-10-27 |
| S24 | Neusesser, T. (2024). "Competitive Usability Evaluations." Nielsen Norman Group. https://www.nngroup.com/articles/competitive-usability-evaluations/ | 3.4: key tasks completable across products; tangentially related businesses offer perspective; "beat the competition, not copy them"; observe what users do | 2026-10-27 |
| S25 | Tankala, S. (2023). "UX & Marketing: Balancing Business Goals and Supporting Users." Nielsen Norman Group. https://www.nngroup.com/articles/ux-and-marketing/ | 0.3 in part: marketing's audience can differ from UX's (buyers vs users); marketing relies on self-report, UX on observed behaviour | 2026-10-27 |
| S26 | Cabinet Office and Government Digital Service (2013). "GOV.UK content principles: conventions and research background." https://www.gov.uk/government/publications/govuk-content-principles-conventions-and-research-background/govuk-content-principles-conventions-and-research-background | A.4: short sentences and paragraphs, simple everyday words, no jargon, spell out acronyms, with the research it cites (Joiner 2002, Spyridakis 2000, Summers et al.) | 2026-10-27 |
| S27 | Samsonov, P. (2025). "In User Research, Don't Stop at 'Yes' or 'No'." Nielsen Norman Group. https://www.nngroup.com/articles/research-yes-or-no/ | 2.1 and 2.3 in part: the purpose of research is to inform decisions; research observes behaviour and needs rather than validating a yes/no | 2026-10-27 |
| S28 | Government Digital Service. "Finding participants for user research." GOV.UK Service Manual, updated 22 September 2026. https://www.gov.uk/service-manual/user-research/find-user-research-participants | 4.2 in part: research with all the different kinds of people who may need the service, including those with limited digital skills or literacy | 2026-10-27 |
| S29 | Rosala, M. (2021, reviewed 2026). "Problem Statements in UX Discovery." Nielsen Norman Group. https://www.nngroup.com/articles/problem-statements/ | 2.3 in part: scope research to the problem; investigating only solutions is not discovery | 2026-10-27 |
| S30 | Kaplan, K. (2019, reviewed 2023). "5 UX Workshops and When to Use Them: A Cheat Sheet." Nielsen Norman Group. https://www.nngroup.com/articles/5-ux-workshops/ | W.1 in part: each workshop type is defined by the outcome it produces | 2026-10-27 |

Located but not read, so not cited: Dillman, D. A., Smyth, J. D. and
Christian, L. M. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys: The
Tailored Design Method*, 4th ed., Wiley (record confirmed in WorldCat; the
chapters on question writing would likely support 5.2 and 5.5 but have not
been checked).

Read on 2026-10-27 but not cited, because they did not support a standard
as written: Nielsen, "Strength of User Research Evidence" (2013); Moran,
"Quantitative UX Research in Practice" (2018); Rosala, "Why Research
Repositories Fail" (2024); Nielsen, "Acting on User Research" (2004);
Rosala, "Research Plans: Organize, Document, Inform" (2024); GOV.UK Service
Manual, "Analyse a research session" (2016); Digital.gov plain language
guides (2025, index pages only).

Books (Portigal, Hall, ISO 9241-210, the full text of S1) are not on the
list to check: the sourcing effort is limited to material that can be read
on the open web.

Standards with no source yet keep "practitioner judgment" as their basis.
Current count: 34 of 60 standards cite a source in full or in part.

## Tools used

| Tool | Role |
| --- | --- |
| Claude (Anthropic) | Drafting the design and the first build in conversation with the author |
| Git and GitHub | Version history, which is itself part of this record |
| Python 3 | The build script in `tools/` |
