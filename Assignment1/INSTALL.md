# Assignment 1

`Assignment 1` project belongs to the Big Data Systems at National Dong Hwa University. The purpose of this project is to set up and operate a Hadoop cluster to process large datasets and implement core big data algorithms and provides instructions for setting up the cluster, running the project, and understanding its key components


## Contents

- [Getting Started](#Getting-Started)
  - [Requirements](#Requirements)
  - [Installation](#Installation)
- [Directory Structure](#Directory-Structure)
- [Deployment](#Deployment)

### Getting Started

###### Requirements

1. Ubuntu 24.04
2. Hodoop 2.7.2

###### **Installation**

1. Upgrade package

```sh
sudo apt-get update
```

2. Install docker engine

```sh
./install-docker.sh
```

### Directory Structure

```
filetree 
├── Assignment1
│   ├── Activity_Mining_mapper.py
│   ├── Activity_Mining_reducer.py
│   ├── Log
│   │   ├── Activity_Mining.txt
│   │   ├── Map_reduce.txt
│   │   ├── Search.txt
│   │   ├── Sorting.txt
│   │   └── TF_IDF.txt
│   ├── Mapper.py
│   ├── Reducer.py
│   ├── Result
│   │   ├── Activity_Mining
│   │   │   ├── Terminal.png
│   │   │   └── Website.png
│   │   ├── Mapper and Reducer
│   │   │   ├── Terminal.png
│   │   │   └── Website.png
│   │   ├── Search
│   │   │   ├── Terminal.png
│   │   │   └── Website.png
│   │   ├── Sorting
│   │   │   ├── Terminal.png
│   │   │   └── Website.png
│   │   └── TF_IDF
│   │       ├── Terminal.png
│   │       └── Website.png
│   ├── Search_mapper.py
│   ├── Search_reducer.py
│   ├── Sort_mapper.py
│   ├── Sort_reducer.py
│   ├── Testcase
│   │   ├── wc_data1.txt
│   │   └── wc_data2.txt
│   ├── TFIDF_mapper.py
│   └── TFIDF_reducer.py
├── build-image.sh
├── building-hadoop.sh
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
├── install-docker.sh
├── LICENSE
├── README.md
└── start-container.sh
```

### Deployment

1. Pull docker image

```sh
./building-hadoop.sh
```

2. Start hadoop cluster

```sh
./start-hadoop.sh
```

3. Open new terminal and show docker container ID

```sh
docker ps -a
```

4. Copy the .py files and the Testcase dictionary.txt file to the master container in Hadoop

```sh
docker cp /path/to/files Container_ID:/root
```

5. Switch to the original terminal on the Hadoop master, and create an HDFS directory in the master container

```sh
hdfs dfs -mkdir -p /user/root/input 
```

6. Upload the file to HDFS 

```sh
hdfs dfs -put /root/wc_data1.txt /user/root/input
hdfs dfs -put /root/wc_data2.txt /user/root/input
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

10. If you want to execute Step8,Step11,Step12,Step13,Step14 again, please use the command to delete the output log

```sh
hdfs dfs -rm -r /user/root/output
```

11. Execute Sorting in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
    -files /root/Sort_mapper.py,/root/Sort_reducer.py \
    -input /user/root/input/wc_data1.txt \
    -output /user/root/output \
    -mapper "python Sort_mapper.py" \
    -reducer "python Sort_reducer.py"
```

12. Execute Search in Hadoop

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

13. Execute TD-IDF in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
    -files /root/TFIDF_mapper.py,/root/TFIDF_reducer.py \
    -input /user/root/input/wc_data1.txt \
    -input /user/root/input/wc_data2.txt \
    -output /user/root/output \
    -mapper "python3 TFIDF_mapper.py" \
    -reducer "python3 TFIDF_reducer.py"
```

14. Execute Activity_Mining in Hadoop

```sh
$HADOOP_HOME/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -files /root/Activity_Mining_mapper.py,/root/Activity_Mining_reducer.py \
  -input /user/root/input/wc_data1.txt \
  -output /user/root/output \
  -mapper "python3 Activity_Mining_mapper.py" \
  -reducer "python3 Activity_Mining_reducer.py"
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
