"""Advent of Code - 2024 - Day 17"""
def execute(a, b, c, program):
    """executes program"""
    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return a
        if operand == 5:
            return b
        if operand == 6:
            return c
        print(f"Invalid operand: {operand}")
        return 0

    pointer = 0
    output = []
    while pointer < len(program)-1:
        opcode = program[pointer]
        operand = program[pointer + 1]
        skip = False

        if opcode == 0: #adv
            a = a >> combo(operand)
        elif opcode == 1: #bxl
            b = b ^ operand
        elif opcode == 2: #bst
            b = combo(operand) % 8
        elif opcode == 3: #jnz
            if a != 0:
                pointer = operand
                skip = True
        elif opcode == 4: #bxc
            b = b ^ c
        elif opcode == 5: #out
            output.append(combo(operand) % 8)
        elif opcode == 6: #bdv
            b = a >> combo(operand)
        elif opcode == 7: #cdv
            c = a >> combo(operand)
        else:
            print(f"Invalid opcode: {opcode}")

        if not skip:
            pointer += 2
    return output

with open(0, encoding="utf-8") as f:
    lines = f.read().splitlines()

Reg_A = int(lines[0][12:])
Reg_B = int(lines[1][12:])
Reg_C = int(lines[2][12:])

Program = list(map(int, lines[4][9:].split(",")))

print(",".join(map(str, execute(Reg_A, Reg_B, Reg_C, Program))))



l = len(Program) -1

def dfs(n, candidate):
    """depth first search"""
    if n == l+1:
        yield candidate
    else:
        for i in range(8):
            a = candidate | (i << (3*(l-n)))
            if a != 0:
                out = execute(a, Reg_B, Reg_C, Program)
                if out[l-n] == Program[l-n]:
                    yield from dfs(n+1, a)

print(dfs(0, 0).__next__())
