import sys

SUPPORT_THRESHOLD = 2  

current_combination = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    combination, count = line.split("\t")
    count = int(count)
    
    if combination == current_combination:
        current_count += count
    else:
        if current_combination and current_count >= SUPPORT_THRESHOLD:
            print("{}\t{}".format(current_combination, current_count))
        current_combination = combination
        current_count = count
    if current_combination and current_count >= SUPPORT_THRESHOLD:
        print("{}\t{}".format(current_combination, current_count))
