"""Advent of Code - 2023 - Day 11"""

from itertools import combinations


def num_in_range(n1: int, n2: int, l: list[int]):
    n1, n2 = min(n1, n2), max(n1, n2)
    count = sum(n1 < num < n2 for num in l)
    return count


def main():
    """Solves Part 1 and 2 of Day 11"""
    with open(0, encoding="utf-8") as f:
        image = f.read().splitlines()

    empty_rows = [i for i, row in enumerate(image) if all(x == "." for x in row)]
    empty_cols = [i for i, col in enumerate(zip(*image)) if all(x == "." for x in col)]

    galaxies = [
        (x, y)
        for y, row in enumerate(image)
        for x, pixel in enumerate(row)
        if pixel == "#"
    ]

    print(solve(1, empty_rows, empty_cols, galaxies))
    print(solve(999999999, empty_rows, empty_cols, galaxies))


def solve(
    expansion_factor: int,
    empty_rows: list[int],
    empty_cols: list[int],
    galaxies: list[tuple[int, int]],
):
    distances: list[int] = []

    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        distance = (
            abs(x1 - x2)
            + expansion_factor * num_in_range(x1, x2, empty_cols)
            + expansion_factor * num_in_range(y1, y2, empty_rows)
            + abs(y1 - y2)
        )
        distances.append(distance)

    return sum(distances)


main()
