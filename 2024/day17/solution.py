import sys, time

def run_prog(prog, a, b, c):

    def combo(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c
        else:
            raise ValueError(f"Invalid operand: {operand}")

    out = []
    pc = 0
    while pc < len(prog):
        ins = prog[pc]
        op = prog[pc + 1]

        if ins == 0:
            a = a // 2**combo(op)
        elif ins == 1:
            b = b^op
        elif ins == 2:
            b = combo(op) % 8
        elif ins == 3:
            if a != 0:
                pc = op
                continue
        elif ins == 4:
            b = b^c
        elif ins == 5:
            out.append(combo(op) % 8)
        elif ins == 6:
            b = a // 2**combo(op)
        elif ins == 7:
            c = a // 2**combo(op)

        pc += 2
    return out

def part1(f):
    a = int(f.readline().strip().split(': ')[1])
    b = int(f.readline().strip().split(': ')[1])
    c = int(f.readline().strip().split(': ')[1])
    f.readline()
    prog = list(map(int, f.readline().strip().split(': ')[1].split(',')))

    out = run_prog(prog, a, b, c)

    return ','.join(map(str, out))

def part2(f):
    a = int(f.readline().strip().split(': ')[1])
    b = int(f.readline().strip().split(': ')[1])
    c = int(f.readline().strip().split(': ')[1])
    f.readline()
    prog = list(map(int, f.readline().strip().split(': ')[1].split(',')))

    # DFS the solution backwards. Since the A register is truncated 3 bits a time
    # we can build the correct value 3 bits at a time, working backwards through the program
    def attempt(x, idx):
        if idx < 0:
            return x
        for i in range(0, 8):
            out = run_prog(prog, ((x << 3) | i), b, c)
            if out[0] == prog[idx]:
                next = attempt((x << 3) | i, idx - 1)
                if next:
                    return next
        return 0

    return attempt(0, len(prog) - 1)

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