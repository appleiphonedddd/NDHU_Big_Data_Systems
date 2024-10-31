hdfs dfs -mkdir -p /user/root/input
hdfs dfs -put /root/word_count_data.txt /user/root/input
hdfs dfs -ls /user/root/input