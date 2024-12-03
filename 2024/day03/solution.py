import sys, time
import re

def part1(f):
    content = f.read()
    matches = re.findall(r'mul\((\d+),(\d+)\)', content)
    total_sum = sum(int(x) * int(y) for x, y in matches)
    return total_sum

def part2(f):
    content = f.read()
    matches = re.findall(r'mul\((\d+),(\d+)\)|(don\'t\(\))|(do\(\))', content, re.DOTALL)
    
    valid = True
    total_sum = 0
    
    for match in matches:
        if match[2] == "don't()":
            valid = False
        elif match[3] == "do()":
            valid = True
        elif match[0] and valid:
            x, y = match[0], match[1]
            total_sum += int(x) * int(y)
    
    return total_sum

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