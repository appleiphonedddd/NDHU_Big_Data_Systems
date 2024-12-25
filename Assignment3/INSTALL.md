# Assignment 3

`Assignment 3`  is a project for the Big Data Systems course at National Dong Hwa University. The purpose of this project is to set up and operate a Spark cluster to process large datasets with an HBase database. It involves implementing core big data algorithms and provides instructions for setting up the cluster, running the project, and understanding its key components.

## Contents

- [Getting Started](#Getting-Started)
  - [Requirements](#Requirements)
  - [Installation](#Installation)
- [Directory Structure](#Directory-Structure)
- [Deployment](#Deployment)

### Getting Started

###### Requirements

1. Ubuntu 24.04
2. Flink
3. Hbase

###### **Installation**

1. Upgrade package

```sh
sudo apt-get update
```

2. Install Docker engine and Docker compose

```sh
./install-docker.sh
./install-docker-compose.sh
```

### Directory Structure

```
filetree 
├── docker-cmd.sh
├── docker-spark-cluster
│   ├── app
│   │   ├── main.py
│   │   ├── mta.conf
│   │   ├── mta-processing.jar
│   │   └── postgresql-42.2.22.jar
│   ├── apps
│   ├── articles
│   │   └── docker-compose.md
│   ├── data
│   ├── docker-compose.yml
│   ├── Dockerfile
│   └── start-spark.sh
├── ID.py
├── install-docker-compose.sh
├── install-docker.sh
├── INSTALL.md
├── Logs
│   ├── ID.txt
│   ├── Peak_hour.txt
│   └── top10.txt
├── Result
│   ├── ID.png
│   ├── Peak_hour.png
│   └── Top10.png
├── setup-hbase-docker.sh
├── start-hbase.sh
├── Top10.py
├── Youbike.csv
└── Youbike_peak_usage_analysis.py
```

### Deployment

1. Build the image

```sh
cd docker-spark-cluster/
docker build -t cluster-apache-spark:3.0.2 .
```

2. Run the docker-compose

```sh
docker-compose up -d
```

3. Build an HBase environment in Docker and configure it to connect to Spark

```sh
./setup-hbase-docker.sh
```

4. Open new terminal and show docker container ID

```sh
docker ps -a
```

5. Copy all the .py files and the Testcase Youbike.csv files to the master container in Spark

```sh
docker cp /path/to/files docker-spark-cluster_spark-master_1:/opt/spark/data/
```

5. Switch to the original terminal on the Spark master

```sh
docker exec -it docker-spark-cluster_spark-master_1 bash
```

6. Setting environment path in Spark master container

```sh
cd data
export PATH=/opt/spark/bin:$PATH
```

7. Execute PageRank in Spark and check the output results

```sh
spark-submit /opt/spark/data/ID.py
spark-submit /opt/spark/data/Top10.py
spark-submit /opt/spark/data/Youbike_peak_usage_analysis.py
```

8. If you want to clear all container in Linux

```sh
./docker-cmd.sh clear
```

### UI

1. Check IP address for host machine

```sh
ifconfig
```

2. Open the browser and enter the URL

```sh
http://localhost:9090/
```