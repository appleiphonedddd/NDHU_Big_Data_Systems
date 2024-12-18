#!/bin/bash

JOB_FILE=$1

if [ -z "$JOB_FILE" ]; then
  echo "Usage: $0 <python_job_file>"
  exit 1
fi

echo "Copying $JOB_FILE to JobManager container..."
docker cp "$JOB_FILE" jobmanager:/job.py

echo "Submitting $JOB_FILE to Flink cluster..."
docker exec -it jobmanager flink run -py /job.py
