type Vec = tuple[int, int]
type State = tuple[Vec, int]

def add(a: Vec, b: Vec) -> Vec:
    return (a[0] + b[0], a[1] + b[1])

def h(n: State, end: Vec):
    return abs(n[0][0] - end[0]) + abs(n[0][1] - end[1])

def a_star(start: State, end: Vec, maze: list[str]):
    openSet = {start}

    gScore = {start: 0}

    fScore = {start: h(start, end)}

    while openSet:
        current = min(openSet, key=lambda x: fScore[x])
        if current[0] == end:
            return gScore[current]
        openSet.remove(current)
        for neighbor, d in get_neighbors(current, maze):
            tentative_gScore = gScore[current] + d
            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor, end)
                openSet.add(neighbor)
    return None

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

dist = a_star((start, 0), end, maze)
print(dist)