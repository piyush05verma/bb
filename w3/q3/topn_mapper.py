#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        name, score = line.split(",")
        score = int(score)
        print(f"{score}\t{name}")
    except:
        continue

