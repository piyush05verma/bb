#!/usr/bin/env python3
import sys

current_word = None
files = set()

for line in sys.stdin:
    word, filename = line.strip().split("\t")

    if word == current_word:
        files.add(filename)
    else:
        if current_word:
            print(f"{current_word}\t{','.join(sorted(files))}")
        current_word = word
        files = {filename}

if current_word:
    print(f"{current_word}\t{','.join(sorted(files))}")
