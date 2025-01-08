"""Advent of Code - 2024 - Day 13"""
import re

def get_price(m: re.Match[str] | None, part2: bool):
    """returns the cost to win"""
    if not m:
        return 0
    ax, ay, bx, by, px, py = map(int, m.groups())

    if part2:
        px += 10000000000000
        py += 10000000000000

    # i * [ax] + j * [bx] = [px]
    #     [ay]       [by]   [py]

    # [ax bx] * [i] = [px]
    # [ay by] * [j]   [py]

    # [i] = [ax bx]^-1 * [px]
    # [j]   [ay by]      [py]

    # [i] = 1/(det(A)) * [ by -bx] * [px]
    # [j]                [-ay  ax]   [py]

    det = ax*by - ay*bx

    # [i] = 1/det * [ by -bx] * [px]
    # [j]           [-ay  ax]   [py]

    # [i] = [ by/det -bx/det] * [px]
    # [j]   [-ay/det  ax/det]   [py]

    # i = (px * by - py * bx) / det
    # j = (py * ax - px * ay) / det

    wi = px * by - py * bx
    wj = py * ax - px * ay
    if wi % det == 0 and wj % det == 0:
        i = int(wi/det)
        j = int(wj/det)
        return 3*i + j
    return 0

PATTERN = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

with open(0, encoding="utf-8") as f:
    equs = f.read().split("\n\n")
print(sum(get_price(re.match(PATTERN, equ), False) for equ in equs))
print(sum(get_price(re.match(PATTERN, equ), True) for equ in equs))
