def make_trie(iterable):
    root = {}
    for s in iterable:
        node = root
        for c in s:
            node = node.setdefault(c, {})
        node[''] = None
    return root


def contains(text, trie):
    if '' in trie:
        return True

    nodes = []
    for c in text:
        nodes.append(trie)
        i = 0
        while i < len(nodes):
            node = nodes[i]
            if c in node:
                node = node[c]
                nodes[i] = node
                if '' in node:
                    return True
                i += 1
            else:
                nodes[i] = nodes[-1]
                nodes.pop()
    return False


with open('patterns.txt') as f:
    trie = make_trie(line.replace('\n', '') for line in f)

with open('corpus.txt') as f:
    for line in f:
        line = line.replace('\n','')
        if contains(line, trie):
            print(line)
