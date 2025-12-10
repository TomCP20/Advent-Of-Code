"""Advent of Code - 2025 - Day 10"""

import heapq

import z3  # type: ignore


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


def solve_joltage(buttons: list[list[int]], joltage: list[int, ...]) -> int:  # type: ignore
    """solves the number of buttons to press to reach the required joltage"""
    solver = z3.Optimize()
    variables: list[z3.ArithRef] = []
    joltages_var: list[z3.ArithRef | None] = [None] * len(joltage)

    for name, button in enumerate(buttons):
        var = z3.Int(str(name))  # type: ignore
        variables.append(var)
        solver.add(var >= 0)  # type: ignore

        for entry in button:
            if joltages_var[entry] is None:
                joltages_var[entry] = var
            else:
                joltages_var[entry] += var

    for jolt_int, entry in enumerate(joltage):
        if joltages_var[jolt_int] is not None:
            solver.add(joltage[jolt_int] == joltages_var[jolt_int])  # type: ignore

    total_presses = solver.minimize(sum(variables))  # type: ignore

    assert solver.check() == z3.sat  # type: ignore
    return total_presses.value().as_long()  # type: ignore


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        machines = list(map(parse_line, f.read().splitlines()))
    print(sum(dijkstra(buttons)[lights] for lights, buttons, _ in machines))
    print(sum(solve_joltage(buttons, joltage) for _, buttons, joltage in machines))


main()
