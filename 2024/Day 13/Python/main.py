def get_seed(h, w, checked):
    for y in range(h):
        for x in range(w):
            if (x, y) not in checked:
                return (x, y)
    print("error checked full")
    return (-1, -1)

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
    perimiter = 0
    while q:
        n = q.pop()
        if n not in region:
            region.add(n)
            checked.add(n)
            west = (n[0]-1, n[1])
            if 0 < n[0] and val == lines[west[1]][west[0]]:
                q.append(west)
            else:
                perimiter += 1
            east = (n[0]+1, n[1])
            if n[0] < w-1 and val == lines[east[1]][east[0]]:
                q.append(east)
            else:
                perimiter += 1
            north = (n[0], n[1]-1)
            if 0 < n[1] and val == lines[north[1]][north[0]]:
                q.append(north)
            else:
                perimiter += 1
            south = (n[0], n[1]+1)
            if n[1] < h-1 and val == lines[south[1]][south[0]]:
                q.append(south)
            else:
                perimiter += 1
    area = len(region)
    price += area * perimiter

print(price)