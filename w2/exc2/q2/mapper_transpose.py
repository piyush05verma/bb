#!/usr/bin/env python3
import sys

for line in sys.stdin:
    matrix, i, j, value = line.strip().split(",")
    print(f"{matrix},{j},{i}\t{value}")
