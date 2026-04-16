from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum

spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Load CSV file
df = spark.read.csv("hdfs://localhost:9000/user/230968114/lab8/sales.csv",
                    header=True, inferSchema=True)

print("\n=== Original Data ===")
df.show()

# Compute revenue
df = df.withColumn("Revenue", col("Price") * col("Quantity"))

print("\n=== Data with Revenue Column ===")
df.show()

# Total revenue per product
revenue_per_product = df.groupBy("Product").agg(_sum("Revenue").alias("Total_Revenue"))

print("\n=== Revenue Per Product ===")
revenue_per_product.show()

# Highest selling product
top_product = revenue_per_product.orderBy(col("Total_Revenue").desc())

print("\n=== Highest Selling Product ===")
top_product.show(1)

# Filter transactions above $500
high_sales = df.filter(col("Revenue") > 500)

print("\n=== Transactions with Revenue > 500 ===")
high_sales.show()

# Revenue per category
revenue_per_category = df.groupBy("Category").agg(_sum("Revenue").alias("Total_Revenue"))

print("\n=== Revenue Per Category ===")
revenue_per_category.show()

# Save results
df.write.mode("overwrite").csv("hdfs://localhost:9000/user/230968114/lab8/output/sales_output", header=True)
revenue_per_category.write.mode("overwrite").csv("hdfs://localhost:9000/user/230968114/lab8/output/category_revenue", header=True)

spark.stop()
