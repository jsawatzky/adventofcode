import sys
from functools import reduce
from collections import defaultdict

cats = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']

def parse(f):
    seeds = [int(s) for s in f.readline().strip()[7:].split()]
    maps = defaultdict(list)
    current_map = ""
    for l in f:
        l = l.strip()
        if not l:
            continue
        if l.endswith("map:"):
            current_map = l[:-5]
            continue
        maps[current_map].append([int(x) for x in l.split()])
    for m in maps:
        maps[m] = sorted(maps[m], key=lambda x: x[1])
    return (seeds, maps)


def part1(f):
    seeds, maps = parse(f)
    for i in range(len(cats)-1):
        for j, s in enumerate(seeds):
            for m in maps[f"{cats[i]}-to-{cats[i+1]}"]:
                if m[1] < s and s < m[1]+m[2]:
                    seeds[j] = m[0] + (s-m[1])
                    break
    return min(seeds)


def part2(f):
    seeds, maps = parse(f)
    seeds = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    for i in range(len(cats)-1):
        current_map = maps[f"{cats[i]}-to-{cats[i+1]}"]
        j = 0
        k = 0
        new_seeds = []
        seeds.sort(key=lambda x: x[0])
        while j < len(seeds) and k < len(current_map):
            m_start = current_map[k][1]
            m_end = m_start + current_map[k][2]
            s_start = seeds[j][0]
            s_end = s_start + seeds[j][1]
            if s_start >= m_start and s_end <= m_end:
                new_seeds.append(seeds[j])
                j += 1
                continue
            if m_end <= s_start:
                k += 1
                continue
            if m_start >= s_end:
                new_seeds.append(seeds[j])
                j += 1
                continue
            if m_start > s_start:
                new_seeds.append((s_start, m_start-s_start))
                seeds[j] = (m_start, seeds[j][1]-(m_start-s_start))
                continue
            if m_end < s_end:
                new_seeds.append((s_start, m_end-s_start))
                seeds[j] = (m_end, seeds[j][1]-(m_end-s_start))
                continue
            print(f"FUCK {s_start}-{s_end} - {m_start}-{m_end}")
            return
        while j < len(seeds):
            new_seeds.append(seeds[j])
            j += 1
        seeds = new_seeds
        for j, s in enumerate(seeds):
            for m in current_map:
                if m[1] <= s[0] and s[0] < m[1]+m[2]:
                    seeds[j] = (m[0] + (s[0]-m[1]), s[1])
                    break


    return min([x[0] for x in seeds])

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))