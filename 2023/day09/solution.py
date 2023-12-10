import sys
from functools import reduce

def part1(f):
    rows = [list(map(int, l.strip().split())) for l in f]
    total = 0
    for r in rows:
        lastDigits = []
        while len(set(r)) != 1:
            lastDigits.append(r[-1])
            r = [r[i] - r[i-1] for i in range(1, len(r))]
        total += reduce(lambda c, d: d + c, reversed(lastDigits), r[0])
    return total

def part2(f):
    rows = [list(map(int, l.strip().split())) for l in f]
    total = 0
    for r in rows:
        firstDigits = []
        while len(set(r)) != 1:
            firstDigits.append(r[0])
            r = [r[i] - r[i-1] for i in range(1, len(r))]
        total += reduce(lambda c, d: d - c, reversed(firstDigits), r[0])
    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))