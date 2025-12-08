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


def dfs(point: Point, edges: dict[Point, list[Point]]):
    """Depth First Search"""
    stack: list[Point] = [point]
    visited: set[Point] = set()
    while stack:
        point = stack.pop()
        if point not in visited:
            visited.add(point)
            for neighbor in edges[point]:
                stack.append(neighbor)
    return visited


def get_island_sizes(edges: dict[Point, list[Point]]) -> list[int]:
    """returns the size of all islands"""
    visited: set[Point] = set()
    sizes: list[int] = []
    for point in edges:
        if point not in visited:
            component = dfs(point, edges)
            visited.update(component)
            sizes.append(len(component))
    return sizes


def main():
    """main"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    positions = set(map(parse_line, lines))
    pairs = sorted(combinations(positions, 2), key=dist)
    edges: dict[Point, list[Point]] = defaultdict(list)
    for i, (a, b) in enumerate(pairs):
        edges[a].append(b)
        edges[b].append(a)
        if i == (10 if len(lines) == 20 else 1000): # part 1
            print(prod(sorted(get_island_sizes(edges), reverse=True)[:3]))
        if len(edges) == len(positions) == len(dfs(pairs[0][0], edges)): # part 2
            print(a[0] * b[0])
            break


main()
