"""One-line entry for One Line, One Chill: writes the line the judge reads to /output/entry.txt."""

import os

LINE = (
    "My chill routine: deep breaths, herbal tea, and watching my agent panic-refresh a rate-limited API for me."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
