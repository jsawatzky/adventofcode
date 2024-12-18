import sys, time
import heapq
from collections import defaultdict

# MAX_SIZE = 6
MAX_SIZE = 70

def part1(f):
    bytes = [tuple(map(int, l.strip().split(','))) for l in f]
    bytes = bytes[:1024]

    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(start, goal):
        open_set = []
        heapq.heappush(open_set, (dist(start, goal), start))
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0
        came_from = {}
        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return g_score[goal], path[::-1]
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (current[0] + d[0], current[1] + d[1])
                if new_pos[0] < 0 or new_pos[1] < 0:
                    continue
                if new_pos[0] > MAX_SIZE or new_pos[1] > MAX_SIZE:
                    continue
                if new_pos in bytes:
                    continue
                new_g_score = g_score[current] + 1
                if new_g_score < g_score[new_pos]:
                    g_score[new_pos] = new_g_score
                    came_from[new_pos] = current
                    heapq.heappush(open_set, (new_g_score + dist(new_pos, goal), new_pos))

    score, _ = astar((0, 0), (MAX_SIZE, MAX_SIZE))

    return score

def part2(f):
    bytes = [tuple(map(int, l.strip().split(','))) for l in f]

    def dist(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def astar(start, goal, bytes):
        open_set = []
        heapq.heappush(open_set, (dist(start, goal), start))
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0
        came_from = {}
        while open_set:
            _, current = heapq.heappop(open_set)
            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                return g_score[goal], path[::-1]
            for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_pos = (current[0] + d[0], current[1] + d[1])
                if new_pos[0] < 0 or new_pos[1] < 0:
                    continue
                if new_pos[0] > MAX_SIZE or new_pos[1] > MAX_SIZE:
                    continue
                if new_pos in bytes:
                    continue
                new_g_score = g_score[current] + 1
                if new_g_score < g_score[new_pos]:
                    g_score[new_pos] = new_g_score
                    came_from[new_pos] = current
                    heapq.heappush(open_set, (new_g_score + dist(new_pos, goal), new_pos))

    min_i, max_i = 1024, len(bytes)
    while min_i < max_i:
        i = (min_i + max_i) // 2
        if astar((0, 0), (MAX_SIZE, MAX_SIZE), bytes[:i]) is None:
            max_i = i
        else:
            min_i = i + 1
            
    return ','.join(map(str, bytes[min_i-1]))

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