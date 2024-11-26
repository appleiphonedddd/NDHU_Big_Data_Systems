from pyspark import SparkContext
from pyspark.sql import SparkSession
import jieba

sc = SparkContext("local", "Inverted Index")
spark = SparkSession.builder.appName("Inverted Index").getOrCreate()

documents = sc.textFile("/opt/spark/data/article.txt")


def parse_document(line):
    parts = line.split(" ", 1) 
    doc_id = parts[0]  
    text = parts[1] if len(parts) > 1 else ""  
    words = jieba.cut(text)  
    return doc_id, list(words)  
parsed_documents = documents.map(parse_document)  


def word_count(doc):
    doc_id, words = doc
    return [(word, (doc_id, 1)) for word in words]  

word_counts = parsed_documents.flatMap(word_count)


def combine_counts(values):
    doc_counts = {}
    for doc_id, count in values:
        doc_counts[doc_id] = doc_counts.get(doc_id, 0) + count
    return list(doc_counts.items())

inverted_index = word_counts.groupByKey().mapValues(combine_counts)


def format_output(index):
    word, values = index
    total = sum(count for _, count in values)  
    return f"{word}: {values}, Total: {total}"

formatted_results = inverted_index.map(format_output)


formatted_results.saveAsTextFile("/opt/spark/data/invert_data")
print("Results saved to /opt/spark/data/invert_data")
