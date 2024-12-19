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

start_date = "2024-12-01"
end_date = "2024-12-07"
selected_state = "Bahia"

filtered_table = data_table \
    .filter((col("state") == selected_state) & 
            (col("timestamp") >= start_date) & 
            (col("timestamp") <= end_date)) \
    .select(col("timestamp"), col("temperature")) \
    .group_by(col("timestamp")) \
    .select(col("timestamp"), col("temperature").avg.alias("avg_temperature")) \
    .order_by(col("timestamp"))

def table_to_dataframe(table_result):
    result = table_result.execute()
    columns = table_result.get_schema().get_field_names()
    rows = [row for row in result.collect()]
    return pd.DataFrame(rows, columns=columns)

df = table_to_dataframe(filtered_table)

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by="timestamp")

plt.figure(figsize=(10, 6))
plt.plot(df["timestamp"], df["avg_temperature"], marker='o', linestyle='-', color='b', label=f'State: {selected_state}')
plt.title(f"Average Temperature Trend in {selected_state}\n{start_date} to {end_date}", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Average Temperature (°C)", fontsize=12)
plt.grid(True)
plt.legend(fontsize=10)
plt.tight_layout()

output_path = f"average_temperature_trend_{selected_state}.png"
plt.savefig(output_path, dpi=300)
plt.show()

print(f"Chart saved as {output_path}")
