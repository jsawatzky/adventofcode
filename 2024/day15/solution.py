import sys, time, os

DIRS = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

def part1(f):
    grid = []
    for line in f:
        line = line.strip()
        if not line:
            break
        grid.append(list(line.strip()))

    steps = ''
    for l in f:
        steps += l.strip()

    robot = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                robot = (x, y)
                break

    def move(sym, pos, dir):
        if grid[pos[1]][pos[0]] == '#':
            return False
        if grid[pos[1]][pos[0]] == '.':
            grid[pos[1]][pos[0]] = sym
            return True
        if grid[pos[1]][pos[0]] == 'O':
            if move('O', (pos[0] + dir[0], pos[1] + dir[1]), dir):
                grid[pos[1]][pos[0]] = sym
                return True
            return False
        raise Exception("Invalid grid")

    for s in steps:
        new_pos = (robot[0] + DIRS[s][0], robot[1] + DIRS[s][1])
        if move('@', new_pos, DIRS[s]):
            grid[robot[1]][robot[0]] = '.'
            robot = new_pos

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'O':
                total += 100*y + x

    return total

def part2(f):
    grid = []
    for line in f:
        line = line.strip()
        if not line:
            break
        row = []
        for c in line.strip():
            if c == '@':
                row += ['@', '.']
            elif c == '#':
                row += ['#', '#']
            elif c == '.':
                row += ['.', '.']
            elif c == 'O':
                row += ['[', ']']
        grid.append(row)

    steps = ''
    for l in f:
        steps += l.strip()

    robot = None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                robot = (x, y)
                break

    def move(pos, dir, apply):
        if grid[pos[1]][pos[0]] == '#':
            return False
        if grid[pos[1]][pos[0]] == '.':
            return True
        new_pos = (pos[0] + DIRS[dir][0], pos[1] + DIRS[dir][1])
        if dir in '<>':
            if grid[pos[1]][pos[0]] in '[]':
                if move(new_pos, dir, apply):
                    if apply: grid[new_pos[1]][new_pos[0]] = grid[pos[1]][pos[0]]
                    return True
                return False
        if dir in '^v':
            if grid[pos[1]][pos[0]] in '[]':
                other = (pos[0]-1, pos[1]) if grid[pos[1]][pos[0]] == ']' else (pos[0]+1, pos[1])
                other_new = (other[0] + DIRS[dir][0], other[1] + DIRS[dir][1])
                if move(new_pos, dir, apply) and move(other_new, dir, apply):
                    if apply:
                        grid[new_pos[1]][new_pos[0]] = grid[pos[1]][pos[0]]
                        grid[other_new[1]][other_new[0]] = '[' if grid[pos[1]][pos[0]] == ']' else ']'
                        grid[pos[1]][pos[0]] = '.'
                        grid[other[1]][other[0]] = '.'
                    return True
                return False
        raise Exception("Invalid grid")

    for s in steps:
        new_pos = (robot[0] + DIRS[s][0], robot[1] + DIRS[s][1])
        if move(new_pos, s, False):
            move(new_pos, s, True)
            grid[new_pos[1]][new_pos[0]] = '@'
            grid[robot[1]][robot[0]] = '.'
            robot = new_pos

    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '[':
                total += 100*y + x

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