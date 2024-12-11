from functools import cache
import math
from typing import Generator, Iterable

@cache
def process_stone(stone: int):
    if stone == 0:
        return 1
    else:
        digits = int(math.log10(stone)) + 1
        if digits % 2 == 0:
            a: int = stone // 10 ** ((digits//2))
            b: int = stone % (10**(digits//2))
            return (a, b)
        else:
            return stone * 2024

def blink(stones: Iterable[int]) -> Generator[int, None, None]:
    for stone in stones:
        x = process_stone(stone)
        if type(x) is tuple:
            yield from x
        elif type(x) is int:
            yield x
        else:
            print(f"error: x is type {type(x)}")

@cache
def num_stones(stone: int, blinks: int) -> int:
    if blinks == 75:
        return 1
    x = process_stone(stone)
    if type(x) is tuple:
        return num_stones(x[0], blinks + 1) + num_stones(x[1], blinks + 1)
    elif type(x) is int:
        return num_stones(x, blinks + 1)
    else:
        print(f"error: x is type {type(x)}")
        return 0

input = map(int, open(0).read().split())
print(sum(num_stones(stone, 0) for stone in input))