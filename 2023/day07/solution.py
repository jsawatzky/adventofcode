import sys
from functools import reduce, cmp_to_key
from collections import Counter

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

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
        elif len(h1c) == 5:
            h1s = sorted(h1, key=lambda x: order.index(x))
            h2s = sorted(h2, key=lambda x: order.index(x))
            if order.index(h1s[0]) < order.index(h2s[0]):
                return 1
            elif order.index(h1s[0]) > order.index(h2s[0]):
                return -1
    for i in range(len(h1)):
        if h1[i] == h2[i]:
            continue
        elif order.index(h1[i]) < order.index(h2[i]):
            return 1
        elif order.index(h1[i]) > order.index(h2[i]):
            return -1
    print("Uh oh")

def part1(f):
    # hands = list(sorted(map(lambda h: (h[0], int(h[1])), [l.strip().split() for l in f]), key=cmp_to_key(lambda h1, h2: cmp(h1[0], h2[0]))))
    return reduce(lambda p, x: p + (x[0]+1)*x[1][1], enumerate(sorted(map(lambda h: (h[0], int(h[1])), [l.strip().split() for l in f]), key=cmp_to_key(lambda h1, h2: cmp(h1[0], h2[0])))), 0)

def part2(f):
    return 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))