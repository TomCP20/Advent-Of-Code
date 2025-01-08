"""Advent of Code - 2024 - Day 18"""
from collections import deque

Vec = tuple[int, int]
VecSet = set[Vec]
VecList = list[Vec]
VecQueue = deque[Vec]
DistDict = dict[Vec, int]

def bfs(size: int, corrupted: VecSet) -> (int | None):
    """breadth first search"""
    def neighbors(n: Vec):
        for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
            new = (n[0] + direction[0], n[1] + direction[1])
            if (new not in corrupted) and 0 <= new[0] <= size and 0 <= new[1] <= size:
                yield new

    q: VecQueue = deque()
    q.append((0, 0))
    dist: DistDict = {(0, 0): 0}

    while q:
        current = q.popleft()
        if current == (size, size):
            return dist[current]
        for neighbor in neighbors(current):
            if neighbor not in dist:
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)
    return None

def binary_search(array: VecList, low: int, high: int):
    """binary search"""
    while low <= high:
        mid = (low + high) // 2
        if bfs(SIZE, set(array[:(mid+1)])):
            low = mid + 1
        elif low != mid:
            high = mid
        else:
            return mid
    assert False

#SIZE = 6
#BYTES = 12

SIZE = 70
BYTES = 1024

def parse_line(line: str):
    """parse a line of the input"""
    line_split = list(map(int, line.split(",")))
    return (line_split[0], line_split[1])

with open(0, encoding="utf-8") as f:
    all_corrupted = list(map(parse_line, f.read().splitlines()))
print(bfs(SIZE, set(all_corrupted[:BYTES])))

s = binary_search(all_corrupted, BYTES+1, len(all_corrupted)-1)
print(f"{all_corrupted[s][0]},{all_corrupted[s][1]}")
