"""Advent of Code - 2025 - Day 10"""

import heapq


def parse_line(line: str) -> tuple[int, list[list[int]]]:
    """parses a line of input"""
    diagram, *schematics, _ = line.split()
    lights = (light == "#" for light in diagram[1:-1])
    goal = sum(int(bit) << i for (i, bit) in enumerate(lights))
    buttons: list[list[int]] = [list(map(int, b[1:-1].split(","))) for b in schematics]
    return (goal, buttons)


def dijkstra(buttons: list[list[int]]):
    """Dijkstra's algorithm"""
    dist: dict[int, int] = {0: 0}
    prev: dict[int, int] = {}
    q: list[tuple[int, int]] = []
    heapq.heappush(q, (0, 0))

    while q:
        _, node = heapq.heappop(q)
        for button in buttons:
            neighbor = node ^ sum(1 << k for k in button)
            alt = dist[node] + 1
            if neighbor not in dist or alt < dist[neighbor]:
                prev[neighbor] = node
                dist[neighbor] = alt
                heapq.heappush(q, (alt, neighbor))

    return dist


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        machines = list(map(parse_line, f.read().splitlines()))
    print(sum(dijkstra(buttons)[goal] for goal, buttons in machines))


main()
