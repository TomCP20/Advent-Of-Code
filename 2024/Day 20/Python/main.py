from collections import deque
from itertools import combinations

Vec = tuple[int, int]
VecQueue = deque[Vec]
DistDict = dict[Vec, int]

def BFS(end: Vec, maze: list[str]) -> DistDict:
    def neighbors(n: Vec):
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new = (n[0] + dir[0], n[1] + dir[1])
            if 0 <= new[0] < len(maze[0]) and 0 <= new[1] < len(maze) and maze[new[1]][new[0]] != '#':
                yield new
    
    q: VecQueue = deque()
    q.append(end)
    dist: DistDict = {end: 0}

    while q:
        current = q.popleft()
        for neighbor in neighbors(current):
            if neighbor not in dist.keys():
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)
    return dist

def manhattan(a: Vec, b: Vec) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def saves(cheatLen: int, minSave: int, dist: DistDict, a: Vec, b: Vec):
    if dist[a] < dist[b]:
        a, b = b, a
    if dist[a] - dist[b] >= minSave:
        m = manhattan(a, b)
        if m <= cheatLen:
            if dist[a] - dist[b] - m >= minSave:
                return True
    return False

maze = open(0).read().splitlines()
E = (-1, -1)

for y, line in enumerate(maze):
    for x, c in enumerate(line):
        if c == 'E':
            E = (x, y)
dist: DistDict = BFS(E, maze)
minSave = 100
print(sum(1 for (a, b) in combinations(dist, 2) if saves(2, minSave, dist, a, b)))
print(sum(1 for (a, b) in combinations(dist, 2) if saves(20, minSave, dist, a, b)))
