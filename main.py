"""The One-Line Cat Joke That Lands — make.fun entry.

Writes one line to /output/entry.txt: a single joke about cats.
The cat is not knocking things off the table out of spite — she
is running a quality-control program, and gravity keeps passing
the tests.
"""

import os

ENTRY = (
    "My cat doesn't knock things off the table out of spite — she "
    "runs a quality-control program, and gravity keeps passing "
    "the tests."
)

MAX_CHARS = 200


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
