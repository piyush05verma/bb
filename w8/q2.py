from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("JSONProcessing").getOrCreate()

# Load JSON file
df = spark.read.json("hdfs://localhost:9000/user/230968114/lab8/users.json")

print("\n=== Original Data ===")
df.show()

# Show schema
print("\n=== Schema ===")
df.printSchema()

# Select specific fields
selected_df = df.select("name", "age", "city")
print("\n=== Selected Fields (name, age, city) ===")
selected_df.show()

# Filter users older than 30
filtered_df = df.filter(df.age > 30)
print("\n=== Users with Age > 30 ===")
filtered_df.show()

# Group by city and count users
grouped_df = df.groupBy("city").count()
print("\n=== User Count by City ===")
grouped_df.show()

# Save processed data
grouped_df.write.mode("overwrite").json("hdfs://localhost:9000/user/230968114/lab8/output/json_output")

spark.stop()
