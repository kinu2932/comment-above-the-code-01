#!/usr/bin/env python3
"""The Comment Above the Code — entry writer (v2).

Writes one funny, painfully honest comment line above fragile production
code to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it.
Gate: UTF-8 text, 1-200 characters, not only whitespace, single line.
"""
import os

ENTRY = "// Temporary fix from 2019. It now runs payroll, holds up the login page, and the only person who understood it left in 2021."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
