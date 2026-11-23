"""Advent of Code - 2023 - Day 18"""

import re


def main():
    """Solves Part 1 and 2 of Day 18"""
    with open(0, encoding="utf-8") as f:
        data = f.read().splitlines()
    matches = [re.match(r"([RLUD]) (\d+) [(]#([0-9a-f]{5})([0-4])[)]", row) for row in data]

    directions_1 = [m.group(1) for m in matches if m]
    distances_1 = [int(m.group(2)) for m in matches if m]
    directions_2 = [m.group(4) for m in matches if m]
    distances_2 = [int(m.group(3), 16) for m in matches if m]

    print(calculate_volume(directions_1, distances_1))
    print(calculate_volume(directions_2, distances_2))


def calculate_volume(directions: list[str], distances: list[int]) -> int:
    prev_x, prev_y = 0, 0
    total = 0
    for direction, distance in zip(directions, distances):
        x, y = 0, 0
        match direction:
            case "R" | "0":
                x, y = (prev_x + distance, prev_y)
            case "L" | "2":
                x, y = (prev_x - distance, prev_y)
            case "U" | "3":
                x, y = (prev_x, prev_y - distance)
            case "D" | "1":
                x, y = (prev_x, prev_y + distance)
            case _:
                assert False, distance
        total += (prev_y + y) * (prev_x - x) + distance
        prev_x, prev_y = x, y
    return abs(total) // 2 + 1


main()
