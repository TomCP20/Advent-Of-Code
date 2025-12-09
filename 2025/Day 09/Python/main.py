"""Advent of Code - 2025 - Day 9"""

from itertools import combinations, pairwise

Point = tuple[int, int]
Rect = tuple[Point, Point]
Line = tuple[int, int, int]


def parse_line(line: str) -> Point:
    """Parses a line of input"""
    x, y = line.split(",")
    return (int(x), int(y))


def rectangle_area(rect: Rect) -> int:
    """Calculates the area of a rectangle"""
    (ax, ay), (bx, by) = rect
    dx = abs(ax - bx) + 1
    dy = abs(ay - by) + 1
    return dx * dy


def intersect(vert: list[Line], hori: list[Line], rect: Rect):
    """checks if any lines intersects rect"""
    (ax, ay), (bx, by) = rect
    min_x = min(ax, bx) + 0.5
    max_x = max(ax, bx) - 0.5
    min_y = min(ay, by) + 0.5
    max_y = max(ay, by) - 0.5
    if any(vert_intersect(line, min_x, max_x, min_y, max_y) for line in vert):
        return True
    if any(hori_intersect(line, min_x, max_x, min_y, max_y) for line in hori):
        return True
    return False


def vert_intersect(line: Line, min_x: float, max_x: float, min_y: float, max_y: float):
    """checks if a vertical lines intersects rect"""
    v_x, min_v_y, max_v_y = line
    return min_x <= v_x <= max_x and (
        min_v_y <= min_y <= max_v_y or min_v_y <= max_y <= max_v_y
    )


def hori_intersect(line: Line, min_x: float, max_x: float, min_y: float, max_y: float):
    """checks if any vertical lines intersects rect"""
    h_y, min_h_x, max_h_x = line
    return min_y <= h_y <= max_y and (
        min_h_x <= min_x <= max_h_x or min_h_x <= max_x <= max_h_x
    )


def main():
    """Solves Part 1 and 2 of Day 9"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    tiles = list(map(parse_line, lines))
    rectangles = list(combinations(tiles, 2))
    areas = list(map(rectangle_area, rectangles))

    print(max(areas))

    sorted_rectangles = sorted(rectangles, key=rectangle_area, reverse=True)

    edges = list(pairwise(tiles + [tiles[0]]))
    vert = [(ax, min(ay, by), max(ay, by)) for (ax, ay), (bx, by) in edges if ax == bx]
    hori = [(ay, min(ax, bx), max(ax, bx)) for (ax, ay), (bx, by) in edges if ay == by]

    for rect in sorted_rectangles:
        if not intersect(vert, hori, rect):
            print(rectangle_area(rect))
            break


main()
