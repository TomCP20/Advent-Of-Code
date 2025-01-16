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

    def get_path(state: State):
        if state[0] == start_state[0]:
            yield [state]
            return
        for prev_state in prev[state]:
            for path in get_path(prev_state):
                yield path + [state]

    return dist_map[current], get_path(current)


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

dist, paths = dijkstra((start, 0), end)

print(dist)
print(len({state[0] for path in paths for state in path}))
