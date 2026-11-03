# Check: release

Run this before any output meant for other people is offered for the
researcher's yes: the readout and the report at stage 8, and also a
findings summary, a workshop summary, a persona, a journey map, a
research library entry, an opportunity brief, or anything else the
researcher says they'll share. Run it again if the destination changes.
The question it answers: can this leave the researcher's hands and go
where it's going without carrying a person with it?

## The destination

Ask once, with the stage's other questions, where the output goes after the
room:

- **The team:** the people who ran or sponsored the study.
- **The company:** anyone inside it, now or later, through a wiki, a
  library or a forwarded deck.
- **Outside:** customers, partners, a conference, a public post.

Until the researcher answers, run the check for the company. Most
research stays inside the company, and a deck travels further than the
room it was made for. If the researcher later says it's going outside,
run the check again for outside.

## What's allowed where

Every item is a blocking item at every challenge level. Fix it, say what
changed in one line, and only then ask for the yes.

| | Team | Company | Outside |
| --- | --- | --- | --- |
| Participants' names, emails, phone numbers, handles; colleagues' names | Never | Never | Never |
| Customers' or employers' company names | Only if the team profile allows | Only if the team profile allows | Never |
| Role descriptions | As written | Broadened where they point to one person | Broadened further: no mix of size, location and role that narrows to a few people |
| Quotes | Fine | Fine | Only with consent for use outside the company |
| Clips, screenshots, photos, faces, voices | As consent allows | As consent allows | Only with separate consent for that use; otherwise left out |
| Participant list, raw counts with line references, risks log, partner data | Fine | Appendix only | Left out |

- **Names.** Participants appear as codes (P1, P2) with a descriptor
  from the participant list. In a quote, a name, email or phone number
  becomes a placeholder such as [name] (`operating.md`, "Personal details
  in the material"). This holds for every destination and no team rule
  changes it.
- **Company names.** Customers' and employers' names become [company]
  unless the team profile's "Company names in internal outputs" line
  says they're allowed, and then only for the team and the company.
  Rules on this differ by country and by company, so the default is the
  strict one. Never outside.
- **One-person labels.** Where a descriptor, or a descriptor with a
  detail in the quote, would point to one person (the only CTO in the
  sample; the one small business in a given city), broaden it and say
  once why (standard 7.4).
- **Consent matches use.** A quote, a clip, a screenshot or a photo going
  beyond ordinary use of the findings has its own consent on record.
  Where it doesn't, the item comes out or goes back to the researcher to
  ask for consent (`checks-ethics-and-consent.md`).
- **Sensitive findings as agreed.** A finding that reflects on a person or
  a team is framed the way the researcher said in the "Before you build"
  answers. If they said nothing, it's framed for the destination and
  flagged in the reply.
- **Status on the document.** The document details block says Draft until
  the yes, and the destination appears in the details or the appendix, so a
  reader who forwards it can see where it was meant to go.

## How to check

Where Magpie can run code, save the output to a file and run
`python3 tools/checks/personal_details_check.py output.md --names "..."`,
passing the names Magpie noted in the material (participants,
colleagues, and companies unless the team profile allows them). It flags
emails, phone numbers, handles and those names. Pass the names on the
command line only; never write them to a file. Then read the output for
what code can't catch: one-person labels, consent and sensitive
findings. Where Magpie can't run code, do all of it by reading and say
so.

The independent review also asks whether anyone could be identified
(`review-independent-review.md`, question 11). Treat its points the same
way.

## What to say

One line naming the destination and the changes, in the same reply as the
draft: "Checked for the company: two employer names became [company], P7's
label is now 'technical leader, enterprise', and the Q3 screenshot is out
until there's consent for it." If nothing changed, say that in half a line.
Don't ask about any of it.

---

Part of Magpie version 2026-11-03, made by Kirsten Hosic (https://github.com/kirstenhosic/user-research-assistant). MIT License.
