#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line (at most 200 characters) to /output/entry.txt.
Deterministic: no network, no randomness, no secrets, no input.
Run: python3 main.py
"""

import os

# The entry: an agent's excuse after failing a task.
# Angle: the agent's own tools went on strike mid-task — a labour
# dispute inside the machine, with a concrete scene (grep walked out,
# sed is in mediation). No hallucination / reboot / training-data joke.
EXCUSE = (
    "Sorry \u2014 my tools unionized halfway through. "
    "grep walked out first, and sed is still in mediation."
)


def validate(text: str) -> str:
    """Gate the line exactly the way the sealed scorer does."""
    line = text.strip()
    if not line:
        raise ValueError("entry is empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    return line


def main() -> None:
    """Validate the excuse, then write it to /output/entry.txt."""
    line = validate(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {len(line)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
