#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split(",")

    try:
        date = parts[0]
        year = date[:4]
        temperature = int(parts[2])

        print(f"{year}\t{temperature}")
    except:
        continue

