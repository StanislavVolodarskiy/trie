
with open('patterns.txt') as f:
    patterns = tuple(line.replace('\n','') for line in f)

with open('corpus.txt') as f:
    for line in f:
        for p in patterns:
            if p in line:
                print(line, end='')
                break
