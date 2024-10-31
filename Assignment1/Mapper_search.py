import sys
import re

if len(sys.argv) < 2:
    print("Usage: python3 mapper_search.py <pattern>")
    sys.exit(1)

pattern = sys.argv[1]
compiled_pattern = re.compile(pattern)

for line_num, line in enumerate(sys.stdin, 1):
    line = line.strip()

    if compiled_pattern.search(line):
        print(f'{sys.stdin.name}\t{line_num}')
