import sys, time

def part1(f):
    return 0

def part2(f):
    return 0

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