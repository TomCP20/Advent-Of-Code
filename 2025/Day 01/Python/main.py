"""Advent of Code - 2025 - Day 1"""

def parse_line(line: str) -> tuple[int, int]:
    """Parses a line of the input"""
    direction = 1 if line[0] == "R" else -1
    return (direction, int(line[1:]))

def part_1(rotations: list[tuple[int, int]]) -> int:
    """Solves Part 1 of Day 1"""
    dial = 50
    password = 0
    for direction, distance in rotations:
        dial = (dial + direction*distance) % 100
        if dial == 0:
            password += 1
    return password

def part_2(rotations: list[tuple[int, int]]) -> int:
    """Solves Part 2 of Day 1"""
    dial = 50
    password = 0
    for direction, distance in rotations:
        for _ in range(distance):
            dial = (dial + direction) % 100
            if dial == 0:
                password += 1
    return password

def main():
    """Solves Part 1 and 2 of Day 1"""
    with open(0, encoding="utf-8") as f:
        rotations = [parse_line(line) for line in f.read().splitlines()]
    print(part_1(rotations))
    print(part_2(rotations))

main()
