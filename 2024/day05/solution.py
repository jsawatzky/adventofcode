import sys, time

def part1(f):
    rules = {}
    updates = []

    # Read the file and parse the rules and updates
    for line in f:
        line = line.strip()
        if '|' in line:
            x, y = map(int, line.split('|'))
            if x not in rules:
                rules[x] = []
            rules[x].append(y)
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

    total = 0
    for u in updates:
        for i, p in enumerate(u):
            if any(x in rules.get(p, []) for x in u[:i]):
                break
        else:
            total += u[len(u)//2]

    return total

def part2(f):
    rules = {}
    updates = []

    # Read the file and parse the rules and updates
    for line in f:
        line = line.strip()
        if '|' in line:
            x, y = map(int, line.split('|'))
            if x not in rules:
                rules[x] = []
            rules[x].append(y)
        elif ',' in line:
            updates.append(list(map(int, line.split(','))))

    def fix_order(u):
        for i, p in enumerate(u):
            for j, x in enumerate(u[:i]):
                if x in rules.get(p, []):
                    return fix_order(u[:j] + [p] + u[j:i] + u[i+1:])
        else:
            return u

    total = 0
    for u in updates:
        fu = fix_order(u)
        if fu != u:
            total += fu[len(fu)//2]

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