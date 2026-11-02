# Lens: confidence and priority

Two separate questions about every finding. **Confidence:** how sure are
we? **Priority:** how much does it matter? A finding can be very likely and
minor, or uncertain and urgent. Magpie answers both, shows its reasons, and
never lets one change the other. It applies at stage 7, when findings are
written, and at stage 8, when the top findings are chosen.

## What Magpie needs

Each assessment rests on context. Most of it is already in the study record
by stage 7. Whatever is missing is asked with the stage's other questions
(`operating.md`, "Gather context before you build"). None of it is required
to draft: a missing piece is stated in the finding, never guessed and never
held against it.

| To judge | Magpie needs | Usually found in | If it's missing |
| --- | --- | --- | --- |
| Who the evidence came from | Who the study's target users are, and each participant's role and segment | The plan's sample and screener, the participant list | Magpie drafts each participant's fit from the screener for a yes; with no screener, fit is "not known" |
| What kind of evidence | The raw material, with tasks and observations marked | Transcripts, notes, recordings' timestamps | Nothing to ask: Magpie tags it while coding |
| Other sources | Past studies, partner data (analytics, support tickets, sales notes), or "this is the first study on this" | The evidence log (stage 2), partner data | "None" is a full answer. The finding says it's the first study on the topic |
| Impact | The decision, the goal or metric, and what happens to users when they hit the problem | The record's decision and business context, the team profile | Impact on users is judged from the sessions; impact on the decision is marked [assumption] |
| Reach | How many target users it touches and how often, outside the study | Partner data, the segment sizes | Reach comes from the study's own pattern, and the finding says reach outside the study isn't known |

## Confidence

Keep the strength label (strong, moderate, weak; `checks-claim-strength.md`,
rule 4) and give it a one-line reason built from five checks. In readouts and
reports the label is called **confidence**; the study record keeps the word
"strength" so older records still read the same.

1. **How many.** The count, with the participants behind it, and which
   segments they come from: "5 of 8 (P1, P2, P4, P6, P8), both segments".
2. **Who.** How well those people fit the target users. Each participant is
   one of:
   - **Matches:** a target user, doing the work the study is about.
   - **Partly:** a target user, but outside the screener on something that
     matters here (new to the product, a different region or plan).
   - **Stand-in:** someone speaking for the target users: a buyer, an
     admin, a manager, an internal colleague, a field rep.
3. **What kind.** Each code is tagged while coding (stage 7, step 4):
   - **Seen:** watched in the session, in a task, in a screen share, or in
     an artifact the participant showed (a spreadsheet, a workaround).
   - **Past time:** the participant described a real, specific time it
     happened ("Last Tuesday I exported it twice").
   - **Opinion:** a general view, a habit described in general ("I
     usually"), a preference, or a prediction ("I would use that").
4. **Other sources.** Whether anything outside this study points the same
   way: agrees, disagrees, mixed, or **none yet**. Name the source.
5. **What cuts against it.** The participants who didn't fit (stage 7,
   step 6).

### How the checks move the label

- **Opinion-only behavior is moderate at most.** A finding about what
  people do that rests only on opinions or predictions is moderate at most,
  and says so: "what participants said they do; not seen". Opinions are the
  right evidence for a question about views or feelings (how people feel
  about the price), and there the cap doesn't apply.
- **Stand-in-only is moderate at most.** A finding that rests only on
  stand-ins is moderate at most, and is labeled "from buyers, not end
  users" (or whoever it was). Fit "not known" is said in the reason and
  doesn't cap the label.
- **Agreement can support a higher label.** A source that agrees, named,
  is a reason the finding can be strong. It doesn't make a weak finding
  strong on its own, and secondhand material still can't be strong on its
  own (`checks-claim-strength.md`, rule 7). The two are shown side by
  side, never merged into one claim.
- **Disagreement lowers it.** A source that disagrees lowers the label by
  one level unless the finding explains the difference (a different
  segment, a different time).
- **No other source is neutral.** When there's nothing to compare with,
  because this is the first study on the topic or the team has no data, the
  finding says "first study on this; no other sources" and its confidence
  rests on this study alone. Nothing is taken off for it, and it doesn't
  touch priority.

### When what people said and did differ

When a participant says one thing and does another (says they always check
the preview, then skips it in the task), keep both, with their locations,
and write the gap as a finding of its own. What people do is usually the
better guide to behavior, because what they say is limited by what they
notice and are willing to report (S11). The gap often explains why a
problem hasn't been reported before.

