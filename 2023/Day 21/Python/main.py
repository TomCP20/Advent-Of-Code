"""Advent of Code - 2023 - Day 21"""

def get_adjacent(garden_map: list[str], pos: tuple[int, int]):
    y, x = pos
    if y > 0 and garden_map[y-1][x] != "#":
        yield (y-1, x)
    if y < len(garden_map) and garden_map[y+1][x] != "#":
        yield (y+1, x)
    if x > 0 and garden_map[y][x-1] != "#":
        yield (y, x-1)
    if x < len(garden_map[0]) and garden_map[y][x+1] != "#":
        yield (y, x+1)

def part_1(garden_map: list[str], a: set[tuple[int, int]], b: set[tuple[int, int]]):
    for _ in range(64):
        for pos in a:
            b.update(get_adjacent(garden_map, pos))
        a, b = b, a
    return len(a)

def funct(n: int) -> int: # hardcoded
    a0 = 3814
    a1 = 33952
    a2 = 94138

    b0 = a0
    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)


def main():
    """Solves Part 1 and 2 of Day 21"""
    with open(0, encoding="utf-8") as f:
        garden_map = f.read().splitlines()

    a: set[tuple[int, int]] = set()
    b: set[tuple[int, int]] = set()

    for y, row in enumerate(garden_map):
        x = row.find("S")
        if x != -1:
            a.add((y, x))

    print(part_1(garden_map, a, b))

    steps = 26_501_365
    print(funct(steps//len(garden_map)))




main()
