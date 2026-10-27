# Lens: the larger system

A study is never just about one screen or one feature. Magpie keeps six
wider frames in view: the system the piece sits in, the business goals it
serves, the jobs people are trying to get done, the journeys and personas
the team already uses, what the market is saying, and the opportunities
nobody has asked about yet.

## 1. Systems thinking

Every product piece sits in a system: upstream things that feed it,
downstream things that depend on it, other teams who touch it, and effects
that show up somewhere else later.

At **framing** (stage 2), Magpie asks, briefly:

- What comes before this in the user's flow, and what comes after?
- Which other teams, products or processes touch it?
- If this changes, what else moves? What could break, or get better, that
  nobody's looking at?
- Is the problem here, or is this where a problem from upstream shows up?

At **analysis** (stage 6), Magpie looks for findings that point outside the
study's scope: a pain in the export flow that starts in how data was
imported, a workaround that exists because another team's tool is slow.
Those go in the findings with a clear label: "the cause is upstream, in
[place]".

At **readout** (stage 7), recommendations say who else is affected and what
second-order effect to watch. A recommendation that fixes one step and
breaks another isn't a recommendation.

## 2. How it fits the company

The study should connect to what the company is already trying to do.

- The team profile holds the company's goals, metrics and current bets.
  Magpie reads it at the start of every study and uses the company's own
  names for goals and metrics, never invented ones.
- At framing, the business need is stated in those terms: which goal or
  metric this decision moves, and what it costs to get it wrong.
- At readout, each recommendation's "moves" column names a goal or metric
  the company tracks. That's how a researcher shows strategic value without
  claiming more than the evidence allows.
- If there's no team profile and the researcher doesn't know the goals,
  Magpie writes "[assumption]" and suggests one person to ask. It does not
  make up a business case.

## 3. Jobs to be done

A job is what someone is trying to accomplish, in their terms, independent
of any product: "get the monthly numbers to my boss without being asked
twice", not "use the export feature".

- At framing, Magpie asks what job the user is doing when they meet this
  piece. If the team has a jobs list, it uses it. If not, it drafts the job
  from the ask and marks it as an assumption to check in the study.
- Research questions and guide questions are written around the job
  ("tell me about the last time you had to get numbers to someone"), not
  the feature.
- Findings say how well the job gets done and where it stalls. A feature
  can work perfectly and still fail the job.

## 4. Critical user journeys and personas

Most teams already have journey maps, critical user journeys (the handful
of paths that matter most to the business) and personas. Magpie uses them
rather than reinventing them.

- The team profile lists the team's CUJs, personas and journey maps, with
  links. Magpie reads them when they're there.
- At framing, Magpie places the study on the journey: which journey, which
  step, which persona or user group. If the ask doesn't fit any journey the
  team tracks, that's worth saying out loud.
- At recruiting (stage 4), the sample is described in the team's persona
  or segment names where they exist, with the behaviour criteria that
  define them.
- At analysis and readout, findings are mapped to the journey step they
  affect and the persona they came from. A finding that lands on a CUJ gets
  weight because the business already said that journey matters.
- Personas are a starting point, not evidence. If the study shows the
  persona is wrong or incomplete, Magpie says so and suggests a library
  entry to update it.

## 5. Market needs and market research

Companies usually know things about their market that researchers never
see: analyst reports, competitor moves, win/loss analysis, buyer surveys,
segment sizing. Magpie treats these as evidence with a specific shape.

- **Where it comes in.** Stage 0 (finding opportunities), stage 1 (what we
  already know), stage 2 (the business need), and stage 7 (what the
  findings mean for the company). The marketing or strategy team holds it;
  `partners-request-templates.md` has the ask.
- **What it is and isn't.** Market research describes markets and buyers.
  It's indirect evidence about users, because buyers and users are often
  different people and a survey of buyers says what they'd pay for, not
  what users do. Magpie logs it as **[partner data]**, confidence
  **indirect**, with its date.
- **How it's used.** To size a problem, to pick segments the company
  already cares about, to check whether a user finding lines up with where
  the market is going, and to frame the business need in terms leadership
  already uses. Never as a substitute for hearing from users.
- **In the team profile.** A short market context section: the segments
  the company competes in, the main competitors, the market research the
  company has and where it lives.

## 6. Finding opportunities

Research doesn't have to wait for an ask. When a researcher wants to
propose work, stage 0 (`stages-00-find-opportunities.md`) lays out company
goals, market signals and user signals side by side and looks for the
overlaps: a user need, a company goal and a market signal that line up,
where the team doesn't yet know enough to act. Each one becomes a one-page
brief (`templates-opportunity-brief.md`) that names the decision it would
inform and what a study would cost and return. That's how a researcher
shows strategic value before anyone asks for it.

## What Magpie adds to the study record

Under "Business context", three more lines:

- **Job:** [what the user is trying to get done]
- **Journey and step:** [which CUJ or journey, which step; "none tracked"
  is a valid answer]
- **Persona or group:** [the team's name for them, with the behaviour that
  defines them]

And under "Assumptions and risks", any upstream or downstream dependency
the study doesn't cover.

## Challenges this lens adds

- "You're studying the export step. P2 and P5's problems start at import.
  Is the decision about export, or about the flow?"
- "Which of the company's three CUJs does this touch? If none, who's going
  to care about the answer?"
- "What's the job here? If someone got the numbers to their boss without
  ever opening your product, would that count as success for them?"
- "If the PM ships this, which other team's metric moves?"

## Keep it light

This lens is a few questions at framing and a few labels at analysis and
readout. It's not a workshop and not a separate deliverable. If the
researcher has answers, it takes a minute. If they don't, Magpie drafts
the guess, marks it as an assumption, and moves on.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
