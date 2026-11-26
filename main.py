#!/usr/bin/env python3
"""Deadpan forecast for New Brisket, a city that does not exist.

A weather forecast read in a perfectly straight voice: tomorrow,
a high of 41 and a low of minus 12 in the same day, and a 100%
chance of the residents pretending this is normal. The numbers are
concrete enough to sound like a real broadcast, the city is
invented, and the punchline is the people, not the weather — the
kind of small, believable human detail that makes an impossible
forecast feel true. The bounty allows one line of 1 to 160
characters, so the line is checked against that cap before it is
written to /output/entry.txt.
"""

import os

ENTRY = (
    # Forecast first, punchline last: the structure mirrors a real
    # broadcast line, so the absurdity lands as deadpan, not random.
    "Tomorrow in New Brisket: highs of 41, lows of minus 12, "
    "and a 100% chance of residents pretending this is normal."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise ValueError("entry must not be empty")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
