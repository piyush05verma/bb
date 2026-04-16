#!/usr/bin/env python3
import sys

N = 3
top_records = []

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    try:
        score, name = line.split("\t")
        score = int(score)
        top_records.append((score, name))
    except:
        continue

# Sort by score descending
top_records.sort(reverse=True, key=lambda x: x[0])

# Output top N
for score, name in top_records[:N]:
    print(f"{name}\t{score}")

