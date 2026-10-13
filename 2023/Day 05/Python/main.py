"""Advent of Code - 2023 - Day 5"""


def new_seed(seed: int, ranges: list[list[int]]):
    for dest, src, rng in ranges:
        if seed in range(src, src + rng):
            return seed - src + dest
    return seed


def new_seeds(
    seeds: list[tuple[int, int]], ranges: list[list[int]]
) -> list[tuple[int, int]]:
    new: list[tuple[int, int]] = []
    while seeds:
        new.append(new_range(seeds, ranges))
    return new


def new_range(seeds: list[tuple[int, int]], ranges: list[list[int]]):
    start, end = seeds.pop()
    for destination, source, value_range in ranges:
        os = max(start, source)
        oe = min(end, source + value_range)
        if os < oe:
            if os > start:
                seeds.append((start, os))
            if end > oe:
                seeds.append((oe, end))
            return (os - source + destination, oe - source + destination)
    return (start, end)


def main():
    """Solves Part 1 and 2 of Day 5"""
    with open(0, encoding="utf-8") as f:
        head, *blocks = f.read().split("\n\n")

    seeds_1 = list(map(int, head.split()[1:]))
    seeds_2 = [
        (seeds_1[i], seeds_1[i] + seeds_1[i + 1]) for i in range(0, len(seeds_1), 2)
    ]

    for block in blocks:
        ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
        seeds_1 = [new_seed(seed, ranges) for seed in seeds_1]

    print(min(seeds_1))

    for block in blocks:
        ranges = [[int(x) for x in line.split()] for line in block.splitlines()[1:]]
        seeds_2 = new_seeds(seeds_2, ranges)
    print(sorted(seeds_2)[0][0])


main()
