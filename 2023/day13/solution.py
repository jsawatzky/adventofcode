import sys
from functools import reduce

def rot(p):
    return [''.join([r[i] for r in p]) for i in range(len(p[0]))]

def part1(f):
    patterns = []
    curPat = []
    total = 0
    for l in f:
        if l.strip():
            curPat.append(l.strip())
            continue
        patterns.append(curPat)
        curPat = []
    patterns.append(curPat)
    

    for curPat in patterns:
        for i in range(1, len(curPat)):
            t, b = curPat[:i], curPat[i:]
            l = min(len(t), len(b))
            if t[-l:] == list(reversed(b[:l])):
                total += 100*i
                break
        else:
            curPat = rot(curPat)
            for i in range(1, len(curPat)):
                t, b = curPat[:i], curPat[i:]
                l = min(len(t), len(b))
                if t[-l:] == list(reversed(b[:l])):
                    total += i
                    break
        
    return total

def diffs(t, b):
    total = 0
    assert len(t) == len(b)
    for i in range(len(t)):
        assert len(t[i]) == len(b[i])
        for j in range(len(t[i])):
            if t[i][j] != b[i][j]:
                total += 1
    return total

def part2(f):
    patterns = []
    curPat = []
    total = 0
    for l in f:
        if l.strip():
            curPat.append(l.strip())
            continue
        patterns.append(curPat)
        curPat = []
    patterns.append(curPat)
    

    for curPat in patterns:
        for i in range(1, len(curPat)):
            t, b = curPat[:i], curPat[i:]
            l = min(len(t), len(b))
            t, b = t[-l:], list(reversed(b[:l]))
            if diffs(t, b) == 1:
                total += 100*i
                break
        else:
            curPat = rot(curPat)
            for i in range(1, len(curPat)):
                t, b = curPat[:i], curPat[i:]
                l = min(len(t), len(b))
                t, b = t[-l:], list(reversed(b[:l]))
                if diffs(t, b) == 1:
                    total += i
                    break
        
    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))