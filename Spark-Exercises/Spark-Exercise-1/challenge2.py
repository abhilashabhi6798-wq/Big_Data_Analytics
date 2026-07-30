from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCountChallenge2").getOrCreate()
sc = spark.sparkContext

text_file = sc.textFile("sample.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

# Find top 10 words based on frequency
top_10 = counts.takeOrdered(10, key=lambda x: -x[1])

print("\n=== TOP 10 MOST FREQUENT WORDS ===")

for word, count in top_10:
    print(f"{word}: {count}")

spark.stop()
