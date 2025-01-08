"""Advent of Code - 2024 - Day 2"""
from itertools import combinations, pairwise
from typing import Iterable

def is_safe(report: Iterable[int]) -> bool:
    """checks if values are all increasing or all decreasing 
    and adjacent values differ by at least 1 and at most 3"""
    return (
        (all(1 <= a-b <= 3 for (a, b) in pairwise(report))) or
        (all(1 <= b-a <= 3 for (a, b) in pairwise(report)))
        )

def skip_safe(report: list[int]) -> bool:
    """check if report can be made safe by removing a value"""
    return any(is_safe(comb) for comb in combinations(report, len(report)-1))

with open(0, encoding="utf-8") as f:
    reports = list(map(lambda x : list(map(int, x.split())), f.read().splitlines()))

print(sum(is_safe(report) for report in reports))

print(sum(is_safe(report) or skip_safe(report) for report in reports))
