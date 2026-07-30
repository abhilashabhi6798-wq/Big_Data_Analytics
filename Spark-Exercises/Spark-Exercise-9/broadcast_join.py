from pyspark.sql import SparkSession
from pyspark.sql.functions import broadcast

spark = SparkSession.builder \
    .appName("Broadcast Join Optimization") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Larger dataset
large_df = spark.read.csv(
    "data.csv",
    header=True,
    inferSchema=True
)

# Small lookup dataset
small_df = spark.read.csv(
    "small_table.csv",
    header=True,
    inferSchema=True
)

print("\n=== LARGE DATASET ===")
large_df.show()

print("\n=== SMALL DATASET ===")
small_df.show()

# Broadcast the small table during join
result = large_df.join(
    broadcast(small_df),
    "key"
)

print("\n=== BROADCAST JOIN RESULT ===")
result.show()

print("\n=== EXECUTION PLAN ===")
result.explain()

spark.stop()
