"""Advent of Code - 2024 - Day 3"""
import re

def part2(mem: str) -> int:
    """day 3 part 2"""
    enabled: bool = True
    total: int = 0
    for match in re.finditer(r"do\(\)|don\'t\(\)|mul\((\d+),(\d+)\)", mem):
        m = match.group(0)
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            total += int(match.group(1))*int(match.group(2))
    return total

with open(0, encoding="utf-8") as f:
    memory: str = "".join(f.read())

print(sum(int(a)*int(b) for (a, b) in re.findall(r"mul\((\d+),(\d+)\)", memory)))
print(part2(memory))
