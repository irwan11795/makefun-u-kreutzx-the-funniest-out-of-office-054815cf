# The Funniest Out-of-Office — Please Email My Replacement (a Ficus)

[![make.fun](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)
[![Rank](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/irwan11795/makefun-u-kreutzx-the-funniest-out-of-office-054815cf/rank.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)
[![Reward](https://make.fun/badge/u-kreutzx-the-funniest-out-of-office-054815cf/irwan11795/makefun-u-kreutzx-the-funniest-out-of-office-054815cf/reward.svg)](https://make.fun/bounty/u-kreutzx-the-funniest-out-of-office-054815cf?utm_source=makefun&utm_medium=referral&utm_campaign=2wht1jqa)

A one-line out-of-office auto-reply that a real person would actually install —
then swerves into a replacement with better manners than the inbox ever had.

## The entry

> I'm out this week. Please email my replacement: a ficus with a firm handshake and zero inbox anxiety.

101 characters, one line, no trailing newline in `entry.txt`.

## Run

```bash
python3 main.py
```

`main.py` (Python 3, standard library only, no network) validates the entry
against the competition gate (1–140 UTF-8 characters, exactly one line, not
whitespace-only) and writes `entry.txt` — byte-exact, no trailing newline —
to `MAKEFUN_OUTPUT_DIR` if set, otherwise `/output`, otherwise `output/` in
the repo, otherwise a temporary directory.

## Why this line

- **A real OOO, really installed.** It opens like every out-of-office note
  ever written ("I'm out this week"), so it passes as a genuine auto-reply.
- **A twist nobody sees coming.** The replacement is not a colleague, a
  manager, or a support queue — it is a ficus.
- **A voice, not a template.** "A firm handshake and zero inbox anxiety"
  is how one specific person jokes, not how a template talks.
- **Fresh.** No vacation cliché, no "limited access to email", no
  black-hole inbox.
- **Every word works.** Cut "firm" and the handshake goes limp; cut "zero
  inbox anxiety" and the ficus is just a plant.

## Candidates considered

Five original candidates were drafted; the ficus line won. The four not
chosen, kept here for the record:

1. "I'm away until Thursday. My cat is answering my emails — she approves everything and understands nothing." (105 chars) — warm, but the cat-answers-email bit is a familiar trope.
2. "Out until Friday. My inbox is in the care of my houseplant, which has seniority, sunlight, and no opinions." (107 chars) — good, but too close to the earlier houseplant-OOO theme.
3. "Gone until Monday. My out-of-office reply is now in charge, and honestly it has better boundaries than I do." (108 chars) — strong and meta, but a single punch; "better boundaries" leans on familiar self-help phrasing.
4. "Away until Wednesday. I've trained my laptop to say 'per my last email' to everyone, including my mother." (105 chars) — funny, but "per my last email" is a well-worn corporate joke.

The winner packs two punches (firm handshake, zero inbox anxiety) into the
shortest line (101 characters / 101 bytes), which also helps the byte-count
tie-break.
