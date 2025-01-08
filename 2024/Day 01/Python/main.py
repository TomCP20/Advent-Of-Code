"""Advent of Code - 2024 - Day 1"""
from collections import Counter

with open(0, encoding="utf-8") as f:
    lists = [line.split("   ") for line in f.read().splitlines()]
left = [int(line[0]) for line in lists]
right = [int(line[1]) for line in lists]

print(sum(abs(l-r) for (l, r) in zip(sorted(left), sorted(right))))

c = Counter(right)
print(sum(l*c[l] for l in left))
