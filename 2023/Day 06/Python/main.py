"""Advent of Code - 2023 - Day 6"""

from math import prod
import re


def count_wins(time: int, distance: int):
    """Count the number of ways to win the race."""
    return sum(t * (time - t) > distance for t in range(time + 1))


def main():
    """Solves Part 1 and 2 of Day 6"""
    with open(0, encoding="utf-8") as f:
        time_line, distance_line = f.read().splitlines()
    times = map(int, time_line.split()[1:])
    distances = map(int, distance_line.split()[1:])
    print(prod(count_wins(time, distance) for time, distance in zip(times, distances)))

    time = int(re.sub(r"\D", "", time_line))
    distance = int(re.sub(r"\D", "", distance_line))
    print(count_wins(time, distance))


main()
