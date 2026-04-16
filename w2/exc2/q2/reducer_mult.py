#!/usr/bin/env python3
import sys
from collections import defaultdict

current_key = None
values = []

for line in sys.stdin:
    key, val = line.strip().split("\t")

    if key != current_key:
        if current_key:
            result = 0
            dictA = {}
            dictB = {}
            for v in values:
                matrix, index, value = v.split(",")
                if matrix == 'A':
                    dictA[int(index)] = int(value)
                else:
                    dictB[int(index)] = int(value)
            for k in range(3):
                result += dictA.get(k,0) * dictB.get(k,0)
            print(f"{current_key}\t{result}")
        current_key = key
        values = [val]
    else:
        values.append(val)

if current_key:
    result = 0
    dictA = {}
    dictB = {}
    for v in values:
        matrix, index, value = v.split(",")
        if matrix == 'A':
            dictA[int(index)] = int(value)
        else:
            dictB[int(index)] = int(value)
    for k in range(3):
        result += dictA.get(k,0) * dictB.get(k,0)
    print(f"{current_key}\t{result}")
