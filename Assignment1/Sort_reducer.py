import sys

word_count = {}
for line in sys.stdin:
    line = line.strip()
    parts = line.split("\t", 1)
    if len(parts) < 2:
        continue

    word, count = parts

    try:
        count = int(count)
    except ValueError:
        continue

    if word in word_count:
        word_count[word] += count
    else:
        word_count[word] = count


for word in sorted(word_count):
    print("{}\t{}".format(word, word_count[word]))