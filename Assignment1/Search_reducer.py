import sys
from collections import defaultdict
import ast
file_matches = defaultdict(list)

for line in sys.stdin:
    filename, content, positions = line.strip().split("\t", 2)
    positions = ast.literal_eval(positions) 

    file_matches[filename].append((content, positions))

for current_file, matches in file_matches.items():
    print("{}\t{}".format(current_file, matches))