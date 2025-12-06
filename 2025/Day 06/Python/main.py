"""Advent of Code - 2025 - Day 6"""

import math
import itertools


def solve_problems(num_columns: list[list[int]], operators: list[str]):
    """Solves Cephalopod math"""
    return sum(
        sum(nums) if operator == "+" else math.prod(nums)
        for operator, nums in zip(operators, num_columns)
    )


def part_1(lines: list[str]) -> int:
    """Solves Part 1"""
    num_rows = map((lambda line: map(int, line.split())), lines[:-1])
    num_columns = list(map(list, zip(*num_rows)))
    operators = lines[-1].split()
    return solve_problems(num_columns, operators)


def part_2(lines: list[str]) -> int:
    """Solves Part 2"""
    operators = lines[-1].split()
    str_columns = list(map("".join, zip(*lines[:-1])))
    groups = itertools.groupby(str_columns, lambda s: s == " " * (len(lines) - 1))
    num_columns = [list(map(int, group)) for is_gap, group in groups if not is_gap]
    return solve_problems(num_columns, operators)


def main():
    """Solves Part 1 and 2"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    print(part_1(lines))
    print(part_2(lines))
