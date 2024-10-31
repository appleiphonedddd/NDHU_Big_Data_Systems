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
│   ├── Reducer.py
│   ├── Result
│   │   └── Mapper and reduce.png
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
├── docker-cmd.sh
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

3. Open new terminal and show docker container ID

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

9. Execute Sorting in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
    -files /root/Sort_mapper.py,/root/Sort_reducer.py \
    -input /user/root/input/wc_data1.txt \
    -output /user/root/output \
    -mapper "python Sort_mapper.py" \
    -reducer "python Sort_reducer.py"
```

10. Execute Search in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
    -files /root/Search_mapper.py,/root/Search_reducer.py \
    -input /user/root/input/wc_data1.txt \
    -input /user/root/input/wc_data2.txt \
    -output /user/root/output \
    -mapper "python Search_mapper.py" \
    -reducer "python Search_reducer.py" \
    -cmdenv SEARCH_WORD="beer"
```

10. Execute TD-IDF in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
    -files /root/TFIDF_mapper.py,/root/TFIDF_reducer.py \
    -input /user/root/input/wc_data1.txt \
    -input /user/root/input/wc_data2.txt \
    -output /user/root/output \
    -mapper "python3 TFIDF_mapper.py" \
    -reducer "python3 TFIDF_reducer.py"
```

11. Execute Activity_Mining in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -files /root/Activity_Mining_mapper.py,/root/Activity_Mining_reducer.py \
  -input /user/root/input/wc_data1.txt \
  -output /user/root/output \
  -mapper "python3 Activity_Mining_mapper.py" \
  -reducer "python3 Activity_Mining_reducer.py"
```

12. Check the output results

```sh
$HADOOP_HOME/bin/hdfs dfs -cat /user/root/output/part-00000
```

13. If you want to execute Step8 again, please use the command to delete the output log

```sh
hdfs dfs -rm -r /user/root/output
```

14. If you want to clear all container in Linux

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
http://host_IP:8088/
```

### Frameworks Used

- [Apache Hadoop](https://hadoop.apache.org/)

### Author

611221201@gms.ndhu.edu.tw

Egor Lee