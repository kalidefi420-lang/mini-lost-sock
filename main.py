"""Entry for the make.fun bounty "Funniest Lost Sock Status Update".

Writes one status update, in the voice of a lost sock, to entry.txt.
Standard library only.
"""

import os

LINE = "Still single. The dryer took my partner, my dignity, and \u2014 worst of all \u2014 my leftness."

MAX_CHARS = 120


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1 to {MAX_CHARS} characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
