import sys
from functools import reduce, cmp_to_key
from collections import Counter

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
order2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def cmp(h1, h2):
    h1c = Counter(h1)
    h2c = Counter(h2)
    if len(h1c) > len(h2c):
        return -1
    elif len(h1c) < len(h2c):
        return 1
    elif len(h1c) == len(h2c):
        if max(h1c.values()) > max(h2c.values()):
            return 1
        elif max(h1c.values()) < max(h2c.values()):
            return -1
    for i in range(len(h1)):
        if h1[i] == h2[i]:
            continue
        elif order.index(h1[i]) < order.index(h2[i]):
            return 1
        elif order.index(h1[i]) > order.index(h2[i]):
            return -1
    print("Uh oh")

def cmp2(h1, h2):
    h1c = Counter(h1)
    if len(h1c) > 1:
        jokers = h1c['J']
        del h1c['J']
        h1c[h1c.most_common(1)[0][0]] += jokers
    h2c = Counter(h2)
    if len(h2c) > 1:
        jokers = h2c['J']
        del h2c['J']
        h2c[h2c.most_common(1)[0][0]] += jokers
    if len(h1c) > len(h2c):
        return -1
    elif len(h1c) < len(h2c):
        return 1
    elif len(h1c) == len(h2c):
        if max(h1c.values()) > max(h2c.values()):
            return 1
        elif max(h1c.values()) < max(h2c.values()):
            return -1
    for i in range(len(h1)):
        if h1[i] == h2[i]:
            continue
        elif order2.index(h1[i]) < order2.index(h2[i]):
            return 1
        elif order2.index(h1[i]) > order2.index(h2[i]):
            return -1
    print("Uh oh")

def part1(f):
    return reduce(lambda p, x: p + (x[0]+1)*x[1][1], enumerate(sorted(map(lambda h: (h[0], int(h[1])), [l.strip().split() for l in f]), key=cmp_to_key(lambda h1, h2: cmp(h1[0], h2[0])))), 0)

def part2(f):
    return reduce(lambda p, x: p + (x[0]+1)*x[1][1], enumerate(sorted(map(lambda h: (h[0], int(h[1])), [l.strip().split() for l in f]), key=cmp_to_key(lambda h1, h2: cmp2(h1[0], h2[0])))), 0)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))