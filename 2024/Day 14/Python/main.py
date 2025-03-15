"""Advent of Code - 2024 - Day 14"""

import re


def skip(t: int):
    """skips to state at time t"""
    result: list[tuple[int, int]] = []
    for px, py, vx, vy in drones:
        npx = (px + t * vx) % W
        npy = (py + t * vy) % H
        result.append((npx, npy))
    return result


def print_state(positions: list[tuple[int, int]]):
    """prints state"""
    for cy in range(H):
        print("".join("#" if (cx, cy) in positions else " " for cx in range(W)))


def skip_print_state(t: int):
    """print state at time t"""
    print(f"state after {t} seconds")
    print_state(skip(t))


W = 101
H = 103

PATTERN = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"
drones: list[tuple[int, int, int, int]] = []
with open(0, encoding="utf-8") as f:
    for line in f.read().splitlines():
        if m := re.match(PATTERN, line):
            drones.append(
                (
                    int(m.groups()[0]),
                    int(m.groups()[1]),
                    int(m.groups()[2]),
                    int(m.groups()[3]),
                )
            )

MX = (W - 1) // 2
MY = (H - 1) // 2
q1: int = 0
q2: int = 0
q3: int = 0
q4: int = 0
for x, y in skip(100):
    if x < MX and y < MY:
        q1 += 1
    elif x > MX and y < MY:
        q2 += 1
    elif x < MX and y > MY:
        q3 += 1
    elif x > MX and y > MY:
        q4 += 1

print(q1 * q2 * q3 * q4)

# at 30 there is a horizontal bar that repeats every 103(h) steps
# at 89 there is a vertical bar that repeats every 101(w) steps
# they intersect when t = 30 + a*103 = 89 + b*101
# a = (59 + b*101)/103 where 59 + b*101 is a multiple of 103
# therefore a = 80 b = 81
# therefore they intersect at t = 8270

skip_print_state(8270)
