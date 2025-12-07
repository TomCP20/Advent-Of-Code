"""Advent of Code - 2025 - Day 7"""

from collections import defaultdict


def part_1(head: str, tail: list[str]):
    beams: set[int] = {head.find("S")}
    solution: int = 0

    for line in tail:
        next_beams: set[int] = set()
        for beam in beams:
            if line[beam] == "^":
                solution += 1
                next_beams.add(beam - 1)
                next_beams.add(beam + 1)
            else:
                next_beams.add(beam)
        beams = next_beams
    return solution


def part_2(head: str, tail: list[str]):
    beams: dict[int, int] = {head.find("S"): 1}
    for line in tail:
        next_beams: dict[int, int] = defaultdict(int)
        for i, val in beams.items():
            if line[i] == "^":
                next_beams[i - 1] += val
                next_beams[i + 1] += val
            else:
                next_beams[i] += val
        beams = next_beams
    return sum(beams.values())


with open(0, encoding="utf-8") as f:
    head, *tail = f.read().splitlines()


print(part_1(head, tail))
print(part_2(head, tail))
