#!/usr/bin/env python3

import sys
from collections import defaultdict

current_date = None
users = set()
song_count = defaultdict(int)
artist_count = defaultdict(int)
total_duration = 0.0
total_plays = 0

def print_result():
    if current_date is None or total_plays == 0:
        return

    top_song = max(song_count.items(), key=lambda x: x[1])[0]
    top_artist = max(artist_count.items(), key=lambda x: x[1])[0]
    avg_duration = total_duration / total_plays

    print(f"{current_date}\t{total_plays}\t{len(users)}\t{avg_duration:.2f}\t{top_song}\t{top_artist}")

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    date, value = line.split("\t", 1)
    user_id, song, artist, duration = value.split(",")

    duration = float(duration)

    if current_date is None:
        current_date = date

    if date != current_date:
        print_result()

        current_date = date
        users = set()
        song_count = defaultdict(int)
        artist_count = defaultdict(int)
        total_duration = 0.0
        total_plays = 0

    users.add(user_id)
    song_count[song] += 1
    artist_count[artist] += 1
    total_duration += duration
    total_plays += 1

print_result()
