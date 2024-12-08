def parseline(line: str) -> tuple[int, list[int]]:
    a, b = line.split(": ")
    val = int(a)
    nums = list(map(int, b.split(" ")))
    return val, nums

def check(val: int, nums: list[int]):
    if len(nums) == 1:
        return nums[0] == val
    if check(val, [nums[0] + nums[1]] + nums[2:]):
        return True
    if check(val, [nums[0] * nums[1]] + nums[2:]):
        return True
    if check(val, [int(str(nums[0]) + str(nums[1]))] + nums[2:]):
        return True
    return False

input = list(map(parseline, open(0).read().splitlines()))
total = sum(val for val, nums in input if check(val, nums))
print(total)