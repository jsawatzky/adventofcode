import sys, time

def part1(f):
    disk_map = list(map(int, f.read().strip()))
    disk = ['.'] * sum(disk_map)
    i = 0
    for j, l in enumerate(disk_map):
        if j % 2 == 1:
            i += l
            continue
        disk[i:i+l] = [j//2] * l
        i += l

    i = 0
    for j in range(len(disk)-1, 0, -1):
        if disk[j] == '.':
            continue
        while disk[i] != '.' and i < j:
            i += 1
        if i >= j:
            break
        disk[i] = disk[j]
        disk[j] = '.'

    checksum = sum([disk[i]*i if disk[i] != '.' else 0 for i in range(len(disk))])
    return checksum

def part2(f):
    disk_map = list(map(int, f.read().strip()))
    files = {}
    space = []
    i = 0
    for j, l in enumerate(disk_map):
        if j % 2 == 1:
            space.append((i,l))
        else:
            files[j//2] = (i, l)
        i += l
    
    for fid in sorted(files.keys(), reverse=True):
        i, l = files[fid]
        for j, s in enumerate(space):
            if s[0] >= i:
                break
            if s[1] >= l:
                files[fid] = (s[0], l)
                space[j] = (s[0]+l, s[1]-l)
                break

    checksum = 0
    for fid, (i, l) in files.items():
        for j in range(i, i+l):
            checksum += fid * j

    return checksum

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        start_time = time.process_time()
        result1 = part1(f)
        end_time = time.process_time()
        print(f"Part 1: {result1} (Time: {(end_time - start_time) * 1000:.2f} ms)")

    with open(sys.argv[1]) as f:
        start_time = time.process_time()
        result2 = part2(f)
        end_time = time.process_time()
        print(f"Part 2: {result2} (Time: {(end_time - start_time) * 1000:.2f} ms)")