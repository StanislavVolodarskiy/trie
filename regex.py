import re

with open('patterns.txt') as f:
    patterns = re.compile('|'.join(re.escape(line.replace('\n','')) for line in f))

with open('corpus.txt') as f:
    for line in f:
        if patterns.search(line) is not None:
            print(line, end='')
