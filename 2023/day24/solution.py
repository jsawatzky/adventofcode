import sys
from functools import reduce

# WINDOW = (7, 27)
WINDOW = (200000000000000, 400000000000000)
def part1(f):
    hail = [tuple(map(lambda x: tuple(map(int, x.split(", "))), l.strip().split(' @ '))) for l in f]
    count = 0
    for i, h1 in enumerate(hail):
        if h1[1][0] == 0:
            return 'fuck'
        m1 = h1[1][1]/h1[1][0]
        b1 = h1[0][1] - m1*h1[0][0]
        for j, h2 in enumerate(hail[i+1:], start=i+1):
            m2 = h2[1][1]/h2[1][0]
            b2 = h2[0][1] - m2*h2[0][0]
            if m1 == m2: continue
            ix = (b2-b1)/(m1-m2)
            iy = m1*ix+b1
            t1 = (ix-h1[0][0])/h1[1][0]
            t2 = (ix-h2[0][0])/h2[1][0]
            if t1 > 0 and t2 > 0 and ix >= WINDOW[0] and ix <= WINDOW[1] and iy >= WINDOW[0] and iy <= WINDOW[1]:
                count += 1

    return count

def part2(f):
    return 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))