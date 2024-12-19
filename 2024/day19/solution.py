import sys, time
from functools import lru_cache

def part1(f):
    patterns = f.readline().strip().split(', ')
    f.readline()
    designs = [l.strip() for l in f]

    @lru_cache(maxsize=None)
    def dfs(design):
        if len(design) == 0:
            return True
        for p in patterns:
            if design.startswith(p):
                if dfs(design[len(p):]):
                    return True
        return False

    c = 0 
    for d in designs:
        if dfs(d):
            c += 1

    return c

def part2(f):
    patterns = f.readline().strip().split(', ')
    f.readline()
    designs = [l.strip() for l in f]

    @lru_cache(maxsize=None)
    def dfs(design):
        if len(design) == 0:
            return 1
        c = 0
        for p in patterns:
            if design.startswith(p):
                c += dfs(design[len(p):])
        return c

    c = 0 
    for d in designs:
        c += dfs(d)

    return c

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