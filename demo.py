import pprint


def make_trie(iterable):
    root = {}
    for s in iterable:
        node = root
        for c in s:
            node = node.setdefault(c, {})
        node[''] = None
    return root


pprint.pprint(make_trie(('then', 'than', 'thing', 'those')))
