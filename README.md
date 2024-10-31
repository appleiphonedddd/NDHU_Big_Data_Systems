# NDHU_Big_Data_Systems_Fall

`NDHU_Big_Data_Systems_Fall` project belongs to the Big Data Systems at National Dong Hwa University. The purpose of this project is to set up and operate a Hadoop cluster to process large datasets and implement core big data algorithms and provides instructions for setting up the cluster, running the project, and understanding its key components


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

2. Install docker engine

```sh
./Install_docker.sh
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
│       ├── wc_data1.txt
│       └── wc_data2.txt
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
├── LICENSE
├── README.md
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
    -input /user/root/input/wc_data1.txt \
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