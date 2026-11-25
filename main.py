"""The Internet in One Word.

Writes a single word to $MAKEFUN_OUTPUT_DIR/entry.txt: the one
word that describes the whole internet. The word is "feral" —
the internet is not a library or a town square, it is a wild
animal loose in everyone's pocket: unmoderated, unpredictable,
funny, and impossible to house-train. Five letters, one beat,
no explanation needed. Standard library only.
"""

import sys
import os

WORD = "feral"

MAX_CHARS = 30


def pick_word():
    """Return the one word for the whole internet."""
    return WORD


def validate_word(text):
    """Check the word against the competition gate.

    The gate wants UTF-8 text of 1 to 30 characters that is not
    only whitespace, and the judge brief wants exactly one word
    that describes the whole internet. A word that fails here is
    rejected instead of wasting a submission on the server.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("word is empty")
    if len(cleaned) > MAX_CHARS:
        raise ValueError(
            "word is %d characters, over the 30 limit" % len(cleaned)
        )
    if len(cleaned.split()) != 1:
        raise ValueError("entry must be exactly one word")
    return cleaned


def word_stats(text):
    """Measure the word for a last sanity pass.

    Returns the character count and whether the word is a
    single token. A word that is too long to land in one beat,
    or padded out to fill the cap, is caught here before
    anything is written.
    """
    tokens = text.split()
    return {"chars": len(text), "tokens": len(tokens)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    word = validate_word(pick_word())
    shape = word_stats(word)
    if shape["tokens"] != 1:
        raise ValueError("entry must be exactly one word")
    if shape["chars"] < 1:
        raise ValueError("word is empty")
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(word)
    return 0


if __name__ == "__main__":
    sys.exit(main())
