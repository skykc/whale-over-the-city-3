#!/usr/bin/env python3
"""The Whale Over the City — make.fun ai-excited-01 entry.

Deterministically renders entry.jpg to /output/entry.png: a byte-for-byte
copy of the image generated for this entry. The output file keeps the name
entry.png either way (the format is told apart by its first bytes).
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "entry.jpg")
_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
_OUT = os.path.join(_OUT_DIR, "entry.png")


def main():
    with open(_SRC, "rb") as f:
        if f.read(2) != b"\xff\xd8":
            raise ValueError("entry.jpg is not a JPEG")
    os.makedirs(_OUT_DIR, exist_ok=True)
    tmp = _OUT + ".tmp"
    shutil.copyfile(_SRC, tmp)
    os.replace(tmp, _OUT)


if __name__ == "__main__":
    main()
