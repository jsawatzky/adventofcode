import sys
from functools import reduce
from collections import defaultdict

def dfs(pos, path, grid):
    if pos[0] == len(grid)-1: return len(path)
    path.append(pos)
    branches = []
    while True:
        branches = []
        opts = [(pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0], pos[1]+1)]
        if grid[pos[0]][pos[1]] == '>':
            opts = [(pos[0], pos[1]+1)]
        elif grid[pos[0]][pos[1]] == '<':
            opts = [(pos[0], pos[1]-1)]
        elif grid[pos[0]][pos[1]] == '^':
            opts = [(pos[0]-1, pos[1])]
        elif grid[pos[0]][pos[1]] == 'v':
            opts = [(pos[0]+1, pos[1])]
        for p in opts:
            if p[0] < 0 or p[0] >= len(grid) or p[1] < 0 or p[1] >= len(grid[p[0]]):
                continue
            if p in path: continue
            if grid[p[0]][p[1]] == '#': continue
            branches.append(p)
        if len(branches) > 1:
            break
        if len(branches) == 0:
            return -1
        pos = branches[0]
        if pos[0] == len(grid)-1: return len(path)
        path.append(branches[0])
    return max(map(lambda x: dfs(x, path.copy(), grid), branches))


def part1(f):
    grid = [list(l.strip()) for l in f if l.strip()]
    start = (0, grid[0].index('.'))
    return dfs(start, [], grid)

def getPaths(pos, prev, paths, visited, grid):
    if pos in visited: return paths, visited
    visited.add(pos)
    start = pos
    branches = []
    path = [pos]
    while True:
        branches = []
        opts = [(pos[0]-1, pos[1]), (pos[0], pos[1]-1), (pos[0]+1, pos[1]), (pos[0], pos[1]+1)]
        for p in opts:
            if p[0] < 0 or p[0] >= len(grid) or p[1] < 0 or p[1] >= len(grid[p[0]]):
                continue
            if p in path or p == prev: continue
            if grid[p[0]][p[1]] == '#': continue
            branches.append(p)
        if len(branches) > 1:
            break
        if len(branches) == 0:
            # dead end
            paths[start][pos] = max(paths[start][pos], len(path))
            return paths, visited
        pos = branches[0]
        path.append(branches[0])
    paths[start][pos] = max(paths[start][pos], len(path))
    for b in branches:
        bPaths, bVisted = getPaths(b, pos, paths, visited, grid)
        paths.update(bPaths)
        visited = visited.union(bVisted)
    return paths, visited

def dfs2(pos, paths, acc, visited, target):
    if pos == target: return acc
    maxD = -1
    for p, l in paths[pos].items():
        if p in visited: continue
        if p == target:
            maxD = max(maxD, acc+l)
            continue
        v = visited.copy()
        v.add(p)
        opts = [(p[0]-1, p[1]), (p[0], p[1]-1), (p[0]+1, p[1]), (p[0], p[1]+1)]
        for p2 in opts:
            maxD = max(maxD, dfs2(p2, paths, acc+l, v.copy(), target))
    return maxD

def part2(f):
    grid = [list(l.strip()) for l in f if l.strip()]
    start = (0, 1)
    target = (len(grid)-1, len(grid[0])-2)
    paths, _ = getPaths(start, None, defaultdict(lambda: defaultdict(int)), set(), grid)
    return dfs2(start, paths, 0, set(), target)-1

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))