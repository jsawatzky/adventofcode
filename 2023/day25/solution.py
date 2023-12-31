import sys
from collections import defaultdict
from copy import deepcopy
from operator import itemgetter

def dijkstra(nodes, edges, start):
    q = list(nodes)
    dist = defaultdict(lambda: float('inf'))
    prev = defaultdict(lambda: None)
    dist[start] = 0
    while len(q) > 0:
        u = min(q, key=lambda x: dist[x])
        q.remove(u)
        for n in edges[u]:
            if not edges[u][n]: continue
            if n not in q:
                continue
            alt = dist[u] + 1
            if alt < dist[n]:
                dist[n] = alt
                prev[n] = u
    return dist, prev

def connected(start, edges, known):
    known.add(start)
    for n in edges[start]:
        if not edges[start][n]: continue
        if n in known: continue
        known = connected(n, edges, known)
    return known

def part1(f):
    nodes = set()
    edges = defaultdict(lambda: defaultdict(bool))
    edgeList = []
    for l in f:
        l = l.strip()
        n, rest = l.split(': ')
        neighbors = rest.split(' ')
        nodes.add(n)
        for ne in neighbors:
            nodes.add(ne)
            edges[n][ne] = True
            edges[ne][n] = True
            edgeList.append((n, ne))

    n = list(nodes)[0]
    dist, _ = dijkstra(nodes, edges, n)
    start = max(dist.items(), key=itemgetter(1))[0]
    dist, _ = dijkstra(nodes, edges, start)
    end = max(dist.items(), key=itemgetter(1))[0]

    cEdges = deepcopy(edges)
    for _ in range(3):
        dist, prev = dijkstra(nodes, cEdges, start)
        p = end
        while p != start:
            np = prev[p]
            cEdges[p][np] = False
            cEdges[np][p] = False
            p = np

    dists, _ = dijkstra(nodes, cEdges, start)
    s = list(filter(lambda x: x[1] != float('inf'), dists.items()))
    return len(s)*(len(nodes)-len(s))

def part2(f):
    return "Merry Christmas!"

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))