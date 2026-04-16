from pyspark.sql import SparkSession

# Create Spark session
spark = SparkSession.builder.appName("SalesSQL_230968114").getOrCreate()

# Load sales CSV from HDFS
sales = spark.read.csv("hdfs://localhost:9000/user/230968114/lab10/sales_data.csv", header=True, inferSchema=True)

# Create temporary view
sales.createOrReplaceTempView("sales")

monthly_sales = spark.sql("""
SELECT SUBSTRING(OrderDate,1,7) as Month, SUM(Quantity*Price) as TotalSales
FROM sales
GROUP BY SUBSTRING(OrderDate,1,7)
ORDER BY Month
""")
monthly_sales.show()

top_customers = spark.sql("""
SELECT Customer, SUM(Quantity*Price) as Revenue
FROM sales
GROUP BY Customer
ORDER BY Revenue DESC
LIMIT 5
""")
top_customers.show()

avg_product = spark.sql("""
SELECT Product, AVG(Quantity*Price) as AvgRevenue
FROM sales
GROUP BY Product
""")
avg_product.show()
