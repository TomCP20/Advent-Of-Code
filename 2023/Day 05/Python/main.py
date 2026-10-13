"""Advent of Code - 2023 - Day 5"""


def new_seed(seed: int, ranges: list[list[int]]):
    for dest, src, rng in ranges:
        if seed in range(src, src + rng):
            return seed - src + dest
    return seed


def main():
    """Solves Part 1 and 2 of Day 5"""
    with open(0, encoding="utf-8") as f:
        head, *blocks = f.read().split("\n\n")

    seeds = list(map(int, head.split()[1:]))

    for block in blocks:
        seeds = [
            new_seed(
                seed, [list(map(int, line.split())) for line in block.splitlines()[1:]]
            )
            for seed in seeds
        ]

    print(min(seeds))


main()
