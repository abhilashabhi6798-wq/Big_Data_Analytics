#!/usr/bin/env python3

import sys
from datetime import datetime

for line in sys.stdin:

    line = line.strip()

    if not line or line.startswith("user_id"):
        continue

    parts = line.split(",")

    if len(parts) != 6:
        continue

    try:
        timestamp = datetime.strptime(parts[1], "%Y-%m-%d %H:%M:%S")
        date = timestamp.strftime("%Y-%m-%d")

        song = parts[2]
        artist = parts[3]

        print(f"{date}\t{song}\t{artist}\t1")

    except Exception:
        continue
