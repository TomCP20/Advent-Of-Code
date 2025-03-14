"""Advent of Code - 2024 - Day 24"""

import re

REG = dict[str, bool]
GATES = dict[str, tuple[str, str, str]]


def get_val(reg: REG, gates: GATES, name: str) -> int:
    """get value of gate"""
    if name in reg:
        return reg[name]
    (l, r, operand) = gates[name]
    val1 = get_val(reg, gates, l)
    val2 = get_val(reg, gates, r)
    if operand == "AND":
        return val1 & val2
    if operand == "OR":
        return val1 | val2
    return val1 ^ val2


def solve(reg: REG, gates: GATES, zgates: list[str]):
    """solve"""
    num = 0
    for operand in zgates:
        num = (num << 1) + get_val(reg, gates, operand)
    return num


def get_swap(gates: GATES, name: str) -> str:
    """gets the swap"""
    if name[0] == "z":
        return f"z{int(name[1:])-1:02d}"
    for out, (l, r, op) in gates.items():
        if name in (l, r) and op != "AND":
            return get_swap(gates, out)
    assert False


def get_badgates(reg: REG, gates: GATES, zgates: list[str]):
    """finds the bad gates"""
    rule1, rule2 = get_rules(gates, zgates)

    for rule in rule2:
        swap = get_swap(gates, rule)
        gates[rule], gates[swap] = gates[swap], gates[rule]

    num = solve(reg, gates, zgates)
    truenum = get_truenum(reg)
    trailing = ((num ^ truenum) & -(num ^ truenum)).bit_length() - 1
    badgates = rule1 + rule2
    for gate, (a, b, _) in gates.items():
        if set((a, b)) == set((f"x{trailing:02d}", f"y{trailing:02d}")):
            badgates.append(gate)
    return badgates


def get_truenum(reg: REG):
    """calculates the true result"""
    xnum: int = 0
    ynum: int = 0
    for name in sorted(reg, reverse=True):
        if name[0] == "x":
            xnum = (xnum << 1) + reg[name]
        if name[0] == "y":
            ynum = (ynum << 1) + reg[name]
    truenum = xnum + ynum
    return truenum


def get_rules(gates: GATES, zgates: list[str]):
    """finds the gates that violate rule 1 and 2"""
    rule1: list[str] = []
    rule2: list[str] = []
    for gate, (a, b, op) in gates.items():
        if gate in zgates[1:] and op != "XOR":
            rule1.append(gate)
        if gate not in zgates:
            if (
                a[0] != "x"
                and a[0] != "y"
                and b[0] != "x"
                and b[0] != "y"
                and op == "XOR"
            ):
                rule2.append(gate)
    return rule1, rule2


def main():
    """main function"""
    with open(0, encoding="utf-8") as f:
        p, q = f.read().split("\n\n")
    reg: REG = {line[:3]: line[5:] == "1" for line in p.splitlines()}
    gates: GATES = {}
    for line in q.splitlines():
        m = re.fullmatch("(...) (AND|OR|XOR) (...) -> (...)", line)
        if m:
            (a, op, b, c) = m.groups()
            gates[c] = (a, b, op)

    zgates: list[str] = sorted(filter(lambda gate: gate[0] == "z", gates), reverse=True)

    print(solve(reg, gates, zgates))
    print(",".join(sorted(get_badgates(reg, gates, zgates))))


main()
