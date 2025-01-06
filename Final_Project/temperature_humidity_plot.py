from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table.expressions import col
import pandas as pd
import matplotlib.pyplot as plt

env_settings = EnvironmentSettings.in_batch_mode()
t_env = TableEnvironment.create(env_settings)

data_file = "data.csv"  

t_env.execute_sql(f"""
    CREATE TABLE weather (
        station_id INT,
        state STRING,
        `timestamp` STRING,
        temperature DOUBLE,
        humidity INT,
        pressure DOUBLE,
        wind_speed DOUBLE,
        wind_direction INT,
        rainfall DOUBLE
    ) WITH (
        'connector' = 'filesystem',
        'format' = 'csv',
        'csv.ignore-parse-errors' = 'true',
        'csv.disable-quote-character' = 'false',
        'csv.field-delimiter' = ',',
        'path' = '{data_file}'
    )
""")

data_table = t_env.from_path("weather")

sampled_table = data_table.limit(10000)

filtered_table = sampled_table.filter((col("temperature") >= 15) & (col("temperature") <= 35))

temp_humidity_table = filtered_table.select(col("temperature"), col("humidity"))

def table_to_dataframe(table_result):
    result = table_result.execute()
    columns = table_result.get_schema().get_field_names()
    rows = [row for row in result.collect()]
    return pd.DataFrame(rows, columns=columns)

df = table_to_dataframe(temp_humidity_table)

plt.figure(figsize=(8, 6))
plt.scatter(df["temperature"], df["humidity"], alpha=0.5, color='green')
plt.title("Temperature vs Humidity (Sampled Data)", fontsize=16)
plt.xlabel("Temperature (°C)", fontsize=12)
plt.ylabel("Humidity (%)", fontsize=12)
plt.grid(True)
plt.tight_layout()

output_path = "temperature_vs_humidity_sampled.png"
plt.savefig(output_path, dpi=300)
plt.show()

print(f"Chart saved as {output_path}")
