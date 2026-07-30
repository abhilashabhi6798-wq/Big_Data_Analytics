from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("Complex Transaction Rule") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Create sample transaction data
data = [
    ("user1", 500.0, 3),
    ("user2", 1200.0, 7),
    ("user3", 1500.0, 4),
    ("user4", 2000.0, 8),
    ("user5", 800.0, 10),
    ("user6", 2500.0, 12)
]

schema = StructType([
    StructField("user_id", StringType()),
    StructField("amount", DoubleType()),
    StructField("transaction_count", IntegerType())
])

transactions = spark.createDataFrame(data, schema)

print("\n=== ALL TRANSACTIONS ===")
transactions.show()

# Complex event rule:
# amount > 1000 AND transaction_count > 5
complex_events = transactions.filter(
    (col("amount") > 1000) &
    (col("transaction_count") > 5)
)

print("\n=== COMPLEX EVENTS ===")
complex_events.show()

spark.stop()
