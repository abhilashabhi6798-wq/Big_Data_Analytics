from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("SparkSQLExercise") \
    .getOrCreate()

# Load CSV into DataFrame
df = spark.read.csv(
    "students.csv",
    header=True,
    inferSchema=True
)

print("\n=== STUDENT DATA ===")
df.show()

# Create temporary SQL view
df.createOrReplaceTempView("students")

# Query 1: Students with marks greater than 80
print("\n=== STUDENTS WITH MARKS > 80 ===")
spark.sql("""
    SELECT *
    FROM students
    WHERE marks > 80
""").show()

# Query 2: Average marks by department
print("\n=== AVERAGE MARKS BY DEPARTMENT ===")
spark.sql("""
    SELECT department, AVG(marks) AS average_marks
    FROM students
    GROUP BY department
""").show()

# Query 3: Students sorted by marks
print("\n=== STUDENTS SORTED BY MARKS ===")
spark.sql("""
    SELECT *
    FROM students
    ORDER BY marks DESC
""").show()

spark.stop()
