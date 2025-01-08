"""Advent of Code - 2024 - Day 20"""
from collections import deque
from itertools import combinations

Vec = tuple[int, int]
VecQueue = deque[Vec]
DistDict = dict[Vec, int]

def bfs() -> DistDict:
    "breadth first search"
    def neighbors(n: Vec):
        for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
            new = (n[0] + direction[0], n[1] + direction[1])
            if 0 <= new[0] < w and 0 <= new[1] < h and maze[new[1]][new[0]] != '#':
                yield new

    q: VecQueue = deque()
    q.append(end)
    dist: DistDict = {end: 0}

    while q:
        current = q.popleft()
        for neighbor in neighbors(current):
            if neighbor not in dist:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)
    return dist

def manhattan(a: Vec, b: Vec) -> int:
    """returns the manhattan distance between a and b"""
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def saves(cheat_len: int, dist: DistDict, a: Vec, b: Vec):
    """calculates if the cheat saves enough time"""
    if dist[a] < dist[b]:
        a, b = b, a
    if dist[a] - dist[b] >= MIN_SAVE:
        m = manhattan(a, b)
        if m <= cheat_len:
            if dist[a] - dist[b] - m >= MIN_SAVE:
                return True
    return False

with open(0, encoding="utf-8") as f:
    maze = f.read().splitlines()

h = len(maze)
w = len(maze[0])

end = (-1, -1)

for y, line in enumerate(maze):
    for x, c in enumerate(line):
        if c == 'E':
            end = (x, y)
res: DistDict = bfs()
MIN_SAVE = 100
print(sum(1 for (a, b) in combinations(res, 2) if saves(2, res, a, b)))
print(sum(1 for (a, b) in combinations(res, 2) if saves(20, res, a, b)))
