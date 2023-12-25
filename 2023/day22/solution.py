import sys
from functools import reduce, cache
from collections import defaultdict

def part1(f):
    blocks = [tuple(map(lambda x: tuple(map(int, x.split(','))), l.strip().split('~'))) for l in f if l.strip()]
    blocks.sort(key=lambda x: min(x, key=lambda y: y[2])[2])
    minZs = [[0 for _ in range(10)] for _ in range(10)]
    topBlocks = [[0 for _ in range(10)] for _ in range(10)]
    supportedBy = defaultdict(set)
    supports = defaultdict(set)
    for n, b in enumerate(blocks, start=1):
        minZ = 0
        for i in range(b[0][0], b[1][0]+1):
            for j in range(b[0][1], b[1][1]+1):
                if minZ < minZs[i][j]:
                    minZ = minZs[i][j]
                    supportedBy[n] = {topBlocks[i][j]}
                elif minZ == minZs[i][j]:
                    supportedBy[n].add(topBlocks[i][j])
        for s in supportedBy[n]:
            supports[s].add(n)
        height = b[1][2]-b[0][2]
        for i in range(b[0][0], b[1][0]+1):
            for j in range(b[0][1], b[1][1]+1):
                minZs[i][j] = minZ+1+height
                topBlocks[i][j] = n
    return len(list(filter(lambda x: all(map(lambda y: len(supportedBy[y]) != 1, supports[x])), range(1, len(blocks)+1))))

supports = None
supportedBy = None

def process(gone):
    next = gone.copy()
    for g in gone:
        for s in supports[g]:
            if s in gone:
                continue
            if len(supportedBy[s] - gone) == 0: next.add(s)
    if next == gone: return len(gone) - 1
    return process(next)

def part2(f):
    global supports, supportedBy
    blocks = [tuple(map(lambda x: tuple(map(int, x.split(','))), l.strip().split('~'))) for l in f if l.strip()]
    blocks.sort(key=lambda x: min(x, key=lambda y: y[2])[2])
    minZs = [[0 for _ in range(10)] for _ in range(10)]
    topBlocks = [[0 for _ in range(10)] for _ in range(10)]
    supportedBy = defaultdict(set)
    supports = defaultdict(set)
    for n, b in enumerate(blocks, start=1):
        minZ = 0
        for i in range(b[0][0], b[1][0]+1):
            for j in range(b[0][1], b[1][1]+1):
                if minZ < minZs[i][j]:
                    minZ = minZs[i][j]
                    supportedBy[n] = {topBlocks[i][j]}
                elif minZ == minZs[i][j]:
                    supportedBy[n].add(topBlocks[i][j])
        if len(supportedBy[n]) == 0: supportedBy[n].add(0)
        for s in supportedBy[n]:
            supports[s].add(n)
        height = b[1][2]-b[0][2]
        for i in range(b[0][0], b[1][0]+1):
            for j in range(b[0][1], b[1][1]+1):
                minZs[i][j] = minZ+1+height
                topBlocks[i][j] = n
    
    return sum(map(lambda x: process({x}), range(1, len(blocks)+1)))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))