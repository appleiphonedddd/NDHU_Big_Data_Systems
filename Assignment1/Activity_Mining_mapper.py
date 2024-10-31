import sys
from itertools import combinations

MIN_LENGTH = 2  

for line in sys.stdin:
    line = line.strip().lower()  
    words = line.split() 

    for length in range(MIN_LENGTH, len(words) + 1):
        for subset in combinations(words, length):
            print("{}\t1".format("->".join(subset)))