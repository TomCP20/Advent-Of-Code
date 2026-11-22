"""Advent of Code - 2023 - Day 17"""

from queue import PriorityQueue

import numpy as np


def navigate(grid: np.ndarray[tuple[int, int]], min_val: int, max_val: int) -> int:
    q: PriorityQueue[tuple[int, tuple[int, int, int]]] = PriorityQueue()
    max_y, max_x = (v - 1 for v in grid.shape)
    goal = max_y, max_x
    q.put((0, (0, 0, 0)))
    q.put((0, (0, 0, 1)))
    seen: set[tuple[int, int, int]] = set()
    cost = 0

    while q:
        cost, (y, x, direction) = q.get()
        if (y, x) == goal:
            break
        if (y, x, direction) in seen:
            continue
        seen.add((y, x, direction))
        original_cost = cost
        for s in [-1, 1]:
            cost = original_cost
            new_y, new_x = y, x
            for i in range(1, max_val + 1):
                if direction == 1:
                    new_x = x + i * s
                else:
                    new_y = y + i * s
                if new_x < 0 or new_y < 0 or new_x > max_x or new_y > max_y:
                    break
                cost += grid[new_y, new_x]
                if (new_y, new_x, 1 - direction) in seen:
                    continue
                if i >= min_val:
                    q.put((cost, (new_y, new_x, 1 - direction)))
    return cost


def main():
    """Solves Part 1 and 2 of Day 17"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()
    grid = np.array([[int(char) for char in line] for line in lines])
    print(navigate(grid, 0, 3))
    print(navigate(grid, 4, 10))


main()
