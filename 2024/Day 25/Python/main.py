"""Advent of Code - 2024 - Day 25"""
from itertools import product
with open(0, encoding="utf-8") as f:
    schematics = list(map(lambda x : x.splitlines(), f.read().split("\n\n")))
locks = [[[r[x] for r in l].count("#") for x in range(5)] for l in schematics if l[0] == "#####"]
keys = [[[r[x] for r in k].count("#") for x in range(5)] for k in schematics if k[0] == "....."]

print(sum(all(((k + l) <= 7) for (k, l) in zip(key, lock)) for key, lock in product(keys, locks)))
