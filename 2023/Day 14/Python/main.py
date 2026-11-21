"""Advent of Code - 2023 - Day 14"""

import re

PATTERN = r"[O.]+"
CYCLES = 1_000_000_000


def tilt_line(line: str, r: bool):
    """Tilt the line"""
    return re.sub(PATTERN, lambda x: "".join(sorted(x.group(), reverse=r)), line)


def tilt_grid(grid: list[str], r: bool):
    """Tilt the grid"""
    return [tilt_line(line, r) for line in grid]


def rotate_grid(grid: list[str]):
    """Rotate the grid"""
    return ["".join(line[i] for line in grid) for i in range(len(grid[0]))]


def part_1(rows: list[str]):
    """Solves 2023 Day 14 Part 1"""
    cols = rotate_grid(rows)
    cols = tilt_grid(cols, True)
    score = 0
    for col in cols:
        for i, c in enumerate(col):
            if c == "O":
                score += len(col) - i
    return score


def part_2(rows: list[str]):
    """Solves 2023 Day 14 Part 2"""


def main():
    """Solves Part 1 and 2 of Day 14"""
    with open(0, encoding="utf-8") as f:
        rows = f.read().splitlines()
    print(part_1(rows))


main()
