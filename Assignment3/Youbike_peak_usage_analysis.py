from pyspark.sql import SparkSession
from pyspark.sql.functions import col, hour, desc, sum as _sum, rank
from pyspark.sql.window import Window

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Youbike Peak Usage Analysis") \
    .getOrCreate()

# Load data
file_path = "Youbike.csv"
data = spark.read.csv(file_path, header=True, inferSchema=True)

# Extract hour from time
data = data.withColumn("Hour", hour(col("Time")))

# Calculate total activity (borrow + return) for each hour at each station
hourly_activity = data.groupBy("Station", "Hour") \
    .agg(_sum((col("Action") == "Borrow").cast("int")).alias("Borrow_Count"),
         _sum((col("Action") == "Return").cast("int")).alias("Return_Count")) \
    .withColumn("Total_Activity", col("Borrow_Count") + col("Return_Count"))

# Identify the busiest hour for each station
window_spec = Window.partitionBy("Station").orderBy(desc("Total_Activity"))
busiest_hours = hourly_activity.withColumn("Rank", rank().over(window_spec)) \
    .filter(col("Rank") == 1)

# Rank all stations by their peak usage
overall_rank_spec = Window.orderBy(desc("Total_Activity"))
ranked_busiest_hours = busiest_hours.withColumn("Overall_Rank", rank().over(overall_rank_spec))

# Display results
ranked_busiest_hours.select("Station", "Hour", "Total_Activity", "Borrow_Count", "Return_Count", "Overall_Rank") \
    .orderBy("Overall_Rank") \
    .show(100, truncate=False)

# Stop Spark Session
spark.stop()
