"""Advent of Code - 2025 - Day 4"""

from typing import Iterator


Vec = tuple[int, int]


def add_vec(a: Vec, b: Vec) -> Vec:
    """adds 2 vecs together"""
    ax, ay = a
    bx, by = b
    return (ax + bx, ay + by)


def get_neighbors(pos: Vec) -> Iterator[Vec]:
    """returns the coords for all neighbors of pos"""
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            d = (dx, dy)
            if d == (0, 0):
                continue
            yield add_vec(pos, d)


def count_rolls(rolls: set[Vec], pos: Vec) -> int:
    """count the rolls adgacent to pos"""
    count = sum(1 for n in get_neighbors(pos) if n in rolls)
    return count

def get_access_rolls(rolls: set[Vec], h: int, w: int) -> set[Vec]:
    """Returns the set of accessable rolls in rolls"""
    access_rolls: set[Vec] = set()
    for y in range(h):
        for x in range(w):
            if (x, y) in rolls and count_rolls(rolls, (x, y)) < 4:
                access_rolls.add((x, y))
    return access_rolls

def main():
    """Solves part 1 and 2 of day 4"""

    with open(0, encoding="utf-8") as f:
        grid = f.read().splitlines()

    h: int = len(grid)
    w: int = len(grid[0])

    rolls: set[Vec] = set()
    for y, row in enumerate(grid):
        for x, space in enumerate(row):
            if space == "@":
                rolls.add((x, y))


    access_rolls: set[Vec] = get_access_rolls(rolls, h, w)
    print(len(access_rolls))
    solution = 0
    while access_rolls:
        solution += len(access_rolls)
        rolls -= access_rolls
        access_rolls: set[Vec] = get_access_rolls(rolls, h, w)
    print(solution)


main()
