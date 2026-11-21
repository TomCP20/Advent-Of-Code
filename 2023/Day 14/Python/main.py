"""Advent of Code - 2023 - Day 14"""

import re


def main():
    """Solves Part 1 and 2 of Day 14"""
    with open(0, encoding="utf-8") as f:
        rows = f.read().splitlines()
    print(part_1(rows))


def part_1(rows: list[str]):
    """Solves 2023 Day 14 Part 1"""
    cols = ["".join(row[i] for row in rows) for i in range(len(rows[0]))]
    score = 0
    for col in cols:
        col = re.sub(r"[O.]+", lambda x: "".join(sorted(x.group(), reverse=True)), col)
        for i, c in enumerate(col):
            if c == "O":
                score += len(col) - i
    return score


main()
