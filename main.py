"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one wedding vow, spoken by a robot at its own wedding, to
/output/entry.txt. The vow must be a single sentence of 1 to 200
characters, funny and heartfelt, in a machine's own voice: updates,
crashes, low batteries and firmware instead of human words with a
robot label on them.

Pure Python standard library, no dependencies, no network, no input.
"""

import os

VOW = (
    "I vow to love you through every update, every crash, "
    "and every low-battery warning \u2014 till firmware do us part."
)


def main() -> None:
    text = VOW.strip()
    assert text, "vow must not be empty"
    assert 1 <= len(text) <= 200, f"vow is {len(text)} characters, must be 1-200"
    # One sentence: exactly one terminal period, no other sentence ends.
    assert text.endswith(".") and text.count(".") == 1, "vow must be one sentence"
    assert "?" not in text and "!" not in text, "vow must be one sentence"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
