#!/usr/bin/env python3
import sys

current_year = None
max_temp = None

for line in sys.stdin:
    year, temp = line.strip().split("\t")
    temp = int(temp)

    if year == current_year:
        if temp > max_temp:
            max_temp = temp
    else:
        if current_year is not None:
            print(f"{current_year}\t{max_temp}")
        current_year = year
        max_temp = temp

if current_year is not None:
    print(f"{current_year}\t{max_temp}")

