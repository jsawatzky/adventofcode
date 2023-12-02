import sys

def part1(f):
    total = 0
    limits = {'blue': 14, 'red': 12, 'green': 13}
    for g in f:
        possible = True
        game, rest = g.split(": ")
        shows = rest.split("; ")
        for s in shows:
            cubes = s.split(", ")
            for c in cubes:
                count, color = c.split()
                if int(count) > limits[color]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            total += int(game.split()[1])

    return total

def part2(f):
    total = 0
    for g in f:
        min = {'blue': 0, 'red': 0, 'green': 0}
        game, rest = g.split(": ")
        shows = rest.split("; ")
        for s in shows:
            cubes = s.split(", ")
            for c in cubes:
                count, color = c.split()
                min[color] = max(min[color], int(count))
        total += min["blue"]*min["green"]*min["red"]

    return total

if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        print(part1(f))
    with open(sys.argv[1]) as f:
        print(part2(f))