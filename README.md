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

###### **Installation**

1. Upgrade package

```sh
sudo apt-get update
```

2. Install Conda

```sh

chmod 777 Install_miniconda.sh
./Install_miniconda.sh
```

### Directory Structure

```
filetree 
├── Assignment1
│   ├── testcase
│   │   └── wc_data.txt
│   └── word_count.ipynb
├── Install_miniconda.sh
├── LICENSE
└── README.md
```

### Deployment

1. Building environment in conda

```sh
conda create --name BigData python=3.9
```

2. Active environment

```sh
conda activate BigData
```

### Frameworks Used

- [Apache Hadoop](https://hadoop.apache.org/)

### Author

611221201@gms.ndhu.edu.tw

Egor Lee