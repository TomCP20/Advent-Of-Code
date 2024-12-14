import re

def skip(drones: list[tuple[int, int, int, int]], w: int, h: int, t: int):
    result = []
    for (px, py, vx, vy) in drones:
        npx = (px + t * vx) % w
        npy = (py + t * vy) % h
        result.append((npx, npy))
    return result

def print_state(positions: list[tuple[int, int]], w: int, h: int):
    for y in range(h):
        print("".join("#" if (x, y) in positions else " " for x in range(w)))

def skip_print_state(t: int, w: int, h: int):
    print(f"state after {t} seconds")
    print_state(skip(drones, w, h, t), w ,h)

w = 101
h = 103

pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
lines = open(0).read().splitlines()
drones = []
for line in lines:
    m = re.match(pattern, line)
    if m:
        drones.append(tuple(map(int, m.groups())))

mx = (w-1)//2
my = (h-1)//2
q1 = 0
q2 = 0
q3 = 0
q4 = 0
for (x, y) in skip(drones, w, h, 100):
    if x < mx and y < my:
        q1 += 1
    elif x > mx and y < my:
        q2 += 1
    elif x < mx and y > my:
        q3 += 1
    elif x > mx and y > my:
        q4 += 1

print(q1 * q2 * q3 * q4)

'''
for i in range(200):
    print(f"state after {i} seconds")
    print_state(skip(drones, w, h, i), w ,h)
'''


# at 30 there is a horizontal bar that repeats every 103(h) steps
# at 89 there is a vertical bar that repeats every 101(w) steps
# they intersect when t = 30 + a*103 = 89 + b*101
# a = (59 + b*101)/103 where 59 + b*101 is a multiple of 103
#therefore a = 80 b = 81
#therefore they intersect at t = 8270

skip_print_state(8270, w, h)
