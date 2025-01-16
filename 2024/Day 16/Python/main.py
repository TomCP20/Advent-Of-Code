"""Advent of Code - 2024 - Day 16"""
from heapq import heappop, heappush


type Vec = tuple[int, int]
type State = tuple[Vec, int]

def add(a: Vec, b: Vec) -> Vec:
    """adds 2 vecs"""
    return (a[0] + b[0], a[1] + b[1])

def dijkstra(start_state: State, goal: Vec):
    """dijkstra's algorithm"""
    q: list[tuple[int, State]] = []
    dist_map = {start_state: 0}
    heappush(q, (0, start_state))
    prev: dict[State, set[State]] = {}

    while q:
        _, current = heappop(q)

        if current[0] == goal:
            break

        for neighbor, d in get_neighbors(current):
            alt = dist_map[current] + d
            if alt < dist_map.get(neighbor, float("inf")):
                prev[neighbor] = {current}
                dist_map[neighbor] = alt
                heappush(q, (alt, neighbor))
            elif alt == dist_map.get(neighbor, float("inf")):
                prev[neighbor].add(current)

    return dist_map[current], len(dfs(prev, current))

def dfs(prev, current):
    """Depth First Search to find all unique positions"""
    s = [current]
    tiles: set[Vec] = set()
    while s:
        v = s.pop()
        tiles.add(v[0])
        s.extend(p for p in prev[v] if p in prev)
    return tiles


def get_neighbors(n: State):
    """gets neighbors of n"""
    pos, turns = n
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)][turns]
    npos = add(pos, direction)
    if maze[npos[1]][npos[0]] != '#':
        yield ((npos, turns), 1)
    yield ((pos, (turns + 1)%4), 1000)
    yield ((pos, (turns - 1)%4), 1000)

with open(0, encoding="utf-8") as f:
    maze = f.read().splitlines()
start = (-1, -1)
end = (-1, -1)
for y, line in enumerate(maze):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)

dist, unique_tiles = dijkstra((start, 0), end)
print(dist)
print(unique_tiles)
