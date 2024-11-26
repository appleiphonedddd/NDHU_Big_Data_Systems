# Assignment 2

`Assignment 2` project belongs to the Big Data Systems at National Dong Hwa University. The purpose of this project is to set up and operate a Spark cluster to process large datasets and implement core big data algorithms and provides instructions for setting up the cluster, running the project, and understanding its key components


## Contents

- [Getting Started](#Getting-Started)
  - [Requirements](#Requirements)
  - [Installation](#Installation)
- [Directory Structure](#Directory-Structure)
- [Deployment](#Deployment)

### Getting Started

###### Requirements

1. Ubuntu 24.04
2. Spark 3.0.2

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
├── compute_gpa.py
├── count_frequent.py
├── docker-spark-cluster
│   ├── apps
│   │   ├── main.py
│   │   ├── mta.conf
│   │   ├── mta-processing.jar
│   │   └── postgresql-42.2.22.jar
│   ├── articles
│   │   ├── docker-compose.md
│   │   └── images
│   │       ├── pyspark-demo.png
│   │       ├── spark-master.png
│   │       ├── spark-worker-1.png
│   │       ├── spark-worker-2.png
│   │       └── stats-app.png
│   ├── docker-compose.yml
│   ├── Dockerfile
│   ├── README.md
│   └── start-spark.sh
├── install-docker-compose.sh
├── install-docker.sh
├── INSTALL.md
├── inverted_index.py
├── Log
│   ├── 2A
│   │   ├── Compute GPA.txt
│   │   ├── Invert Index.txt
│   │   └── Pagerank.txt
│   └── 2B
│       └── Count Frequent.txt
├── pagerank.py
├── Result
│   ├── 2A
│   │   ├── Compute GPA
│   │   │   ├── Output course stats.png
│   │   │   ├── Output failure rates.png
│   │   │   └── Output student gpas.png
│   │   ├── Invert Index
│   │   │   ├── Invert output1.png
│   │   │   ├── Invert output2.png
│   │   │   ├── Invert output3.png
│   │   │   ├── Invert output4.png
│   │   │   ├── Invert output5.png
│   │   │   ├── Invert output6.png
│   │   │   └── Invert output7.png
│   │   └── Pagerank
│   │       └── Output Rank.png
│   └── 2B
│       └── Sort Frequent Data.png
└── Testcase
    ├── 2A
    │   ├── academic_credit.txt
    │   ├── article.txt
    │   ├── grades.txt
    │   └── PR_data.txt
    └── 2B
        └── purchase.txt
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

3. Open new terminal and show docker container ID

```sh
docker ps -a
```

4. Copy all the .py files and the Testcase dictionary.txt files to the master container in Spark

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
spark-submit /opt/spark/data/pagerank.py
cat /opt/spark/data/output_ranks.txt 
```


7. If you want to execute Step6,Step8,Step9,Step10 again, please use the command to delete the output log

```sh
rm -r /opt/spark/data/output_ranks.txt
rm -r /opt/spark/data/output_student_gpas
rm -r /opt/spark/data/output_course_stats
rm -r /opt/spark/data/output_failure_rates
rm -rf /opt/spark/data/invert_data
rm -r /opt/spark/data/sorted_frequent_data
```

8. Execute Compute GPA in Spark

```sh
spark-submit /opt/spark/data/compute_gpa.py
```

9. Execute Inverted Index in Spark and check the output results

```sh
spark-submit /opt/spark/data/inverted_index.py
cat /opt/spark/data/output_student_gpas/part-00000
cat /opt/spark/data/output_course_stats/part-00000
cat /opt/spark/data/output_failure_rates/part-00000
```

10. Execute Count Frequent in Spark and check the output results

```sh
spark-submit /opt/spark/data/count_frequent.py
cat /opt/spark/data/invert_data/part-00000
```

11. If you want to clear all container in Linux

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