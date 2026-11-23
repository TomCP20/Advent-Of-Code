"""Advent of Code - 2023 - Day 22"""

from collections import deque


def overlaps(a: list[int], b: list[int]):
    """Checks if a and b overlap"""
    return max(a[0], b[0]) <= min(a[3], b[3]) and max(a[1], b[1]) <= min(a[4], b[4])


def part_1(
    bricks: list[list[int]],
    key_supports_value: dict[int, set[int]],
    value_supports_key: dict[int, set[int]],
):
    """Solves part 1"""
    total = 0
    for i in range(len(bricks)):
        if all(len(value_supports_key[j]) >= 2 for j in key_supports_value[i]):
            total += 1
    return total


def part_2(
    bricks: list[list[int]],
    key_supports_value: dict[int, set[int]],
    value_supports_key: dict[int, set[int]],
):
    """Solves part 2"""
    total = 0

    for i in range(len(bricks)):
        q = deque(j for j in key_supports_value[i] if len(value_supports_key[j]) == 1)
        falling = set(q)
        falling.add(i)

        while q:
            j = q.popleft()
            for k in key_supports_value[j] - falling:
                if value_supports_key[k] <= falling:
                    q.append(k)
                    falling.add(k)

        total += len(falling) - 1
    return total


def main():
    """Solves Part 1 and 2 of Day 22"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    bricks = [list(map(int, line.replace("~", ",").split(","))) for line in lines]

    bricks.sort(key=lambda brick: brick[5])

    for i, brick in enumerate(bricks):
        max_z = 1
        for check in bricks[:i]:
            if overlaps(brick, check):
                max_z = max(max_z, check[5] + 1)
        brick[5] -= brick[2] - max_z
        brick[2] = max_z

    bricks.sort(key=lambda brick: brick[2])

    key_supports_value: dict[int, set[int]] = {i: set() for i in range(len(bricks))}
    value_supports_key: dict[int, set[int]] = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                key_supports_value[i].add(j)
                value_supports_key[j].add(i)

    print(part_1(bricks, key_supports_value, value_supports_key))
    print(part_2(bricks, key_supports_value, value_supports_key))


main()
