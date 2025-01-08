#!/bin/bash

docker cp data.csv jobmanager:/opt/flink
docker cp find_max_rainfall.py jobmanager:/opt/flink
docker cp heavy_rain_analysis.py jobmanager:/opt/flink
docker cp average_temperature_trend.py jobmanager:/opt/flink
docker cp temperature_humidity_plot.py jobmanager:/opt/flink