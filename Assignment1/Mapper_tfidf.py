import sys
import re
from collections import defaultdict

def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

for line in sys.stdin:
    filename, text = line.strip().split('\t', 1)
    word_counts = defaultdict(int)
    words = tokenize(text)

    for word in words:
        word_counts[word] += 1

    for word, count in word_counts.items():
        print(f"{word}\t{filename}\t{count}")