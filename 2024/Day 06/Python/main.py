def part1(initial_guard_pos, obstacles, width, height):
    guard_pos = initial_guard_pos
    guard_path = set()
    turns = 0
    guard_dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        guard_path.add(guard_pos)
        guard_dir = guard_dirs[turns%4]
        next_guard_pos = (guard_dir[0] + guard_pos[0], guard_dir[1] + guard_pos[1])
        if (next_guard_pos in obstacles):
            turns += 1
        else:
            guard_pos = next_guard_pos
    return len(guard_path)

lines = (open(0).read().splitlines())
obstacles = set()
initial_guard_pos = (-1, -1)
width = len(lines[0])
height = len(lines)
for (y, line) in enumerate(lines):
    for (x, char) in enumerate(line):
        if char == "#":
            obstacles.add((x, y))
        elif char == "^":
            initial_guard_pos = (x, y)

print(part1(initial_guard_pos, obstacles, width, height))
