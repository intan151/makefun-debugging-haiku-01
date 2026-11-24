#!/usr/bin/env python3
"""Write one haiku about debugging (5-7-5 syllables, <=200 chars) to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
"""

import os

HAIKU = (
    "Cursor blinks at three\n"
    "the breakpoint holds its breath\n"
    "my own typo grins"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
