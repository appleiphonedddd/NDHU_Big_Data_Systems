#!/bin/bash

FLINK_PROPERTIES="jobmanager.rpc.address: jobmanager"
DEFAULT_TASKMANAGERS=2

# Function to display usage
function usage() {
  echo "Usage: $0 [NUM_TASKMANAGERS]"
  echo "       NUM_TASKMANAGERS: Optional, specify the number of TaskManagers to start (default: $DEFAULT_TASKMANAGERS)."
  echo "       Example: $0 3"
  echo "       Use '--help' to display this help message."
}

# Check for --help argument
if [[ "$1" == "--help" ]]; then
  usage
  exit 0
fi

# Get the number of TaskManagers from the first argument, or use the default
NUM_TASKMANAGERS=${1:-$DEFAULT_TASKMANAGERS}

# Validate NUM_TASKMANAGERS is a positive integer
if ! [[ "$NUM_TASKMANAGERS" =~ ^[0-9]+$ ]] || [[ "$NUM_TASKMANAGERS" -le 0 ]]; then
  echo "Error: NUM_TASKMANAGERS must be a positive integer."
  usage
  exit 1
fi

# Check if the Docker network 'flink-network' already exists
if ! docker network ls | grep -q "flink-network"; then
  echo "Creating flink-network..."
  docker network create flink-network
else
  echo "flink-network already exists. Skipping creation."
fi

# Start the JobManager container
echo "Starting JobManager container..."
docker run \
    -d \
    --rm \
    --name=jobmanager \
    --network flink-network \
    --publish 8081:8081 \
    --env FLINK_PROPERTIES="${FLINK_PROPERTIES}" \
    flink-python:latest jobmanager

# Start the specified number of TaskManager containers
echo "Starting $NUM_TASKMANAGERS TaskManager containers..."
for i in $(seq 1 "$NUM_TASKMANAGERS"); do
  docker run \
      -d \
      --rm \
      --name=taskmanager-$i \
      --network flink-network \
      --env FLINK_PROPERTIES="${FLINK_PROPERTIES}" \
      flink-python:latest taskmanager
  echo "TaskManager-$i started."
done

echo "Flink cluster setup completed. Access the JobManager UI at http://localhost:8081"
