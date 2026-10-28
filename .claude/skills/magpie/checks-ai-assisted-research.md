# Check: when AI runs part of the study

What to do when an AI tool moderates sessions, summarizes transcripts,
recruits participants, or is Magpie itself drafting findings. These tools
are useful enough to create false confidence, which is the risk; the checks
below are what keep the work research rather than something that looks like
it.

## 1. An AI moderator shapes answers

An AI running interviews follows the guide but phrases follow-ups,
sequences questions and acknowledges answers in ways that can narrow what
participants say. Participants are blunter with an AI, and also more
responsive to each question's framing, because there's no person to push
back against. The data comes out tidier and more convergent, and the
tidiness is the problem: it reflects the prompts more than the people.

- The moderator's instructions get the same wording check as a human
  guide (`checks-guide-wording.md`), item by item, before launch.
- The instructions set boundaries (topics in and out of scope) and a
  fallback for unclear answers: ask the participant to say more; don't
  rephrase or interpret.
- Pilot the moderator with two or three internal participants first.
- **Audit the first three transcripts in full** before more sessions run.
  Read the moderator's actual follow-ups. Look for leading phrasing, for
  off-script probes, and for participants converging on the same words,
  which signals shaping. If any of it shows, stop the study and revise the
  instructions. This gate is what makes AI-moderated data credible.

## 2. An AI summary is a first draft

A summary of transcripts reads like findings: confident, structured prose.
It isn't. It compresses what was said by pattern and frequency, without
the judgment about which moments matter for this decision, without
weighing the people who disagreed, and without telling a strong opinion
from passive agreement. The common failure is smoothing: six positive
participants and two seriously confused ones become "generally positive,
some minor confusion", and the two who may represent a real problem
disappear.

- Treat every AI summary, Magpie's own drafts included, as a draft that
  tells you which transcripts to read in full, not as a substitute for
  reading them.
- A human synthesis step sits between any AI output and anything a
  stakeholder sees. The tool finds the candidates; the researcher decides
  which matter and why. Magpie asks the researcher to confirm they've read
  the passages behind each top finding before drafting the readout, and
  logs "not confirmed" as a risk if they haven't.
- Every claim traces to specific participant moments with quotes and
  context. If it can't be traced, it doesn't go in.

## 3. Receipts

Traditional studies build an evidence trail by default: recordings,
timestamped notes, coded transcripts, synthesis documents that link claims
to data. When tools handle moderation and summarizing, that trail thins out
unless the researcher keeps it on purpose.

- Raw transcripts are stored alongside any summaries.
- **No finding goes into a stakeholder-facing document without receipts:**
  at least two traceable participant references (code and location) per
  directional claim, or a single case labeled as one.
- Where the tool links summary claims to timestamped quotes, use that; the
  feature only helps if someone actually follows the links.

## 4. Participant quality

Tools that make recruiting faster also make fraud easier: bots, people who
speed through for the incentive, people who paste AI-written answers. The
risk is low when participants come from your own verified user base and
high with third-party panels, whose incentive economics reward fraud.

- Assume some of the sample is compromised and plan to catch it before
  synthesis, not after.
- Read early transcripts, not just summaries. Watch for answers that are
  too clean, too fast, or too perfectly structured.
- Set a disqualification threshold and a replacement protocol in the plan,
  so removing someone doesn't stall the study.
- Platform fraud detection is worth having and doesn't replace judgment.
  Fast recruiting and good recruiting are different things.

## Basis

S10 (see `docs/PROVENANCE.md`): the five failure modes and their
mitigations, including the first-three-transcript audit, the human
synthesis step, receipts, and the fraud signals, come from the passage
recorded there. The wording and the fit to Magpie's stages are this
project's.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
