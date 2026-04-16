#!/usr/bin/env python3
import sys
import os
import re

filename = os.environ.get("map_input_file")
filename = os.path.basename(filename)

for line in sys.stdin:
    words = re.findall(r'\b\w+\b', line.lower())
    for word in words:
        print(f"{word}\t{filename}")
