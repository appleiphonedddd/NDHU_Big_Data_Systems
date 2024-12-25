#!/bin/bash

docker pull dajobe/hbase

mkdir -p data

id=$(docker run --name hbase-docker \
                --hostname hbase-docker \
                --detach \
                --volume $PWD/data:/data \
                dajobe/hbase)

echo "Started HBase container with ID: $id"

if [ -f "./start-hbase.sh" ]; then
    ./start-hbase.sh
else
    echo "start-hbase.sh script not found! Ensure it's in the current directory."
fi
