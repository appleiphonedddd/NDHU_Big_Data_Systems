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

result_table = data_table.select(col("state"), col("rainfall"))\
    .group_by(col("state"))\
    .select(col("state"), col("rainfall").max.alias("max_rainfall"))\
    .order_by(col("max_rainfall").desc)

def table_to_dataframe(table_result):
    result = table_result.execute()
    
    columns = table_result.get_schema().get_field_names()
    rows = []
    for row in result.collect():
        rows.append(row)
    return pd.DataFrame(rows, columns=columns)


df = table_to_dataframe(result_table)

print(df)

plt.figure(figsize=(12, 6))
df = df.sort_values(by="max_rainfall", ascending=False)
plt.bar(df["state"], df["max_rainfall"], color='skyblue')
plt.title("Maximum Rainfall by State", fontsize=16)
plt.xlabel("State", fontsize=12)
plt.ylabel("Max Rainfall (mm)", fontsize=12)
plt.xticks(rotation=45, fontsize=10)
plt.tight_layout()

output_path = "max_rainfall_by_state.png"
plt.savefig(output_path, dpi=300)
plt.show()

print(f"Chart saved as {output_path}")