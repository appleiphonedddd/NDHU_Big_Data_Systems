# Final+Project

`Final+Project` project belongs to the Big Data Systems at National Dong Hwa University. The purpose of this project is to set up and operate a Spark cluster to process large datasets and implement core big data algorithms and provides instructions for setting up the cluster, running the project, and understanding its key components


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
├── average_temperature_trend.py
├── data.csv
├── deploy_files.sh
├── docker-cmd.sh
├── Dockerfile
├── find_max_rainfall.py
├── heavy_rain_analysis.py
├── INSTALL.md
├── requirement.txt
├── Result
│   ├── average_temperature_trend_Bahia.png
│   ├── heavy_rain_days_pie_by_state.png
│   └── max_rainfall_by_state.png
└── run_flink_cluster.sh
```

### Deployment

1. Build the image

```sh
docker build -t flink-python:latest .
```

2. Run the docker-compose

```sh
./run_flink_cluster.sh number of taskmanager
```

4. Deploy file to container

```sh
./deploy_files.sh
```

4. Enter Master container

```sh
docker exec -it jobmanager bash
```

5. Create a symbolic link for python to point to python3

```sh
ln -s /usr/bin/python3 /usr/bin/python
```

6. Verify the Python version

```sh
python --version
```

7. Execute python file

```sh
pythons filename.py
```