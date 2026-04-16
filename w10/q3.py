from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DeptInsights_230968114").getOrCreate()

employees = spark.read.csv("/home/bdalab/Desktop/Piyush_230968114/w10/employee_extended.csv", header=True, inferSchema=True)

employees.createOrReplaceTempView("employees")

departments = spark.read.csv("/home/bdalab/Desktop/Piyush_230968114/w10/departments.csv", header=True, inferSchema=True) 

departments.createOrReplaceTempView("departments")

# --- a) Join employees with departments ---
join_df = spark.sql("""
SELECT e.Name, d.DepartmentName
FROM employees e
JOIN departments d
ON e.Department = d.DepartmentName
""")
print("Employee names with their departments:")
join_df.show()

# --- b) Count employees per department ---
count_df = spark.sql("""
SELECT Department, COUNT(*) as EmployeeCount
FROM employees
GROUP BY Department
""")
print("Employee count per department:")
count_df.show()

# --- c) Departments with average salary > 60000 ---
avg_salary_df = spark.sql("""
SELECT Department, AVG(MonthlyIncome) as AvgSalary
FROM employees
GROUP BY Department
HAVING AVG(MonthlyIncome) > 60000
""")
print("Departments with avg salary > 60000:")
avg_salary_df.show()
