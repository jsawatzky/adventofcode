import sys

def part1(f):
    x = [[int(x) for c in s if c.isdigit()] for s in f]
    print(x)
    y = [a[0]*10 + a[1] for a in x]
    return sum(y)

def part2(f):
    return 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))