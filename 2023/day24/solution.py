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

def process(hail):
    n = 0
    while True:
        for x in range(n+1):
            y = n-x
            for vx in [-x, x]:
                for vy in [-y, y]:
                    poi = None
                    for i, h1 in enumerate(hail[:1]):
                        if h1[1][0]-vx == 0 and h1[1][1]-vy == 0:
                            break
                        m1 = float('inf') if (h1[1][0]-vx) == 0 else (h1[1][1]-vy)/(h1[1][0]-vx)
                        b1 = h1[0][1] - m1*h1[0][0]
                        for j, h2 in enumerate(hail[i+1:], start=i+1):
                            if h2[1][0]-vx == 0 and h2[1][1]-vy == 0:
                                break
                            m2 = float('inf') if (h2[1][0]-vx) == 0 else (h2[1][1]-vy)/(h2[1][0]-vx)
                            b2 = h2[0][1] - m2*h2[0][0]
                            if m1 == m2:
                                if b1 != b2:
                                    break
                                continue
                            ix = h1[0][0] if m1 == float('inf') else h2[0][0] if m2 == float('inf') else (b2-b1)/(m1-m2)
                            iy = m2*ix+b2 if m1 == float('inf') else m1*ix+b1
                            t1 = (iy-h1[0][1])/(h1[1][1]-vy) if (h1[1][0]-vx) == 0 else (ix-h1[0][0])/(h1[1][0]-vx)
                            t2 = (iy-h2[0][1])/(h2[1][1]-vy) if (h2[1][0]-vx) == 0 else (ix-h2[0][0])/(h2[1][0]-vx)
                            rix, riy = round(ix), round(iy)
                            if t1 > 0 and t2 > 0:
                                if not poi:
                                    poi = (rix, riy)
                                    continue
                                if (rix, riy) != poi:
                                    break
                            else:
                                break
                        else:
                            continue
                        break
                    else:
                        yield (vx, vy, poi)
        n += 1
        

def part2(f):
    hail = [tuple(map(lambda x: tuple(map(int, x.split(", "))), l.strip().split(' @ '))) for l in f]
    for vx, vy, poi in process(hail):
        print(vx, vy, poi)
        vz = None
        h1 = hail[0]
        for h2 in hail[1:]:
            t1 = (poi[1]-h1[0][1])/(h1[1][1]-vy) if (h1[1][0]-vx) == 0 else (poi[0]-h1[0][0])/(h1[1][0]-vx)
            t2 = (poi[1]-h2[0][1])/(h2[1][1]-vy) if (h2[1][0]-vx) == 0 else (poi[0]-h2[0][0])/(h2[1][0]-vx)
            if t1 == t2:
                print('huh?')
                break
            nvz = (h1[0][2]-h2[0][2] + h1[1][2]*t1 - h2[1][2]*t2)/(t1-t2)
            if vz == None:
                vz = round(nvz)
                continue
            if vz != round(nvz):
                print(f"func {nvz} {vz}")
                break
        else:
            t = (poi[0]-h1[0][0])/(h1[1][0]-vx)
            z = hail[0][0][2] + (hail[0][1][2]-vz)*t
            return poi[0]+poi[1]+round(z)
    return 0

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))