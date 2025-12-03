"""Advent of Code - 2025 - Day 3"""


def max_joltage(bank: list[int], digits: int) -> int:
    """Calculates the max joltage of a bank"""
    digits -= 1
    i, digit = max(enumerate(bank[: len(bank) - digits]), key=lambda x : x[1])
    if digits == 0:
        return digit
    return digit * 10**digits + max_joltage(bank[i + 1 :], digits)


with open(0, encoding="utf-8") as f:
    banks = list(map(lambda bank: list(map(int, bank)), f.read().splitlines()))
print(sum(max_joltage(bank, 2) for bank in banks))
print(sum(max_joltage(bank, 12) for bank in banks))
