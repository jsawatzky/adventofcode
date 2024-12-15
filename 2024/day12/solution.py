import sys, time
from collections import defaultdict

def part1(f):
    grid = [list(l.strip()) for l in f]

    result = 0

    visited = set()
    region_frontier = [(0, 0)]

    while region_frontier:
        x, y = region_frontier.pop(0)
        if (x, y) in visited:
            continue

        current_region = grid[y][x]
        area = 0
        perimeter = 0
        frontier = [(x, y)]

        while frontier:
            x, y = frontier.pop(0)
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                perimeter += 1
                continue

            if grid[y][x] != current_region:
                if (x, y) not in visited: region_frontier.append((x, y))
                perimeter += 1
                continue

            if (x, y) in visited:
                continue

            visited.add((x, y))
            area += 1

            frontier.append((x + 1, y))
            frontier.append((x - 1, y))
            frontier.append((x, y + 1))
            frontier.append((x, y - 1))

        result += area * perimeter

    return result

def part2(f):
    grid = [list(l.strip()) for l in f]

    result = 0

    visited = set()
    region_frontier = [(0, 0)]

    while region_frontier:
        x, y = region_frontier.pop(0)
        if (x, y) in visited:
            continue

        current_region = grid[y][x]
        area = 0
        region = defaultdict(lambda: defaultdict(bool))
        min_x, min_y = len(grid[0]), len(grid)
        max_x, max_y = 0, 0
        frontier = [(x, y)]

        while frontier:
            x, y = frontier.pop(0)
            if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                continue

            if grid[y][x] != current_region:
                if (x, y) not in visited: region_frontier.append((x, y))
                continue

            if (x, y) in visited:
                continue

            visited.add((x, y))
            region[x][y] = True
            if x < min_x: min_x = x
            if y < min_y: min_y = y
            if x > max_x: max_x = x
            if y > max_y: max_y = y
            area += 1

            frontier.append((x + 1, y))
            frontier.append((x - 1, y))
            frontier.append((x, y + 1))
            frontier.append((x, y - 1))

        if area == 1:
            result += 4
            continue

        sides = 0
        
        edges = set()
        for x in range(min_x, max_x + 2):
            new_edges = set()
            cur_in = False
            for y in range(min_y - 1, max_y + 2):
                if region[x][y] != cur_in:
                    new_edges.add(f"{y}{'-' if cur_in else '+'}")
                    cur_in = not cur_in
            sides += len(edges - new_edges)
            edges = new_edges

        edges = set()
        for y in range(min_y, max_y + 2):
            new_edges = set()
            cur_in = False
            for x in range(min_x - 1, max_x + 2):
                if region[x][y] != cur_in:
                    new_edges.add(f"{x}{'-' if cur_in else '+'}")
                    cur_in = not cur_in
            sides += len(edges - new_edges)
            edges = new_edges  

        result += area * (sides)

    return result

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