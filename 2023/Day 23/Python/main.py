"""Advent of Code - 2023 - Day 23"""

from itertools import pairwise

type Point = tuple[int, int]


def dfs(graph: dict[Point, dict[Point, int]], start: Point, end: Point):
    """Depth First Search"""
    max_path = 0
    s: list[list[Point]] = []
    s.append([start])
    while s:
        v = s.pop()
        if v[-1] == end:
            max_path = max(max_path, path_len(graph, v))
            continue
        for neighbor in graph[v[-1]]:
            if neighbor not in v:
                new_path = v + [neighbor]
                s.append(new_path)
    return max_path


def path_len(graph: dict[Point, dict[Point, int]], path: list[Point]):
    """Calculate the length of the path"""
    l = 0
    for a, b in pairwise(path):
        l += graph[a][b]
    return l


def generate_neighbors(maze: list[str], point: Point, is_part_1: bool):
    """Find all the valid neighbors of point"""
    y, x = point
    if is_part_1:
        if y > 0 and (maze[y - 1][x] == "." or maze[y - 1][x] == "^"):
            yield (y - 1, x)
        if y < len(maze) - 1 and (maze[y + 1][x] == "." or maze[y + 1][x] == "v"):
            yield (y + 1, x)
        if x > 0 and (maze[y][x - 1] == "." or maze[y][x - 1] == "<"):
            yield (y, x - 1)
        if x < len(maze[0]) - 1 and (maze[y][x + 1] == "." or maze[y][x + 1] == ">"):
            yield (y, x + 1)
    else:
        if y > 0 and (maze[y - 1][x] != "#"):
            yield (y - 1, x)
        if y < len(maze) - 1 and (maze[y + 1][x] != "#"):
            yield (y + 1, x)
        if x > 0 and (maze[y][x - 1] != "#"):
            yield (y, x - 1)
        if x < len(maze[0]) - 1 and (maze[y][x + 1] != "#"):
            yield (y, x + 1)


def adjacent_junctions(
    maze: list[str], point: Point, start: Point, end: Point, is_part_1: bool
):
    """Find all the adjacent junctions"""
    s: list[list[Point]] = []
    s.append([point])
    while s:
        v = s.pop()
        neighbors = list(generate_neighbors(maze, v[-1], is_part_1))
        if (len(neighbors) > 2 or v[-1] == end or v[-1] == start) and len(v) > 1:
            yield (v[-1], len(v) - 1)
            continue
        for neighbor in neighbors:
            if neighbor not in v:
                new_path = v + [neighbor]
                s.append(new_path)


def create_graph(maze: list[str], start: Point, end: Point, is_part_1: bool):
    """Generate a simplified graph of the maze"""
    graph: dict[Point, dict[Point, int]] = {}

    q: list[Point] = [start]

    while q:
        point = q.pop()
        adjacent_nodes = list(adjacent_junctions(maze, point, start, end, is_part_1))
        graph[point] = {}
        for node, distance in adjacent_nodes:
            graph[point][node] = distance
            if node not in graph:
                q.append(node)
    return graph


def main():
    """Solves Part 1 and 2 of Day 23"""
    with open(0, encoding="utf-8") as f:
        maze = f.read().splitlines()
    start = (0, maze[0].index("."))
    end = (len(maze) - 1, maze[len(maze) - 1].index("."))

    print(dfs(create_graph(maze, start, end, True), start, end))
    print(dfs(create_graph(maze, start, end, False), start, end))


main()
