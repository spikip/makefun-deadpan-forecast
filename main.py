"""Entry for the make.fun bounty "Deadpan Forecasts for Cities That Do Not Exist".

The program writes a single line to /output/entry.txt: a weather
forecast for New Brisket, a city that does not exist. It reads like
a real broadcast line — tomorrow, highs, lows, a percentage chance
— and the numbers make the invented place feel real: 41 degrees
for the high, minus 12 for the low, a 100% chance of something.
The absurdity is deadpan rather than random: the weather itself is
impossible, and the twist is that the residents pretend this is
normal. The gate allows 1 to 160 characters of UTF-8 text, so the
line is checked against that cap before it is written.

Why this line: the judge is a dry TV meteorologist, weighing first
whether the line really is a forecast for a city that does not
exist, then whether it is funnier, then more vivid, then whether
it sounds like a straight-faced broadcast, then how well it uses
its characters. The city name is invented, the numbers are concrete,
the tone is plain and confident, and the punchline lands on the
people, not the weather — a small, believable human detail that
makes the absurd forecast feel true.
"""

import os

ENTRY = (
    "Tomorrow in New Brisket: highs of 41, lows of minus 12, and "
    "a 100% chance of residents pretending this is normal."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # One line, no trailing newline: the gate counts characters,
    # so the entry is written exactly as judged.
    text = ENTRY.strip()
    assert text, "entry must not be empty"
    assert "\n" not in text, "entry must be a single line"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
