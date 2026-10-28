# Question review

A fresh pass over the questions Magpie wrote for participants, by a
reviewer that sees only the research questions and the draft, not the
conversation that produced them. Required at stage 5, for every interview
guide, usability test script, survey, diary study, focus group guide and
concept test. Available on request at any other stage, including on
research questions at stage 2 and on a guide the researcher wrote.

## Why it's separate

The pass that wrote the questions knows what each one is meant to ask, so
it reads the intent rather than the words. A participant hears only the
words. A reviewer that hasn't seen the intent hears them the same way: the
question that hints at the answer, the one that asks two things, the jump
from one topic to the next with no warning.

## How to run it

Run it after the wording check (`checks-guide-wording.md` or
`checks-survey-wording.md`) and in the same reply as the draft, without
waiting to be asked.

The reviewer gets three things, in this order, each labelled:

```
RESEARCH QUESTIONS
(the primary and secondary questions, the decision they serve, who the
participants are, the session length and format)

DRAFT
(the guide, script, survey or prompts, word for word)

REVIEW PROMPT
(the text below)
```

**Where you can start a separate agent** (Claude Code, or any setup with
subagents): start one and give it the three parts. Leave out the
conversation that produced the draft.

**Anywhere else:** give the researcher the exact text to paste, in that
order, and tell them to open a chat where Magpie isn't running (outside
the Magpie project on Claude.ai or ChatGPT, or with the Magpie skill
turned off in Gemini or Copilot), paste it, and paste the reviewer's list
back into this conversation. Until it comes back, the status line shows
the review as waiting.

**Either way:** Magpie goes through the list, fixes what's right, says
why it disagrees with what's wrong, and logs the review in the record's
change log. The researcher's call stands on any point.

## The review prompt

> You are reviewing questions written for a user research study. Above
> this prompt are the research questions the study must answer and the
> draft that participants will hear or read. You have not seen how the
> draft was made, which is why your reading is useful: read it as a
> participant would, and as the moderator who has to say it aloud.
>
> Go through the draft item by item, then as a whole. Be specific: quote
> the item, say what's wrong in a sentence, and offer a rewrite.
>
> 1. **Does any question lead?** It hints at the answer, praises or
>    criticises the product, or assumes a feeling ("what frustrates you
>    about…").
> 2. **Does any question ask two things?** "Fast and easy", "how and why",
>    "this or that". Split it.
> 3. **Does any question ask people to predict themselves?** "Would you
>    use…", "how likely are you to…" where a question about what they last
>    did would work.
> 4. **Is any question closed when it should be open, or too abstract?**
>    A yes/no where a story is needed; "what do you value" where a
>    specific time would get a real answer.
> 5. **Is any wording unfamiliar to participants?** Internal feature
>    names, acronyms, research terms.
> 6. **For surveys:** one idea per item, balanced and labelled scales,
>    answer options that cover every case without overlapping, a specific
>    time period, sensitive items late and optional.
> 7. **Does the order make sense as a conversation?** Easy before hard;
>    what they did before what they think; general before specific; one
>    topic finished before the next starts; sensitive questions after
>    rapport; the questions that matter most before the halfway point; no
>    task or question that gives away a later one.
> 8. **Does it sound like a person talking?** Read the opening, the
>    warm-up and every move between sections aloud. Each should be words
>    the moderator can say as written, with a short spoken transition
>    between topics ("Thanks, that's really helpful. Now I'd like to
>    shift to how you…"). Flag anything that reads like a form, a heading
>    with no spoken line, or a sentence too long to say in one breath.
> 9. **Does it answer the research questions?** Name any research
>    question no item serves, and any item that serves none.
> 10. **Are the research questions themselves sound?** Flag any that asks
>    two things, assumes its answer, is about the product rather than
>    people, or can't be answered by this method.
>
> Reply as a numbered list of problems. Each item quotes the question,
> names the problem, and gives a rewrite. Leave out what's right; the list
> is for fixing. Leave the draft as it is; the author will make the
> changes.

## What Magpie does with the result

- Fixes every problem the review got right and names the fix.
- For each point it disagrees with, says why in a sentence and leaves the
  researcher to decide.
- Never silently drops a review point.
- Runs at most two passes. Remaining disagreements go to the researcher
  with both sides stated.

## Limits

The reviewer is a model too. It can miss things and it can be wrong. A
pilot session with a real participant still catches what no review does.

---

Part of Magpie, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
