def get_trailheads(topo_map: list[list[int]], w: int, h: int):
    for y in range(h):
        for x in range(w):
            if topo_map[y][x] == 0:
                yield (x, y)

def get_neighbors(x: int, y: int, w: int, h: int):
    if y < h-1:
        yield (x, y+1)
    if y > 0:
        yield (x, y-1)
    if x < w-1:
        yield (x+1, y)
    if x > 0:
        yield (x-1, y)

def DFS(topo_map: list[list[int]], x: int, y: int, w: int, h: int):
    val = topo_map[y][x]
    if val == 9:
        yield (x, y)
    else:
        for (nx, ny) in get_neighbors(x, y, w, h):
            if topo_map[ny][nx] == val+1:
                yield from DFS(topo_map, nx, ny, w, h)

topo_map = [list(map(int, line)) for line in open(0).read().splitlines()]
w = len(topo_map[0])
h = len(topo_map)

print(sum(len(set(DFS(topo_map, x, y, w, h))) for (x, y) in get_trailheads(topo_map, w, h)))
print(sum(len(list(DFS(topo_map, x, y, w, h))) for (x, y) in get_trailheads(topo_map, w, h)))