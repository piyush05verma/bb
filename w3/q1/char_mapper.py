#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    for ch in line:
        if ch != ' ':
            print(f"{ch}\t1")

