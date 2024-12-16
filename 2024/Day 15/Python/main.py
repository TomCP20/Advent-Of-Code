def move_box(box_pos: tuple[int, int], dir: tuple[int, int], boxes: set[tuple[int, int]], walls: set[tuple[int, int]]):
    npos = (box_pos[0] + dir[0], box_pos[1] + dir[1])
    if npos in boxes:
        if move_box(npos, dir, boxes, walls):
            boxes.add(npos)
            boxes.remove(box_pos)
            return True
        else:
            return False
    elif npos in walls:
        return False
    else:
        boxes.add(npos)
        boxes.remove(box_pos)
        return True

def display(w: int, h: int, boxes: set[tuple[int, int]], walls: set[tuple[int, int]], robot: tuple[int, int]):
    for y in range(h):
        line = ""
        for x in range(w):
            if (x, y) in walls:
                line += '#'
            elif (x, y) in boxes:
                line += 'O'
            elif (x, y) == robot:
                line += '@'
            else:
                line += '.'
        print(line)



warehouse, moves = open(0).read().split("\n\n")
moves = "".join(moves.splitlines())
warehouse = warehouse.splitlines()
w = len(warehouse[0])
h = len(warehouse)


walls = set()
boxes = set()
robot = (-1, -1)

for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
        if c == '#':
            walls.add((x, y))
        elif c == 'O':
            boxes.add((x, y))
        elif c == '@':
            robot = (x, y)

dirs = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
for move in moves:
    dir = dirs[move]
    npos = (robot[0] + dir[0], robot[1] + dir[1])
    if npos in boxes:
        if move_box(npos, dir, boxes, walls):
            robot = npos
    elif npos not in walls:
        robot = npos

print(sum(100*pos[1] + pos[0] for pos in boxes))