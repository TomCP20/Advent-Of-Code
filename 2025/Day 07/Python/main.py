"""Advent of Code - 2025 - Day 7"""

with open(0, encoding="utf-8") as f:
    head, *tail = f.read().splitlines()[::2]
beams: list[int] = [0] * len(head)
beams[head.find("S")] = 1
splits: int = 0
for line in tail:
    next_beams: list[int] = [0] * len(head)
    for i, val in enumerate(beams):
        if val:
            if line[i] == "^":
                splits += 1
                next_beams[i - 1] += val
                next_beams[i + 1] += val
            else:
                next_beams[i] += val
    beams = next_beams
print(splits)
print(sum(beams))
