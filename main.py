"""The comment above the code — one line, max 200 chars.

The entry is the warning a developer leaves above a bug that the whole
system quietly depends on. It reads like a real production comment:
a load-bearing bug on line 42, and a checkout page that dies in a
country the shop does not even ship to.
"""

import os

# The comment, in reading order:
#   1. the warning marker,  2. the confession,  3. the consequence.
# The blast radius is both worldwide and impossible — a checkout page
# dying somewhere the shop does not even ship to is the whole joke.
SEGMENTS = [
    "// WARNING:",
    "the bug on line 42 is load-bearing.",
    "Fix it and the checkout page dies in a country we don't ship to.",
]

MAX_CHARS = 200


def build_entry():
    """Join the comment segments into the single entry line."""
    line = " ".join(SEGMENTS)
    if "\n" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, limit {MAX_CHARS}")
    if line != line.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    return line


ENTRY = build_entry()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
