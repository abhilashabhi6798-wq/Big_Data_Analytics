from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

spark = SparkSession.builder \
    .appName("HyperparameterTuning") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Load dataset
data = spark.read.csv(
    "customer_data.csv",
    header=True,
    inferSchema=True
)

# Convert categorical column to numeric
indexer = StringIndexer(
    inputCol="category",
    outputCol="category_index"
)

# Combine features
assembler = VectorAssembler(
    inputCols=[
        "age",
        "income",
        "purchase_history",
        "website_visits",
        "category_index"
    ],
    outputCol="features"
)

# Random Forest classifier
rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    seed=42
)

pipeline = Pipeline(
    stages=[indexer, assembler, rf]
)

# Hyperparameter combinations
paramGrid = ParamGridBuilder() \
    .addGrid(rf.numTrees, [10, 20]) \
    .addGrid(rf.maxDepth, [3, 5]) \
    .build()

evaluator = BinaryClassificationEvaluator(
    labelCol="label"
)

# Cross-validation
crossval = CrossValidator(
    estimator=pipeline,
    estimatorParamMaps=paramGrid,
    evaluator=evaluator,
    numFolds=3,
    seed=42
)

# Split dataset
train_data, test_data = data.randomSplit(
    [0.8, 0.2],
    seed=42
)

print("Training records:", train_data.count())
print("Testing records:", test_data.count())

# Train models and select best one
cv_model = crossval.fit(train_data)

# Prediction
predictions = cv_model.transform(test_data)

print("\n=== PREDICTIONS ===")
predictions.select(
    "age",
    "category",
    "label",
    "prediction",
    "probability"
).show(truncate=False)

# Evaluate
auc = evaluator.evaluate(predictions)

print("AUC:", auc)

# Best Random Forest model
best_rf = cv_model.bestModel.stages[-1]

print("Best numTrees:", best_rf.getNumTrees)
print("Best maxDepth:", best_rf.getOrDefault("maxDepth"))

spark.stop()
