import sys
from functools import reduce
from operator import itemgetter

def part1(f):
    steps = list(map(lambda x: (x[0], int(x[1]), x[2].strip('()#')), [l.strip().split() for l in f if l.strip]))
    pos = (0, 0)
    grid = {}
    for s in steps:
        dir, count, color = s
        update = None
        if dir == 'U':
            update = lambda x: (x[0], x[1]+1)
        elif dir == 'D':
            update = lambda x: (x[0], x[1]-1)
        elif dir == 'L':
            update = lambda x: (x[0]-1, x[1])
        else:
            update = lambda x: (x[0]+1, x[1])
        for _ in range(count):
            pos = update(pos)
            grid[pos] = color

    xs = list(map(itemgetter(0), grid.keys()))
    minX, maxX = min(xs)-1, max(xs)+1
    ys = list(map(itemgetter(1), grid.keys()))
    minY, maxY = min(ys)-1, max(ys)+1

    frontier = set()
    frontier.add((minX, minY))
    outside = []

    while len(frontier) > 0:
        p = frontier.pop()
        if p in grid:
            continue
        outside.append(p)
        for p2 in [(p[0]-1, p[1]),(p[0]+1, p[1]),(p[0], p[1]+1),(p[0], p[1]-1)]:
            if p2[0] < minX or p2[0] > maxX or p2[1] < minY or p2[1] > maxY:
                continue
            elif p2 in outside:
                continue
            frontier.add(p2)

    totalSize = (maxX-minX+1)*(maxY-minY+1)

    return totalSize - len(outside)

def part2(f):
    steps = list(map(lambda x: (int(x[-1]), int(x[:5], 16)), [l.strip().split()[2].strip('()#') for l in f if l.strip]))
    area = 0
    path = 0
    pos = (0, 0)
    for s in steps:
        dir, count = s
        newPos = None
        if dir == 3 or dir == 'U':
            newPos = (pos[0], pos[1]-count)
        elif dir == 1 or dir == 'D':
            newPos = (pos[0], pos[1]+count)
        elif dir == 2 or dir == 'L':
            newPos = (pos[0]-count, pos[1])
        else:
            newPos = (pos[0]+count, pos[1])
        
        area += pos[0]*newPos[1] - pos[1]*newPos[0]
        path += count
        pos = newPos

    return area//2 + path//2 + 1

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))