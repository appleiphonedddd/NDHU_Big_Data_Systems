# NDHU_Big_Data_Systems_Fall

`NDHU_Big_Data_Systems_Fall` project belongs to the Big Data Systems at National Dong Hwa University. The purpose of this project is to know about 

Big data concepts, operational architecture, and related system tools. The system introduced is mainly open source software, including General purpose big data platforms): Hadoop/MatReduce, Apache Spark, HPCC, ...

 . Big data storage architecture and systems: distributed storage and file system, Google GFS, Apache HDFS, GlusterFS, ...

 . Big data systems for structured/semi-structured data: NoSQL/NewSQL/Distributed SQL, Apache HBase, Cassandra, Hive, MongoDB, ...

 .Systems for big graph processing: BSP, Pregel, Giraph, Spark GraphX, Neo4j, Titan, ...

 . Systems for streaming big data: Spark Streaming, Structured Streaming, Apache Storm, Samza, Flink, SAMOA, ...

 . Big data pipelineing, ETL, workflow and orchestration systems: Apache Airflow, Apache Kafka, Apache NiFi, Dagster, Prefect, ...

 . Big data analytics and advanced topics

## Contents

- [Getting Started](#Getting-Started)
  - [Requirements](#Requirements)
  - [Installation](#Installation)
- [Directory Structure](#Directory-Structure)
- [Deployment](#Deployment)
- [Frameworks Used](#Frameworks-Used)
- [Author](#Author)

### Getting Started

###### Requirements

1. Python 3.9
2. Ubuntu 24.04
3. Hodoop 2.7.2

###### **Installation**

1. Upgrade package

```sh
sudo apt-get update
```

2. Install Conda and Docker

```sh
./Install_miniconda.sh
./Install_docker.sh
```

3. Building environment in conda

```sh
conda create --name BigData python=3.9
```

4. Active environment

```sh
conda activate BigData
```

### Directory Structure

```
filetree 
├── Assignment1
│   ├── Log
│   │   └── Map_reduce_log.txt
│   ├── Mapper.py
│   ├── Mapper_search.py
│   ├── Mapper_tfidf.py
│   ├── Reducer.py
│   ├── Reducer_search.py
│   ├── Reducer_tfidf.py
│   ├── Result
│   │   └── Mapper and reduce.png
│   ├── Sorting.py
│   └── Testcase
│       └── wc_data1.txt
├── build-image.sh
├── building_Hadoop.sh
├── config
│   ├── core-site.xml
│   ├── hadoop-env.sh
│   ├── hdfs-site.xml
│   ├── mapred-site.xml
│   ├── run-wordcount.sh
│   ├── slaves
│   ├── ssh_config
│   ├── start-hadoop.sh
│   └── yarn-site.xml
├── Dockerfile
├── Install_docker.sh
├── Install_miniconda.sh
├── LICENSE
├── README.md
├── resize-cluster.sh
└── start-container.sh
```

### Deployment

1. Pull docker image

```sh
./building_Hadoop.sh
```

2. Start hadoop cluster

```sh
./start-hadoop.sh
```

3. Open new windows and show docker container ID

```sh
docker ps -a
```

4. Copy these files `.py` and Testcase dictionary `.txt` to the master container of Hadoop

```sh
docker cp /path/to/files Container_ID:/root
```

5. Switch to original terminal and create a directory in master container

```sh
hdfs dfs -mkdir -p /user/root/input 
```

6. Upload the file to HDFS 

```sh
hdfs dfs -put /root/wc_data1.txt /user/root/input
```

7. Confirm whether the file was successfully uploaded

```sh
hdfs dfs -ls /user/root/input
```

8. Execute mapper and reduce in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
    -files /root/Mapper.py,/root/Reducer.py \
    -input /user/root/input/word_count_data.txt \
    -output /user/root/output \
    -mapper "python Mapper.py" \
    -reducer "python Reducer.py" 
```

9. Check the output results

```sh
$HADOOP_HOME/bin/hdfs dfs -cat /user/root/output/part-00000 
```

10. If you want to execute Step8 again, please use the command to delete the output log

```sh
hdfs dfs -rm -r /user/root/output
```

### Frameworks Used

- [Apache Hadoop](https://hadoop.apache.org/)

### Author

611221201@gms.ndhu.edu.tw

Egor Lee