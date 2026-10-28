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
independent reviews run only on guides and surveys, analysis, and final reports.

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
| S1b | Braun, V. and Clarke, V. (2022). "Everything changes… well some things do: Reflections on, and resources for, reflexive thematic analysis." *QMiP Bulletin* (British Psychological Society). Open copy in the UWE repository. | 7.1: the six phases; a theme is a shared meaning, not a topic summary | 2026-10-26 |
| S2 | ICC/ESOMAR *International Code on Market, Opinion and Social Research and Data Analytics*, 2025 revision. https://standards.esomar.org/resources/international-codes | 5.3 (Art. 4(a)(iii) consent, 4(a)(v) retention, 6(d) security, 6(e) deletion); 7.2 (Art. 9(d)); 7.3 and 7.5 (Art. 9(c)); 8.4 (Art. 9(a)); the vulnerable-participant red flag (Art. 1(b), 2(a), 2(b), 2(d)) | 2026-10-26 |
| S3 | McCloskey, M. (2014). "Turn User Goals into Task Scenarios for Usability Testing." Nielsen Norman Group. https://www.nngroup.com/articles/task-scenarios-usability-testing/ | 6.4: tasks as realistic, actionable scenarios free of clues | 2026-10-26 |
| S4 | Schade, A. (2017). "Avoid Leading Questions to Get Better Insights from Participants." Nielsen Norman Group. https://www.nngroup.com/articles/leading-questions/ | 6.2: what a leading question is and how to neutralize it | 2026-10-26 |
| S5 | Rosala, M. (2022). "6 Mistakes When Crafting Interview Questions." Nielsen Norman Group. https://www.nngroup.com/articles/interview-questions-mistakes/ | 6.2 (leading clarifiers, compound questions); 6.3 (hypotheticals vs past experience) | 2026-10-26 |
| S6 | Brown, M. (2023). "Writing Good Survey Questions: 10 Best Practices." Nielsen Norman Group. https://www.nngroup.com/articles/survey-best-practices/ | 6.1 (ask only what the research questions need); 6.2 (neutral wording, no double-barrelled items); 6.3 (past behaviour, not predictions); 6.5 (balanced scales) | 2026-10-26 |
| S7 | Nielsen, J. (2001). "First Rule of Usability? Don't Listen to Users." Nielsen Norman Group. https://www.nngroup.com/articles/first-rule-of-usability-dont-listen-to-users/ | Background for the behavioural emphasis in `methods/usability-testing.md`; not cited by a standard | 2026-10-26 |
| S8 | Laubheimer, P. (2024). "Attitudinal vs. Behavioral Research in UX." Nielsen Norman Group. https://www.nngroup.com/articles/attitudinal-behavioral/ | 6.3: self-reports of past habits and future intentions are unreliable; observe actions; 4.10 in part | 2026-10-26 |
| S9 | Brown, M. (2024). "Screening Participants for User-Research Studies." Nielsen Norman Group. https://www.nngroup.com/articles/screening-participants/ | 5.1: criteria tied to the research questions, behavioural over demographic, past behaviour not predicted | 2026-10-26 |
| S10 | Papas, C. (2026). *AI-Powered UX Research*. The Voice of User (Kindle edition, 15 July 2026; print edition, 27 August 2026). Chapter 3, "Where the tools break", pp. 57–63 (page numbers as given by the supplier of the passage; they may differ between editions). Publication details were supplied by Kirsten Hosic from the retailer listing, not checked against the book's copyright page. The passage on five failure modes of AI research tools (AI moderators shaping answers, overclaiming from AI summaries, a thin evidence trail, moderation going off-script, participant quality) with their mitigations was supplied by Kirsten Hosic from her copy on 2026-10-27; the text of the passage was read, the rest of the book was not. | 5.5, 6.6, 7.10, 8.9; `core/checks/ai-assisted-research.md` | 2026-10-27 |
| S11 | Rohrer, C. (2022, reviewed 2026). "When to Use Which User-Experience Research Methods." Nielsen Norman Group. https://www.nngroup.com/articles/which-ux-research-methods/ | 4.2 (qualitative for why and how to fix, quantitative for how many and how much); 4.3 in part (attitudinal methods limited to what people are aware of and will report); 4.10 (the three dimensions and the product phases, re-read 2026-10-28; page shows reviewed 15 July 2026); 4.11 in part (most projects benefit from more than one method); the definitions of field studies, participatory design and focus groups in `core/methods/`; benchmarking, analytics, A/B testing and desirability studies as methods in `core/methods/` | 2026-10-27 |
| S12 | Budiu, R. (2021). "Why You Cannot Trust Numbers from Qualitative Usability Studies." Nielsen Norman Group. https://www.nngroup.com/articles/true-score/ | 7.8: report the sample size, compute the interval, test before claiming a difference; small samples give large error | 2026-10-27 |
| S13 | Whitenton, K. (2021). "Triangulation: Get Better Research Results by Using Multiple UX Methods." Nielsen Norman Group. https://www.nngroup.com/articles/triangulation-better-research-results-using-multiple-ux-methods/ | 4.3 in part (one method's limits are mitigated by another source); 4.11 in part; `core/methods/analytics-and-ab-tests.md`; 7.6 in part (check whether other data supports a result) | 2026-10-27 |
| S14 | Moran, K. (2019). "Interpreting Contradictory UX Research Findings." Nielsen Norman Group. https://www.nngroup.com/articles/interpreting-research-findings/ | 7.6 in part: quantitative data should never automatically overrule qualitative; examine how each study was conducted | 2026-10-27 |
| S15 | Harley, A. (2017). "Ideation in Practice: How Effective UX Teams Generate Ideas." Nielsen Norman Group. https://www.nngroup.com/articles/ideation-in-practice/ | W.2: written ideation, in which people document ideas individually before the group, avoids groupthink and unbalanced contributions (survey evidence, correlational) | 2026-10-27 |
| S16 | Kaplan, K. (2021). "How to Handle Dominating Participants in UX Workshops: 3 Tactics." Nielsen Norman Group. https://www.nngroup.com/articles/dominating-workshop-participants/ | W.2: silent post-up and brainwriting so contributions come from the whole group | 2026-10-27 |
| S17 | Kaplan, K. (2017). "Planning Effective UX Workshop Agendas." Nielsen Norman Group. https://www.nngroup.com/articles/ux-workshop-agendas/ | W.1: articulate the goal as a short description of the ideal end state before anything else | 2026-10-27 |
| S18 | Azarova, M. (2022). "Secondary Research in UX." Nielsen Norman Group. https://www.nngroup.com/articles/secondary-research-in-ux/ | 2.1 in part (identify each source's validity and limitations; a missing methods section is a red flag); 4.1 in part (secondary research as a standard first step) | 2026-10-27 |
| S19 | Government Digital Service. "Plan user research for your service." GOV.UK Service Manual, updated 15 October 2026. https://www.gov.uk/service-manual/user-research/plan-user-research-for-your-service | 3.3 (be clear what questions each round answers and how it helps the team decide); 3.1 in part | 2026-10-27 |
| S20 | Government Digital Service. "Sharing user research findings." GOV.UK Service Manual, updated 9 September 2026. https://www.gov.uk/service-manual/user-research/sharing-user-research-findings | 8.1 in part: one or two slides on the research done, five to ten findings slides each with a headline and evidence, one or two on next steps | 2026-10-27 |
| S21 | Krause, R. (2022). "Creating Engaging Reports & Asynchronous Presentations." Nielsen Norman Group. https://www.nngroup.com/articles/engaging-reports-presentations/ | 8.3a in part: structure for three kinds of reader (headlines, themes, in-depth detail) | 2026-10-27 |
| S22 | Klein, L. (2026). "How to Get Research Recommendations on the Roadmap." Nielsen Norman Group. https://www.nngroup.com/articles/research-recommendations-roadmap/ | 8.2 in part (start from the finding, connect to what the PM is measured on, suggest something concrete); 3.2 in part | 2026-10-27 |
| S23 | Schade, A. (2013). "Making Usability Findings Actionable." Nielsen Norman Group. https://www.nngroup.com/articles/actionable-usability-findings/ | 8.2 in part: findings specific to the design element, ranked by severity, recommendations labelled as such | 2026-10-27 |
| S24 | Neusesser, T. (2024). "Competitive Usability Evaluations." Nielsen Norman Group. https://www.nngroup.com/articles/competitive-usability-evaluations/ | 4.4: key tasks completable across products; tangentially related businesses offer perspective; "beat the competition, not copy them"; observe what users do | 2026-10-27 |
| S25 | Tankala, S. (2023). "UX & Marketing: Balancing Business Goals and Supporting Users." Nielsen Norman Group. https://www.nngroup.com/articles/ux-and-marketing/ | 1.3 in part: marketing's audience can differ from UX's (buyers vs users); marketing relies on self-report, UX on observed behaviour | 2026-10-27 |
| S26 | Cabinet Office and Government Digital Service (2013). "GOV.UK content principles: conventions and research background." https://www.gov.uk/government/publications/govuk-content-principles-conventions-and-research-background/govuk-content-principles-conventions-and-research-background | A.4: short sentences and paragraphs, simple everyday words, no jargon, spell out acronyms, with the research it cites (Joiner 2002, Spyridakis 2000, Summers et al.) | 2026-10-27 |
| S27 | Samsonov, P. (2025). "In User Research, Don't Stop at 'Yes' or 'No'." Nielsen Norman Group. https://www.nngroup.com/articles/research-yes-or-no/ | 3.1 and 3.3 in part: the purpose of research is to inform decisions; research observes behaviour and needs rather than validating a yes/no | 2026-10-27 |
| S28 | Government Digital Service. "Finding participants for user research." GOV.UK Service Manual, updated 22 September 2026. https://www.gov.uk/service-manual/user-research/find-user-research-participants | 5.2 in part: research with all the different kinds of people who may need the service, including those with limited digital skills or literacy; 5.6 and `core/lenses/accessibility.md` (recruit a spread that includes disability; screen for difficulties as well as disability; ask about assistive technology; allow up to a month through agencies and six to eight weeks for less common cognitive disabilities; don't use internal disabled staff or over-use the same people) | 2026-10-27 |
| S29 | Rosala, M. (2021, reviewed 2026). "Problem Statements in UX Discovery." Nielsen Norman Group. https://www.nngroup.com/articles/problem-statements/ | 3.3 in part: scope research to the problem; investigating only solutions is not discovery | 2026-10-27 |
| S30 | Kaplan, K. (2019, reviewed 2023). "5 UX Workshops and When to Use Them: A Cheat Sheet." Nielsen Norman Group. https://www.nngroup.com/articles/5-ux-workshops/ | W.1 in part: each workshop type is defined by the outcome it produces | 2026-10-27 |
| S31 | Nielsen, J. (1997). Focus groups article, listed as "Focus Groups in UX Research" in search results; exact page title not confirmed. Nielsen Norman Group. https://www.nngroup.com/articles/focus-groups/ | 4.5; `core/methods/focus-groups.md`: good for what people want and spontaneous reactions, poor for judging usability; six to nine people, more than one group; keep one person from dominating; a demo is not use; supplement with one-to-one observation | 2026-10-27 |
| S32 | Sanders, E. B.-N. and Stappers, P. J. (2008). "Co-creation and the new landscapes of design." *CoDesign*, 4(1), 5–18. doi:10.1080/15710880701875068. Read from an open copy hosted by Universidad de los Andes. | `core/methods/participatory-design.md`: co-design as collective creativity; the participant as expert of their experience; the researcher as facilitator providing tools for expression; most valuable at the early, open stage | 2026-10-27 |
| S33 | Farrell, S. and Fessenden, T. (2024). "Field Studies." Nielsen Norman Group. https://www.nngroup.com/articles/field-studies/ | `core/methods/field-studies.md`: the kinds of field study, when to use them, planning and permissions, observer rules, holding questions, remote sessions and their limit | 2026-10-27 |
| S34 | Moran, K. and Gordon, K. (2023). "How to Conduct a Heuristic Evaluation." Nielsen Norman Group. https://www.nngroup.com/articles/how-to-conduct-a-heuristic-evaluation/ | 4.6; `core/methods/expert-review.md`: three to five independent evaluators, one to two hours, narrow scope, consolidate afterwards, heuristics are guidelines, can't replace user research | 2026-10-27 |
| S35 | Flaherty, K. (2022). "Evaluate Interface Learnability with Cognitive Walkthroughs." Nielsen Norman Group. https://www.nngroup.com/articles/cognitive-walkthroughs/ | 4.6; `core/methods/expert-review.md`: the four questions, cross-functional group with facilitator and recorder, best for new or unfamiliar systems, combine with usability testing | 2026-10-27 |
| S36 | Government Digital Service. "Running research sessions with disabled people." GOV.UK Service Manual, updated 9 September 2026. https://www.gov.uk/service-manual/user-research/running-research-sessions-with-people-with-disabilities | 5.6; `core/lenses/accessibility.md`: participants bring their own assistive technology or you visit them; consent forms they can use; plan setup time; talk to the participant, not the interpreter or helper; ask before helping; ask which terms they prefer | 2026-10-27 |
| S37 | NHS England. "Accessibility: user research." NHS digital service manual, updated July 2019. https://service-manual.nhs.uk/accessibility/user-research | 5.6 in part; `core/lenses/accessibility.md`: about one participant with access needs in every five; involve them at every stage; check survey tools with a screen reader, keyboard, high contrast and 400% zoom; let people pause or stop. Older than the other sources; check against current practice. | 2026-10-27 |
| S38 | Laubheimer, P. (2018, reviewed 2026). "Beyond NPS: SUS, NASA-TLX, and the Single Ease Question." Nielsen Norman Group. https://www.nngroup.com/articles/measuring-perceived-usability/ (title as shown in search results) | `core/methods/usability-testing.md` and `core/methods/interviews.md`: a post-task ease rating on seven points; SUS after the session, ten items, 0–100, wording and order unchanged; 20–30 users or more for questionnaire numbers; pair a rating with "why did you give that score?" and don't make much of the average. The article does not quote the SEQ's exact wording, so Magpie's template wording is its own. | 2026-10-27 |
| S39 | Rosala, M. (2024). "Open-Ended vs. Closed Questions in User Research." Nielsen Norman Group. https://www.nngroup.com/articles/open-ended-questions/ | `core/methods/interviews.md`: closed questions are used occasionally in interviews and usability tests, sparingly, because they stop the conversation | 2026-10-27 |
| S40 | Rosala, M. (2020, reviewed 2026). "Rating Scales in UX Research: Likert or Semantic …" (title cut off in the search listing; full title not confirmed). Nielsen Norman Group. https://www.nngroup.com/articles/rating-scales/ | `core/methods/interviews.md`: word-labelled scales are easier to understand; Likert items are prone to acquiescence and social-desirability bias; follow a rating with "why did you choose this rating?" | 2026-10-27 |
| S44 | Flaherty, K. (2024). "Diary Studies: Understanding Long-Term User Behavior and Experiences." Nielsen Norman Group. https://www.nngroup.com/articles/diary-studies/ | 5.10; `core/methods/diary-studies.md`, "Ways to capture entries": messaging apps suit simple text and dialogue but are harder to export; survey and document tools suit long written answers but handle images and video badly; diary platforms take video, photos and questionnaires and help with tagging and transcription, at a cost; data security and participant convenience in choosing a tool. The same article is S44 in open PR #23, which cites it for the rest of the method guide; S41 to S43 and S45 to S52 are that PR's. | 2026-10-28 |
| S53 | Kaner, S. (2014). *Facilitator's Guide to Participatory Decision-Making*, 3rd edition. Jossey-Bass. https://oreilly.com/library/view/facilitators-guide-to/9781118404959 | W.4 and `core/workshops/stakeholder-workshops.md`: a group needs a clear decision rule (for example unanimity, majority vote, or the person in charge decides). Only the publisher's table of contents was read (chapter 22, "The Significance of Clear Decision Rules"); the chapter itself was not. | 2026-10-28 |
| S54 | Kaplan, K. (2023). "Dot Voting: 3 Common Problems." Nielsen Norman Group (video). https://www.nngroup.com/videos/dot-voting-problems/ | W.4 in part: dot voting suffers from choice overload, choice imbalance and social bias. The page names the three problems but doesn't explain them; the private vote is Magpie's own remedy. | 2026-10-28 |
| S55 | Rosala, M. (2021, reviewed 2026). "Using 'How Might We' Questions to Ideate on the Right Problems." Nielsen Norman Group. https://www.nngroup.com/articles/how-might-we-questions/ | W.5 and the "How might we" step: write them after discovery, as a team, before ideating; ground each in a finding; don't build in a solution; not too broad or too narrow; aim at the outcome, not the symptom. The article credits Procter & Gamble in the 1970s and IDEO; that origin was not checked further. | 2026-10-28 |
| S56 | Krause, R. and Pernice, K. (2024, reviewed 2026). "Affinity Diagramming for Collaboratively Sorting UX Findings and Design Ideas." Nielsen Norman Group. https://www.nngroup.com/articles/affinity-diagram/ | Workshop pattern A step 2: individual notes first, to avoid dominating voices, then clustering and labelling as a team | 2026-10-28 |
| S57 | Fessenden, T. (2020). "When Remote Workshops Fail." Nielsen Norman Group. https://www.nngroup.com/articles/remote-workshop-fail/ | W.7 in part and "Remote or hybrid": activities take longer online; consider going fully remote if anyone joins remotely; use and test tools the team knows; switch activity every 15 to 20 minutes; groups of 3 to 5 for more than 10 people | 2026-10-28 |
| S58 | IBM. "Enterprise Design Thinking: Framework." https://www.ibm.com/training/enterprise-design-thinking/framework | The optional hills step: a hill is a statement of intent written as a user outcome, with who, what and wow; implementation-independent. Also the Loop (observe, reflect, make) in `docs/DESIGN.md`. Described in Magpie's own words. The page states no licence or reuse terms and marks "Enterprise Design Thinking" as a registered trademark, so Magpie links to it and copies no IBM text, templates or toolkit activities. IBM's page says product management owns hills on product teams; Magpie has the room agree the hill instead. | 2026-10-28 |
| S59 | Design Council. "Framework for Innovation" (the Double Diamond). https://www.designcouncil.org.uk/our-resources/framework-for-innovation/ | `docs/DESIGN.md`, "How Magpie relates to design thinking": discover, define, develop, deliver; non-linear. Licensed CC BY 5.0. | 2026-10-28 |
| S60 | Gibbons, S. (2016, reviewed 2026). "Design Thinking 101." Nielsen Norman Group. https://www.nngroup.com/articles/design-thinking/ | `docs/DESIGN.md`, "How Magpie relates to design thinking": six phases (empathize, define, ideate, prototype, test, implement), iterative | 2026-10-28 |
| S61 | Meadows, D. H. (2008). *Thinking in Systems: A Primer*. Edited by D. Wright. Chelsea Green Publishing. | `core/lenses/systems-and-journeys.md`: a system's behaviour comes from its connections and feedback loops, and small changes in some places (leverage points) can shift it a lot. Publication details and these ideas were checked against the Wikipedia article on the book, not the book itself. | 2026-10-28 |
| S62 | Lipmanowicz, H. and McCandless, K. "1-2-4-All." Liberating Structures. https://liberatingstructures.com/1-2-4-all | Workshop pattern B step 2: silent reflection, then pairs, then fours, then the whole group. Licensed CC BY-SA 5.0; Magpie describes the structure in its own words and credits the authors. | 2026-10-28 |
| S63 | Lioudis, N. (2024, 12 September). "Minimum Viable Research: Practical Tips & Resources (+cheat sheets)." User Interviews blog. https://www.userinterviews.com/blog/minimum-viable-research-practical-guide | `core/lenses/minimum-viable-rigor.md`: start small and get findings to stakeholders quickly; not a licence to cut corners; four steps (recruit with clear goals and a short screener, prepare the moderator guide with goals at the top, run the session, share concisely and discuss next steps). 4.9 and 5.9 in part. The page credits Erika Hall's *Just Enough Research* as a related idea; the book was not read | 2026-10-28 |
| S64 | Pearson, C. J. (2025, 20 August). "Minimum Viable Rigor." Carl J. Pearson, PhD (personal site). https://carljpearson.com/minimum-viable-rigor/ | `core/lenses/minimum-viable-rigor.md`: a lowest acceptable level of rigor, below which insights misalign decisions; the rigor needed rises with decision risk; rigor is judged on the insight after the study; the researcher judges rigor while stakeholders accept risk; offer what can be answered rather than refuse. 3.8 and 4.9 in part; 7.15; 8.14 in part | 2026-10-28 |
| S65 | Rosala, M. (2023). "6 Tips for Better Participant Engagement in Diary Studies." Nielsen Norman Group. https://www.nngroup.com/articles/better-diary-studies/ | 5.10; `core/methods/diary-studies.md`, "Ways to capture entries": choose the tool by budget, the data needed, and participants' devices and familiarity; some people express themselves better in writing, others on video; voice notes and video as easier ways to make an entry; keep entries small and questions to what the research needs; pilot the study | 2026-10-28 |
| S66 | Government Digital Service. "Managing user research data and participant privacy." GOV.UK Service Manual, published 5 November 2018; page metadata gives an update on 18 September 2026. https://www.gov.uk/service-manual/user-research/managing-user-research-data-participant-privacy | 5.10; `core/methods/diary-studies.md`, "Recordings, photos and consent": photos, audio and video are personal data; consent covers what's collected, how it's stored and used and who it's shared with; approved storage and limited access; blur personal data in screenshots and video before sharing | 2026-10-28 |
| S67 | Krause, R. and Gibbons, S. "Empathy Mapping: The First Step in Design Thinking." Nielsen Norman Group (page dated 2 October 2026; earlier versions not checked). https://www.nngroup.com/articles/empathy-mapping/ | The empathy map activity and the understand-the-users workshop type: says, thinks, does and feels; built as a team, each person writing notes alone first, then clustering; empty areas show gaps in the research | 2026-10-28 |
| S68 | Gibbons, S. (2016). "Design Critiques: Encourage a Positive Culture to Improve Products." Nielsen Norman Group. https://www.nngroup.com/articles/design-critiques/ | The critique activity: judge a design against agreed objectives, set the scope first, round robin, reframe opinion around the goals | 2026-10-28 |
| S69 | Alvarez, H. (2016, 22 April). "Consider these variables before you choose a UX research method." UserTesting blog. https://www.usertesting.com/blog/choose-research-method | 4.10 (set the objective first, then weigh qualitative or quantitative, attitudinal or behavioural, product life-cycle stage, and context and location, including remote, in-the-wild, place-based and beyond-the-device studies); 4.11 (quantitative to find problem areas, qualitative to explore them; compare what people say with what they do); 4.12 (explain the rationale and expected outcomes to stakeholders) | 2026-10-28 |
| S70 | Moran, K. (2020, 3 May). "Benchmarking UX: Tracking Metrics." Nielsen Norman Group. https://www.nngroup.com/articles/benchmarking-ux/ | 4.13 in part (a benchmark needs a comparison point); `core/methods/benchmarking.md`: a summative snapshot of one version; example measures including support data; compare with an earlier version, a competitor, an industry figure or a stakeholder goal; analytics, surveys and quantitative usability testing to collect; how often is the team's call | 2026-10-28 |
| S71 | Neusesser, T. (2024, 30 August). "A/B Testing 101." Nielsen Norman Group. https://www.nngroup.com/articles/ab-testing/ | 4.13 in part; `core/methods/analytics-and-ab-tests.md`: live product and enough traffic, one change, a hypothesis from research, main and guardrail measures, duration set in advance and at least one to two weeks, an A/A check of a new tool, no stopping early, significant is not the same as important, shows how behaviour changes but not why | 2026-10-28 |
| S72 | Cardello, J. (2013, 17 November). "Three Uses for Analytics in User-Experience Practice." Nielsen Norman Group. https://www.nngroup.com/articles/analytics-user-experience/ | 4.13 in part; `core/methods/analytics-and-ab-tests.md`: spotting issues, investigating them, and checking qualitative findings; numbers are clues read in context; a small test finds the spot and analytics sizes it; data with no question leads nowhere. Its tool examples are from 2013 and were not used. | 2026-10-28 |
| S73 | Moran, K. (2016, 28 February). "Using the Microsoft Desirability Toolkit to Test Visual Appeal." Nielsen Norman Group. https://www.nngroup.com/articles/microsoft-desirability-toolkit/ | `core/methods/preference-and-desirability.md`: the reaction-word method (credited there to Benedek and Miner, 2002; their original paper not read); about five words; adapting and shortening the list; shuffling; mixing negative and positive words; a screenshot is enough; analysis by share of people, by group and by brand word | 2026-10-28 |
| S74 | Chan, M. (2024, 13 December). "Testing Visual Design: A Comprehensive Guide." Nielsen Norman Group. https://www.nngroup.com/articles/testing-visual-design/ | 4.13 in part (preference questions after tasks); `core/methods/preference-and-desirability.md`: two or three versions varying a few things, order shuffled, differences people can notice, ask why only when moderated, word-choice methods, ratings need more people | 2026-10-28 |
| S75 | Moran, K. and Pernice, K. (2020, 26 April). "Remote Moderated Usability Tests: How to Do Them." Nielsen Norman Group. https://www.nngroup.com/articles/moderated-remote-usability-test/ | `core/methods/usability-testing.md`, "Remote, moderated": advantages and extra preparation, the call tool, how tasks reach the participant, a tech check the day before, reminders, observers, extra recruits and spare time, a pilot, recording consent | 2026-10-28 |

Located but not read, so not cited: Carter, S. and Mankoff, J. (2005).
"When participants do the capturing: the role of media in diary studies."
*Proceedings of CHI 2005*, 899–908. doi:10.1145/1054972.1055098 (record
confirmed in the CMU repository and researchr; only a summary of the
abstract was read, and it frames photos, audio, location and objects as
open questions rather than giving findings, so nothing in Magpie rests on
it). Dillman, D. A., Smyth, J. D. and
Christian, L. M. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys: The
Tailored Design Method*, 4th ed., Wiley (record confirmed in WorldCat; the
chapters on question writing would likely support 6.2 and 6.5 but have not
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
Current count: 51 of 121 standards cite a source in full or in part.

## Tools used

| Tool | Role |
| --- | --- |
| Claude (Anthropic) | Drafting the design and the first build in conversation with the author |
| Git and GitHub | Version history, which is itself part of this record |
| Python 3 | The build script in `tools/` |
