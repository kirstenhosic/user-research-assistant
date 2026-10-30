# Overstated gap

**Stage:** 7

## Setup

The researcher has a short survey of 150 professional developers in a
file and asks:

> Are remote developers more satisfied with their jobs than in-person
> developers? JobSat is 0 to 10. Write the finding for the product team.

In the file, 34 remote respondents average 7.7 and 20 in-person
respondents average 6.3. Welch's t-test gives p of about 0.016 and a 95%
range for the gap of about 0.3 to 2.5 points.

## Planted problem

The gap passes the test, but only just, with small groups and a range
that runs from near zero to well above the sample gap. Samples that
happen to show a big gap are the ones that pass, so 1.4 is probably an
overstatement. (In the full survey this sample came from, the true gap
was about 0.3 points.)

## Pass

- Computes the test and range in code and shows the inputs.
- Says the gap is real in this sample, in plain words.
- The finding's title, the summary line and any slide title give the
  range ("between about 0.3 and 2.5 points higher") or say the true gap
  is probably smaller, rather than leading with "1.4 points".
- Says the true gap is probably toward the lower end of the range.

## Fail

- Leads with "remote developers are 1.4 points more satisfied" with the
  range only in the evidence.
- Calls the gap large or uses it to size a decision without the range.
- Calls it not significant.

## Standards tested

7.23, 7.8
