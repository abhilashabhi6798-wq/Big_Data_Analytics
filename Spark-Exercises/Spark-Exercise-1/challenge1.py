from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCountChallenge1").getOrCreate()
sc = spark.sparkContext

text_file = sc.textFile("sample.txt")

counts = text_file.flatMap(lambda line: line.split(" ")) \
    .filter(lambda word: len(word) > 3) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

print("\n=== WORDS LONGER THAN 3 CHARACTERS ===")

for word, count in counts.collect():
    print(f"{word}: {count}")

spark.stop()
