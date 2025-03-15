"""Advent of Code - 2024 - Day 6"""
from itertools import pairwise

type State = tuple[tuple[int, int], int]
type Map = set[tuple[int, int]]

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def traverse(initial_state: State, obstacles: Map, width: int, height: int):
    """simulates the guard traversing the map"""
    (guard_pos, turns) = initial_state
    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        yield (guard_pos, turns)
        guard_dir = dirs[turns]
        next_guard_pos = (guard_dir[0] + guard_pos[0], guard_dir[1] + guard_pos[1])
        if next_guard_pos in obstacles:
            turns = (turns + 1) % 4
        else:
            guard_pos = next_guard_pos

def get_obstacle_pos(initial_state: State, obstacles: Map, width: int, height: int):
    """yields candidate obstacle positions"""
    checked: set[tuple[int, int]] = set()
    for new_start, (obstacle_pos, _) in pairwise(traverse(initial_state, obstacles, width, height)):
        if obstacle_pos not in checked:
            checked.add(obstacle_pos)
            yield (new_start, obstacle_pos)

def detect_loop(initial_state: State, obstacles: Map, width: int, height: int):
    """detects if the guard would make a loop"""
    state_set: set[tuple[tuple[int, int], int]] = set()
    for state in traverse(initial_state, obstacles, width, height):
        if state in state_set:
            return True
        state_set.add(state)
    return False

if __name__ == '__main__':
    with open(0, encoding="utf-8") as f:
        lines: list[str] = f.read().splitlines()
    i_obstacles: Map = set()
    i_state: State = ((-1, -1), -1)
    w: int = len(lines[0])
    h: int = len(lines)
    for (y, line) in enumerate(lines):
        for (x, char) in enumerate(line):
            match char:
                case "#":
                    i_obstacles.add((x, y))
                case "^":
                    i_state = ((x, y), 0)
                case ">":
                    i_state = ((x, y), 1)
                case "v":
                    i_state = ((x, y), 2)
                case "<":
                    i_state = ((x, y), 3)
                case _:
                    pass

    print((len({ pos for (pos, _) in traverse(i_state, i_obstacles, w, h) })))
    loops: int = 0
    for start, obs_pos in get_obstacle_pos(i_state, i_obstacles, w, h):
        if detect_loop(start, i_obstacles | {obs_pos}, w, h):
            loops += 1
    print(loops)
