import sys, time
from collections import defaultdict

def part1(f):
    grid = [list(line.strip()) for line in f]
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                antennas[grid[y][x]].append((x, y))
    
    max_x = len(grid[0])
    max_y = len(grid)

    antinodes = set()
    for freq in antennas:
        for i, a in enumerate(antennas[freq]):
            for b in antennas[freq][i+1:]:
                rise = b[1] - a[1]
                run = b[0] - a[0]
                tx, ty = a[0]-run, a[1]-rise
                if 0 <= tx < max_x and 0 <= ty < max_y:
                    antinodes.add((tx, ty))
                tx, ty = b[0]+run, b[1]+rise
                if 0 <= tx < max_x and 0 <= ty < max_y:
                    antinodes.add((tx, ty))

    return len(antinodes)

def part2(f):
    grid = [list(line.strip()) for line in f]
    antennas = defaultdict(list)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != '.':
                antennas[grid[y][x]].append((x, y))
    
    max_x = len(grid[0])
    max_y = len(grid)

    antinodes = set()
    for freq in antennas:
        for i, a in enumerate(antennas[freq]):
            for b in antennas[freq][i+1:]:
                rise = b[1] - a[1]
                run = b[0] - a[0]
                tx, ty = a[0], a[1]
                while 0 <= tx < max_x and 0 <= ty < max_y:
                    antinodes.add((tx, ty))
                    tx += run
                    ty += rise
                tx, ty = a[0], a[1]
                while 0 <= tx < max_x and 0 <= ty < max_y:
                    antinodes.add((tx, ty))
                    tx -= run
                    ty -= rise
                
    return len(antinodes)

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