"""Advent of Code - 2025 - Day 8"""

from collections import defaultdict
from itertools import combinations
from math import prod


Point = tuple[int, int, int]


def parse_line(line: str) -> Point:
    """Parses a line into a 3d point"""
    x, y, z = line.split(",")
    return (int(x), int(y), int(z))


def dist(pair: tuple[Point, Point]) -> int:
    """gives the squared distance between a pair of points"""
    (x1, y1, z1), (x2, y2, z2) = pair
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def part_1(n: int, sorted_paris: list[tuple[Point, Point]]):
    """Solves Part 1"""
    edges: dict[Point, list[Point]] = defaultdict(list)
    for a, b in sorted_paris[:n]:
        edges[a].append(b)
        edges[b].append(a)

    visited: set[Point] = set()
    sizes: list[int] = []
    for point in edges:
        if point not in visited:
            stack: list[Point] = [point]
            size: int = 0
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    size += 1
                    for neighbor in edges[node]:
                        stack.append(neighbor)
            sizes.append(size)
    return prod(sorted(sizes, reverse=True)[:3])


def main():
    """main"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    n: int = 10 if len(lines) == 20 else 1000
    positions = set(map(parse_line, lines))
    pairs = combinations(positions, 2)
    sorted_paris = sorted(pairs, key=dist)
    print(part_1(n, sorted_paris))


main()
