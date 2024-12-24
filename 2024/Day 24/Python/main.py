from queue import Queue
import re

p, q = open(0).read().split("\n\n")
reg = {line[:3]:int(line[5:]) for line in p.splitlines()}
gates = {}
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
        out = val1 & val2
    elif op == "OR":
        out = val1 | val2
    else:
        out = val1 ^ val2
    reg[name] = out
    return out

num=0
for op in sorted(gates, reverse=True):
    if op[0] == "z":
        num = (num << 1) + getVal(op)
print(num)