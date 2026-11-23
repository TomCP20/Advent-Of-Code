"""Advent of Code - 2023 - Day 9"""

from itertools import pairwise

def predict_value_1(report: list[int]) -> int:
    """Predicts the next value for part 1."""
    differences = [report]
    while not all(v == 0 for v in differences[-1]):
        differences.append([pair[1]-pair[0] for pair in pairwise(differences[-1])])
    return sum(difference[-1] for difference in differences)

def predict_value_2(report: list[int]) -> int:
    """Predicts the next value for part 2."""
    differences = [report]
    while not all(v == 0 for v in differences[-1]):
        differences.append([pair[1]-pair[0] for pair in pairwise(differences[-1])])
    vals = [difference[0] for difference in reversed(differences)]
    result = 0
    for val in vals:
        result = val - result
    return result

def main():
    """Solves Part 1 and 2 of Day 9"""
    with open(0, encoding="utf-8") as f:
        reports = [[int(val) for val in report.split()] for report in f.readlines()]
    print(sum(map(predict_value_1, reports)))
    print(sum(map(predict_value_2, reports)))


main()
