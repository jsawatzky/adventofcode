import sys
from functools import reduce
from operator import itemgetter

def part1(f):
    universe = [l.strip() for l in f]
    emptyCols = [i for i, s in [(j, set(map(itemgetter(j), universe))) for j in range(len(universe[0]))] if len(s) == 1]
    emptyRows = [i for i, s in enumerate(map(set, universe)) if len(s) == 1]
    offset = 0
    for j in emptyCols:
        for i, r in enumerate(universe):
            universe[i] = r[:j+offset] + '.' + r[j+offset:]
        offset += 1
    offset = 0
    for i in emptyRows:
        universe.insert(i+offset, '.'*len(universe[0]))
        offset += 1
            
    galaxies = [(i, j) for i, r in enumerate(universe) for j, c in enumerate(r) if c == '#']

    dists = []
    for i, p1 in enumerate(galaxies):
        if i == len(galaxies)-1:
            continue
        for j, p2 in enumerate(galaxies[i+1:]):
            dists.append(abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))
    return sum(dists)

def part2(f):
    universe = [l.strip() for l in f]
    emptyCols = [i for i, s in [(j, set(map(itemgetter(j), universe))) for j in range(len(universe[0]))] if len(s) == 1]
    emptyRows = [i for i, s in enumerate(map(set, universe)) if len(s) == 1]
            
    galaxies = [(i, j) for i, r in enumerate(universe) for j, c in enumerate(r) if c == '#']

    dists = []
    for i, p1 in enumerate(galaxies):
        if i == len(galaxies)-1:
            continue
        for j, p2 in enumerate(galaxies[i+1:]):
            rows = [p1[0], p2[0]]
            cols = [p1[1], p2[1]]
            xDist = abs(p1[0]-p2[0]) + 999999*len(list(filter(lambda c: min(cols) < c and max(cols) > c, emptyCols)))
            yDist = abs(p1[1]-p2[1]) + 999999*len(list(filter(lambda r: min(rows) < r and max(rows) > r, emptyRows)))
            dists.append(xDist + yDist)
    return sum(dists)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))