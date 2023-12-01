import sys

def part1(f):
    return sum([a[0]*10 + a[-1] for a in [[int(c) for c in s if c.isdigit()] for s in f]])

def part2(f):
    digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    arrs = []
    for l in f:
        a = []
        for i in range(len(l)):
            if l[i].isdigit():
                a.append(int(l[i]))
                continue
            for d in range(len(digits)):
                if l[i:].startswith(digits[d]):
                    a.append(d)
                    break
        arrs.append(a)
    return sum([a[0]*10 + a[-1] for a in arrs])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))