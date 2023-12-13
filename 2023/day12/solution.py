import sys
from functools import cache

def part1(f):
    rows = [(x[0], list(map(int, x[1].split(',')))) for x in [l.strip().split() for l in f if l.strip()]]
    total = 0
    for r in rows:
        indexes = [i for i in range(len(r[0])) if r[0][i] == '?']
        for n in range(2 ** len(indexes)):
            s = ''
            for i in range(len(r[0])):
                if i not in indexes:
                    s += r[0][i]
                elif ((n >> indexes.index(i)) & 1) == 1:
                    s += '.'
                else:
                    s += '#'
            lens = [len(x) for x in s.split('.') if x]
            if lens == r[1]:
                total += 1

    return total

@cache
def process(r, g):
    if len(r) < sum(g):
        return 0
    if not r:
        return not g
    if not g:
        return '#' not in r
    
    total = 0
    i = r.find('?')
    if i < 0:
        return tuple(len(x) for x in r.split('.') if x) == g
    
    before = r[:i]
    after = r[i+1:]

    gBefore = tuple(len(x) for x in before.split('.') if x)
    if gBefore == g[:len(gBefore)]:
        total += process(after, g[len(gBefore):])

    gBefore = tuple(len(x) for x in (before+'#').split('.') if x)
    posGroups = g[:len(gBefore)]
    if gBefore[:-1] == posGroups[:-1]:
        if gBefore[-1] < posGroups[-1]:
            total += process(before+'#'+after, g)
        if gBefore[-1] == posGroups[-1] and (not after or after[0] != '#'):
            total += process(after[1:], g[len(gBefore):])

    return total

def part2(f):
    rows = [('?'.join([x[0] for n in range(5)]), tuple(map(int, x[1].split(',')))*5) for x in [l.strip().split() for l in f if l.strip()]]
    total = 0
    for r in rows:
        total += process(r[0], r[1])

    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))