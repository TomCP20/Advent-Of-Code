"""Advent of Code - 2025 - Day 7"""

from collections import defaultdict


with open(0, encoding="utf-8") as f:
    head, *tail = f.read().splitlines()


beams: dict[int, int] = {head.find("S"): 1}
splits: int = 0
for line in tail:
    next_beams: dict[int, int] = defaultdict(int)
    for i, val in beams.items():
        if line[i] == "^":
            splits += 1
            next_beams[i - 1] += val
            next_beams[i + 1] += val
        else:
            next_beams[i] += val
    beams = next_beams
print(splits)
print(sum(beams.values()))
