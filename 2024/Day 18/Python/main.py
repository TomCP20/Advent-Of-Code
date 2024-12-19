from collections import deque

Vec = tuple[int, int]
VecSet = set[Vec]
VecList = list[Vec]
VecQueue = deque[Vec]
DistDict = dict[Vec, int]

def BFS(size: int, corrupted: VecSet) -> (int | None):
    def neighbors(n: Vec):
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new = (n[0] + dir[0], n[1] + dir[1])
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
            if neighbor not in dist.keys():
                dist[neighbor] = dist[current] + 1
                q.append(neighbor)
    return None

#size = 6
#bytes = 12

size = 70
bytes = 1024

all_corrupted: VecList = [(int(line.split(",", 1)[0]), int(line.split(",", 1)[1])) for line in open(0).read().splitlines()]
print(BFS(size, set(all_corrupted[:bytes])))

while BFS(size, set(all_corrupted[:bytes])):
    bytes += 1
print(f"{all_corrupted[bytes-1][0]},{all_corrupted[bytes-1][1]}")