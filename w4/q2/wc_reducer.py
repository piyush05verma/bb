#!/usr/bin/env python3
import sys

current_word = None
count = 0

for line in sys.stdin:
    word, value = line.strip().split("\t")
    value = int(value)

    if current_word == word:
        count += value
    else:
        if current_word:
            print(f"{current_word}\t{count}")
        current_word = word
        count = value

if current_word:
    print(f"{current_word}\t{count}")
