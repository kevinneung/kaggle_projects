from pyspark.sql import SparkSession

# Initialize a SparkSession
spark = SparkSession.builder.appName("example").getOrCreate()

# Create a simple DataFrame
data = [("Alice", 34), ("Bob", 45), ("Catherine", 29)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
df.show()

# Stop the SparkSession
spark.stop()