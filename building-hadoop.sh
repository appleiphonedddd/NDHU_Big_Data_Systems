#!/bin/bash

# Pull the Docker image
echo "Pulling the Docker image for Hadoop..."
sudo docker pull kiwenlau/hadoop:1.0

# Create a Hadoop Docker network if it doesn't exist
echo "Creating Hadoop network..."
if ! sudo docker network ls | grep -q hadoop; then
    sudo docker network create --driver=bridge hadoop
    echo "Hadoop network created."
else
    echo "Hadoop network already exists."
fi

# Start the container
echo "Starting the Hadoop container..."
sudo ./start-container.sh

echo "Deployment completed successfully."
