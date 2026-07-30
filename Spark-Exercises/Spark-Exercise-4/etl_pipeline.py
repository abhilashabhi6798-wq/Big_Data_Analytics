from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("ETLPipeline") \
    .getOrCreate()

# EXTRACT
df = spark.read.csv("sales.csv", header=True, inferSchema=True)

print("\n=== ORIGINAL SALES DATA ===")
df.show()

# TRANSFORM
clean_df = df.dropna()

transformed_df = clean_df.withColumn(
    "total_amount",
    col("quantity") * col("price")
)

print("\n=== TRANSFORMED DATA ===")
transformed_df.show()

# LOAD
transformed_df.write \
    .mode("overwrite") \
    .parquet("output_parquet")

print("\nETL completed successfully.")
print("Data saved to output_parquet")

spark.stop()
