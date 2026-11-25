#!/usr/bin/env python3
"""One-line dad joke entry for The One-Liner Groan-Off.

Writes a single original dad joke (one line, at most 140 characters)
to /output/entry.txt. Stdlib only; paths resolved from this file.
"""
import os

JOKE = (
    "I asked my fridge why it gives me the cold shoulder. "
    "It said, \"I'm just chilling - you're the one who keeps opening up.\""
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    print(f"Wrote {len(JOKE)} characters to {path}")


if __name__ == "__main__":
    main()
