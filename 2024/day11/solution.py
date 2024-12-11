import sys, time
from functools import lru_cache

def part1(f):
    stones = list(map(int, f.read().strip().split()))
    
    @lru_cache(maxsize=None)
    def handle_stone(s, b):
        if b == 25:
            return 1
        if s == 0:
            return handle_stone(1, b + 1)
        if len(str(s)) % 2 == 0:
            s_str = str(s)
            return handle_stone(int(s_str[:len(s_str)//2]), b + 1) + handle_stone(int(s_str[len(s_str)//2:]), b + 1)
        return handle_stone(s * 2024, b + 1)
    
    return sum([handle_stone(s, 0) for s in stones])

def part2(f):
    stones = list(map(int, f.read().strip().split()))
    
    @lru_cache(maxsize=None)
    def handle_stone(s, b):
        if b == 75:
            return 1
        if s == 0:
            return handle_stone(1, b + 1)
        if len(str(s)) % 2 == 0:
            s_str = str(s)
            return handle_stone(int(s_str[:len(s_str)//2]), b + 1) + handle_stone(int(s_str[len(s_str)//2:]), b + 1)
        return handle_stone(s * 2024, b + 1)
    
    return sum([handle_stone(s, 0) for s in stones])

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