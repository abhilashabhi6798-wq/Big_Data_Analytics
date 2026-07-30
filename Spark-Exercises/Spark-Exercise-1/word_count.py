from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder.appName("WordCount").getOrCreate()

# Create Spark Context
sc = spark.sparkContext

# Read the text file as an RDD
text_file = sc.textFile("sample.txt")

# Word Count
counts = text_file.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

# Display results
print("\n=== WORD COUNT OUTPUT ===")
for word, count in counts.collect():
    print(f"{word}: {count}")

# Stop Spark
spark.stop()
