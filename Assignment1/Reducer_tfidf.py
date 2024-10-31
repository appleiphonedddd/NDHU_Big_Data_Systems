import sys
from math import log
from collections import defaultdict

total_docs = 10
current_word = None
doc_counts = defaultdict(int)
word_doc_counts = defaultdict(lambda: defaultdict(int))

for line in sys.stdin:
    line = line.strip()
    word, filename, count = line.split('\t')
    count = int(count)

    word_doc_counts[word][filename] = count
    doc_counts[word] += 1

for word, docs in word_doc_counts.items():
    idf = log(total_docs / (1 + doc_counts[word]))
    for filename, tf in docs.items():
        tf_idf = tf * idf

        print(f"{word}\t{filename}\t{tf_idf:.6f}")