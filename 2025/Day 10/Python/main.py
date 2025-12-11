"""Advent of Code - 2025 - Day 10"""

import heapq

import scipy.optimize


def parse_line(line: str) -> tuple[int, list[list[int]], list[int]]:
    """parses a line of input"""
    diagram, *schematics, requirements = line.split()
    positions = (light == "#" for light in diagram[1:-1])
    lights = sum(int(bit) << i for (i, bit) in enumerate(positions))
    buttons = [list(map(int, b[1:-1].split(","))) for b in schematics]
    joltage = list(map(int, requirements[1:-1].split(",")))
    return (lights, buttons, joltage)


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

# Ax = b
# x = A^(+)b + (I-A^(+)A)w

def solve_joltage(buttons: list[list[int]], joltage: list[int]) -> int:
    """solves the number of buttons to press to reach the required joltage"""
    h = len(joltage)
    w = len(buttons)
    a: list[list[int]] = [[int(i in button) for button in buttons] for i in range(h)]
    x = scipy.optimize.linprog([1] * w, A_eq=a, b_eq=joltage, integrality=1)
    out = x.fun
    assert out is not None
    return round(out)


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        machines = list(map(parse_line, f.read().splitlines()))
    print(sum(dijkstra(buttons)[lights] for lights, buttons, _ in machines))
    print(sum(solve_joltage(buttons, joltage) for _, buttons, joltage in machines))


main()
