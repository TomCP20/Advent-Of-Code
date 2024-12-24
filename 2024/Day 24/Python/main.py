from queue import Queue
import re

p, q = open(0).read().split("\n\n")
reg = {line[:3]:int(line[5:]) for line in p.splitlines()}
gates: dict[str, tuple[str, ...]] = {}
for line in q.splitlines():
    m = re.fullmatch("(...) (AND|OR|XOR) (...) -> (...)", line)
    if m:
        (a, op, b, c) = m.groups()
        gates[c] = (a, b, op)

def getVal(name: str) -> int:
    if name in reg:
        return reg[name]
    (a, b, op) = gates[name]
    val1 = getVal(a)
    val2 = getVal(b)
    if op == "AND":
        return val1 & val2
    elif op == "OR":
        return val1 | val2
    else:
        return val1 ^ val2

zgates: list[str] = [gate for gate in sorted(gates, reverse=True) if gate[0] == "z"]
def solve():
    num=0
    for op in zgates:
        num = (num << 1) + getVal(op)
    return num

num1 = solve()
print(num1)

rule1 = []
rule2 = []
for gate, (a, b, op) in gates.items():
    if gate in zgates[1:] and op != "XOR":
        rule1.append(gate)
    if gate not in zgates and a[0] != "x" and a[0] != "y" and b[0] != "x" and b[0] != "y" and op =="XOR":
        rule2.append(gate)

def get_swap(name: str):
    if name[0] == "z":
        return f"z{int(name[1:])-1:02d}"
    for out, (a, b, _) in gates.items():
        if name == a or name == b:
            return get_swap(out)
    assert False

for rule in rule2:
    swap = get_swap(rule)
    gates[rule], gates[swap] = gates[swap], gates[rule]

num2 = solve()

xnum=0
for op in sorted(reg, reverse=True):
    if op[0] == "x":
        xnum = (xnum << 1) + reg[op]

ynum=0
for op in sorted(reg, reverse=True):
    if op[0] == "y":
        ynum = (ynum << 1) + reg[op]

truenum = xnum + ynum
trailing = ((num2 ^ truenum) & -(num2 ^ truenum)).bit_length() -1

badgates = rule1 + rule2

for gate, (a, b, _) in gates.items():
    if (a == f"x{trailing:02d}" and b == f"y{trailing:02d}") or (b == f"x{trailing:02d}" and a == f"y{trailing:02d}"):
        badgates.append(gate)

print(",".join(sorted(badgates)))
