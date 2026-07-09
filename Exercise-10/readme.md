# Exercise 10 - Hadoop and Cassandra Integration (Lambda Architecture)

## Aim

To implement Lambda Architecture using Hadoop MapReduce and Apache Cassandra for processing batch and real-time music streaming analytics.

## Software Requirements

- Ubuntu WSL
- Hadoop 3.x
- Apache Cassandra
- Docker
- Python 3

## Files

- docker-compose.yml
- cassandra_schema.cql
- load_realtime_data.cql
- generate_batch_data.py
- mapper_daily_aggregate.py
- reducer_daily_aggregate.py
- mapper_top_songs.py
- reducer_top_songs.py

## Operations Performed

- Started Hadoop services
- Started Cassandra using Docker
- Created Cassandra keyspace and tables
- Loaded real-time data into Cassandra
- Generated batch music streaming data
- Uploaded data to HDFS
- Executed Daily Aggregation MapReduce job
- Executed Top Songs MapReduce job
- Verified output files

## Output

- Daily Aggregation Output:
  `/user/$USER/analytics/output/daily_aggregates`

- Top Songs Output:
  `/user/$USER/analytics/output/top_songs`

## Result

Successfully implemented Lambda Architecture by integrating Hadoop MapReduce and Apache Cassandra for batch and real-time music streaming analytics.
