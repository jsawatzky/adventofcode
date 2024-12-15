import sys, time, re, math
from collections import defaultdict

# GRID_SIZE = (11, 7)
GRID_SIZE = (101, 103)

def part1(f):
    positions = defaultdict(int)
    for l in f:
        x, y, vx, vy = map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l.strip()).groups())
        positions[((x + vx*100) % GRID_SIZE[0], (y + vy*100) % GRID_SIZE[1])] += 1

    midx = GRID_SIZE[0] // 2
    midy = GRID_SIZE[1] // 2

    quads = [0, 0, 0, 0]
    for p, c in positions.items():
        if p[0] < midx and p[1] < midy:
            quads[0] += c
        elif p[0] > midx and p[1] < midy:
            quads[1] += c
        elif p[0] < midx and p[1] > midy:
            quads[2] += c
        elif p[0] > midx and p[1] > midy:
            quads[3] += c

    return quads[0] * quads[1] * quads[2] * quads[3]

def part2(f):
    robots = []
    for l in f:
        x, y, vx, vy = map(int, re.match(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", l.strip()).groups())
        robots.append((x, y, vx, vy))

    orig_robots = robots.copy()

    minvx = 10**100
    minvx_i = -1
    minvy = 10**100
    minvy_i = -1

    for i in range(1, max(GRID_SIZE)+1):
        tx, ty = 0, 0
        for j in range(len(robots)):
            x, y, vx, vy = robots[j]
            x += vx
            x %= GRID_SIZE[0]
            y += vy
            y %= GRID_SIZE[1]
            tx += x
            ty += y
            robots[j] = (x, y, vx, vy)

        mx, my = tx / len(robots), ty / len(robots)
        dx, dy = 0, 0
        for j in range(len(robots)):
            x, y, _, _ = robots[j]
            dx += (x - mx) ** 2
            dy += (y - my) ** 2

        vx = dx / len(robots)
        if vx < minvx:
            minvx = vx
            minvx_i = i
        vy = dy / len(robots)
        if vy < minvy:
            minvy = vy
            minvy_i = i

    ans = minvx_i + ((pow(GRID_SIZE[0], -1, GRID_SIZE[1])*(minvy_i-minvx_i)) % GRID_SIZE[1]) * GRID_SIZE[0]

    positions = defaultdict(int)
    for r in orig_robots:
        x, y, vx, vy = r
        positions[((x + vx*ans) % GRID_SIZE[0], (y + vy*ans) % GRID_SIZE[1])] += 1

    for y in range(GRID_SIZE[1]):
        for x in range(GRID_SIZE[0]):
            if positions[(x, y)] > 0:
                print("#", end="")
            else:
                print(".", end="")
        print()

    return ans

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