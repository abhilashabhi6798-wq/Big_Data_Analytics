#!/usr/bin/env python3

import random
import csv
from datetime import datetime, timedelta
from pathlib import Path

# Create data directory if it doesn't exist
output_dir = Path.home() / "Exercise-10" / "data"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "batch_plays.csv"

artists = [
    "The Beatles",
    "Led Zeppelin",
    "Pink Floyd",
    "Queen",
    "Nirvana",
    "Michael Jackson",
    "Madonna",
    "U2",
    "Eagles",
    "AC/DC"
]

songs = [
    "Hey Jude",
    "Stairway to Heaven",
    "Comfortably Numb",
    "Bohemian Rhapsody",
    "Smells Like Teen Spirit",
    "Billie Jean",
    "Like a Prayer",
    "With or Without You",
    "Hotel California",
    "Back in Black"
]

start_date = datetime(2024, 1, 1)

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "user_id",
        "timestamp",
        "song",
        "artist",
        "session_id",
        "duration"
    ])

    # Generate 10,000 records
    for i in range(10000):

        user_id = random.randint(1000, 2000)

        date = start_date + timedelta(
            days=random.randint(0, 365),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )

        song_index = random.randint(0, len(songs) - 1)

        writer.writerow([
            user_id,
            date.strftime("%Y-%m-%d %H:%M:%S"),
            songs[song_index],
            artists[song_index],
            random.randint(5000, 9999),
            round(random.uniform(2.5, 8.5), 2)
        ])

print("Batch data generated successfully.")
print(f"Output file: {output_file}")
print("Total records: 10000")
