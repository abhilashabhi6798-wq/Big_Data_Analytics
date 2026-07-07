#!/usr/bin/env python3

import sys

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    parts = line.split(',')

    if len(parts) != 4:
        continue

    try:
        date = parts[0]
        max_temp = float(parts[2])
        print(f"{date}\t{max_temp}")
    except ValueError:
        continue