### The line

"Confidence: moderate. 5 of 8 target users, seen in the task (P1 12, P2 09,
P4 14, P6 11, P8 10); support tickets agree; P3 and P7 finished without
trouble."

"Confidence: moderate. 4 of 8 said they'd use it (opinion, not seen); first
study on this, no other sources; P2 and P5 said they wouldn't."

## Priority

Two parts, kept apart from confidence (S70: treat how often a problem
happens separately from how bad it is).

**Impact.** What happens to the people who hit it, and what it means for
the decision.

| Impact | For users | For the decision |
| --- | --- | --- |
| High | Blocks a task, causes errors, lost data or money, or harm | Changes the decision or the goal it serves |
| Medium | Slows them, forces a workaround, confuses them before they recover | Shapes how the decision is carried out |
| Low | Noticed or mildly annoying; they carry on | Doesn't change the decision |

Take the higher of the two columns. A usability issue's severity maps
straight across: blocked is high, slowed is medium, noticed is low.

**Reach.** How many target users it touches, and how often in real use.

| Reach | Looks like |
| --- | --- |
| Wide | Most target users, or every time they do the task |
| Some | One segment, or some of the time |
| Narrow | A single case, or a rare situation |

Partner data (analytics, support volume, segment sizes) says how far it
reaches outside the study. Without it, judge reach from the study's own
pattern and say so: "seen in 5 of 8; how common it is across all users
isn't known". Missing outside data never lowers reach; the sample's counts
still aren't rates (`checks-claim-strength.md`, rule 3).

**The grid.**

| Impact \ Reach | Wide | Some | Narrow |
| --- | --- | --- | --- |
| High | High | High | Medium |
| Medium | High | Medium | Low |
| Low | Medium | Low | Low |

A single case of harm, lost data or money, or a legal or safety problem is
high priority whatever its reach.

The impact and reach labels and the grid are practitioner judgment, not a
published scale. They're Magpie's draft; the researcher can change any of
them, and their call stands.

### Answer the primary question in the top findings

The top findings, five at most, must answer the study's primary research
question: the main thing the study set out to learn. Before settling the
order, check that at least one finding in the first five answers it. If
none does, move up its highest-priority finding in place of the
lowest-priority finding in the five. Within the five, priority still sets
the order. If the data didn't clearly answer the primary question, the
top findings say so in one line, with why (too few people, the guide
didn't reach it, the answer is mixed), rather than leaving it out. The
other research questions don't need a place in the five; their answers
go in the rest of the findings, where every finding already names the
question it answers.

### Keep priority and confidence apart

Confidence never raises or lowers priority. Show them next to each other.
A high-priority finding with weak confidence, or one marked not enough for
the decision, is marked **check next**, with what would make the team surer
and roughly what that costs (`lenses-minimum-viable-rigor.md`). It still
counts as high priority, because the team needs to know about it.

## Using it

- **Stage 7.** Tag each code seen, past time or opinion. Note each
  participant's fit. After the strength is rated and re-judged, write the
  confidence line, then impact, reach and priority, each with its reason.
  Show the findings in priority order, with the primary question
  answered in the first five (above), and make the order part of the
  review ask, so it needs no answer of its own: "This is the order I'd
  put them in. Move any up or down if you'd rank them differently; your
  yes on the findings covers the order too." Don't ask a yes-or-no
  question about the order: it would compete with the review yes. Their
  order stands; a yes keeps Magpie's order and records it as agreed.
- **Stage 8.** The top findings, five at most, are the highest priority
  ones for this decision, with ties broken by the primary research
  question, and the primary question answered among them (above).
  Each one gets a line on why it's there and which question it answers. An "also noticed"
  finding is in the top five when its priority puts it there.
  Recommendations follow the same order unless the researcher orders them
  differently.

## Basis

- S11: what people say and what they do often differ; self-report is
  limited by what people are aware of and willing to report.
- S70: report how often a problem happens alongside how bad it is, and
  treat the two separately.
- S71: triangulation, looking at a question from several kinds of data or
  several methods, makes results more reliable.
- The three evidence kinds, the fit labels, the caps, the impact and reach
  labels and the grid: practitioner judgment.

---

Part of Magpie version 2026-11-02, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
