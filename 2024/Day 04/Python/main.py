"""Advent of Code - 2024 - Day 4"""
import re

def part1(r: int, word_search: str) -> int:
    """day 4 part 1"""
    count = 0
    for o in map(str, [0, r, r-1, r-2]):
        pattern = "(?=(X.{"+o+"}M.{"+o+"}A.{"+o+"}S|S.{"+o+"}A.{"+o+"}M.{"+o+"}X))"
        count += len(re.findall(pattern, word_search))
    return count

def part2(n: str, word_search: str) -> int:
    """day 4 part 2"""
    count = 0
    for perm in ["MMSS", "MSMS", "SMSM", "SSMM"]:
        pattern = "(?=("+perm[0]+"."+perm[1]+".{"+n+"}A.{"+n+"}"+perm[2]+"."+perm[3]+"))"
        count += len(re.findall(pattern, word_search))
    return count

with open(0, encoding="utf-8") as f:
    lines = f.read().splitlines()
    row = len(lines[0]) + 6
    PADDED_INPUT = "".join("..." + line + "..." for line in lines)


print(part1(row, PADDED_INPUT))
print(part2(str(row-2), PADDED_INPUT))
