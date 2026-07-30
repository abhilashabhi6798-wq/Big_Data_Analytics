from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StandardScaler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Create Spark Session
spark = SparkSession.builder \
    .appName("MachineLearningPipeline") \
    .getOrCreate()

# Load dataset
df = spark.read.csv(
    "customer_data.csv",
    header=True,
    inferSchema=True
)

print("\n=== CUSTOMER DATA ===")
df.show()

# Feature columns
feature_cols = [
    "age",
    "income",
    "purchase_history",
    "website_visits"
]

# Convert category into numeric values
string_indexer = StringIndexer(
    inputCol="category",
    outputCol="category_index"
)

# Combine features into one vector
assembler = VectorAssembler(
    inputCols=feature_cols + ["category_index"],
    outputCol="features_vector"
)

# Scale features
scaler = StandardScaler(
    inputCol="features_vector",
    outputCol="scaled_features",
    withStd=True,
    withMean=True
)

# Random Forest model
rf = RandomForestClassifier(
    featuresCol="scaled_features",
    labelCol="label",
    numTrees=50,
    seed=42
)

# Create ML pipeline
pipeline = Pipeline(
    stages=[string_indexer, assembler, scaler, rf]
)

# Split dataset
train_data, test_data = df.randomSplit(
    [0.8, 0.2],
    seed=42
)

print("Training records:", train_data.count())
print("Testing records:", test_data.count())

# Train model
model = pipeline.fit(train_data)

# Generate predictions
predictions = model.transform(test_data)

print("\n=== PREDICTIONS ===")
predictions.select(
    "age",
    "income",
    "category",
    "label",
    "prediction"
).show()

# Evaluate accuracy
evaluator = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
)

accuracy = evaluator.evaluate(predictions)

print("Model Accuracy:", accuracy)

spark.stop()
