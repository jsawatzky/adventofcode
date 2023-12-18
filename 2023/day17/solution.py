import sys
from functools import reduce
from collections import defaultdict
from queue import PriorityQueue
import time

# node = (i, j, dir, steps)
# edge = (node, cost)
def part1(f):
    grid = [list(map(int, l.strip())) for l in f if l.strip()]
    edges = defaultdict(list)
    dists = defaultdict(lambda: 2**32)
    prev = {}
    unvisited = set()
    pq = PriorityQueue()
    dists[(0,0,'R',1)] = 0
    for i, r in enumerate(grid):
        for j, _ in enumerate(r):
            for d in 'RDLU':
                for s in range(1, 4):
                    node = (i, j, d, s)
                    if d in 'RL':
                        cumm = 0
                        negCumm = 0
                        for si in range(1, 4):
                            if i+si < len(grid):
                                cumm += grid[i+si][j]
                                edges[node].append(((i+si, j, 'D', si), cumm))
                            if i-si >= 0:
                                negCumm += grid[i-si][j]
                                edges[node].append(((i-si, j, 'U', si), negCumm))
                    else:
                        cumm = 0
                        negCumm = 0
                        for sj in range(1, 4):
                            if j+sj < len(grid[0]):
                                cumm += grid[i][j+sj]
                                edges[node].append(((i, j+sj, 'R', sj), cumm))
                            if j-sj >= 0:
                                negCumm += grid[i][j-sj]
                                edges[node].append(((i, j-sj, 'L', sj), negCumm))
                    if len(edges[node]) > 0:
                        unvisited.add(node)
    pq.put((0, (0,0,'R',1)))
    while not pq.empty():
        cummCost, node = pq.get()
        unvisited.remove(node)
        if node[0] == len(grid)-1 and node[1] == len(grid[0])-1:
            break

        for e in edges[node]:
            if e[0] not in unvisited:
                continue

            alt = cummCost + e[1]
            if alt < dists[e[0]]:
                dists[e[0]] = alt
                prev[e[0]] = node
                pq.put((alt, e[0]))
        i += 1
                
    return min([dists[n] for n in filter(lambda x: x[0] == len(grid)-1 and x[1] == len(grid[0])-1, dists.keys())])

def makeEdges(node, grid):
    i, j, d, s = node
    edges = []
    if d in 'RL ':
        cumm = 0
        negCumm = 0
        for si in range(1, 11):
            if i+si < len(grid):
                cumm += grid[i+si][j]
                if si >= 4:
                    edges.append(((i+si, j, 'D', si), cumm))
            if i-si >= 0:
                negCumm += grid[i-si][j]
                if si >= 4:
                    edges.append(((i-si, j, 'U', si), negCumm))
    if d in 'DU ':
        cumm = 0
        negCumm = 0
        for sj in range(1, 11):
            if j+sj < len(grid[0]):
                cumm += grid[i][j+sj]
                if sj >= 4:
                    edges.append(((i, j+sj, 'R', sj), cumm))
            if j-sj >= 0:
                negCumm += grid[i][j-sj]
                if sj >= 4:
                    edges.append(((i, j-sj, 'L', sj), negCumm))
    return edges

def part2(f):
    grid = [list(map(int, l.strip())) for l in f if l.strip()]
    edges = defaultdict(list)
    dists = defaultdict(lambda: 2**32)
    prev = {}
    unvisited = set()
    pq = PriorityQueue()
    dists[(0,0,' ',0)] = 0
    for i, r in enumerate(grid):
        for j, _ in enumerate(r):
            for d in 'RDLU':
                for s in range(4, 11):
                    node = (i, j, d, s)
                    edges[node] = makeEdges(node, grid)
                    if len(edges[node]) > 0:
                        unvisited.add(node)
    
    edges[(0,0,' ',0)] = makeEdges((0,0,' ',0), grid)
    unvisited.add((0,0,' ',0))
    pq.put((0, (0,0,' ',0)))
    while len(unvisited) > 0:
        cummCost, node = pq.get()
        unvisited.remove(node)
        if node[0] == len(grid)-1 and node[1] == len(grid[0])-1:
            break

        for e in edges[node]:
            if e[0] not in unvisited:
                continue
            alt = cummCost + e[1]
            if alt < dists[e[0]]:
                dists[e[0]] = alt
                prev[e[0]] = node
                pq.put((alt, e[0]))
        i += 1
                
    return min([dists[n] for n in filter(lambda x: x[0] == len(grid)-1 and x[1] == len(grid[0])-1, dists.keys())])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))