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
price1 = 0
price2 = 0
while len(checked) < w * h:
    seed = get_seed(h, w, checked)
    q = [seed]
    val = lines[seed[1]][seed[0]]
    region = set()
    perimiter = 0
    corners = 0
    while q:
        n = q.pop()
        if n not in region:
            region.add(n)
            checked.add(n)
            west = (n[0]-1, n[1])
            left = 0 < n[0] and val == lines[west[1]][west[0]]
            if left:
                q.append(west)
            else:
                perimiter += 1
            east = (n[0]+1, n[1])
            right = n[0] < w-1 and val == lines[east[1]][east[0]]
            if right:
                q.append(east)
            else:
                perimiter += 1
            north = (n[0], n[1]-1)
            up = 0 < n[1] and val == lines[north[1]][north[0]]
            if up:
                q.append(north)
            else:
                perimiter += 1
            south = (n[0], n[1]+1)
            down = n[1] < h-1 and val == lines[south[1]][south[0]]
            if down:
                q.append(south)
            else:
                perimiter += 1
            
            neighbors = left + right + up + down
            if neighbors == 0:
                corners += 4
            elif neighbors == 1:
                corners += 2
            elif neighbors == 2:
                if up and left:
                    corners += 1
                    if lines[n[1]-1][n[0]-1] != val:
                        corners += 1
                elif up and right:
                    corners += 1
                    if lines[n[1]-1][n[0]+1] != val:
                        corners += 1
                elif down and right:
                    corners += 1
                    if lines[n[1]+1][n[0]+1] != val:
                        corners += 1
                elif down and left:
                    corners += 1
                    if lines[n[1]+1][n[0]-1] != val:
                        corners += 1
            elif neighbors == 3:
                corners += 0 #TODO
                if not up:
                    if lines[n[1]+1][n[0]+1] != val:
                        corners += 1
                    if lines[n[1]+1][n[0]-1] != val:
                        corners += 1
                elif not down:
                    if lines[n[1]-1][n[0]-1] != val:
                        corners += 1
                    if lines[n[1]-1][n[0]+1] != val:
                        corners += 1
                elif not left:
                    if lines[n[1]-1][n[0]+1] != val:
                        corners += 1
                    if lines[n[1]+1][n[0]+1] != val:
                        corners += 1
                elif not right:
                    if lines[n[1]-1][n[0]-1] != val:
                        corners += 1
                    if lines[n[1]+1][n[0]-1] != val:
                        corners += 1
            elif neighbors == 4:
                if lines[n[1]-1][n[0]-1] != val:
                    corners += 1
                if lines[n[1]-1][n[0]+1] != val:
                    corners += 1
                if lines[n[1]+1][n[0]+1] != val:
                    corners += 1
                if lines[n[1]+1][n[0]-1] != val:
                    corners += 1

    area = len(region)
    price1 += area * perimiter
    price2 += area * corners

print(price1)
print(price2)