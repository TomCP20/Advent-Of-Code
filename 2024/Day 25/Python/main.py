"""Advent of Code - 2024 - Day 25"""

from itertools import product

with open(0, encoding="utf-8") as f:
    schematics = [x.splitlines() for x in f.read().split("\n\n")]

str_locks = filter(lambda s: s[0] == "#####", schematics)
str_keys = filter(lambda s: s[0] == ".....", schematics)

locks = [[col.count("#") for col in zip(*l)] for l in str_locks]
keys = [[col.count("#") for col in zip(*k)] for k in str_keys]

print(
    sum(
        all(k + l <= 7 for k, l in zip(key, lock)) for key, lock in product(keys, locks)
    )
)
