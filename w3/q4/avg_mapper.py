#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        key, value = line.split(",")
        value = float(value)
        print(f"{key}\t{value}")
    except:
        continue

