def add(a: tuple[int, int], b: tuple[int, int]):
    return (a[0] + b[0], a[1] + b[1])

def move_box1(box_pos: tuple[int, int], dir: tuple[int, int], boxes: set[tuple[int, int]], walls: set[tuple[int, int]]):
    npos = add(box_pos, dir)
    if npos in walls or (npos in boxes and not move_box1(npos, dir, boxes, walls)):
        return False
    boxes.add(npos)
    boxes.remove(box_pos)
    return True

def move_box2(box_pos: tuple[int, int], dir: tuple[int, int], boxes: set[tuple[int, int]], walls: set[tuple[int, int]]):
    npos = add(box_pos, dir)
    if npos in walls or (npos in boxes and not move_box1(npos, dir, boxes, walls)):
        return False
    boxes.add(npos)
    boxes.remove(box_pos)
    return True


def display1(w: int, h: int, boxes: set[tuple[int, int]], walls: set[tuple[int, int]], robot: tuple[int, int]):
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


def display2(w: int, h: int, boxes: set[tuple[int, int]], walls: set[tuple[int, int]], robot: tuple[int, int]):
    for y in range(h):
        line = ""
        for x in range(w*2):
            if (x, y) in walls:
                line += '#'
            elif (x, y) in boxes:
                line += '['
            elif (x-1, y) in boxes:
                line += ']'
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


walls1 = set()
boxes1 = set()
robot1 = (-1, -1)
walls2 = set()
boxes2 = set()
robot2 = (-1, -1)

for y, line in enumerate(warehouse):
    for x, c in enumerate(line):
        if c == '#':
            walls1.add((x, y))
            walls2.add((2*x, y))
            walls2.add((2*x+1, y))
        elif c == 'O':
            boxes1.add((x, y))
            boxes2.add((2*x, y))
        elif c == '@':
            robot1 = (x, y)
            robot2 = (2*x, y)

dirs = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
for move in moves:
    dir = dirs[move]
    npos = (robot1[0] + dir[0], robot1[1] + dir[1])
    if npos in boxes1:
        if move_box1(npos, dir, boxes1, walls1):
            robot1 = npos
    elif npos not in walls1:
        robot1 = npos

print(sum(100*pos[1] + pos[0] for pos in boxes1))

display2(w, h, boxes2, walls2, robot2)