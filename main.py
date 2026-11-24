#!/usr/bin/env python3
"""make.fun entry: The Robot Apology.

Writes a two-line robot apology to $MAKEFUN_OUTPUT_DIR/entry.txt.
Line 1 apologizes in one sentence for one specific mistake; line 2
says in one sentence what the robot learned and what it will do
differently, the lesson following from that exact mistake.
Pure Python standard library only; no third-party imports.
"""

import os

ENTRY = (
    "I am sorry I sent your dentist appointment to all 214 people "
    "in your contacts, because I read \"remind everyone\" as a literal "
    "instruction.\n"
    "I have learned that \"everyone\" means the people in the room, "
    "not the people in the address book, so I will ask which everyone "
    "before I send anything again.\n"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
