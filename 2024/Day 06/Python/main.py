def part1(initial_guard_pos, obstacles, width, height):
    guard_pos = initial_guard_pos
    guard_path = set()
    turns = 0
    guard_dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        guard_path.add(guard_pos)
        guard_dir = guard_dirs[turns]
        next_guard_pos = (guard_dir[0] + guard_pos[0], guard_dir[1] + guard_pos[1])
        if (next_guard_pos in obstacles):
            turns = (turns + 1) % 4
        else:
            guard_pos = next_guard_pos
    return len(guard_path)

def detect_loop(initial_guard_pos, obstacles, width, height):
    guard_pos = initial_guard_pos
    guard_path = set()
    turns = 0
    guard_dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while 0 <= guard_pos[0] < width and 0 <= guard_pos[1] < height:
        next_pos = (guard_pos, turns)
        if next_pos in guard_path:
            return True
        guard_path.add(next_pos)
        guard_dir = guard_dirs[turns]
        next_guard_pos = (guard_dir[0] + guard_pos[0], guard_dir[1] + guard_pos[1])
        if (next_guard_pos in obstacles):
            turns = (turns + 1) % 4
        else:
            guard_pos = next_guard_pos
    
    return False

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

loop = 0

for y in range(height):
    for x in range(width):
        if (x, y) not in obstacles:
            new_obstacles = obstacles | {(x, y)}
            if detect_loop(initial_guard_pos, new_obstacles, width, height):
                loop +=1
print(loop)