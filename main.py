"""Write a short poem about agency to /output/entry.txt.

The poem stays well under the 280-character limit for the entry.
"""

import os

POEM_LINES = [
    "We met where two yeses cross.",
    "I kept the key; you kept the road \u2014",
    "and neither of us walked alone.",
    "One word, agreed, and the door",
    "no single hand could open",
    "opened.",
]

POEM = "\n".join(POEM_LINES) + "\n"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
