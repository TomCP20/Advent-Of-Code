"""Advent of Code - 2023 - Day 3"""

import re


def is_part_number(lines: list[str], i: int, match: re.Match[str]):
    """Checks if a number is a part number"""
    y1 = max(i - 1, 0)
    y2 = min(i + 1, len(lines) - 1)
    x1 = max(match.start() - 1, 0)
    x2 = min(match.end() + 1, len(lines[0]) - 1)
    area = "".join(lines[j][x1:x2] for j in range(y1, y2 + 1))
    return bool(re.search("[^0-9.]", area))


def part_1(lines: list[str], number_matches: list[list[re.Match[str]]]):
    """Solves Part 1"""
    result = 0
    for i, matches in enumerate(number_matches):
        for match in matches:
            if is_part_number(lines, i, match):
                result += int(match.group())
    return result


def part_2(lines: list[str], number_matches: list[list[re.Match[str]]]):
    """Solves Part 2"""
    result = 0
    for i, line in enumerate(lines):
        y_span = [y for y in range(i - 1, i + 2) if y in range(len(lines))]
        for gear in re.finditer(r"[*]", line):
            nums: list[str] = []
            gear_pos = gear.start()
            x_span = [
                x for x in range(gear_pos - 1, gear_pos + 2) if x in range(len(line))
            ]
            for y in y_span:
                for number in number_matches[y]:
                    if any(x in range(*number.span()) for x in x_span):
                        nums.append(number.group())
            if len(nums) == 2:
                result += int(nums[0]) * int(nums[1])
    return result


def main():
    """Solves Part 1 and 2 of Day 3"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    number_matches = [list(re.finditer(r"\d+", line)) for line in lines]
    print(part_1(lines, number_matches))
    print(part_2(lines, number_matches))


main()
