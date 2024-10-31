import sys

for line in sys.stdin:

    line = line.strip().lower()
    words = line.split()
    
    # give every word 1 count    
    for word in words:
        print(f'{word}\t1')