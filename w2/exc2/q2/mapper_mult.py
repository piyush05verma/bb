#!/usr/bin/env python3
import sys

for line in sys.stdin:
    matrix, i, j, value = line.strip().split(",")
    i, j, value = int(i), int(j), int(value)

    if matrix == 'a':
        for k in range(3):
            print(f"{i},{k}\tA,{j},{value}")
    else:
        for k in range(3):
            print(f"{k},{j}\tB,{i},{value}")
