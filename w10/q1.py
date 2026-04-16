from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("EmployeeSQL_230968114").getOrCreate()

df = spark.read.csv("hdfs://localhost:9000/user/230968114/lab10/employee_extended.csv", header=True, inferSchema=True)

df.createOrReplaceTempView("employees")

high_salary = spark.sql("""
SELECT e.Department, e.Name, e.MonthlyIncome
FROM employees e
JOIN (
    SELECT Department, MAX(MonthlyIncome) as MaxSalary
    FROM employees
    GROUP BY Department
) m
ON e.Department = m.Department AND e.MonthlyIncome = m.MaxSalary
""")
high_salary.show()

gender_salary = spark.sql("""
SELECT Gender, AVG(MonthlyIncome) as AvgSalary, MAX(MonthlyIncome) as MaxSalary, MIN(MonthlyIncome) as MinSalary
FROM employees
GROUP BY Gender
""")
gender_salary.show()

high_salary.write.csv("hdfs://localhost:9000/user/230968114/lab10/output/high_salary", header=True, mode="overwrite")
gender_salary.write.csv("hdfs://localhost:9000/user/230968114/lab10/output/gender_salary", header=True, mode="overwrite")
