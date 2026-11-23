"""Advent of Code - 2023 - Day 12"""

from functools import cache


def recursion_count(
    springs: str,
    blocks: list[int],
):
    """recursively calculate the number of arrangements"""

    @cache
    def inner_recursion_count(springs_i: int, blocks_i: int, current: int) -> int:
        if springs_i == len(springs):
            if blocks_i == len(blocks) and current == 0:
                return 1
            if blocks_i == len(blocks) - 1 and blocks[blocks_i] == current:
                return 1
            return 0
        answer = 0
        for c in [".", "#"]:
            if springs[springs_i] == c or springs[springs_i] == "?":
                if c == "." and current == 0:
                    answer += inner_recursion_count(springs_i + 1, blocks_i, 0)
                elif (
                    c == "."
                    and current > 0
                    and blocks_i < len(blocks)
                    and blocks[blocks_i] == current
                ):
                    answer += inner_recursion_count(springs_i + 1, blocks_i + 1, 0)
                elif c == "#":
                    answer += inner_recursion_count(
                        springs_i + 1, blocks_i, current + 1
                    )
        return answer

    return inner_recursion_count(0, 0, 0)


def main():
    """Solves Part 1 and 2 of Day 12"""
    with open(0, encoding="utf-8") as f:
        rows = f.read().splitlines()

    total_1 = 0
    total_2 = 0

    for row in rows:
        springs, blocks = row.split()
        blocks = [int(num) for num in blocks.split(",")]
        total_1 += recursion_count(springs, blocks)
        springs = "?".join([springs] * 5)
        blocks *= 5
        total_2 += recursion_count(springs, blocks)

    print(total_1)
    print(total_2)


main()
