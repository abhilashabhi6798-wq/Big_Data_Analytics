Exercise 8 : Apache Cassandra
File : setup_exercise.cql

--Create Keyspace
CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
    'class' : 'SimpleStrategy',
    'replication_factor' : 1
};

-- Use Keyspace
USE sparkify;

-- Create Table 1
CREATE TABLE IF NOT EXISTS song_info_by_session (
    session_id INT,
    item_in_session INT,
    artist TEXT,
    song TEXT,
    length DECIMAL,
    PRIMARY KEY (session_id, item_in_session)
) WITH CLUSTERING ORDER BY (item_in_session ASC);

-- Create Table 2
CREATE TABLE IF NOT EXISTS song_playing_history_by_user (
    user_id INT,
    session_id INT,
    item_in_session INT,
    artist TEXT,
    song TEXT,
    first_name TEXT,
    last_name TEXT,
    PRIMARY KEY ((user_id, session_id), item_in_session)
) WITH CLUSTERING ORDER BY (item_in_session DESC);

-- Create Table 3
CREATE TABLE IF NOT EXISTS who_listened_to_song (
    song TEXT,
    user_id INT,
    first_name TEXT,
    last_name TEXT,
    PRIMARY KEY (song, user_id)
);

-- Insert Records into song_info_by_session
INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES (100, 1, 'The Beatles', 'Hey Jude', 7.11);

INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES (100, 2, 'Led Zeppelin', 'Stairway to Heaven', 8.02);

INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES (100, 3, 'Pink Floyd', 'Comfortably Numb', 6.53);

INSERT INTO song_info_by_session
(session_id, item_in_session, artist, song, length)
VALUES (101, 1, 'Queen', 'Bohemian Rhapsody', 5.55);

-- Insert Records into song_playing_history_by_user
INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (1, 100, 1, 'The Beatles', 'Hey Jude', 'John', 'Doe');

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (1, 100, 2, 'Led Zeppelin', 'Stairway to Heaven', 'John', 'Doe');

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (1, 100, 3, 'Pink Floyd', 'Comfortably Numb', 'John', 'Doe');

INSERT INTO song_playing_history_by_user
(user_id, session_id, item_in_session, artist, song, first_name, last_name)
VALUES (2, 200, 1, 'Queen', 'Bohemian Rhapsody', 'Jane', 'Smith');

-- Insert Records into who_listened_to_song
INSERT INTO who_listened_to_song
(song, user_id, first_name, last_name)
VALUES ('Hey Jude', 1, 'John', 'Doe');

INSERT INTO who_listened_to_song
(song, user_id, first_name, last_name)
VALUES ('Hey Jude', 2, 'Jane', 'Smith');

INSERT INTO who_listened_to_song
(song, user_id, first_name, last_name)
VALUES ('Comfortably Numb', 1, 'John', 'Doe');

-- Display Tables
DESC TABLES;

-- Display Records
SELECT * FROM song_info_by_session;

SELECT * FROM song_playing_history_by_user;

SELECT * FROM who_listened_to_song;

-- Query 1
SELECT * FROM song_info_by_session
WHERE session_id = 100;

-- Query 2
SELECT * FROM song_playing_history_by_user
WHERE user_id = 1
AND session_id = 100;

-- Query 3
SELECT * FROM who_listened_to_song
WHERE song = 'Hey Jude';
