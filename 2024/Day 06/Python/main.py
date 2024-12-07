from itertools import pairwise


dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def traverse(initial_guard_state: tuple[tuple[int, int], int], obstacles: set[tuple[int, int]], width: int, height: int):
    (guard_pos, turns) = initial_guard_state
    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        yield (guard_pos, turns)
        guard_dir = dirs[turns]
        next_guard_pos = (guard_dir[0] + guard_pos[0], guard_dir[1] + guard_pos[1])
        if (next_guard_pos in obstacles):
            turns = (turns + 1) % 4
        else:
            guard_pos = next_guard_pos

def get_path(initial_guard_state: tuple[tuple[int, int], int], obstacles: set[tuple[int, int]], width: int, height: int):
    return { guard_pos for (guard_pos, _) in traverse(initial_guard_state, obstacles, width, height) }

def detect_loop(initial_guard_state: tuple[tuple[int, int], int], obstacles: set[tuple[int, int]], width: int, height: int):
    state_set: set[tuple[tuple[int, int], int]] = set()
    for (guard_pos, turns) in traverse(initial_guard_state, obstacles, width, height):
        if (guard_pos, turns) in state_set:
            return True
        state_set.add((guard_pos, turns))
    return False

def main():
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

    path: set[tuple[int, int]] = get_path((initial_guard_pos, 0), obstacles, width, height)

    print((len(path)))
    checked: set[tuple[int, int]] = set()
    loops = 0
    for new_start, (obstacle_pos, _) in pairwise(traverse((initial_guard_pos, 0), obstacles, width, height)):
        if obstacle_pos not in checked:
            checked.add(obstacle_pos)
            if detect_loop(new_start, obstacles | {obstacle_pos}, width, height):
                loops+=1
    print(loops)
main()