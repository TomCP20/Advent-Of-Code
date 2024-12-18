def execute(Reg_A, Reg_B, Reg_C, Program):
    def Combo(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return Reg_A
        elif operand == 5:
            return Reg_B
        elif operand == 6:
            return Reg_C
        print(f"Invalid operand: {operand}")
        return 0

    pointer = 0
    out = []
    while pointer < len(Program)-1:
        opcode = Program[pointer]
        operand = Program[pointer + 1]
        skip = False

        if opcode == 0: #adv
            Reg_A = Reg_A >> Combo(operand)
        elif opcode == 1: #bxl
            Reg_B = Reg_B ^ operand
        elif opcode == 2: #bst
            Reg_B = Combo(operand) % 8
        elif opcode == 3: #jnz
            if Reg_A != 0:
                pointer = operand
                skip = True
        elif opcode == 4: #bxc
            Reg_B = Reg_B ^ Reg_C
        elif opcode == 5: #out
            out.append(Combo(operand) % 8)
        elif opcode == 6: #bdv
            Reg_B = Reg_A >> Combo(operand)
        elif opcode == 7: #cdv
            Reg_C = Reg_A >> Combo(operand)
        else:
            print(f"Invalid opcode: {opcode}")

        if not skip:
            pointer += 2
    return out

lines = open(0).read().splitlines()

Reg_A = int(lines[0][12:])
Reg_B = int(lines[1][12:])
Reg_C = int(lines[2][12:])

Program = list(map(int, lines[4][9:].split(",")))

out = execute(Reg_A, Reg_B, Reg_C, Program)

print(",".join(map(str, out)))



l = len(Program) -1

def DFS(n, candidate):
    if n == l+1:
        yield candidate
    else:
        for i in range(8):
            A = candidate | (i << (3*(l-n)))
            if A != 0:
                out = execute(A, Reg_B, Reg_C, Program)
                if out[l-n] == Program[l-n]:
                    yield from DFS(n+1, A)

print(DFS(0, 0).__next__())