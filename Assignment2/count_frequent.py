from pyspark import SparkContext
from pyspark.sql import SparkSession
from itertools import combinations

sc = SparkContext("local", "Frequent Itemsets")
spark = SparkSession.builder.appName("Frequent Itemsets").getOrCreate()

threshold = 10

transactions = sc.textFile("/opt/spark/data/purchase.txt")


parsed_transactions = transactions.map(lambda line: set(line.strip().split()[1:]))


def generate_combinations(transaction):
    return list(set([tuple(sorted(combo)) for size in range(1, len(transaction) + 1) for combo in combinations(transaction, size)]))


itemsets = parsed_transactions.flatMap(generate_combinations)
itemset_counts = itemsets.map(lambda itemset: (itemset, 1)).reduceByKey(lambda a, b: a + b)


frequent_itemsets = itemset_counts.filter(lambda x: x[1] >= threshold)


sorted_frequent_itemsets = frequent_itemsets.sortBy(lambda x: x[1], ascending=False)


sorted_frequent_itemsets.map(lambda x: f"Itemset: {', '.join(x[0])}, Count: {x[1]}").saveAsTextFile("/opt/spark/data/sorted_frequent_data")

print("Sorted frequent itemsets have been saved to /opt/spark/data/sorted_frequent_data")