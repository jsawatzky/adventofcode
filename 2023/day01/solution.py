import sys
from functools import reduce

def part1(f):
    return sum([a[0]*10 + a[-1] for a in [[int(c) for c in s if c.isdigit()] for s in f]])

def part2(f):
    return sum([a[0]*10 + a[-1] for a in [[int(c) for c in s if c.isdigit()] for s in [reduce(lambda x, y: x.replace(y[1], y[1][:-1]+str(y[0])+y[1][1:]), {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}.items(), l) for l in f]]])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))