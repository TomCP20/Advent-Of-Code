from heapq import heappop, heappush


type Vec = tuple[int, int]
type State = tuple[Vec, int]

def add(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1])

def Dijkstra(start: State, end: Vec, maze: list[str]):
    Q: list[tuple[int, State]] = []
    dist = {start: 0}
    heappush(Q, (0, start))
    prev: dict[State, set[State]] = dict()

    while Q:
        _, current = heappop(Q)

        if current[0] == end:
            break

        for neighbor, d in get_neighbors(current, maze):
            alt = dist[current] + d
            if alt < dist.get(neighbor, float("inf")):
                prev[neighbor] = {current}
                dist[neighbor] = alt
                heappush(Q, (alt, neighbor))
            elif alt == dist.get(neighbor, float("inf")):
                prev[neighbor].add(current)
    

    def get_path(state: State):
        if state[0] == start[0]:
            yield [state]
            return
        for prev_state in prev[state]:
            for path in get_path(prev_state):
                yield path + [state]
    
    return dist[current], get_path(current)


def get_neighbors(n: State, maze: list[str]):
    pos, turns = n
    dir = dirs[turns]
    npos = add(pos, dir)
    if maze[npos[1]][npos[0]] != '#':
        yield ((npos, turns), 1)
    yield ((pos, (turns + 1)%4), 1000)
    yield ((pos, (turns - 1)%4), 1000)


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

maze = open(0).read().splitlines()
start = (-1, -1)
end = (-1, -1)
for y, line in enumerate(maze):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
        elif c == "E":
            end = (x, y)

dist, paths = Dijkstra((start, 0), end, maze)

print(dist)
print(len({state[0] for path in paths for state in path}))