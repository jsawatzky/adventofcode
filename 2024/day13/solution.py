import sys, time, re

def part1(f):
    lines = [l.strip() for l in f.readlines()]

    total = 0

    i = 0
    while i < len(lines):
        bax, bay = map(int, re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[i]).groups())
        bbx, bby = map(int, re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[i+1]).groups())
        px, py = map(int, re.match(r"Prize: X=(\d+), Y=(\d+)", lines[i+2]).groups())

        for ta in range(101):
            for tb in range(101):
                if bax * ta + bbx * tb == px and bay * ta + bby * tb == py:
                    total += 3*ta + tb

        i += 4
    return total

def part2(f):
    lines = [l.strip() for l in f.readlines()]

    total = 0

    i = 0
    while i < len(lines):
        bax, bay = map(int, re.match(r"Button A: X\+(\d+), Y\+(\d+)", lines[i]).groups())
        bbx, bby = map(int, re.match(r"Button B: X\+(\d+), Y\+(\d+)", lines[i+1]).groups())
        px, py = map(int, re.match(r"Prize: X=(\d+), Y=(\d+)", lines[i+2]).groups())
        px += 10000000000000
        py += 10000000000000

        det = bax * bby - bay * bbx
        ta = (px * bby - py * bbx) // det
        tb = (bax * py - bay * px) // det

        if bax * ta + bbx * tb == px and bay * ta + bby * tb == py:
            total += 3*ta + tb

        i += 4
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