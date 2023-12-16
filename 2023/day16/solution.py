import sys
from functools import reduce

def process(grid, startBeams):
    energized = set()
    beams = startBeams
    while beams:
        newBeams = []
        for b in beams:
            if b[0][0] < 0 or b[0][0] >= len(grid):
                continue
            if b[0][1] < 0 or b[0][1] >= len(grid[0]):
                continue
            if b in energized:
                continue
            energized.add(b)
            tile = grid[b[0][0]][b[0][1]]
            if tile in '/\\':
                if b[1][1] != 0:
                    newDir = b[1][1]*(-1 if tile == '/' else 1)
                    newBeams.append(((b[0][0]+newDir, b[0][1]), (newDir, 0)))
                else:
                    newDir = b[1][0]*(-1 if tile == '/' else 1)
                    newBeams.append(((b[0][0], b[0][1]+newDir), (0, newDir)))
            elif tile == '-':
                if b[1][0] != 0:
                    newBeams.append(((b[0][0], b[0][1]+1), (0, 1)))
                    newBeams.append(((b[0][0], b[0][1]-1), (0, -1)))
                else:
                    newBeams.append(((b[0][0]+b[1][0], b[0][1]+b[1][1]), b[1]))
            elif tile == '|':
                if b[1][1] != 0:
                    newBeams.append(((b[0][0]+1, b[0][1]), (1, 0)))
                    newBeams.append(((b[0][0]-1, b[0][1]), (-1, 0)))
                else:
                    newBeams.append(((b[0][0]+b[1][0], b[0][1]+b[1][1]), b[1]))
            else:
                newBeams.append(((b[0][0]+b[1][0], b[0][1]+b[1][1]), b[1]))
        beams = newBeams

    energized = set(map(lambda x: x[0], energized))
    return len(energized)

def part1(f):
    grid = [l.strip() for l in f if l.strip()]
    return process(grid, [((0, 0), (0, 1))])

def part2(f):
    grid = [l.strip() for l in f if l.strip()]
    allEnergized = []
    for i in range(len(grid)):
        allEnergized.append(process(grid, [((i, 0), (0, 1))]))
        allEnergized.append(process(grid, [((i, len(grid[0])-1), (0, -1))]))
    for i in range(len(grid[0])):
        allEnergized.append(process(grid, [((0, i), (1, 0))]))
        allEnergized.append(process(grid, [((len(grid)-1, 0), (-1, 0))]))
    return max(allEnergized)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))