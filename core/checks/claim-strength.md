# Check: claim strength

Run this over every finding before it leaves stage 7, and again over every
slide or paragraph of the readout and report. The question each time is:
does the wording match the evidence?

## Rules

1. **Say the numbers.** "6 of 8 participants" not "most". "41 of 120, 34%"
   not "a third". Vague quantities read as bigger than they are.
2. **Name the counter-evidence.** Every finding says who didn't fit and
   what they did instead. "All participants" is almost never true; check.
3. **Qualitative counts aren't rates.** Eight interviews tell you what
   exists and how it works, not how common it is. Write "participants
   described…" not "users want…". Never a percentage from under about
   thirty people.
4. **Strength label matches the evidence.**
   - Strong: consistent across most participants, or a statistically
     reliable result with the test named.
   - Moderate: a clear pattern with exceptions you can name.
   - Weak: few participants, one segment, mixed signals, or secondhand.

   Mixed signals get a reason before the label: two groups that differ
   (write a finding for each), people really divided (give each side's reasons), not enough data yet (say what would settle
   it), or something about the sessions (`stages/07-analyze.md` step 6a).

   Each label carries a confidence line with its reasons: how many, who
   they are against the target users, whether it was seen or said, and
   whether other sources agree (`lenses/confidence-and-priority.md`).
5. **Causes need more than correlation.** "People who used feature X
   renewed more" is not "feature X causes renewal". Say what's known and
   what would be needed to know more.
6. **Quotes carry a code, not a conclusion.** Each quote has a participant
   code and a location. One quote illustrates; it doesn't prove. In a
   readout or report, the code comes with a short descriptor from the
   participant list, so the reader knows who is speaking: "— P3, finance
   manager, SMB". Use the role and the team's own segment names (company
   size or type, plan, region, end user or buyer), the ones that matter
   for this decision, or the team profile's quote label if it sets one.
   Never a name or a company name. If a combination would point to one
   person (the only CTO in the study), use a broader label and say so
   once (`operating.md`, "Personal details in the material").
7. **Secondhand stays secondhand.** A finding that rests on partner data or
   a stakeholder's account is labeled that way and can't be "strong" on
   its own.
8. **Confidence doesn't drift.** The strength on the slide is the strength
   in the record. Check every finding against the record before the
   readout.
9. **Recommendations stay inside the findings.** A recommendation that
   needs a fact the study didn't establish says so and marks that fact as
   an assumption.
10. **Absence of evidence is labeled.** "No participant mentioned X" is a
    finding about the sessions, not proof that X doesn't matter.
11. **Every finding has receipts.** At least two participant references
    with locations per directional claim, or a single case labeled as
    one. No receipts, no slide. Each count carries its own: "3 of 8 (P1 06,
    P5 06, P7 06)", one code per person counted, so a script can confirm
    the count matches the list and every line exists. The record and the
    report keep the codes; a slide can move them to the speaker notes or
    the appendix.
12. **A summary is not a finding.** Anything a tool produced from the
    transcripts, Magpie's drafts included, is a draft until a person has
    read the passages it rests on. Smoothing is the tell: "generally
    positive, some minor confusion" where two of eight were seriously
    stuck. `checks/ai-assisted-research.md`.
13. **Said isn't seen.** A claim about what people do that rests only on
    what they said they do or would do is moderate at most and says so
    ("participants said they…"). Same for a claim that rests only on
    buyers, admins or colleagues speaking for the users. Where saying and
    doing differ, both are reported.
14. **No other source isn't a weakness.** "First study on this; no other
    sources" is stated plainly and lowers nothing. Only a source that
    disagrees lowers the label.
15. **Key findings say what would prove them wrong.** Each finding the
    decision rests on carries a "Would be wrong if" line and at least one
    other explanation for the same evidence, each marked ruled out (with
    the evidence) or still open (with what would settle it). An open
    explanation that fits the evidence as well as the finding does means
    the finding can't be strong (`stages/07-analyze.md`, step 11a).

## Wording to replace

| Instead of | Write |
| --- | --- |
| Users want | 5 of 8 participants asked for |
| Everyone struggled | 4 of 5 participants failed task 2; P3 completed it |
| Proves | Suggests, supports, is consistent with |
| Significant (without a test) | Large, clear, noticeable, or the number itself |
| Many, most, some, a few | The count |
| It's clear that | (delete) |
| Users check the preview (from interviews) | 5 of 8 said they check the preview; in the task, 2 of them did |

## Words to look for

Go through the draft for these words, outside quotes from participants.
Each one is a sentence to reread, not an automatic error: keep it if it
reports what someone said ("P3 said it was because of the deadline") or
a tested result, and reword it otherwise. Where Magpie can run code,
`python3 tools/checks/wording_check.py findings.md` finds them; where it
can't, search for them by hand and say so in the record. Running this as
code rather than by eye follows claim-stress-tester (S102).

| Kind | Words | Fine when | Otherwise |
| --- | --- | --- | --- |
| Every or none | all, always, never, every, everyone, everybody, nobody, no one, none, without exception | the sentence gives the count, and it's true for every person | give the count and name who didn't fit |
| Cause | causes, caused, drives, drove, driven by, leads to, led to, results in, because of, due to | a test showed the cause, or it's a reason someone gave | say what's known: a pattern, or what people said |
| Vague amount | most, many, some, a few, several, the majority, nearly all, almost all, almost everyone, users want, customers want, people want | the sentence gives the count | replace with the count |
| Overclaiming | proves, proven, clearly, obviously, definitely, undeniably, it's clear that | never | "suggests", "supports", "is consistent with", or delete |
| Significant | significant, significantly | the test is named (a p-value, t-test, chi-square, confidence interval) | "large", "clear", or the number |

## Basis

Practitioner judgment, consistent with widely published guidance on
reporting qualitative and survey research. Rule 15 and the word search
as code take their idea from claim-stress-tester (S102); the rules and
word lists as written are Magpie's own. Sources will be added to
`docs/PROVENANCE.md` as they are checked.
