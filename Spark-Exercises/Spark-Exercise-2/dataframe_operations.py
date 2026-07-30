from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col

# Create Spark Session
spark = SparkSession.builder \
    .appName("DataFrameOperations") \
    .getOrCreate()

# Load CSV file
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

print("\n=== EMPLOYEE DATA ===")
df.show()

# Filter employees with salary greater than 50000
print("\n=== EMPLOYEES WITH SALARY > 50000 ===")
df.filter(col("salary") > 50000).show()

# Average salary by department
print("\n=== AVERAGE SALARY BY DEPARTMENT ===")
df.groupBy("department") \
    .agg(avg("salary").alias("average_salary")) \
    .show()

# Sort employees by salary in descending order
print("\n=== EMPLOYEES SORTED BY SALARY ===")
df.orderBy(col("salary").desc()).show()

# Add 10% bonus column
print("\n=== EMPLOYEES WITH 10% BONUS ===")
df.withColumn("bonus", col("salary") * 0.10).show()

spark.stop()
