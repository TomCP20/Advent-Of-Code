"""Advent of Code - 2023 - Day 16"""


def get_directions(direction: tuple[int, int], tile: str) -> list[tuple[int, int]]:
    """Determine the next direction(s) based on the current direction and tile"""
    match tile:
        case ".":
            return [direction]
        case "|":
            return [direction] if direction[1] == 0 else [(1, 0), (-1, 0)]
        case "-":
            return [direction] if direction[0] == 0 else [(0, 1), (0, -1)]
        case "\\":  # (0,1) <-> (1,0)
            return [(direction[1], direction[0])]
        case "/":  # (0,1) <-> (-1,0), (0,-1) <-> (1,0)
            return [(-direction[1], -direction[0])]
        case _:
            assert False


def next_nodes(
    contraption: list[str], pos: tuple[int, int], direction: tuple[int, int]
):
    """Generate the next nodes based pn the current position and direction"""
    for d in get_directions(direction, contraption[pos[0]][pos[1]]):
        next_pos = (pos[0] + d[0], pos[1] + d[1])
        if (0 <= next_pos[0] < len(contraption)) and (
            0 <= next_pos[1] < len(contraption[0])
        ):
            yield (next_pos, d)


def dfs(
    contraption: list[str], start_pos: tuple[int, int], start_direction: tuple[int, int]
):
    """Depth First Search"""
    to_visit = {(start_pos, start_direction)}
    visited: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    while to_visit:
        n = to_visit.pop()
        if n in visited:
            continue
        visited.add(n)
        for node in next_nodes(contraption, *n):
            to_visit.add(node)
    return visited


def count_energized(
    contraption: list[str], start_pos: tuple[int, int], start_direction: tuple[int, int]
):
    """Count the number of tiles energised by the beam"""
    visited = dfs(contraption, start_pos, start_direction)
    energized = {pos for (pos, _) in visited}
    return len(energized)


def main():
    """Solves Part 1 and 2 of Day 16"""
    with open(0, encoding="utf-8") as f:
        contraption = f.read().splitlines()

    print(count_energized(contraption, (0, 0), (0, 1)))

    x_len = len(contraption[0])
    y_len = len(contraption)

    starts: list[tuple[tuple[int, int], tuple[int, int]]] = []

    for x in range(x_len):
        starts.append(((0, x), (1, 0)))
        starts.append(((y_len - 1, x), (-1, 0)))

    for y in range(y_len):
        starts.append(((y, 0), (0, 1)))
        starts.append(((y, x_len - 1), (0, -1)))

    print(max(count_energized(contraption, *s) for s in starts))


main()
