from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col, desc

# Create Spark session
spark = SparkSession.builder \
    .appName("Exercise11_WordCount") \
    .master("local[*]") \
    .getOrCreate()

# Input data
data = spark.sparkContext.parallelize([
    "Hello world Hello Spark",
    "Spark is great for big data",
    "Hello Python and Spark"
])

# Convert RDD to DataFrame
df = data.map(lambda x: (x,)).toDF(["line"])

# Split lines into individual words
words_df = df.select(
    explode(split(col("line"), " ")).alias("word")
)

# Count each word
word_counts = words_df.groupBy("word").count()

# Sort by count
sorted_word_counts = word_counts.orderBy(desc("count"))

print("\n=== Exercise 11: Word Count ===")
sorted_word_counts.show()

# Advanced Task: Read from sample.txt
file_df = spark.read.text("sample.txt")

file_words = file_df.select(
    explode(split(col("value"), " ")).alias("word")
)

file_counts = file_words.groupBy("word").count().orderBy(desc("count"))

print("\n=== Advanced Task: sample.txt Word Count ===")
file_counts.show()

spark.stop()
