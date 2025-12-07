"""Advent of Code - 2025 - Day 7"""


def part_1(head: str, tail: list[str]):
    beams: set[int] = {head.find("S")}
    next_beams: set[int] = set()
    solution: int = 0

    for line in tail:
        for beam in beams:
            if line[beam] == "^":
                solution += 1
                next_beams.add(beam-1)
                next_beams.add(beam+1)
            else:
                next_beams.add(beam)
        beams = next_beams
        next_beams = set()
    return solution

with open(0, encoding="utf-8") as f:
    head, *tail = f.read().splitlines()


print(part_1(head, tail))
