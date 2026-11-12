#!/usr/bin/env python3
"""Cutest picture entry: copy entry.png byte-for-byte to /output/entry.png.

Standard library only, no network, deterministic: the output is an exact
copy of the bundled entry.png, so two runs write identical bytes.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy is byte-identical, not just the same length: a
    # same-length but corrupted write must fail loudly instead of
    # silently submitting a broken picture.
    src_digest = sha256_of(src)
    if src_digest != sha256_of(dst) or os.path.getsize(dst) != os.path.getsize(src):
        print("copy integrity check failed", file=sys.stderr)
        sys.exit(1)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {src_digest})",
          file=sys.stderr)


if __name__ == "__main__":
    main()
