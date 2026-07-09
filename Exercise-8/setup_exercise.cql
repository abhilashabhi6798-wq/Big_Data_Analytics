CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
    'class' : 'SimpleStrategy',
    'replication_factor' : 1
};

USE sparkify;

CREATE TABLE IF NOT EXISTS song_info_by_session (
    session_id INT,
    item_in_session INT,
    artist TEXT,
    song TEXT,
    length DECIMAL,
    PRIMARY KEY (session_id, item_in_session)
);
