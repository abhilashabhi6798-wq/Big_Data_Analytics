from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import re

# Create Spark session
spark = SparkSession.builder \
    .appName("Custom UDF Text Cleaning") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Load data
df = spark.read.csv(
    "text_data.csv",
    header=True,
    inferSchema=True
)

print("\n=== ORIGINAL DATA ===")
df.show(truncate=False)

# Function to clean text
def clean_text(text):
    if text is None:
        return None
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

# Convert Python function into Spark UDF
clean_udf = udf(clean_text, StringType())

# Apply UDF
cleaned_df = df.withColumn(
    "cleaned_text",
    clean_udf(col("text"))
)

print("\n=== CLEANED DATA ===")
cleaned_df.show(truncate=False)

spark.stop()
