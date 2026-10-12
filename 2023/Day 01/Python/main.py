"""Advent of Code - 2023 - Day 1"""

import re

DIGIT_MAP = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def word_to_digit(s: str) -> str:
    """convets a word into it's digit form, e.g. three into 3"""
    return DIGIT_MAP.get(s, s)


def get_val_1(line: str) -> int:
    """gets the calibration value for a line for part 1"""
    digits = re.findall(r"\d", line)
    return int(digits[0] + digits[-1])


def get_val_2(line: str) -> int:
    """gets the calibration value for a line for part 2"""
    digits = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    return int(word_to_digit(digits[0]) + word_to_digit(digits[-1]))


def main():
    """Solves Part 1 and 2 of Day 1"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
        print(sum(map(get_val_1, lines)))
        print(sum(map(get_val_2, lines)))


main()
