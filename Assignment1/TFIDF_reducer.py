import sys
import math

from collections import defaultdict

tf_values = defaultdict(list)
df_counts = defaultdict(int)
documents = set()

for line in sys.stdin:
    word, file_name, tf = line.strip().split("\t")
    tf = float(tf)
    tf_values[word].append((file_name, tf))
    df_counts[word] += 1
    documents.add(file_name)

total_docs = len(documents)
print("DEBUG: Total documents =", total_docs)

for word, file_tfs in tf_values.items():
    print("DEBUG: DF count for word '{}': {}".format(word, df_counts[word]))  
    idf = math.log(total_docs / df_counts[word]) if df_counts[word] > 0 else 0

for file_name, tf in file_tfs:
    tf_idf = tf * idf
    print("{}\t{}\t{:.6f}".format(word, file_name, tf_idf))