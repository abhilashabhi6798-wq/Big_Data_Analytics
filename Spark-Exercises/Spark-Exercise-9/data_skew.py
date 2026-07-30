from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat, lit, rand

spark = SparkSession.builder \
    .appName("Data Skew Handling") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Load dataset
df = spark.read.csv(
    "data.csv",
    header=True,
    inferSchema=True
)

print("\n=== ORIGINAL DATA ===")
df.show()

# Create salted key
df_salted = df.withColumn(
    "salted_key",
    concat(
        col("key"),
        lit("_"),
        (rand(seed=42) * 10).cast("int")
    )
)

print("\n=== DATA AFTER SALTING ===")
df_salted.show(truncate=False)

spark.stop()
