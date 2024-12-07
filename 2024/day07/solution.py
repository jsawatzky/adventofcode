import sys, time

def part1(f):
    def is_valid_expression(target, numbers):
        for i in range(1 << len(numbers)-1):
            cumm = numbers[0]
            for j in range(1, len(numbers)):
                if i & (1 << j-1):
                    cumm += numbers[j]
                else:
                    cumm *= numbers[j]
            if cumm == target:
                return True
        return False

    result = 0
    for line in f:
        t, ns = line.strip().split(':')
        t = int(t)
        numbers = [int(x) for x in ns.strip().split() if x.isdigit()]
        if is_valid_expression(t, numbers):
            result += t

    return result

def part2(f):
    def is_valid_expression(target, numbers):
        opts = {numbers[0]}
        for i in range(1, len(numbers)):
            new_opts = set()
            for opt in opts:
                new_opts.add(opt + numbers[i])
                new_opts.add(opt * numbers[i])
                new_opts.add(int(str(opt) + str(numbers[i])))
            opts = new_opts
        return target in opts

    result = 0
    for line in f:
        t, ns = line.strip().split(':')
        t = int(t)
        numbers = [int(x) for x in ns.strip().split() if x.isdigit()]
        if is_valid_expression(t, numbers):
            result += t

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