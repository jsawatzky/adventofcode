import sys
from functools import reduce
from collections import defaultdict

def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val

def part1(f):
    return sum(map(hash, f.read().strip().split(',')))

def part2(f):
    boxes = defaultdict(list)
    {}.items
    steps = f.read().strip().split(',')
    for s in steps:
        if s[-1] == '-':
            s = s[:-1]
            b = hash(s)
            for i, l in enumerate(boxes[b]):
                if l[0] == s:
                    boxes[b].pop(i)
                    break
        else:
            s, f = s.split("=")
            f = int(f)
            b = hash(s)
            for i, l in enumerate(boxes[b]):
                if l[0] == s:
                    boxes[b][i] = (s, f)
                    break
            else:
                boxes[b].append((s, f))

    return sum([sum([(i+1)*j*l[1] for j, l in enumerate(b, 1)]) for i, b in boxes.items()])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))