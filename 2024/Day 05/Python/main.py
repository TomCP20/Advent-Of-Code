from functools import cmp_to_key

def getCmp(rules: list[list[int]]):
    def cmp(a: int, b: int):
        for (l, r) in rules:
            if a == l and b == r:
                return 1
            if b == l and a == r:
                return -1
        return 0
    return cmp

def isSorted(rules: list[list[int]], update: list[int]) -> bool:
    return all(not (l in update and r in update and not (update.index(l) < update.index(r))) for (l,r) in rules)

input = open(0).read()
a, b = input.split("\n\n", 1)

rules = [list(map(int, rule.split("|"))) for rule in a.splitlines()]
updates = [list(map(int, update.split(","))) for update in b.splitlines()]

sum1 = 0
sum2 = 0
for update in updates:
    mid = int((len(update) - 1)/2)
    if isSorted(rules, update):
        sum1 += update[mid]
    else:
        update.sort(key=cmp_to_key(getCmp(rules)))
        sum2 += update[mid]
print(sum1)
print(sum2)