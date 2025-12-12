"""Advent of Code - 2025 - Day 12"""


def parse_region(region: str) -> tuple[tuple[int, int], list[int]]:
    """parses a region"""
    a, b = region.split(": ")
    x, y = map(int, a.split("x"))
    return ((x, y), list(map(int, b.split())))


def main():
    """Solves Day 12"""
    with open(0, encoding="utf-8") as f:
        regions = list(map(parse_region, f.read().split("\n\n")[-1].splitlines()))
    print(sum(x * y >= 9 * sum(shape_ids) for (x, y), shape_ids in regions))


main()
