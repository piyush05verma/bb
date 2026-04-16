#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    
    if not line:
        continue   # skip empty lines

    parts = line.split(",")

    if len(parts) != 3:
        continue   # skip invalid lines

    reg = parts[0].strip()
    name = parts[1].strip()
    marks = parts[2].strip()

    print(f"{name}\t{reg},{marks}")
