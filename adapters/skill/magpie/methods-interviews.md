# Method: interviews

One-to-one conversations to understand how people do something, why, and
what gets in the way.

## Use it when

- The question is about *why* or *how*: motivations, workflows, workarounds,
  decisions.
- You need to understand a problem before designing anything.
- You have access to the right people and time to talk to them.

## Don't use it when

- The question is *how many* or *how often*. Interviews can't tell you that.
- You already know the problem and need to know whether a design works.
  Test it instead.
- You can't reach the people the decision is about.

## Sample

- Start at five or six for a single, fairly uniform group, and analyze as
  you go. Add people while sessions still bring new codes; stop when they
  add little. Five is often not enough for interviews, and a broad question
  across varied people can need twenty or more.
- Where groups differ, recruit across the differences that could change the
  answers. A fixed number per persona ("five each") can mean far more
  interviews than the question needs.
- Recruit on recent behaviour ("did X in the last month"), not on
  self-description ("considers themselves a power user").

## Session shape (45 to 60 minutes)

1. Opening: who you are, what it's for, what's recorded, they can stop. Two
   minutes.
2. Warm-up: about them and their work. Easy. Five minutes.
3. Main questions: past, specific, concrete. "Tell me about the last time…"
   Thirty minutes.
4. Deep dive on one thing they raised. Ten minutes.
5. Close: anything we didn't ask, thanks, what happens next.

## What makes it good

- Specific stories over general opinions. The last time, not the usual.
- Silence. Count to five before filling it.
- Probes ready: "what happened next?", "what did you do instead?", "can you
  show me?"
- Notes capture what they did and said, separately from what you think it
  means.

## Ratings with a "why"

A rating question followed by "why that number?" is a quick way into a
conversation, and it lets you compare how people felt about the same
moment. In an interview the reason is the data; the number is a prompt.

- **Ask about a specific moment.** "Thinking about the last time you
  [did the thing], how easy or hard was it, from 1, very hard, to 7, very
  easy?" Not "how easy is it in general".
- **Follow every rating with "Why that number?"** Then probe the reason
  as you would any answer: "What happened that made it a 3?" If it isn't
  already clear, ask what would have moved it up or down.
- **Keep it to one to three ratings per session.** Closed questions stop
  the conversation; too many turn an interview into a spoken survey.
- **Use the same scale every time,** with words on both ends, so answers
  can be compared across people.
- **Expect ratings to run kind.** People rate higher to the researcher's
  face than they feel. A 6 with a story of a workaround is a problem,
  whatever the number says.

In analysis, report each person's rating next to their reason ("P3: 2 of
7, because the export failed twice"). Don't average interview ratings or
turn them into percentages; with eight people a mean looks precise and
isn't. The reasons, coded like any other answer, are the finding.

## Analysis

Thematic analysis: read everything, code what's there, group codes into
themes, check each theme against the participants who don't fit it. Keep
quotes tied to participant codes and timestamps. Stage 6 covers this.

## Pitfalls

- Asking people to predict their future behaviour.
- Letting a talkative participant set the agenda for the whole study.
- Hearing what you hoped to hear. Write down the disconfirming cases.
- Treating eight interviews as "most users think…". They tell you what
  exists, not how common it is.

## If an AI moderates

Some tools run interviews from a guide. They're blunter-friendly but shape
answers through phrasing and follow-ups, and the data comes out tidier than
the people were. Treat the moderator's instructions as a guide (wording
check, boundaries, fallback for unclear answers) and read the first three
transcripts in full before the rest run. `checks/ai-assisted-research.md`.

## Template

`templates/interview-guide.md`

## Basis

Sample: S42 (no fixed number; start with five or six and add while new
codes appear; five is often not enough; broad, varied studies can need 20
to 30 or more; a fixed number per persona can mean too many). Session and
questions: S41 (easy questions first to put people at ease; ask about
specific events, because memory is flawed; follow-up questions prepared,
probes used as they arise; leading questions compromise the data); S5
(past experience over hypotheticals); S8 (self-reported intentions are
unreliable). Recruiting on behaviour: S9. Analysis: S1b. Ratings with a
"why": S38 (pair a rating with "why did you give it that score?" for
qualitative insight, and don't make much of the average from a few users);
S39 (closed questions used sparingly in qualitative research, because they
stop the conversation); S40 (word-labelled scales are easier to understand;
rating scales are prone to acquiescence and social-desirability bias); S12
(numbers from small qualitative studies carry large error). Session timings,
counting to five in silences, one to three ratings, and the AI-moderator
section's reading rule: practitioner judgment (the AI-moderator risks
themselves: S10).
