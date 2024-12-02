import sys, time

def part1(f):
    def is_safe(report):
        levels = list(map(int, report.split()))
        increasing = all(1 <= levels[i+1] - levels[i] <= 3 for i in range(len(levels) - 1))
        decreasing = all(1 <= levels[i] - levels[i+1] <= 3 for i in range(len(levels) - 1))
        return increasing or decreasing

    reports = f.readlines()

    safe_count = sum(1 for report in reports if is_safe(report.strip()))
    return safe_count

def part2(f):
    def is_safe_with_removal(report):
        levels = list(map(int, report.split()))
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i+1:]
            increasing = all(1 <= modified_levels[j+1] - modified_levels[j] <= 3 for j in range(len(modified_levels) - 1))
            decreasing = all(1 <= modified_levels[j] - modified_levels[j+1] <= 3 for j in range(len(modified_levels) - 1))
            if increasing or decreasing:
                return True
        return False

    reports = f.readlines()

    safe_count = sum(1 for report in reports if is_safe_with_removal(report.strip()))
    return safe_count

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