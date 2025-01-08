"""Advent of Code - 2024 - Day 7"""
import math

def parseline(line: str) -> tuple[int, list[int]]:
    """parses a line of the input file"""
    a, b = line.split(": ")
    val = int(a)
    nums = list(map(int, b.split(" ")))
    return val, nums

def digits(num: int) -> int:
    """returns the number of digits in a number"""
    return int(math.log10(num))+1

def check(val: int, nums: list[int], part2: bool) -> bool:
    """check if equation is valid"""
    if len(nums) == 1:
        return nums[0] == val
    if check(val, [nums[0] + nums[1]] + nums[2:], part2):
        return True
    if check(val, [nums[0] * nums[1]] + nums[2:], part2):
        return True
    if part2 and check(val, [(nums[0] * (10**digits(nums[1]))) + nums[1]] + nums[2:], part2):
        return True
    return False
with open(0, encoding="utf-8") as f:
    equations = list(map(parseline, f.read().splitlines()))
print(sum(val for val, nums in equations if check(val, nums, False)))
print(sum(val for val, nums in equations if check(val, nums, True)))
