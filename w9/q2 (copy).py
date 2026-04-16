

from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator

spark = SparkSession.builder.appName("Promotion_230968114").getOrCreate()

# Load data
df = spark.read.csv(
    "hdfs://localhost:9000/user/230968114/lab9/employee_promotion.csv",
    header=True, inferSchema=True
)

# 🔥 OPTIONAL BEST PRACTICE (avoid future errors)
df = df.toDF(*[c.strip() for c in df.columns])

print("Columns:", df.columns)

# -----------------------------
# Correct categorical columns
# -----------------------------
categorical_cols = ["Department", "Education", "Gender"]

for col_name in categorical_cols:
    indexer = StringIndexer(inputCol=col_name, outputCol=col_name+"_idx")
    df = indexer.fit(df).transform(df)

# -----------------------------
# Features (FIXED NAMES)
# -----------------------------
features = ["Age", "PreviousYearRating",
            "LengthOfService", "Department_idx"]

assembler = VectorAssembler(inputCols=features, outputCol="features")
data = assembler.transform(df)

# -----------------------------
# Model
# -----------------------------
lr = LogisticRegression(featuresCol="features", labelCol="IsPromoted")

train, test = data.randomSplit([0.8, 0.2], seed=42)

model = lr.fit(train)

pred = model.transform(test)

pred.select("IsPromoted", "prediction").show()

spark.stop()
