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

def get_obstacle_pos(initial_guard_state: tuple[tuple[int, int], int], obstacles: set[tuple[int, int]], width: int, height: int):
    checked: set[tuple[int, int]] = set()
    for new_start, (obstacle_pos, _) in pairwise(traverse(initial_guard_state, obstacles, width, height)):
        if obstacle_pos not in checked:
            checked.add(obstacle_pos)
            yield (new_start, obstacle_pos)

def detect_loop(initial_guard_state: tuple[tuple[int, int], int], obstacles: set[tuple[int, int]], width: int, height: int):
    state_set: set[tuple[tuple[int, int], int]] = set()
    for state in traverse(initial_guard_state, obstacles, width, height):
        if state in state_set:
            return True
        state_set.add(state)
    return False

def main():
    lines: list[str] = (open(0).read().splitlines())
    obstacles: set[tuple[int, int]] = set()
    initial_guard_state: tuple[tuple[int, int], int] = ((-1, -1), -1)
    w: int = len(lines[0])
    h: int = len(lines)
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(line):
            match char:
                case "#":
                    obstacles.add((x, y))
                case "^":
                    initial_guard_state = ((x, y), 0)
                case ">":
                    initial_guard_state = ((x, y), 1)
                case "v":
                    initial_guard_state = ((x, y), 2)
                case "<":
                    initial_guard_state = ((x, y), 3)

    print((len({ guard_pos for (guard_pos, _) in traverse(initial_guard_state, obstacles, w, h) })))
    print(sum(detect_loop(state, obstacles | {obstacle_pos}, w, h) for state, obstacle_pos in get_obstacle_pos(initial_guard_state, obstacles, w, h)))
main()