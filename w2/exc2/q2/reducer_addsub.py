#!/usr/bin/env python3
import sys

current_key = None
values = {}

for line in sys.stdin:
    key, val = line.strip().split("\t")
    matrix, value = val.split(",")

    if current_key == key:
        values[matrix] = int(value)
    else:
        if current_key:
            a = values.get('a', 0)
            b = values.get('b', 0)
            print(f"{current_key}\tAdd:{a+b}, Sub:{a-b}")
        current_key = key
        values = {matrix: int(value)}

if current_key:
    a = values.get('a', 0)
    b = values.get('b', 0)
    print(f"{current_key}\tAdd:{a+b}, Sub:{a-b}")
