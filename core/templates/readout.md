# Readout: [study name]

Slide-by-slide outline. Each heading is one slide unless it says otherwise.
Formatting follows the team's template if there is one, and
`templates/house-style.md` for anything it leaves open.
No more than 20 slides by default; many teams want fewer. Before drafting,
Magpie asks who's in the room and how long the slot is, and sizes the deck
to that.

The deck tells one story: why we asked, what we did, what we found, what it
means, what to do. Each slide should follow from the one before it. If a
slide doesn't move the story, it goes to the appendix.

## 1. Title

[Study name] · [date] · [researcher] · [the team or group it's for]

## 2. Why we did this

The foundation. One slide, sometimes two.

- **The product:** [optional: what it is, what it does, who uses it, in one line]
- **The decision:** By [when], the team will decide [what]
- **The business need:** [goal or metric at stake, in the team's own words]
- **What we already knew:** [prior research, partner data, or "no prior
  evidence"]
- **The question:** [primary research question in plain words]
- **Where it sits:** [job, journey step, persona, in the team's names]

## 3. What we did

Brief and factual: [method], [N] participants, [who they were], [dates].
One slide. Keep it to the structure of the study. Weaknesses and gaps are
not on this slide; see "Limits" below.

## 4. Top findings

Never more than five: the findings the decision rests on. One line each,
with strength and whether it's enough for this decision. This is the slide people photograph. An unexpected finding
belongs here if it's serious enough.

1. [Finding, one line] · [strength] · [enough / enough if [caveat] / not enough]
2. …

## 5 to [n]. Findings in detail

One finding per slide, in the same order as the top findings. Pitched for a
PM and engineering audience: enough to believe it and act on it, no more.

**Finding [n]: [claim in plain words]** · Strength: [label]

- [Evidence with numbers: "6 of 8 participants…"]
- [Receipts: at least two participant codes with locations, or "single case"]
- [One quote with a participant code and descriptor, "— P3, finance manager, SMB"; two at most]
- **What cuts against it:** [who didn't fit, in one line]
- **What it means:** [one line]

Anything deeper (coding, more quotes, per-participant detail) goes in the
appendix.

## [n+1]. Other findings

One slide. Every finding that met the evidence bar but isn't in the top
five, one line each with strength. Tag the ones that fell outside the
research questions "unexpected". Nothing that passed the evidence bar is
dropped; a finding whose evidence didn't hold goes in the appendix with
the reason.

- [Finding, one line] · [strength] · [unexpected, if so]
- …

## [n+2]. Summary

The story in three or four lines, drawn from this study's focus, goals
and findings. Things to look for: what we asked, what we found, what it
means for the product or the business, how confident we are. Use the
ones this study speaks to. For an audience that wants the answer first,
this slide can come second, right after the title.

## [n+3]. Recommendations

Detailed. Each one is an action, the teams it touches, the finding it
rests on, and the goal or metric it moves. The "moves" column is where
business value becomes visible: use the names the team already tracks.
Name the teams each action touches, not a person. Who takes each action
is often for the teams to agree together; name a person only when the
researcher asks for it.

| Action | Teams involved | Rests on | Moves |
| --- | --- | --- | --- |
| [action] | [teams] | Finding [n] | [goal or metric] |

If it helps the audience, split into "for design", "for engineering", "for
product".

## [n+4]. Next steps

Same three parts as the report's next steps. Magpie drafts them from the
findings and the record's context; they stay "draft" until the researcher
has reviewed and edited them. Name teams, not one person, unless the
researcher asks for a name.

- **What happens now:** [step, the teams involved, by when]
- **Open questions:** [question → more research / a decision / nothing yet]
- **Researcher's next steps:** [what the researcher will do next]

## [n+5]. Limits (researcher's call)

Magpie always drafts this slide and always writes the limits into the study
record and the report. Whether it appears in the readout is the researcher's
decision, made with the audience in mind. Magpie shows the draft to the
researcher first and asks.

- [Sample gaps]
- [What the method can't tell us]
- [Challenges skipped during the study, from the record's risks]

## Appendix

For anyone who wants the deeper dive. Not counted against the 20.

- Participant profile
- Full findings with evidence, counter-evidence and coding frame
- Instruments
- Independent review summary
- How AI was used: the same lines as the report's (`templates/report.md`, "How AI was used")
- Links: study record, report, raw material (access-controlled)

---

## Option: decision-first order

For a senior audience with ten minutes, or a team that already knows the
study. Magpie offers it when the audience is named as senior or the slot is
under fifteen minutes; otherwise the default above applies.

1. The decision and the answer (decision, what the evidence supports, how
   sure we are, what we recommend)
2. Recommendations, with the teams involved
3. What we did, in one slide
4. Top findings, then detail only where needed
5. Other findings, one slide
6. Next steps
7. Appendix

## Sizing to the audience

| Slot | Slides | What to cut first |
| --- | --- | --- |
| 10 minutes, senior | 6 to 8 | Detailed findings beyond the top three; partner sections. The other-findings slide stays, even if it's the last one |
| 30 minutes, product trio | 12 to 16 | Second quotes, appendix material on main slides |
| 60 minutes, wider team | up to 20 | Nothing on the main deck; put discussion time in the agenda |
