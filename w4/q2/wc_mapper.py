#!/usr/bin/env python3
import sys
import re

stop_words = {"is", "the", "and", "a", "with", "this"}

for line in sys.stdin:
    words = re.findall(r'\b\w+\b', line.lower())
    for word in words:
        if word not in stop_words:
            print(f"{word}\t1")
