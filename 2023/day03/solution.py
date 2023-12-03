import sys
from functools import reduce
from collections import defaultdict

def part1(f):
    rows = []
    for l in f:
        rows.append(l.strip())
    rows.insert(0, '.' * len(rows[0]))
    rows.append('.' * len(rows[0]))

    total = 0
    for i, r in enumerate(rows):
        if i == 0 or i == len(rows)-1:
            continue

        curNum = 0
        adjacent = False
        for j, c in enumerate(r):
            if c.isdigit():
                curNum = curNum*10 + int(c)
                adjacent = adjacent or (not rows[i-1][j].isdigit() and rows[i-1][j] != '.') or (not rows[i+1][j].isdigit() and rows[i+1][j] != '.')
            else:
                if curNum > 0:
                    adjacent = adjacent or (not rows[i-1][j].isdigit() and rows[i-1][j] != '.') or (not rows[i][j].isdigit() and rows[i][j] != '.') or (not rows[i+1][j].isdigit() and rows[i+1][j] != '.')
                    if adjacent:
                        total += curNum
                    curNum = 0
                adjacent = (not rows[i-1][j].isdigit() and rows[i-1][j] != '.') or (not rows[i][j].isdigit() and rows[i][j] != '.') or (not rows[i+1][j].isdigit() and rows[i+1][j] != '.')
        if curNum > 0 and adjacent:
            total += curNum
    return total

def part2(f):
    rows = []
    for l in f:
        rows.append(l.strip())
    rows.insert(0, '.' * len(rows[0]))
    rows.append('.' * len(rows[0]))

    adjacency = defaultdict(list)
    gears = []
    for i, r in enumerate(rows):
        if i == 0 or i == len(rows)-1:
            continue

        curNum = 0
        adjacentTo = []
        for j, c in enumerate(r):
            if c.isdigit():
                if curNum == 0 and j > 0:
                    adjacentTo.extend([(i-1, j-1), (i, j-1), (i+1, j-1)])
                curNum = curNum*10 + int(c)
                adjacentTo.extend([(i-1, j), (i+1, j)])
            else:
                if curNum > 0:
                    adjacentTo.extend([(i-1, j), (i, j), (i+1, j)])
                    for a in adjacentTo:
                        adjacency[a].append(curNum)
                    curNum = 0
                    adjacentTo = []
                if c == '*':
                    gears.append((i, j))
        
        if curNum > 0:
            for a in adjacentTo:
                adjacency[a].append(curNum)
        
        total = 0
        for g in gears:
            if len(adjacency[g]) == 2:
                total += adjacency[g][0] * adjacency[g][1]
    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))