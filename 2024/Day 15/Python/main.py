"""Advent of Code - 2024 - Day 15"""

type Vec = tuple[int, int]

def add(a: Vec, b: Vec):
    """adds 2 Vecs together"""
    return (a[0] + b[0], a[1] + b[1])

def move_box1(box_pos: Vec, d: Vec, boxes: set[Vec], walls: set[Vec]):
    """moves a box using part 1 rules"""
    next_pos = add(box_pos, d)
    if next_pos in walls or (next_pos in boxes and not move_box1(next_pos, d, boxes, walls)):
        return False
    boxes.add(next_pos)
    boxes.remove(box_pos)
    return True

def move_box2(box_pos: Vec, d: Vec, boxes: set[Vec], walls: set[Vec]):
    """moves a box using part 2 rules"""
    next_pos = add(box_pos, d)

    if d == (1, 0): # right
        if add(box_pos, (2, 0)) in walls:
            return False
        if add(box_pos, (2, 0)) in boxes:
            if move_box2(add(box_pos, (2, 0)), d, boxes, walls):
                boxes.add(next_pos)
                boxes.remove(box_pos)
                return True
            return False
        boxes.add(next_pos)
        boxes.remove(box_pos)
        return True
    if d == (-1, 0): # left
        if next_pos in walls:
            return False
        if add(box_pos, (-2, 0)) in boxes:
            if move_box2(add(box_pos, (-2, 0)), d, boxes, walls):
                boxes.add(next_pos)
                boxes.remove(box_pos)
                return True
            return False
        boxes.add(next_pos)
        boxes.remove(box_pos)
        return True
    # up or down
    if next_pos in walls or add(next_pos, (1, 0)) in walls:
        return False

    il = check_intersect(next_pos, boxes)
    ir = check_intersect(add(next_pos, (1, 0)), boxes)
    if il and ir:
        if il != ir:
            copy_boxes = boxes.copy()
            if move_box2(il, d, copy_boxes, walls) and move_box2(ir, d, copy_boxes, walls):
                boxes.clear()
                boxes |= copy_boxes
                boxes.add(next_pos)
                boxes.remove(box_pos)
                return True
            return False
        if move_box2(il, d, boxes, walls):
            boxes.add(next_pos)
            boxes.remove(box_pos)
            return True
        return False
    if il:
        if move_box2(il, d, boxes, walls):
            boxes.add(next_pos)
            boxes.remove(box_pos)
            return True
        return False
    if ir:
        if move_box2(ir, d, boxes, walls):
            boxes.add(next_pos)
            boxes.remove(box_pos)
            return True
        return False
    boxes.add(next_pos)
    boxes.remove(box_pos)
    return True

def check_intersect(pos, boxes):
    """checks if pos intersects with a box"""
    if pos in boxes:
        return pos
    if add(pos, (-1, 0)) in boxes:
        return add(pos, (-1, 0))
    return None

with open(0, encoding="utf-8") as f:
    warehouse, moves = f.read().split("\n\n")
moves: str = "".join(moves.splitlines())
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
    direction = dirs[move]
    npos = (robot1[0] + direction[0], robot1[1] + direction[1])
    if npos in boxes1:
        if move_box1(npos, direction, boxes1, walls1):
            robot1 = npos
    elif npos not in walls1:
        robot1 = npos

print(sum(100*pos[1] + pos[0] for pos in boxes1))

for move in moves:
    direction = dirs[move]
    npos = add(robot2, direction)
    intersect = check_intersect(npos, boxes2)
    if intersect:
        if move_box2(intersect, direction, boxes2, walls2):
            robot2 = npos
    elif npos not in walls2:
        robot2 = npos

print(sum(100*pos[1] + pos[0] for pos in boxes2))
