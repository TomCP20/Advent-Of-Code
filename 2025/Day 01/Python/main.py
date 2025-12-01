"""Advent of Code - 2025 - Day 1"""

with open(0, encoding="utf-8") as f:
    lines = f.read().splitlines()

def part_1(rotations: list[str]) -> int:
    """Function that solves Part 1 of Day 1"""
    dial = 50
    password = 0

    for rotation in rotations:
        direction = rotation[:1]
        distance = int(rotation[1:])
        if direction == "R":
            dial = (dial + distance) % 100
        elif direction == "L":
            dial = (dial - distance) % 100
        if dial == 0:
            password += 1
    return password

def part_2(rotations: list[str]) -> int:
    """Function that solves Part 2 of Day 1"""
    dial = 50
    password = 0

    for rotation in rotations:
        direction = rotation[:1]
        distance = int(rotation[1:])
        if direction == "R":
            for _ in range(distance):
                dial = (dial + 1) % 100
                if dial == 0:
                    password += 1
        elif direction == "L":
            for _ in range(distance):
                dial = (dial - 1) % 100
                if dial == 0:
                    password += 1
    return password

print(part_1(lines))
print(part_2(lines))
