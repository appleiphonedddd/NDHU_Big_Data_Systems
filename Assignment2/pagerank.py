from pyspark import SparkContext, SparkConf


conf = SparkConf().setAppName("PageRank")
sc = SparkContext(conf=conf)


data_path = "/opt/spark/data/PR_data.txt" 
lines = sc.textFile(data_path)


links = lines.map(lambda line: line.split()).groupByKey().mapValues(list)
ranks = links.mapValues(lambda _: 1.0)


iterations = 10
for _ in range(iterations):
    contributions = links.join(ranks).flatMap(
        lambda url_neighbors: [
            (neighbor, url_neighbors[1][1] / len(url_neighbors[1][0]))
            for neighbor in url_neighbors[1][0]
        ]
    )
    ranks = contributions.reduceByKey(lambda x, y: x + y).mapValues(lambda rank: 0.15 + 0.85 * rank)


output_path = "/opt/spark/data/output_ranks.txt"
with open(output_path, "w") as f:
    for node, rank in ranks.collect():
        f.write(f"Node: {node}, Rank: {rank}")

print(f"Results saved to {output_path}")

sc.stop()