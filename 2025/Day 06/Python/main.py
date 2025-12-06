"""Advent of Code - 2025 - Day 6"""

from math import prod
from itertools import groupby
from typing import Iterable


def solve_problems(num_columns: Iterable[Iterable[int]], operators: list[str]):
    """Solves Cephalopod math"""
    return sum(
        sum(nums) if op == "+" else prod(nums)
        for op, nums in zip(operators, num_columns)
    )


def part_1(num_lines: list[str], operators: list[str]) -> int:
    """Solves Part 1"""
    num_rows = map((lambda line: map(int, line.split())), num_lines)
    num_columns = zip(*num_rows)
    return solve_problems(num_columns, operators)


def part_2(num_lines: list[str], operators: list[str]) -> int:
    """Solves Part 2"""
    str_columns = map("".join, zip(*num_lines))
    groups = groupby(str_columns, str.isspace)
    num_columns = (map(int, group) for is_gap, group in groups if not is_gap)
    return solve_problems(num_columns, operators)


def main():
    """Solves Part 1 and 2"""
    with open(0, encoding="utf-8") as f:
        *num_lines, operator_line = f.read().splitlines()
    operators = operator_line.split()
    print(part_1(num_lines, operators))
    print(part_2(num_lines, operators))


main()
