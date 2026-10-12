"""Advent of Code - 2023 - Day 1"""

import re


def word_to_digit(s: str) -> str:
    """convets a word into it's digit form, e.g. three into 3"""
    digit_map = {
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
    return digit_map.get(s, s)


def main():
    """Solves Part 1 and 2 of Day 1"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
        sum1 = 0
        for line in lines:
            digits = re.findall(r"\d", line)
            if digits:
                num = int(digits[0] + digits[-1])
                sum1 += num
        print(sum1)
        sum2 = 0
        for line in lines:
            digits = re.findall(
                r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line
            )
            num = int(word_to_digit(digits[0]) + word_to_digit(digits[-1]))
            sum2 += num
        print(sum2)


main()
