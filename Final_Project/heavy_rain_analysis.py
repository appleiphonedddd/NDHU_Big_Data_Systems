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

heavy_rain_days = data_table.filter(col("rainfall") <20) \
    .group_by(col("state")) \
    .select(col("state"), col("rainfall").count.alias("heavy_rain_days"))

def table_to_dataframe(table_result):
    result = table_result.execute()
    columns = table_result.get_schema().get_field_names()
    rows = [row for row in result.collect()]
    return pd.DataFrame(rows, columns=columns)

df = table_to_dataframe(heavy_rain_days)

plt.figure(figsize=(10, 8))
plt.pie(
    df["heavy_rain_days"],
    labels=df["state"],
    autopct='%1.1f%%',
    startangle=140,
    colors=plt.cm.Paired.colors
)
plt.title("Heavy Rain Days by State (<20mm)", fontsize=16)

output_path_pie = "heavy_rain_days_pie_by_state.png"
plt.savefig(output_path_pie, dpi=300)
plt.show()

print(f"Chart saved as {output_path_pie}")
