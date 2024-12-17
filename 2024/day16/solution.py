import sys, time
from collections import defaultdict
import heapq

def part1(f):
    maze = [list(l.strip()) for l in f]
    
    def dijkstra(start, end):
        q = [(0, (start, (0, 1), True))]
        visited = set()
        while q:
            d, state = heapq.heappop(q)
            p, dir, can_turn = state
            if p == end:
                return d
            if state in visited:
                continue
            visited.add(state)
            x, y = p[0] + dir[0], p[1] + dir[1]
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                q.append((d + 1, ((x, y), dir, True)))
            if can_turn:
                q.append((d + 1000, (p, (dir[1], -dir[0]), False)))
                q.append((d + 1000, (p, (-dir[1], dir[0]), False)))
        return -1

    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if start and end:
        return dijkstra(start, end)
    else:
        return -1

def part2(f):
    maze = [list(l.strip()) for l in f]
    
    def dijkstra(start, end):
        q = [(0, (start, (0, 1), True, []))]
        min_dists = defaultdict(lambda: 10**100)
        all_paths = set()
        min_score = 10**100
        while q:
            d, state = heapq.heappop(q)
            p, dir, can_turn, path = state
            if d > min_score:
                continue
            if p == end:
                min_score = d
                all_paths.update(path)
                continue
            x, y = p[0] + dir[0], p[1] + dir[1]
            if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#':
                if d + 1 <= min_dists[(x, y, dir)]:
                    min_dists[(x, y, dir)] = d + 1
                    npath = path.copy()
                    npath.append(p)
                    heapq.heappush(q, (d + 1, ((x, y), dir, True, npath)))
            if can_turn:
                heapq.heappush(q, (d + 1000, (p, (dir[1], -dir[0]), False, path)))
                heapq.heappush(q, (d + 1000, (p, (-dir[1], dir[0]), False, path)))

        return len(all_paths) + 1

    start = end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)

    if start and end:
        return dijkstra(start, end)
    else:
        return -1

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        start_time = time.process_time()
        result1 = part1(f)
        end_time = time.process_time()
        print(f"Part 1: {result1} (Time: {(end_time - start_time) * 1000:.2f} ms)")

    with open(sys.argv[1]) as f:
        start_time = time.process_time()
        result2 = part2(f)
        end_time = time.process_time()
        print(f"Part 2: {result2} (Time: {(end_time - start_time) * 1000:.2f} ms)")