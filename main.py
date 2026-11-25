#!/usr/bin/env python3
"""Roast Your Fridge — one-line roast entry (u-suzy).

Writes the keeper line byte-exact to /output/entry.txt, no trailing newline.
Pure stdlib; deterministic.

Gate: 1-200 characters (keeper is 112). Judge: roast of a fridge or a phone,
twist in the last few words. Round 1, cutoff today 2:10pm CST.
"""
import os

ENTRY = "Firmware 3.9.1 fixed the ice maker by declaring ice a legacy feature. The fridge now makes room-temperature ice."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
