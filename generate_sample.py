import string
import random

# В файле порядка 50'000 уникальных искомых подстрок
# В каждом файле порядка 700'000 уникальных строк
# средняя длина строк в файлах, где проводится поиск - от 18 символов до 500, на вскидку.
# cредняя длина искомых строк (подстрок) порядка 65-72 символов. Доля 

# Пример искомых подстрок списка linesA:
# sjfrhfereirevb
# fvbdjvejeirerer
# wiuewuewifwwcb
# bvdfkbdvbevkbeee
# 
# Пример строк списка listB, в которых производится поиск:
# djcwjbcbcwiebcwebcerbuevitbbtvietbvndwnecwoewrnen
# ewwfsjfrhfereirevbewdownwonewrnoenrviernveonvoenrveornveor
# weacewewijernceirvetvnenrvernvernveoitnvetnvenrvoenrverv
# euccdwiuewuewifwwcbewcwcwwirbeiwrorjoeroehroverivheiveveeverv


r = random.Random(42)


def random_string(n):
    return ''.join(r.choice(string.ascii_lowercase) for _ in range(n))


def random_pattern():
    return random_string(r.randrange(10, 21))


def random_line(patterns):
    n = r.randrange(22, 101)
    if r.random() < 1e-3:
        p = r.choice(patterns)
        m = n - len(p)
        m1 = r.randrange(0, m + 1)
        m2 = m - m1
        return ''.join((random_string(m1), p, random_string(m2)))
    return random_string(n)


n_patterns = 50000
n_lines = 20000

patterns = tuple(random_pattern() for _ in range(n_patterns))

with open('patterns.txt', 'w') as f:
    for p in patterns:
        print(p, file=f)

with open('corpus.txt', 'w') as f:
    for _ in range(n_lines):
        print(random_line(patterns), file=f)
