

from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator, RegressionEvaluator

spark = SparkSession.builder.appName("Attrition_230968114").getOrCreate()

df = spark.read.csv("hdfs://localhost:9000/user/230968114/lab9/employee_attrition.csv",
                    header=True, inferSchema=True)

print("=== Data Loaded ===")
df.show(5)

df = df.dropna()

categorical_cols = ["Gender", "Department", "JobRole", "Attrition"]

for col_name in categorical_cols:
    indexer = StringIndexer(inputCol=col_name, outputCol=col_name+"_idx")
    df = indexer.fit(df).transform(df)

print("=== Attrition Count ===")
df.groupBy("Attrition").count().show()

print("=== Avg Salary by Department ===")
df.groupBy("Department").avg("MonthlyIncome").show()

# ---------------- Classification ----------------
features = ["Age", "MonthlyIncome", "YearsAtCompany",
            "Gender_idx", "Department_idx"]

assembler = VectorAssembler(inputCols=features, outputCol="features")
data = assembler.transform(df)

train, test = data.randomSplit([0.8, 0.2], seed=42)

lr = LogisticRegression(featuresCol="features", labelCol="Attrition_idx")
model = lr.fit(train)

pred = model.transform(test)

evaluator = BinaryClassificationEvaluator(labelCol="Attrition_idx")
print("Attrition Accuracy:", evaluator.evaluate(pred))

# ---------------- Regression ----------------
salary_features = ["Age", "YearsAtCompany", "Department_idx"]

assembler2 = VectorAssembler(inputCols=salary_features, outputCol="features2")
data2 = assembler2.transform(df)

train2, test2 = data2.randomSplit([0.8, 0.2], seed=42)

lr2 = LinearRegression(featuresCol="features2", labelCol="MonthlyIncome")
model2 = lr2.fit(train2)

pred2 = model2.transform(test2)

evaluator2 = RegressionEvaluator(labelCol="MonthlyIncome")
print("Salary RMSE:", evaluator2.evaluate(pred2))

spark.stop()
