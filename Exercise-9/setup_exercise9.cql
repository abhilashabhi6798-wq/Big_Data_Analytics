USE sparkify;

-- Insert a new record
INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES (102, 1, 'Nirvana', 'Smells Like Teen Spirit', 5.01);

-- UPSERT
INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES (100, 1, 'The Beatles', 'Let It Be', 4.03);

-- Check consistency level
CONSISTENCY;

-- Set consistency level
CONSISTENCY ONE;

-- Verify updated data
SELECT * FROM song_info_by_session
WHERE session_id = 100;

EXIT;
