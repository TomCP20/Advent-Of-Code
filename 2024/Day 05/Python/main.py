def isSorted(rules: list[list[int]], update: list[int]) -> bool:
    for rule in rules:
        l, r = rule
        if (not (l in update and r in update)):
            continue
        if (not (update.index(l) < update.index(r))):
            return False
    return True

input = open(0).read()
a, b = input.split("\n\n", 1)

rules = [list(map(int, rule.split("|"))) for rule in a.splitlines()]
updates = [list(map(int, update.split(","))) for update in b.splitlines()]

sum1 = 0
sum2 = 0
for update in updates:
    passed = isSorted(rules, update)
    mid = int((len(update) - 1)/2)
    if passed:
        sum1 += update[mid]
    else:
        while(not isSorted(rules, update)):
            for rule in rules:
                l, r = rule
                if (not (l in update and r in update)):
                    continue
                li = update.index(l)
                ri = update.index(r)
                if (not (li < ri)):
                    update[li], update[ri] = update[ri], update[li]
        sum2 += update[mid]
print(sum1)
print(sum2)