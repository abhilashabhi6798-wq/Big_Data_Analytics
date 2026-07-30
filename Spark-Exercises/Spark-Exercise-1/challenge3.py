from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("WordCountChallenge3").getOrCreate()
sc = spark.sparkContext

text_file = sc.textFile("sample.txt")

# Common stop words
stop_words = {"the", "is", "a", "an", "and", "of", "to", "in"}

counts = text_file.flatMap(lambda line: line.split(" ")) \
    .filter(lambda word: word.lower() not in stop_words) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a + b)

print("\n=== WORD COUNT WITHOUT STOP WORDS ===")

for word, count in counts.collect():
    print(f"{word}: {count}")

spark.stop()
