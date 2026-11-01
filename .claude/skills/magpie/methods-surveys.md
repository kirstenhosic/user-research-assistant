# Method: surveys

Ask many people the same questions to measure how common an attitude,
behavior or need is.

## Use it when

- The question is *how many*, *how often*, or *which groups differ*.
- You already understand the problem well enough to write good closed
  questions. (If you don't, interview first.)
- You can reach enough of the right people to say something about them.

## Don't use it when

- The question is *why*. Surveys get thin answers to why.
- You'd be surveying whoever's easiest to reach and calling it "users".
- A number already exists in analytics.
- You can't get enough answers to analyze. Check this first; see "Can it
  get enough answers?" below.

## Can it get enough answers?

Before writing a single item, do this sum. It's the first question in
survey planning, and it can be done on a phone calculator.

1. **Responses needed.** How many answers the analysis needs. For an
   overall picture of one group, a few hundred. To compare groups, enough
   in each group that a difference would show; the smaller the difference
   you need to see, the more you need. Stage 7 has the sample size rules.
2. **Response rate.** What share of invited people answer. Use the rate
   from a past survey to a similar group; otherwise guess low, and say
   it's a guess.
3. **Invites needed** = responses needed ÷ response rate.
4. **Invites available.** How many of the right people the tool can reach,
   after removing anyone who can't be contacted or was surveyed recently.
5. **Viability** = invites available ÷ invites needed.

Above 1, the survey can get what it needs (at exactly 1 it uses every
invite, leaving none for other surveys). A little below 1 means weaker
results the team may accept. Well below 1, the survey isn't viable as
planned. To raise the number: shorten the survey, add an incentive or a
reminder, target better, cut the number of groups to compare, or widen who
is eligible. Don't lower the bar for how sure you need to be.

Example: a team wants 390 answers, past surveys to this group got 1.5%,
so they need 26,000 invites. They can reach 100,000 people. Viability is
about 3.9. Go ahead.

## Sample

- Who answers matters more than how many. A self-selected sample describes
  the people who chose to answer. Engaged users answer more than others,
  so the answers lean their way.
- Rough guide: a few hundred responses for an overall picture; enough in
  each group you want to compare that the comparison means something. Plan
  the cross-tabs before you send.
- Where the team knows the make-up of the whole user base (from logs:
  tenure, plan, usage, country), the answers can be weighted so each
  group counts in proportion to its real size. This needs an analyst and
  a larger sample; say in the readout whether it was done. Don't weight
  an experiment where people were assigned at random; that already
  handles it.
- The margin of error shrinks with the square root of the sample, not
  the sample: halving it takes about four times the responses (a margin
  of about 20 points from 20 answers needs about 80 answers to reach 10
  points). Decide the precision the decision needs, then the sample.
- Say the response rate and who answered in the readout.

## Question types

- **Closed, one answer.** The workhorse. Keep lists short, four or five
  options where you can; more only for factual items such as role or
  country. Lists must cover every real answer and not overlap; add "other"
  and "don't know" where they're honestly possible.
- **Closed, pick all that apply.** People pick fewer than they would if
  asked one by one. Where the list is short, ask each as its own yes/no
  (forced choice); answers are more accurate, especially on sensitive
  topics.
- **Rating scale.** Five or seven points, words on every point or at least
  both ends, as many positive as negative points, and the same scale
  throughout. Keep the order of the scale fixed; its order carries
  meaning. If you worry the first option draws answers, show half the
  people the scale reversed.
- **Agree/disagree.** Use sparingly. People lean toward agreeing, more so
  with less schooling and with an interviewer present. Ask the thing
  directly instead ("How often do you…", "How would you rate…"), or offer
  a choice between two statements.
- **Open-ended.** One or two, where a story helps, never required. An open
  item early in a survey can find the answers a closed list should offer
  later; run a small open pilot, then build the closed list from what
  people said.
- **Validated questionnaires.** For common things (perceived usability, task
  ease), use a published scale as written (`methods-usability-testing.md`,
  "Follow-up questions"). The wording has already been tested, and the
  score can be compared with published figures. Beyond the SUS: the
  CSUQ (16 items, seven points, free) for any system; the SUPR-Q (eight
  items) for websites, with paid norms; the WAMMI (20 items, licensed)
  for websites; the UEQ or AttrakDiff when the question is how a
  product feels rather than how usable it is; the TAM's two six-item
  scales for perceived usefulness and ease of use. Use one as
  published; small wording swaps ("website" for "system") don't change
  what it measures. When space allows only two items, the UMUX-LITE
  stands in for the SUS (`methods-usability-testing.md`, "Debrief").
  If the survey carries a Net Promoter question, keep the 0 to 10
  answers and report their mean with a range, not only the net score
  (`methods-benchmarking.md`).

## Wording

Small changes move answers a lot, so every item goes through
`checks-survey-wording.md`. The rules that matter most:

- One idea per item. No double-barreled questions.
- Plain words for the audience. No jargon, internal names or double
  negatives.
- Behavior over a specific period: "In the last 30 days…" beats "usually".
  The past, not the future: "Would you use…?" gets kind answers, not true
  ones.
- Watch loaded words. The same policy gets different support under two
  names.
- People under-report what looks bad and over-report what looks good.
  Soften the frame ("Some people don't get round to X; in the last month,
  did you…?") and make the less flattering answer easy to give.
- Trend surveys keep wording, order and channel the same every wave.
  Change any of them and the trend breaks.
- Not sure between two wordings? Give each to half the sample at random.
  If the answers differ, the wording did it.

## Order

Earlier questions change later answers.

- General before specific. A specific question first ("How is the export
  feature?") pulls the general one ("How is the product?") toward it.
- Open-ended questions about problems or priorities go early, before
  closed items plant ideas.
- Start with easy, interesting items. Don't stack hard ones. Demographics
  last, unless needed to route people.
- Rotate the order of options in lists with no natural order (brands,
  features). It doesn't remove the order effect; it spreads it evenly.
  Don't rotate a scale.

## Survey shape (under ten minutes)

1. Intro: what it's for, how long, what's done with answers.
2. Screener: behavior-based.
3. Main sections, general to specific, one topic each.
4. One or two optional open-ends where a story helps.
5. Demographics last, each with "prefer not to say".
6. Thanks, and what happens next.

The survey is part of the product experience. People don't separate "the
survey" from the company that sent it. Too long, too often, broken
branching, an image that doesn't load, or a question that makes no sense
all cost goodwill, and a mistake reaches thousands of people at once.
Match length to what people are motivated to give, watch how often the
same people are invited, and test the built survey, not only the
question list.

## Test it before sending

Every new survey gets a cognitive test: a few people answer it while
thinking aloud, then say what each question meant to them, why they chose
their answer, and where the words or the options were unclear. It
catches four kinds of failure: the question isn't understood, the event
can't be recalled, the answer is shaped by an earlier item or by what
looks good, or the options don't fit.

- **Fast way (one to two days).** Put the survey link in an unmoderated
  testing tool with instructions to flag unclear words, missing options
  and confusing questions. Four or five people from one group find most
  of the problems; with several groups, two or three from each. Save the
  test as a template and rerun it after changes.
- **Moderated way.** Worth it for a complex survey, a tracking survey
  (bad wording compounds every wave and can't be changed later without
  breaking the trend), a survey in more than one language (test each
  language, or at least have a native speaker who didn't translate it
  read it), or a decision too big to get wrong.
- **Skip or shorten it** only for items taken from a published, validated
  questionnaire.

Have colleagues click through the built survey too. Branching that leads
nowhere and text that fails to fill in show up only in the real thing.

## Analysis

Descriptives first: counts and percentages with the base shown. Cross-tabs
only where groups are big enough. Open-ends coded like interview data
(`methods-customer-feedback-coding.md` covers coding at volume). Say what
the numbers can and can't support; don't claim significance without a
test, and even with one explain it in plain words. Stage 7 covers this,
including how to state a test result, a margin of error or a sample size.

Report differences in their own units: "9 percentage points more
completed", "17 seconds faster", "0.4 points higher on a 7-point scale",
with the range the true difference probably sits in. A standardized
effect size on its own ("d = 0.3") means nothing to the team. Whether a
difference is big enough to act on is a separate question from whether it
is real; agree the bar before the data arrives, not after.

## Worked example

> **Decision.** Whether Larder (meal planning) builds a shared household
> plan, or keeps plans personal. Decision in eight weeks.
>
> **Research question.** How many Larder users plan meals with someone
> else in their household, and does that differ by household size?
>
> **Viability.** Needed: 400 responses to see a 10-point difference
> between one-adult and two-adult households. Past response rate to this
> list: 2%. Invites needed: 20,000. Reachable, excluding anyone surveyed
> in the last 90 days: 64,000. Viability 3.2. Go.
>
> **Items.** Behavior over a period ("In the last 30 days, how many times
> did someone else in your household change your meal plan?"), one
> rating with labels on every point, demographics last. Cognitive test
> with five users in an unmoderated tool: "change your meal plan" read
> three ways; reworded to "add, remove or swap a meal".
>
> **Result, as reported.** 441 responses (2.2% of 20,000 invited;
> respondents skewed to weekly users). 38% of two-adult households
> (112 of 295) said someone else changed the plan in the last 30 days,
> against 9% of one-adult households (13 of 146); a difference of 29
> points, likely between 21 and 37. Agreed bar before fielding: 15 points.

## Pitfalls

- "Would you use…?" items. Ask about the past, not the future.
- Agree/disagree batteries that people agree their way through.
- A 25-item survey that gets ten honest answers and fifteen fast ones.
- Reporting percentages from forty responses as if they were the market.
- Sending without a cognitive test, then finding out from the open-ends
  that a question was read three ways.
- A viability sum done after the survey is written, when the team has
  already promised the result.

## Template

`templates-survey.md`

## Basis

Viability: S79 (invites needed = target responses ÷ response rate;
viability = invites available ÷ invites needed; above 1 proceed, at 1 no
invites left for other surveys, well below 1 not viable; ways to raise it;
don't lower alpha or power; the worked example). Weighting: S83
(respondents rarely mirror the user base; engaged users respond more;
in-house teams can weight on log variables such as tenure and usage;
don't weight a randomized experiment; weighting needs a larger sample and
expert tools). Question types, wording and order: S88 (closed lists of
four or five options; forced choice over select-all; agree/disagree
invites acquiescence, stronger among less-educated respondents and with
an interviewer; loaded words; social desirability and softening the
frame; identical wording and mode for trends; split-sample wording tests;
contrast and assimilation effects; open before closed on the same topic;
engaging items first, demographics late; ordinal scales kept in order,
sometimes reversed for half the sample; nominal lists rotated; open pilot
to build closed lists; pretesting with cognitive interviews). Also S6
(ask only what the research questions need; neutral wording); S8 (past
behavior over future intentions); S40 (word-labeled scales; acquiescence
and social desirability bias). The survey as part of the product
experience: S82 (people don't separate a survey from the brand; length,
frequency, broken branching and media; test the built instrument; a
colleague click-through). Cognitive testing: S80 (the four stages
comprehension, retrieval, judgment, response; when it's needed most:
tracking surveys, high-stakes decisions, multiple languages; validated
scales need less); S81 (the unmoderated fast way, one to two days; four
or five from one group, two or three per segment; save as a template).
Reporting differences: S84 (raw, unstandardized differences with
intervals; standardized effects hide the unit and distort near a scale
ceiling); S85 (set the "big enough" bar before collecting data; make
effects concrete). The other standardized questionnaires: S100 (pp. 226–237: WAMMI,
SUPR-Q and their norms databases and licensing; CSUQ as a PSSUQ
variant with the same scoring; USE; hedonic quality, AttrakDiff and
the UEQ; the TAM's two scales; minor wording changes don't change the
factor structure; pp. 211–214: the UMUX-LITE as a two-item stand-in
where survey space is short; p. 235: the NPS and its lost sensitivity).
The four-times rule for halving a margin of error: S100 (pp. 19–24:
a confidence interval is set by the confidence level, the variability
and the sample size; to cut the margin in half you need about four
times the sample). Sample size rule of thumb ("a few hundred"), the
ten-minute limit and the survey shape: practitioner judgment.

---

Part of Magpie version 2026-11-01, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
