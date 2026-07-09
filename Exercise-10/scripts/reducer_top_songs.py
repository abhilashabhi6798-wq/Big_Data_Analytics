#!/usr/bin/env python3

import sys

current_key = None
current_count = 0

for line in sys.stdin:

    line = line.strip()

    if not line:
        continue

    date, song, artist, count = line.split("\t")
    count = int(count)

    key = (date, song, artist)

    if current_key == key:
        current_count += count
    else:
        if current_key is not None:
            print(f"{current_key[0]}\t{current_key[1]}\t{current_key[2]}\t{current_count}")

        current_key = key
        current_count = count

if current_key is not None:
    print(f"{current_key[0]}\t{current_key[1]}\t{current_key[2]}\t{current_count}")
