from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, desc

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("Youbike Rent/Return Analysis") \
    .getOrCreate()

# Load data
file_path = "Youbike.csv"
data = spark.read.csv(file_path, header=True, inferSchema=True)

# Separate borrow and return records
borrow_data = data.filter(col("Action") == "Borrow").select(
    col("Bike ID").alias("Bike_ID"),
    col("Time").alias("Borrow_Time"),
    col("Station").alias("Rent_Station")
)

return_data = data.filter(col("Action") == "Return").select(
    col("Bike ID").alias("Bike_ID"),
    col("Time").alias("Return_Time"),
    col("Station").alias("Return_Station")
)

# Join borrow and return records on Bike ID, ensuring Return_Time > Borrow_Time
station_pairs = borrow_data.alias("borrow").join(
    return_data.alias("return"),
    (col("borrow.Bike_ID") == col("return.Bike_ID")) &
    (col("return.Return_Time") > col("borrow.Borrow_Time"))
).select(
    col("borrow.Bike_ID").alias("Bike_ID"),
    col("borrow.Borrow_Time").alias("Borrow_Time"),
    col("return.Return_Time").alias("Return_Time"),
    col("borrow.Rent_Station").alias("Rent_Station"),
    col("return.Return_Station").alias("Return_Station")
)

# Group by rent/return station pairs and count occurrences
station_pair_counts = station_pairs.groupBy("Rent_Station", "Return_Station") \
    .agg(count("*").alias("Count")) \
    .orderBy(desc("Count"))

# Display the top station pairs
station_pair_counts.show(10, truncate=False)

# Stop Spark Session
spark.stop()
