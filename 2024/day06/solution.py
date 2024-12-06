import sys, time

def part1(f):
    grid = [list(line.strip()) for line in f]
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '^':
                cur_x, cur_y = x, y
                break
    dir = (0, -1)
    visited = set()
    while cur_x >= 0 and cur_x < len(grid[0]) and cur_y >= 0 and cur_y < len(grid):
        try:
            if grid[cur_y+dir[1]][cur_x+dir[0]] == '#':
                dir = (-dir[1], dir[0])
                continue
        except IndexError:
            pass
        
        visited.add((cur_x, cur_y))
        cur_x += dir[0]
        cur_y += dir[1]

    return len(visited)

def part2(f):
    grid = [list(line.strip()) for line in f]
    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '^':
                start_x, start_y = x, y
                break

    cur_x, cur_y = start_x, start_y
    dir = (0, -1)
    visited = set()
    while cur_x >= 0 and cur_x < len(grid[0]) and cur_y >= 0 and cur_y < len(grid):
        if grid[cur_y][cur_x] == '#':
            cur_x -= dir[0]
            cur_y -= dir[1]
            visited.add((cur_x, cur_y))
            dir = (-dir[1], dir[0])
        else:
            visited.add((cur_x, cur_y))
            cur_x += dir[0]
            cur_y += dir[1]

    def check_loop(x, y, d):
        v = set()
        while x >= 0 and x < len(grid[0]) and y >= 0 and y < len(grid):
            if (x, y, d) in v:
                return True
            if grid[y][x] == '#':
                x -= d[0]
                y -= d[1]
                v.add((x, y, d))
                d = (-d[1], d[0])
            else:
                v.add((x, y, d))
                x += d[0]
                y += d[1]
        return False
    
    opts = set()
    for c in visited:
        if c == (start_x, start_y):
            continue
        grid[c[1]][c[0]] = '#'
        if check_loop(start_x, start_y, (0, -1)):
            opts.add(c)
        grid[c[1]][c[0]] = '.'
    
    return len(opts)

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