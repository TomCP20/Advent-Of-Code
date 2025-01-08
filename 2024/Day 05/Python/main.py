"""Advent of Code - 2024 - Day 5"""
from functools import cmp_to_key

def get_cmp(page_rules: list[list[int]]):
    """returns a comparison function based on the page rules"""
    def cmp(a: int, b: int):
        for (l, r) in page_rules:
            if a == l and b == r:
                return 1
            if b == l and a == r:
                return -1
        return 0
    return cmp

with open(0, encoding="utf-8") as f:
    rules, updates = f.read().split("\n\n", 1)
rules = [list(map(int, rule.split("|"))) for rule in rules.splitlines()]
updates = [list(map(int, update.split(","))) for update in updates.splitlines()]

sum1: int = 0
sum2: int = 0
for u in updates:
    mid = len(u)//2
    if not any(l in u and r in u and u.index(l) >= u.index(r) for (l,r) in rules):
        sum1 += u[mid]
    else:
        u.sort(key=cmp_to_key(get_cmp(rules)))
        sum2 += u[mid]
print(sum1)
print(sum2)
