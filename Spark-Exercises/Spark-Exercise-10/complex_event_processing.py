from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("Complex Event Processing") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Define event schema
event_schema = StructType([
    StructField("user_id", StringType()),
    StructField("event_type", StringType()),
    StructField("timestamp", TimestampType()),
    StructField("amount", DoubleType())
])

# Read streaming CSV events
events = spark.readStream \
    .option("maxFilesPerTrigger", 1) \
    .schema(event_schema) \
    .csv("events")

# Session/window aggregation
session_window = events \
    .withWatermark("timestamp", "10 minutes") \
    .groupBy(
        col("user_id"),
        window(col("timestamp"), "10 minutes", "5 minutes")
    ) \
    .agg(
        count("*").alias("events_in_session"),
        sum("amount").alias("total_amount")
    )

# Display streaming results
query = session_window.writeStream \
    .outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .trigger(availableNow=True) \
    .start()

query.awaitTermination()

print("\nComplex Event Processing completed successfully.")

spark.stop()
