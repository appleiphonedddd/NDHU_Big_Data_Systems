#!/bin/bash

docker cp visualization.py jobmanager:/opt/flink
docker cp data.csv jobmanager:/opt/flink