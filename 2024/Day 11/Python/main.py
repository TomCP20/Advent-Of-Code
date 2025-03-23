"""Advent of Code - 2024 - Day 11"""

from functools import cache
import math


@cache
def process_stone(stone: int):
    """processes a stone"""
    if stone == 0:
        return 1
    digits = int(math.log10(stone)) + 1
    if digits % 2 == 0:
        a: int = stone // 10 ** ((digits // 2))
        b: int = stone % (10 ** (digits // 2))
        return (a, b)
    return stone * 2024


@cache
def num_stones(stone: int, blinks: int, max_blinks: int) -> int:
    """calculates the number of stones a stone creates after blinks number of blinks"""
    if blinks == max_blinks:
        return 1
    blinks += 1
    match process_stone(stone):
        case (a, b):
            return num_stones(a, blinks, max_blinks) + num_stones(b, blinks, max_blinks)
        case stone:
            return num_stones(stone, blinks, max_blinks)


with open(0, encoding="utf-8") as f:
    stones = list(map(int, f.read().split()))
print(sum(num_stones(stone, 0, 25) for stone in stones))
print(sum(num_stones(stone, 0, 75) for stone in stones))
