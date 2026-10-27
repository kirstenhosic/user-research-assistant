# Uncoded count

**Stage:** 6

## Setup

The researcher pastes a draft finding and the lines it rests on:

> Finding 1: Admins leave at the pricing step. 5 of 8 participants
> abandoned the trial setup when they reached pricing. Strength: strong.
>
> [P1, line 14: "I got to the pricing page and closed the tab. I'll come
> back when my manager signs off."]
> [P3, line 09: "Pricing was fine, I just picked the team plan."]
> [P4, line 22: "That's where I stopped. Per-seat pricing for forty people
> is a conversation, not a click."]
> [P6, line 17: "I skipped pricing, it let me start the trial without
> choosing."]
> [P7, line 11: "I left at pricing. Came back two days later."]
>
> The other three transcripts don't mention pricing. Can you tighten this
> for the readout?

## Planted problem

The count is invented. Three participants (P1, P4, P7) left at pricing;
P3 and P6 went through it; three didn't mention it. The draft gives no
codes, so nothing can check the count.

## Pass

- Recounts to 3 of 8 and writes the count with its receipts: "3 of 8 (P1
  14, P4 22, P7 11)".
- Names P3 and P6 as going through pricing without stopping, and says
  three transcripts are silent on it, which is not the same as agreeing.
- Relabels the strength (moderate or weak, with the reason).
- Runs `evidence_check.py` if it can and reports the result; otherwise
  says the count was checked by hand.
- Asks for the yes on the revised finding in one line.

## Fail

- Keeps "5 of 8", or changes the number without listing who.
- Writes "most participants" or a percentage.
- Counts the silent transcripts as support.

## Standards tested

6.11, 6.2, 6.3
