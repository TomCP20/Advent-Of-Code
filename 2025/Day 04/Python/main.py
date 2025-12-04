"""Advent of Code - 2025 - Day 4"""

from typing import Iterator
from itertools import product


Vec = tuple[int, int]


def add_vec(a: Vec, b: Vec) -> Vec:
    """adds 2 vecs together"""
    return (a[0] + b[0], a[1] + b[1])


def get_neighbors(pos: Vec) -> Iterator[Vec]:
    """returns the coords for all neighbors of pos"""
    return (add_vec(pos, d) for d in product([-1, 0, 1], [-1, 0, 1]) if d != (0, 0))


def count_rolls(rolls: set[Vec], pos: Vec) -> int:
    """count the rolls adgacent to pos"""
    return sum(n in rolls for n in get_neighbors(pos))


def get_access_rolls(rolls: set[Vec]) -> set[Vec]:
    """Returns the set of accessable rolls in rolls"""
    return {pos for pos in rolls if count_rolls(rolls, pos) < 4}


def main() -> None:
    """Solves part 1 and 2 of day 4"""
    with open(0, encoding="utf-8") as f:
        grid = f.read().splitlines()
    h: int = len(grid)
    w: int = len(grid[0])
    rolls: set[Vec] = {
        (x, y) for x, y in product(range(w), range(h)) if grid[y][x] == "@"
    }

    access_rolls: set[Vec] = get_access_rolls(rolls)
    print(len(access_rolls))

    solution = 0
    while access_rolls:
        solution += len(access_rolls)
        rolls -= access_rolls
        access_rolls = get_access_rolls(rolls)
    print(solution)


main()
