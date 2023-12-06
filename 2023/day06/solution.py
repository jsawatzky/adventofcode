import sys
from functools import reduce

def part1(f):
    return reduce(lambda t, y: t*y, map(lambda r: len(list(filter(lambda s: s[0]*s[1] > r[1], [(i, r[0]-i) for i in range(1, r[0])]))), zip([int(x) for x in f.readline().strip().split()[1:] if x], [int(x) for x in f.readline().strip().split()[1:] if x])))

def part2(f):
    return list(map(lambda r: len(list(filter(lambda s: s[0]*s[1] > r[1], [(i, r[0]-i) for i in range(1, r[0])]))), [(int(f.readline().strip().removeprefix("Time:").replace(" ", "")), int(f.readline().strip().removeprefix("Distance:").replace(" ", "")))]))[0]

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))