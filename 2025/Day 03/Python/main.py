"""Advent of Code - 2025 - Day 3"""

def max_joltage(bank: list[int], digits: int) -> int:
    """Calculates the max joltage of a bank"""
    num: int = 0
    i = 0
    l = len(bank)
    for j in range(l-digits+1, l+1):
        s = bank[i:j]
        digit = max(s)
        i += s.index(digit) + 1
        num = num * 10 + digit
    return num

def solve(banks: list[list[int]], digits: int) -> int:
    """Solves Part 1 or 2 of Day 3"""
    return sum(max_joltage(bank, digits) for bank in banks)

def main():
    """Solves Part 1 and 2 of Day 3"""
    with open(0, encoding="utf-8") as f:
        banks = list(map(lambda bank: list(map(int, bank)), f.read().splitlines()))

    print(solve(banks, 2))
    print(solve(banks, 12))

main()
