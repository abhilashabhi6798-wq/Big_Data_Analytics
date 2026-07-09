-- ============================================
-- CASSANDRA SCHEMA FOR MUSIC STREAMING ANALYTICS
-- ============================================

-- Create Keyspace
CREATE KEYSPACE IF NOT EXISTS streaming_analytics
WITH REPLICATION = {
    'class' : 'SimpleStrategy',
    'replication_factor' : 1
};

USE streaming_analytics;

-- Table 1 : Current Top Songs
CREATE TABLE IF NOT EXISTS current_top_songs (
    date DATE,
    song TEXT,
    artist TEXT,
    play_count BIGINT,
    PRIMARY KEY (date, song)
);

-- Table 2 : User Listening History
CREATE TABLE IF NOT EXISTS user_listening_history (
    user_id INT,
    timestamp TIMESTAMP,
    song TEXT,
    artist TEXT,
    session_id INT,
    duration DECIMAL,
    PRIMARY KEY (user_id, timestamp)
) WITH CLUSTERING ORDER BY (timestamp DESC);

-- Table 3 : Hourly Statistics
CREATE TABLE IF NOT EXISTS hourly_stats (
    hour TIMESTAMP,
    total_plays COUNTER,
    unique_users COUNTER,
    total_duration COUNTER,
    PRIMARY KEY (hour)
);

-- Table 4 : User Sessions
CREATE TABLE IF NOT EXISTS user_sessions (
    user_id INT,
    session_id INT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    songs_count INT,
    total_duration DECIMAL,
    PRIMARY KEY ((user_id), session_id)
) WITH CLUSTERING ORDER BY (session_id DESC);

--Table 5 : Daily Aggregates
CREATE TABLE IF NOT EXISTS daily_aggregates (
    date DATE,
    total_plays BIGINT,
    unique_users BIGINT,
    avg_duration DECIMAL,
    top_song TEXT,
    top_artist TEXT,
    PRIMARY KEY (date)
);

-- Table 6 : Top Songs Daily
CREATE TABLE IF NOT EXISTS top_songs_daily (
    date DATE,
    rank INT,
    song TEXT,
    artist TEXT,
    play_count BIGINT,
    PRIMARY KEY (date, rank)
);

-- Table 7 : User Recommendations
CREATE TABLE IF NOT EXISTS user_recommendations (
    user_id INT,
    song TEXT,
    artist TEXT,
    score DECIMAL,
    reason TEXT,
    PRIMARY KEY (user_id, song)
);

DESC TABLES;
