import sys

def part1(f):
    lines = f.readlines()
    numbers = [list(map(int, line.split())) for line in lines]
    c1 = sorted([x[0] for x in numbers])
    c2 = sorted([x[1] for x in numbers])
    differences = [abs(x-y) for x, y in zip(c1, c2)]
    return sum(differences)

def part2(f):
    lines = f.readlines()
    numbers = [list(map(int, line.split())) for line in lines]
    c1 = sorted([x[0] for x in numbers])
    c2 = sorted([x[1] for x in numbers])
    result = sum([x * c2.count(x) for x in c1])
    return result

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))