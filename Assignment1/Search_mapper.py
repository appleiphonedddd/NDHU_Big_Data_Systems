import sys
import os

search_word = os.getenv('SEARCH_WORD', 'default_word')

for line in sys.stdin:

    filepath = os.environ.get('map_input_file', 'unknown_file')
    filename = os.path.basename(filepath)
    line = line.strip()
    line_num = 0  

    positions = []
    start = 0
    while True:
        start = line.find(search_word, start)
        if start == -1:
            break
        positions.append(start)
        start += len(search_word)
    if positions:
        print("{}_line_{}\t{}\t{}".format(filename, line_num, line, positions))