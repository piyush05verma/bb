from pyspark import SparkContext

sc = SparkContext(appName="LogAnalysis")

# Load log file from HDFS
log_rdd = sc.textFile("hdfs://localhost:9000/user/230968114/lab8/server_log.txt")

print("\n=== Sample Log Data ===")
for line in log_rdd.take(5):
    print(line)

# Extract HTTP status codes
status_codes = log_rdd.map(lambda line: line.split(" ")[8])

# Count occurrences of each status code
status_count = status_codes.map(lambda code: (code, 1)) \
                           .reduceByKey(lambda a, b: a + b)

print("\n=== Status Code Count ===")
for item in status_count.collect():
    print(item)

# Extract IP addresses
ips = log_rdd.map(lambda line: line.split(" ")[0])

# Count most common IPs
ip_count = ips.map(lambda ip: (ip, 1)) \
              .reduceByKey(lambda a, b: a + b) \
              .sortBy(lambda x: -x[1])

print("\n=== Most Common IP Addresses ===")
for item in ip_count.collect():
    print(item)

# Filter error logs (4xx and 5xx)
errors = status_codes.filter(lambda code: code.startswith('4') or code.startswith('5'))

print("\n=== Error Status Codes (4xx, 5xx) ===")
for item in errors.collect():
    print(item)

error_count = errors.count()
print("\n=== Total Error Logs ===")
print(error_count)

# Save results to HDFS
status_count.saveAsTextFile("hdfs://localhost:9000/user/230968114/lab8output/status_count")
ip_count.saveAsTextFile("hdfs://localhost:9000/user/230968114/lab8/output/ip_count")
errors.saveAsTextFile("hdfs://localhost:9000/user/230968114/lab8/output/error_logs")

sc.stop()
