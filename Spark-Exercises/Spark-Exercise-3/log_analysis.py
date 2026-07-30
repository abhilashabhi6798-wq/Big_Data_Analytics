from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("LogFileAnalysis") \
    .getOrCreate()

sc = spark.sparkContext

# Read server log file
logs = sc.textFile("server.log")

# Extract HTTP status code from each line
status_codes = logs.map(lambda line: line.split()[-1])

# Count each status code
status_counts = status_codes.map(lambda code: (code, 1)) \
    .reduceByKey(lambda a, b: a + b)

print("\n=== HTTP STATUS CODE COUNTS ===")
for code, count in sorted(status_counts.collect()):
    print(f"{code}: {count}")

# Filter error status codes (400 and above)
error_counts = status_counts.filter(
    lambda x: int(x[0]) >= 400
)

# Sort errors by frequency
frequent_errors = error_counts.sortBy(
    lambda x: x[1],
    ascending=False
)

print("\n=== MOST FREQUENT ERROR CODES ===")
for code, count in frequent_errors.collect():
    print(f"{code}: {count}")

spark.stop()

