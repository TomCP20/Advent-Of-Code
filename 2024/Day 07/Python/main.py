import math

def parseline(line: str) -> tuple[int, list[int]]:
    a, b = line.split(": ")
    val = int(a)
    nums = list(map(int, b.split(" ")))
    return val, nums

def check(val: int, nums: list[int], part2: bool):
    if len(nums) == 1:
        return nums[0] == val
    if check(val, [nums[0] + nums[1]] + nums[2:], part2):
        return True
    if check(val, [nums[0] * nums[1]] + nums[2:], part2):
        return True
    if part2 and check(val, [(nums[0] * (10 ** (int(math.log10(nums[1])) + 1))) + nums[1]] + nums[2:], part2):
        return True
    return False

input = list(map(parseline, open(0).read().splitlines()))
print(sum(val for val, nums in input if check(val, nums, False)))
print(sum(val for val, nums in input if check(val, nums, True)))