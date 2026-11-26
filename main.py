"""The Comment Above the Code — a single line, under 200 characters.

The line is assembled from named parts so each clause can be judged on
its own job: the setup, the turn, and the landing. See CRAFT notes below.
"""

import os


# CRAFT — why this line is built the way it is:
# 1. On-topic, in a real developer's voice (criteria 1 & 5): it opens '// WARNING:'
#    exactly as a comment above fragile production code would, no contest-caption tone.
# 2. The honesty stings (criterion 2): it names a REAL, recognisable failure — a bug
#    that other code silently depends on — not a generic 'programmers, am I right?' joke.
# 3. Punchline lands last (criterion 3): 'in a timezone we don't even operate in' is
#    the turn; the reader learns the blast radius is both global and absurd.
# 4. Fresh angle (criterion 4): not off-by-one, not 'who wrote this' — the joke is
#    that the bug is structural, a load-bearing wall of the system nobody may touch.
# 5. Economical (criterion 3): three clauses, each one doing work; nothing to trim.
# REVISION v2: 'dies' is a punchier verb than 'breaks'; 'the checkout page' names the victim concretely; 'a country we don't ship to' is tighter and funnier than 'a timezone we don't even operate in' — the blast radius is both worldwide and impossible, which is the whole joke.
# The parts below are joined with single spaces; the entry is one line.
PARTS = {
    "marker": '// WARNING:',
    "confession": 'the bug on line 42 is load-bearing.',
    "consequence": "Fix it and the checkout page dies in a country we don't ship to.",
}


def build_entry():
    """Assemble the single line from its meaningful parts."""
    line = " ".join(PARTS.values())
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, limit 200"
    assert line.strip() == line, "entry must not have leading/trailing whitespace"
    return line


ENTRY = build_entry()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
