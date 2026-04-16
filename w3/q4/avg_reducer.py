#!/usr/bin/env python3
import sys

current_key = None
sum_values = 0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    key, value = line.split("\t")
    value = float(value)

    if current_key == key:
        sum_values += value
        count += 1
    else:
        if current_key is not None:
            avg = sum_values / count
            print(f"{current_key}\t{avg}")
        current_key = key
        sum_values = value
        count = 1

# output average for last key
if current_key is not None:
    avg = sum_values / count
    print(f"{current_key}\t{avg}")

