import sys
from functools import reduce

def minRock(i, rocks):
    less = list(filter(lambda x: x < i, rocks))
    if len(less) == 0:
        return -1
    else:
        return len(less) - 1

def part1(f):
    grid = [l.strip() for l in f]
    colRocks = [[i for i in range(len(grid)) if grid[i][j] == '#'] for j in range(len(grid[0]))]

    boulders = [0] * len(grid)
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if c == 'O':
                n = minRock(i, colRocks[j])
                if n < 0:
                    colRocks[j].insert(0, 0)
                    boulders[0] += len(grid)
                else:
                    colRocks[j][n] += 1
                    boulders[colRocks[j][n]] += len(grid) - colRocks[j][n]

    return sum(boulders)

def rotate(g):
    return ["".join(l) for l in zip(*map(reversed, g))]

def part2(f):
    grid = ["".join(c) for c in zip(*[l.strip() for l in f])]
    states = [grid]
    start = 0
    n = 1
    while True:
        for _ in range(4):
            tilted = []
            for c in grid:
                ct = []
                for g in c.split('#'):
                    if g:
                        ct.append("".join(["O"] * g.count("O") + ["."] * g.count(".")))
                    else:
                        ct.append("")
                tilted.append('#'.join(ct))
            grid = rotate(tilted)
        if grid in states:
            start = states.index(grid)
            break
        states.append(grid)
        n += 1

    final = states[(1000000000 - start) % (n - start) + start]

    return sum(sum(i * (c == 'O') for i, c in enumerate(c[::-1], 1)) for c in final)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))