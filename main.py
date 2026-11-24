#!/usr/bin/env python3
"""Famous Last Words at 1 Percent.

The phone's final line: it was never really dying on schedule. It held on
out of pure spite, just long enough to snitch on its owner with its last
breath -- a dying confession that rats out the user's screen time. The
punch lands on the reveal itself, so the line stays tight and ends there.
One line, written to /output/entry.txt.
"""

import os

LINE = (
    "I've been at 1% since lunch \u2014 I held on just to snitch: "
    "nine hours of screen time today."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
