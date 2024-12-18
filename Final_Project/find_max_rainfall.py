from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table.expressions import col

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
        'csv.ignore-parse-errors' = 'true', -- 避免單行解析錯誤導致整個任務失敗
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

result_table.execute().print()