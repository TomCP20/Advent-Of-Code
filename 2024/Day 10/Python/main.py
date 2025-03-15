"""Advent of Code - 2024 - Day 10"""
from typing import Iterable


def get_trailheads():
    """yields all trailheads on the map"""
    for y in range(h):
        for x in range(w):
            if topo_map[y][x] == 0:
                yield (x, y)

def get_neighbors(x: int, y: int):
    """yields all von Neumann neighbors"""
    if y < h-1:
        yield (x, y+1)
    if y > 0:
        yield (x, y-1)
    if x < w-1:
        yield (x+1, y)
    if x > 0:
        yield (x-1, y)

def dfs(x: int, y: int) -> Iterable[tuple[int, int]]:
    """Depth First Search"""
    val = topo_map[y][x]
    if val == 9:
        yield (x, y)
    else:
        for (nx, ny) in get_neighbors(x, y):
            if topo_map[ny][nx] == val+1:
                yield from dfs(nx, ny)

with open(0, encoding="utf-8") as f:
    topo_map = [list(map(int, line)) for line in f.read().splitlines()]
w = len(topo_map[0])
h = len(topo_map)

print(sum(len(set(dfs(x, y))) for (x, y) in get_trailheads()))
print(sum(len(list(dfs(x, y))) for (x, y) in get_trailheads()))
