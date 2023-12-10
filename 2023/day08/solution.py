import sys
from functools import reduce
from math import lcm

def part1(f):
    dirs = f.readline().strip()
    graph = {n[0]: n[1].strip('()').split(', ') for n in [l.strip().split(" = ") for l in f if l.strip()]}
    steps = 0
    curNode = 'AAA'
    while curNode != 'ZZZ':
        for d in dirs:
            steps += 1
            if d == 'L':
                curNode = graph[curNode][0]
            else:
                curNode = graph[curNode][1]
            if curNode == 'ZZZ':
                break
    return steps

def part2(f):
    dirs = f.readline().strip()
    graph = {n[0]: n[1].strip('()').split(', ') for n in [l.strip().split(" = ") for l in f if l.strip()]}
    steps = 0
    curNodes = list(filter(lambda n: n.endswith('A'), graph.keys()))
    firstZ = [-1] * len(curNodes)
    dirMap = {'L': 0, 'R': 1}
    while True:
        for j, d in enumerate(dirs):
            steps += 1
            for i, n in enumerate(curNodes):
                curNodes[i] = graph[n][dirMap[d]]
                if firstZ[i] < 0 and curNodes[i].endswith('Z'):
                    firstZ[i] = steps

            if all(map(lambda n: n >= 0, firstZ)):
                return lcm(*firstZ)

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))