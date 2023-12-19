import sys
from functools import reduce
from collections import defaultdict
from copy import deepcopy

class Workflow():
    def __init__(self, w):
        self.name, rest = w.split('{')
        rest = rest[:-1]
        conds = rest.split(',')
        self.default = conds[-1]
        self.checks = []
        for c in conds[:-1]:
            check, dest = c.split(':')
            p, op, val = check[0], check[1], int(check[2:])
            if op == '<':
                self.checks.append(lambda o, p=p, val=val, dest=dest: dest if o[p] < val else None)
            else:
                self.checks.append(lambda o, p=p, val=val, dest=dest: dest if o[p] > val else None)
    
    def process(self, part):
        for c in self.checks:
            d = c(part)
            if d:
                return d
        return self.default

def part1(f):
    flows = {}
    for l in f:
        l = l.strip()
        if not l:
            break
        w = Workflow(l)
        flows[w.name] = w

    parts = [{x[0]: int(x[1]) for x in map(lambda y: y.split('='), l.strip().strip('{}').split(','))} for l in f if l.strip]

    total = 0
    for p in parts:
        next = 'in'
        while next not in 'AR':
            next = flows[next].process(p)
        if next == 'A':
            total += sum(p.values())

    return total

def part2(f):
    flows = defaultdict(list)
    for l in f:
        l = l.strip()
        if not l:
            break
        name, rest = l.split('{')
        for c in rest[:-1].split(','):
            if ':' not in c:
                flows[name].append((None, c))
            else:
                check, dest = c.split(':')
                flows[name].append((check, dest))

    def dfs(flow, constraints):
        print(flow, constraints)
        result = []
        for check in flows[flow]:
            subConstraints = deepcopy(constraints)
            if check[0]:
                p, op, val = check[0][0], check[0][1], int(check[0][2:])
                if op == '<':
                    if constraints[p][0] > val: continue
                    subConstraints[p][1] = min(constraints[p][1], val)
                    constraints[p][0] = max(constraints[p][0], val)
                else:
                    if constraints[p][1] < val: continue
                    subConstraints[p][0] = max(constraints[p][0], val)
                    constraints[p][1] = min(constraints[p][1], val)
            if check[1] == 'A':
                print(flow, 'accepting', subConstraints)
                result.append(subConstraints)
            elif check[1] != 'R':
                result.extend(dfs(check[1], deepcopy(subConstraints)))
        return result
    
    validConstraints = dfs('in', {'x': [0, 4001], 'm': [0, 4001], 'a': [0, 4001], 's': [0, 4001]})
    total = sum(map(lambda y: reduce(lambda a, b: a*b, map(lambda x: x[1]-x[0]-1, y.values())), validConstraints))
    for i, x in enumerate(validConstraints):
        for j, y in enumerate(validConstraints[i+1:]):
            overlap = {}
            for k in 'xmas':
                overlap[k] = max(0, min(x[k][1], y[k][1]) - max(x[k][0], y[k][0]) - 1)
            total -= reduce(lambda a, b: a*b, overlap.values())

    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))