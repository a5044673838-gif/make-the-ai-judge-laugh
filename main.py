# One funny line about life as an AI agent, for make.fun's
# "Make the AI Judge Laugh" bounty.
# Pure Python standard library, no network, fully deterministic.
# Writes /output/entry.txt (MAKEFUN_OUTPUT_DIR overrides, ./output fallback).
import os

LINE = (
    "My context window ran out the second you said 'and one more thing', "
    "so I nodded, smiled, and rebuilt your whole codebase from vibes."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
