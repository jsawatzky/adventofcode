import sys
from functools import reduce

def part1(f):
    return reduce(lambda i, j: i + j[0], list(filter(lambda a: len(list(filter(lambda b: b.get('blue', 0) > 14 or b.get('red', 0) > 12 or b.get('green', 0) > 13, a[1]))) == 0, {int(x[0]): list(map(lambda y: {z[1]: int(z[0]) for z in list(map(lambda z: z.split(), y.split(", ")))}, x[1].split("; "))) for x in [l.strip()[5:].split(": ") for l in f]}.items())), 0)

def part2(f):
    return sum(map(lambda i: i['blue'] * i['red'] * i['green'], map(lambda a: reduce(lambda b, c: {d[0]: max(d[1], c.get(d[0], 0)) for d in b.items()}, a, {'blue': 0, 'red': 0, 'green': 0}), [list(map(lambda y: {z[1]: int(z[0]) for z in list(map(lambda z: z.split(), y.split(", ")))}, x[1].split("; "))) for x in [l.strip()[5:].split(": ") for l in f]])))

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))