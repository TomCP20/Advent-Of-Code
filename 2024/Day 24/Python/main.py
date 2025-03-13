"""Advent of Code - 2024 - Day 24"""
import re

with open(0, encoding="utf-8") as f:
    p, q = f.read().split("\n\n")
reg = {line[:3]:int(line[5:]) for line in p.splitlines()}
gates: dict[str, tuple[str, ...]] = {}
for line in q.splitlines():
    m = re.fullmatch("(...) (AND|OR|XOR) (...) -> (...)", line)
    if m:
        (a, op, b, c) = m.groups()
        gates[c] = (a, b, op)

def get_val(name: str) -> int:
    """get value of gate"""
    if name in reg:
        return reg[name]
    (l, r, operand) = gates[name]
    val1 = get_val(l)
    val2 = get_val(r)
    if operand == "AND":
        return val1 & val2
    if operand == "OR":
        return val1 | val2
    return val1 ^ val2

zgates: list[str] = [gate for gate in sorted(gates, reverse=True) if gate[0] == "z"]
def solve():
    """solve"""
    num=0
    for operand in zgates:
        num = (num << 1) + get_val(operand)
    return num

num1 = solve()
print(num1)

rule1: list[str] = []
rule2: list[str] = []
for gate, (a, b, op) in gates.items():
    if gate in zgates[1:] and op != "XOR":
        rule1.append(gate)
    if gate not in zgates:
        if a[0] != "x" and a[0] != "y" and b[0] != "x" and b[0] != "y" and op =="XOR":
            rule2.append(gate)

def get_swap(name: str) -> str:
    """gets the swap"""
    if name[0] == "z":
        return f"z{int(name[1:])-1:02d}"
    for out, (l, r, _) in gates.items():
        if name  in (l, r):
            return get_swap(out)
    assert False

for rule in rule2:
    swap = get_swap(rule)
    gates[rule], gates[swap] = gates[swap], gates[rule]

num2 = solve()

xnum: int = 0
for op in sorted(reg, reverse=True):
    if op[0] == "x":
        xnum = (xnum << 1) + reg[op]

ynum: int = 0
for op in sorted(reg, reverse=True):
    if op[0] == "y":
        ynum = (ynum << 1) + reg[op]

truenum = xnum + ynum
trailing = ((num2 ^ truenum) & -(num2 ^ truenum)).bit_length() -1

badgates = rule1 + rule2

for gate, (a, b, _) in gates.items():
    xstr = f"x{trailing:02d}"
    ystr = f"y{trailing:02d}"
    if (a == xstr and b == ystr) or (b == xstr and a == ystr):
        badgates.append(gate)

print(",".join(sorted(badgates)))
