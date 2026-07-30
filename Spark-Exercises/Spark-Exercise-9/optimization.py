from pyspark.sql import SparkSession
from pyspark import StorageLevel

spark = SparkSession.builder \
    .appName("Spark Optimization Techniques") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Load dataset
df = spark.read.csv(
    "data.csv",
    header=True,
    inferSchema=True
)

print("\n=== ORIGINAL DATA ===")
df.show()

# 1. Check number of partitions
print("Original partitions:", df.rdd.getNumPartitions())

# 2. Repartition
df_optimized = df.repartition(4)

print("Partitions after repartition:",
      df_optimized.rdd.getNumPartitions())

# 3. Coalesce
df_coalesced = df_optimized.coalesce(2)

print("Partitions after coalesce:",
      df_coalesced.rdd.getNumPartitions())

# 4. Cache DataFrame
df.cache()
df.count()

print("DataFrame cached successfully")

# 5. Persist using memory and disk
df.persist(StorageLevel.MEMORY_AND_DISK)
df.count()

print("DataFrame persisted successfully")

# 6. Shuffle optimization
spark.conf.set(
    "spark.sql.adaptive.enabled",
    "true"
)

spark.conf.set(
    "spark.sql.adaptive.coalescePartitions.enabled",
    "true"
)

spark.conf.set(
    "spark.sql.shuffle.partitions",
    "4"
)

print("Adaptive Query Execution:",
      spark.conf.get("spark.sql.adaptive.enabled"))

print("Shuffle partitions:",
      spark.conf.get("spark.sql.shuffle.partitions"))

df.unpersist()

spark.stop()
