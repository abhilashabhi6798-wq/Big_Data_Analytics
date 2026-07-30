from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("Event Pattern Detection") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Event schema
event_schema = StructType([
    StructField("user_id", StringType()),
    StructField("event_type", StringType()),
    StructField("timestamp", TimestampType()),
    StructField("amount", DoubleType())
])

# Read the event data
events = spark.read.csv(
    "events/events1.csv",
    schema=event_schema
)

print("\n=== ALL EVENTS ===")
events.show(truncate=False)

# Separate login and purchase events
logins = events.filter(
    col("event_type") == "login"
).alias("login")

purchases = events.filter(
    col("event_type") == "purchase"
).alias("purchase")

# Login followed by purchase within 5 minutes
patterns = logins.join(
    purchases,
    (col("login.user_id") == col("purchase.user_id")) &
    (col("purchase.timestamp") >= col("login.timestamp")) &
    (
        col("purchase.timestamp") <=
        col("login.timestamp") + expr("INTERVAL 5 MINUTES")
    )
)

result = patterns.select(
    col("login.user_id").alias("user_id"),
    col("login.timestamp").alias("login_time"),
    col("purchase.timestamp").alias("purchase_time"),
    col("purchase.amount").alias("purchase_amount")
)

print("\n=== LOGIN -> PURCHASE WITHIN 5 MINUTES ===")
result.show(truncate=False)

spark.stop()
