from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, col
from pyspark.sql.types import StringType
import pandas as pd

spark = SparkSession.builder \
    .appName("Aggregation Pandas UDF") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Load dataset
df = spark.read.csv(
    "text_data.csv",
    header=True,
    inferSchema=True
)

print("\n=== ORIGINAL DATA ===")
df.show(truncate=False)

# Grouped aggregation Pandas UDF
@pandas_udf(StringType())
def aggregate_text_udf(text: pd.Series) -> str:
    return " ".join(text.dropna().astype(str))

# Group by category and combine text
result = df.groupBy("category").agg(
    aggregate_text_udf(col("text")).alias("combined_text")
)

print("\n=== AGGREGATED TEXT BY CATEGORY ===")
result.show(truncate=False)

spark.stop()
