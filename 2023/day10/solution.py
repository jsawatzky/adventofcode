import sys
from functools import reduce

def getLoop(grid):
    curNode = (-1, -1)
    for i, r in enumerate(grid):
        if 'S' in r:
            curNode = (i, r.index('S'))
            break
    pipe = [curNode]
    fromDir = ''
    if curNode[0] > 0 and grid[curNode[0]-1][curNode[1]] in '|7F':
        curNode = (curNode[0]-1, curNode[1])
        fromDir = 'S'
    elif curNode[1] < len(grid[curNode[0]])-1 and grid[curNode[0]][curNode[1]+1] in '-J7':
        curNode = (curNode[0], curNode[1]+1)
        fromDir = 'W'
    elif curNode[0] < len(grid)-1 and grid[curNode[0]+1][curNode[1]] in '|LJ':
        curNode = (curNode[0]+1, curNode[1])
        fromDir = 'N'
    elif curNode[1] > 0 and grid[curNode[0]][curNode[1]-1] in '-LF':
        curNode = (curNode[0], curNode[1]-1)
        fromDir = 'E'

    while grid[curNode[0]][curNode[1]] != 'S':
        pipe.append(curNode)
        node = grid[curNode[0]][curNode[1]]
        if fromDir == 'S':
            if node == '|':
                curNode = (curNode[0]-1, curNode[1])
            elif node == '7':
                curNode = (curNode[0], curNode[1]-1)
                fromDir = 'E'
            elif node == 'F':
                curNode = (curNode[0], curNode[1]+1)
                fromDir = 'W'
        elif fromDir == 'W':
            if node == '-':
                curNode = (curNode[0], curNode[1]+1)
            elif node == 'J':
                curNode = (curNode[0]-1, curNode[1])
                fromDir = 'S'
            elif node == '7':
                curNode = (curNode[0]+1, curNode[1])
                fromDir = 'N'
        elif fromDir == 'N':
            if node == '|':
                curNode = (curNode[0]+1, curNode[1])
            elif node == 'L':
                curNode = (curNode[0], curNode[1]+1)
                fromDir = 'W'
            elif node == 'J':
                curNode = (curNode[0], curNode[1]-1)
                fromDir = 'E'
        elif fromDir == 'E':
            if node == '-':
                curNode = (curNode[0], curNode[1]-1)
            elif node == 'L':
                curNode = (curNode[0]-1, curNode[1])
                fromDir = 'S'
            elif node == 'F':
                curNode = (curNode[0]+1, curNode[1])
                fromDir = 'N'
    
    return pipe

def part1(f):
    grid = [x.strip() for x in f if x.strip()]
    pipe = getLoop(grid)
    return len(pipe) // 2

def part2(f):
    grid = [x.strip() for x in f if x.strip()]
    pipe = getLoop(grid)
    contained = []
    for i, r in enumerate(grid):
        crossingsAbove = 0
        crossingsBelow = 0
        for j, n in enumerate(r):
            if (i, j) in pipe:
                if n == '|':
                    crossingsAbove += 1
                    crossingsBelow += 1
                elif n == '-':
                    pass
                elif n in 'LJ':
                    crossingsAbove += 1
                elif n in '7F':
                    crossingsBelow += 1
                # Pray that the actual shape of 'S' doesn't matter
                continue
            if crossingsAbove%2 == 1 and crossingsBelow%2 == 1:
                contained.append((i, j))
    return len(contained)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))