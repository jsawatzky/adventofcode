import sys, time
from functools import lru_cache

def part1(f):
    grid = [list(map(int, line.strip())) for line in f]

    def hike(pos, x, visited):
        if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
            return 0
        if grid[pos[1]][pos[0]] != x:
            return 0
        if pos in visited:
            return 0
        visited.add(pos)
        if x == 9:
            return 1
        return hike((pos[0] + 1, pos[1]), x+1, visited) + hike((pos[0] - 1, pos[1]), x+1, visited) + hike((pos[0], pos[1] + 1), x+1, visited) + hike((pos[0], pos[1] - 1), x+1, visited)
    
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                total += hike((x, y), 0, set())
    return total

def part2(f):
    grid = [list(map(int, line.strip())) for line in f]
    
    @lru_cache(maxsize=None)
    def hike(pos, x):
        if pos[0] < 0 or pos[0] >= len(grid[0]) or pos[1] < 0 or pos[1] >= len(grid):
            return 0
        if grid[pos[1]][pos[0]] != x:
            return 0
        if x == 9:
            return 1
        return hike((pos[0] + 1, pos[1]), x+1) + hike((pos[0] - 1, pos[1]), x+1) + hike((pos[0], pos[1] + 1), x+1) + hike((pos[0], pos[1] - 1), x+1)
    
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                total += hike((x, y), 0)
    return total

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