"""Advent of Code - 2025 - Day 9"""


from itertools import combinations

Point = tuple[int, int]
Rect = tuple[Point, Point]


def parse_line(line: str) -> Point:
    """Parses a line of input"""
    x, y = line.split(",")
    return (int(x), int(y))

def rectangle_area(rect: Rect) -> int:
    """Calculates the area of a rectangle"""
    (ax, ay), (bx, by) = rect
    dx = abs(ax-bx) + 1
    dy = abs(ay-by) + 1
    return dx*dy


with open(0, encoding="utf-8") as f:
    lines = f.read().splitlines()
tiles = list(map(parse_line, lines))
rectangles = list(combinations(tiles, 2))
areas = list(map(rectangle_area, rectangles))
print(max(areas))
