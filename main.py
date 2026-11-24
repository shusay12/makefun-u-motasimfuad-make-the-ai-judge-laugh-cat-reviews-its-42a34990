#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, in the voice of a house
cat about its human, to /output/entry.txt.

Python 3.13 stdlib only. No network, no files read besides this one.
The review text is a fixed literal: the program is deterministic, so
every run produces byte-identical output.
"""

from pathlib import Path

REVIEW = (
    "One star. My human moved my food bowl two inches to the left, "
    "then watched me stare at the empty floor where it used to be. "
    "I have filed a formal complaint with the dog."
)

MAX_CHARS = 200


def main() -> None:
    text = REVIEW.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"entry is {len(text)} chars"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    # Verify the gate locally: re-read and confirm the file on disk is
    # exactly the validated text (UTF-8, 1-200 chars, single line).
    round_trip = out.read_text(encoding="utf-8")
    assert round_trip == text + "\n", "round-trip mismatch"
    assert 1 <= len(round_trip) <= MAX_CHARS + 1
    print(f"wrote {len(text)} chars to {out}")


if __name__ == "__main__":
    main()
