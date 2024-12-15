from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, desc, rank
from pyspark.sql.window import Window

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Youbike Analysis") \
    .getOrCreate()

# Load data
file_path = "Youbike.csv"
data = spark.read.csv(file_path, header=True, inferSchema=True)

# Extract hour from time
data = data.withColumn("Hour", hour(col("Time")))

# Group by hour and station, calculate borrow and return counts
activity_count = data.groupBy("Hour", "Station", "Action") \
    .count() \
    .groupBy("Hour", "Station") \
    .pivot("Action", ["Borrow", "Return"]) \
    .sum("count") \
    .fillna(0)

# Calculate total activity (borrow + return) for ranking
activity_count = activity_count.withColumn("Total Activity", col("Borrow") + col("Return"))

# Create a window specification for ranking stations by total activity
window_spec = Window.partitionBy("Hour").orderBy(desc("Total Activity"))

# Add rank and filter top 10 stations per hour
ranked_data = activity_count.withColumn("Rank", rank().over(window_spec)) \
    .filter(col("Rank") <= 10)

# Collect and display the result
top_stations = ranked_data.orderBy("Hour", "Rank").select("Hour", "Station", "Borrow", "Return", "Total Activity", "Rank")
top_stations.show(100, truncate=False)

# Stop Spark Session
spark.stop()
