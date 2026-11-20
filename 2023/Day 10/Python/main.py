"""Advent of Code - 2023 - Day 10"""


def find_start(maze: list[str]) -> tuple[int, int]:
    for y, row in enumerate(maze):
        x = row.find("S")
        if x != -1:
            return (x, y)
    assert False


def get_adjacent(maze: list[str], start_pos: tuple[int, int]):
    x, y = start_pos
    if x > 0:
        yield (x - 1, y)  # West
    if x < len(maze[0]):
        yield (x + 1, y)  # East
    if y > 0:
        yield (x, y - 1)  # South
    if y < len(maze):
        yield (x, y + 1)  # North


def get_connected(maze: list[str], pos: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = pos
    shape = maze[y][x]
    match shape:
        case "|":
            return [(x, y + 1), (x, y - 1)]
        case "-":
            return [(x + 1, y), (x - 1, y)]
        case "L":
            return [(x, y - 1), (x + 1, y)]
        case "J":
            return [(x, y - 1), (x - 1, y)]
        case "7":
            return [(x - 1, y), (x, y + 1)]
        case "F":
            return [(x + 1, y), (x, y + 1)]
        case "S":
            out: list[tuple[int, int]] = []
            for xc, yc in get_adjacent(maze, pos):
                if maze[yc][xc] in "|-LJ7F":
                    connected = get_connected(maze, (xc, yc))
                    if connected and pos in connected:
                        out.append((xc, yc))
            return out
        case _:
            assert False, f"invalid case {shape}"


def get_next_node(
    maze: list[str], node: tuple[int, int], visited: set[tuple[int, int]]
):
    for next_node in get_connected(maze, node):
        if next_node not in visited:
            return next_node
    return None


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        maze = f.read().splitlines()
    node = find_start(maze)
    visited: set[tuple[int, int]] = set()

    while node:
        visited.add(node)
        node = get_next_node(maze, node, visited)

    print(len(visited) // 2)

    enclosed: set[tuple[int, int]] = set()
    for y, row in enumerate(maze):
        inside = False
        for x, pipe in enumerate(row):
            pos = (x, y)
            if pos in visited:
                # The S here is exclusively for the case where it replaces an |, L or J.
                # It should be removed otherwise.
                if pipe in "|LJS":
                    inside = not inside
            elif inside:
                enclosed.add(pos)
    print(len(enclosed))


main()
