import re

def get_price(m: re.Match[str] | None, part2: bool):
    if not m:
        return 0
    ax = int(m.group(1))
    ay = int(m.group(2))
    bx = int(m.group(3))
    by = int(m.group(4))
    px = int(m.group(5))
    py = int(m.group(6))

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
        return (3*i + j)
    return 0

pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

input = open(0).read().split("\n\n")
print(sum(get_price(re.match(pattern, equ), False) for equ in input))
print(sum(get_price(re.match(pattern, equ), True) for equ in input))