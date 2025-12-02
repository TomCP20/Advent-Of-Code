"""Advent of Code - 2025 - Day 2"""

import re

def get_range(r: str):
    """create a range based on the string r"""
    i = r.find("-")
    return range(int(r[:i]), int(r[i+1:])+1)

def solve(ids: list[int], part: int):
    """Solves Part 1 of Day 2"""
    pattern = r"^(.+)\1$" if part == 1 else r"^(.+)\1+$"
    return sum(id_int for id_int in ids if re.match(pattern, str(id_int)))

def main():
    """Solves Part 1 and 2 of Day 2"""
    with open(0, encoding="utf-8") as f:
        line = "".join(f.read().splitlines())
    ranges = (get_range(r) for r in line.split(","))
    ids = [id_int for r in ranges for id_int in r]
    print(solve(ids, 1))
    print(solve(ids, 2))

main()
