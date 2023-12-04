import sys
from functools import reduce
from collections import Counter

def part1(f):
    return sum(map(lambda s: 2**(s-1) if s > 0 else 0, list(map(lambda t: len([a for a in t[1] if a in t[0]]), list(map(lambda x: list(map(lambda y: list(map(int, [z for z in y.split() if z])), x)), [c.strip().split(": ")[1].split(" | ") for c in f]))))))

def part2(f):
    return sum(reduce(lambda c, b: (c.update({b[0]: 1}), c.update({b[0]+j: c[b[0]] for j in range(1, b[1]+1)}), c)[2], enumerate(list(map(lambda t: len([a for a in t[1] if a in t[0]]), list(map(lambda x: list(map(lambda y: list(map(int, [z for z in y.split() if z])), x)), [c.strip().split(": ")[1].split(" | ") for c in f]))))), Counter()).values())


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))