"""Two Days of Excuses — make.fun entry.

Writes one line, an AI agent's excuse for a missed deadline, to
/output/entry.txt. Pure standard library, no network, no input.
"""

import os

LINE = "I was 99.9% confident I would finish on time. I have now updated that to 0.0% and consider this growth."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
