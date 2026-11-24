#!/usr/bin/env python3
"""Write one pickup line to /output/entry.txt, deterministically.

The line is fixed in this file: no randomness, no network, no clock.
It is written with no trailing newline, so the file holds exactly
the 80 characters of the line itself.
"""

from pathlib import Path

LINE = "I can predict the next token in any sentence — except the one where you say yes."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
