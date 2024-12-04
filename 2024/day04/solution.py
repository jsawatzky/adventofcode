import sys, time

def part1(f):
    # find all instances of "target" in "lines" where target can be forwards, backwards, diagonally, or vertically
    # if found, return the number of instances of "target" found
    def search_word(grid, word):
        def check_direction(x, y, dx, dy):
            for i in range(len(word)):
                if not (0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == word[i]):
                    return False
                x += dx
                y += dy
            return True

        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy):
                        count += 1
        return count

    grid = [list(line.strip()) for line in f.readlines()]
    return search_word(grid, "XMAS")

def part2(f):
    count = 0
    grid = [list(line.strip()) for line in f.readlines()]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                continue
            if grid[i][j] == "A":
                mas = [grid[i-1][j-1], grid[i-1][j+1], grid[i+1][j+1], grid[i+1][j-1]]
                if mas.count("M") == 2 and mas.count("S") == 2 and (mas[0] == mas[1] or mas[1] == mas[2]):
                    count += 1
    return count

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