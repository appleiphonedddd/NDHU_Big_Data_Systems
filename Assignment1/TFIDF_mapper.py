import sys
import os
import re
from collections import defaultdict

file_name = os.getenv('mapreduce_map_input_file', 'unknown_file').split('/')[-1]
word_counts = defaultdict(int)
total_words = 0

for line in sys.stdin:
    line = line.strip().lower()
    words = re.findall(r'\b\w+\b', line)

    for word in words:
        word_counts[word] += 1
        total_words += 1

for word, count in word_counts.items():
    tf = count / total_words
    print("{}\t{}\t{}".format(word, file_name, tf))