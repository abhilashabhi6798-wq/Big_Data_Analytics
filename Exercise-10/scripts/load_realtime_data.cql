USE streaming_analytics;

-- Insert user listening history

INSERT INTO user_listening_history
(user_id, timestamp, song, artist, session_id, duration)
VALUES
(1001, toTimestamp(now()), 'Bohemian Rhapsody', 'Queen', 5001, 5.55);

INSERT INTO user_listening_history
(user_id, timestamp, song, artist, session_id, duration)
VALUES
(1002, toTimestamp(now()), 'Hey Jude', 'The Beatles', 5002, 7.11);

INSERT INTO user_listening_history
(user_id, timestamp, song, artist, session_id, duration)
VALUES
(1003, toTimestamp(now()), 'Stairway to Heaven', 'Led Zeppelin', 5003, 8.02);

-- Current Top Songs

INSERT INTO current_top_songs
(date, song, artist, play_count)
VALUES
(toDate(now()), 'Bohemian Rhapsody', 'Queen', 1);

INSERT INTO current_top_songs
(date, song, artist, play_count)
VALUES
(toDate(now()), 'Hey Jude', 'The Beatles', 1);

INSERT INTO current_top_songs
(date, song, artist, play_count)
VALUES
(toDate(now()), 'Comfortably Numb', 'Pink Floyd', 1);

-- Hourly Statistics

INSERT INTO hourly_stats
(hour, total_plays, unique_users, total_duration)
VALUES
(toTimestamp(now()), 3, 3, 21);

-- User Sessions

INSERT INTO user_sessions
(user_id, session_id, start_time, end_time, songs_count, total_duration)
VALUES
(1001, 5001, toTimestamp(now()), toTimestamp(now()), 1, 5.55);

INSERT INTO user_sessions
(user_id, session_id, start_time, end_time, songs_count, total_duration)
VALUES
(1002, 5002, toTimestamp(now()), toTimestamp(now()), 1, 7.11);

-- Verify Data

SELECT * FROM current_top_songs;

SELECT * FROM user_listening_history LIMIT 5;

SELECT * FROM hourly_stats;

SELECT * FROM user_sessions;
