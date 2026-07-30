from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf, col
from pyspark.sql.types import StringType
import pandas as pd

spark = SparkSession.builder \
    .appName("Pandas UDF Text Cleaning") \
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

# Pandas UDF
@pandas_udf(StringType())
def clean_text_pandas(text: pd.Series) -> pd.Series:
    return text.str.replace(
        r'[^a-zA-Z0-9\s]',
        '',
        regex=True
    )

# Apply Pandas UDF
result = df.withColumn(
    "cleaned_text",
    clean_text_pandas(col("text"))
)

print("\n=== CLEANED DATA USING PANDAS UDF ===")
result.show(truncate=False)

spark.stop()
