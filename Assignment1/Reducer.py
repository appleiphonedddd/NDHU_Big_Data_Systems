import sys
wordcount = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    try:
        wordcount[word] = wordcount[word] + count
    except:
        wordcount[word] = count
for word in wordcount.keys():
    print("%s\t%s" % (word, wordcount[word]))