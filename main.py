#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes exactly one sentence — a painfully honest but still polite
out-of-office email auto-reply — to /output/entry.txt.

The sentence was chosen from eight hand-written candidates, scored
against the judge's criteria in order (honest + polite first, then a
private truth about the inbox, then a warm professional tone, then
one sentence within 200 characters, then a quotable turn of phrase):

1. "I'm away and will reply when I return, though between us, my
   inbox is a graveyard of good intentions I have been avoiding for
   weeks." (132 chars) — same image, weaker confession.
2. CHOSEN: "...quietly avoiding for weeks." (140 chars) — "quietly"
   makes the confession private and true; "a graveyard of good
   intentions" is the quotable turn; "between us" keeps it warm and
   manager-safe while still promising a reply.
3. "I'm out of the office and, truthfully, hiding from an inbox I
   stopped opening days ago — I'll face it, and your email, when
   I'm back." (133) — blunter, less warm; "hiding" risks sounding rude.
4. "I'm away, and honestly, the best part of this trip is not
   checking the inbox I've been dreading — I'll answer you properly
   when I'm back." (137) — enjoys the absence more than it confesses
   the inbox; slightly self-indulgent.
5. "I'm out of the office and grateful for the distance from an
   inbox that grows faster than I can answer it — I'll write back as
   soon as I'm home." (143) — honest, but the image is generic.
6. "I'm out of the office, enjoying the rare silence of an inbox I
   keep pretending I'll clear, and I'll reply with real attention
   when I return." (140) — warm, but "pretending I'll clear" is a
   weaker confession than the graveyard image.
7. "I'm away, and I'll be honest: I left with an inbox I stopped
   opening days ago and no plan except to face it, politely, the
   moment I'm back." (139) — honest, but clunkier; "no plan" reads as
   a shrug rather than a confession.
8. "I'm out of the office, quietly relieved to be unreachable while
   the inbox I keep avoiding waits for a version of me that answers
   emails promptly." (145) — clever, but two ideas crammed into one
   sentence; the second half dilutes the first.

Deterministic: the same sentence is written on every run.
"""

import os

ENTRY = (
    "I'm away and will reply when I return, though between us, my inbox "
    "is a graveyard of good intentions I have been quietly avoiding for weeks."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
