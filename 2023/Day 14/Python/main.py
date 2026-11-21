"""Advent of Code - 2023 - Day 14"""

import re

CYCLES = 1_000_000_000


def tilt_grid(grid: list[str], reverse: bool):
    """Tilt the grid"""
    return [
        re.sub(r"[O.]+", lambda x: "".join(sorted(x.group(), reverse=reverse)), line)
        for line in grid
    ]


def transpose_grid(grid: list[str]):
    """Transpose the grid"""
    return ["".join(line[i] for line in grid) for i in range(len(grid[0]))]


def part_1(rows: list[str]):
    """Solves 2023 Day 14 Part 1"""
    cols = transpose_grid(rows)
    cols = tilt_grid(cols, True)
    return sum(sum(len(col) - i for i, c in enumerate(col) if c == "O") for col in cols)


def cycle(rows: list[str]) -> list[str]:
    """Cycle the grid by tilting it in each of the 4 cardinal directions."""
    cols = transpose_grid(rows)
    cols = tilt_grid(cols, True)
    rows = transpose_grid(cols)
    rows = tilt_grid(rows, True)
    cols = transpose_grid(rows)
    cols = tilt_grid(cols, False)
    rows = transpose_grid(cols)
    rows = tilt_grid(rows, False)
    return rows


def part_2(rows: list[str]):
    """Solves 2023 Day 14 Part 2"""
    visited: list[list[str]] = []
    cycle_start = 0
    cycle_end = 0
    for i in range(CYCLES):
        visited.append(rows)
        rows = cycle(rows)
        if rows in visited:
            cycle_start = visited.index(rows)
            cycle_end = i
            break

    cycle_len = cycle_end - cycle_start + 1

    offset = (CYCLES - cycle_start) % cycle_len
    vi = cycle_start + offset
    return sum(
        sum(len(rows) - i for c in row if c == "O") for i, row in enumerate(visited[vi])
    )


def main():
    """Solves Part 1 and 2 of Day 14"""
    with open(0, encoding="utf-8") as f:
        rows = f.read().splitlines()
    print(part_1(rows))
    print(part_2(rows))


main()
