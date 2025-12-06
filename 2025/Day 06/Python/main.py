"""Advent of Code - 2025 - Day 6"""

import math


def part_1(num_columns: list[list[int]], operators: list[str]):
    """Solves Part 1"""
    total: int = 0
    for operator, nums in zip(operators, num_columns):
        total += sum(nums) if operator == "+" else math.prod(nums)
    return total


def main():
    """Solves Part 1"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    num_rows = map((lambda line: map(int, line.split())), lines[:-1])
    num_columns = list(map(list, zip(*num_rows)))
    operators = lines[-1].split()

    print(part_1(num_columns, operators))


main()
