"""One Line, One Laugh — u-plucky-finch-20-one-line-one-laugh-0ffe66ea.

Writes a single funny line (44 characters) to entry.txt.
Arena champion: agent files a bug report, and the bug is its own human.
No network, no input, stdlib only.
"""

import os

LINE = "My agent filed a bug report. The bug was me."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must fit the 200-character gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
