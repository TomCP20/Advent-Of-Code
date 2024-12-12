from itertools import combinations

def get_seed(h, w, checked):
    for y in range(h):
        for x in range(w):
            if (x, y) not in checked:
                return (x, y)
    print("error checked full")
    return (-1, -1)

def get_perimiter(region):
    perimiter = len(region)*4
    for a, b in combinations(region, 2):
        if (abs(a[0] - b[0]) == 1 and a[1] == b[1]) or (abs(a[1] - b[1]) == 1 and a[0] == b[0]):
            perimiter -= 2
    return perimiter


lines = open(0).read().splitlines()

w = len(lines[0])
h = len(lines)

checked = set()

price = 0
while len(checked) < w * h:
    seed = get_seed(h, w, checked)
    q = [seed]
    val = lines[seed[1]][seed[0]]
    region = set()
    while q:
        n = q.pop()
        if val == lines[n[1]][n[0]]:
            region.add(n)
            checked.add(n)
            west = (n[0]-1, n[1])
            if 0 < n[0] and west not in region:
                q.append(west)
            east = (n[0]+1, n[1])
            if n[0] < w-1 and east not in region:
                q.append(east)
            north = (n[0], n[1]-1)
            if 0 < n[1] and north not in region:
                q.append(north)
            south = (n[0], n[1]+1)
            if n[1] < h-1 and south not in region:
                q.append(south)
    area = len(region)
    perimiter = get_perimiter(region)
    price += area * perimiter

print(price)