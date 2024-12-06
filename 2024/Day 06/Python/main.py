def step(guard_pos: tuple[int, int], turns: int, obstacles: set[tuple[int, int]]):
    guard_dir = [(0, -1), (1, 0), (0, 1), (-1, 0)][turns]
    next_guard_pos = (guard_dir[0] + guard_pos[0], guard_dir[1] + guard_pos[1])
    if (next_guard_pos in obstacles):
        return (guard_pos, (turns + 1) % 4)
    else:
        return (next_guard_pos, turns)

def get_path(initial_guard_pos: tuple[int, int], obstacles: set[tuple[int, int]], width: int, height: int):
    guard_pos = initial_guard_pos
    guard_path: set[tuple[int, int]] = set()
    turns = 0
    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        guard_path.add(guard_pos)
        (guard_pos, turns) = step(guard_pos, turns, obstacles)
    return guard_path

def detect_loop(initial_guard_pos: tuple[int, int], obstacles: set[tuple[int, int]], width: int, height: int):
    guard_pos = initial_guard_pos
    state_set: set[tuple[tuple[int, int], int]] = set()
    turns = 0
    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        (guard_pos, turns) = step(guard_pos, turns, obstacles)
        if (guard_pos, turns) in state_set:
            return True
        state_set.add((guard_pos, turns))
    return False

lines: list[str] = (open(0).read().splitlines())
obstacles: set[tuple[int, int]] = set()
initial_guard_pos: tuple[int, int] = (-1, -1)
width: int = len(lines[0])
height: int = len(lines)
for (y, line) in enumerate(lines):
    for (x, char) in enumerate(line):
        if char == "#":
            obstacles.add((x, y))
        elif char == "^":
            initial_guard_pos = (x, y)

path: set[tuple[int, int]] = get_path(initial_guard_pos, obstacles, width, height)

print((len(path)))
print(sum(detect_loop(initial_guard_pos, obstacles | {(x, y)}, width, height) for (x, y) in path - {initial_guard_pos}))