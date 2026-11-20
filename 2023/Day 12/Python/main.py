"""Advent of Code - 2023 - Day 12"""


def recursion_count(
    springs: str,
    blocks: list[int],
    key: tuple[int, int, int],
    dp: dict[tuple[int, int, int], int],
) -> int:
    """recursively calculate the number of arrangements"""
    springs_i, blocks_i, current = key
    if key in dp:
        return dp[key]
    if springs_i == len(springs):
        if blocks_i == len(blocks) and current == 0:
            return 1
        if blocks_i == len(blocks) - 1 and blocks[blocks_i] == current:
            return 1
        return 0
    ans = 0
    for c in [".", "#"]:
        if springs[springs_i] == c or springs[springs_i] == "?":
            if c == "." and current == 0:
                new_key = (springs_i + 1, blocks_i, 0)
                ans += recursion_count(springs, blocks, new_key, dp)
            elif (
                c == "."
                and current > 0
                and blocks_i < len(blocks)
                and blocks[blocks_i] == current
            ):
                new_key = (springs_i + 1, blocks_i + 1, 0)
                ans += recursion_count(springs, blocks, new_key, dp)
            elif c == "#":
                new_key = (springs_i + 1, blocks_i, current + 1)
                ans += recursion_count(springs, blocks, new_key, dp)
    dp[key] = ans
    return ans


def main():
    """Solves Part 1 and 2 of Day 12"""
    with open(0, encoding="utf-8") as f:
        rows = f.read().splitlines()

    total_1 = 0
    total_2 = 0

    for row in rows:
        springs, blocks = row.split()
        blocks = [int(num) for num in blocks.split(",")]
        total_1 += recursion_count(springs, blocks, (0, 0, 0), {})
        springs = "?".join([springs] * 5)
        blocks *= 5
        total_2 += recursion_count(springs, blocks, (0, 0, 0), {})

    print(total_1)
    print(total_2)


main()
