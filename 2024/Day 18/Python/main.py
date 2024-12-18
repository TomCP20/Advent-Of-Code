Vec = tuple[int, int]
VecSet = set[Vec]
VecList = list[Vec]
ScoreDict = dict[Vec, int]

def A_Star(size: int, corrupted: VecSet):
    def h(n: Vec):
        return 2*size - n[0] - n[1]
    def neighbors(n: Vec):
        for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
            new = (n[0] + dir[0], n[1] + dir[1])
            if (new not in corrupted) and 0 <= new[0] <= size and 0 <= new[1] <= size:
                yield new
    
    openSet: VecSet = {(0, 0)}

    gScore: ScoreDict = {(0, 0): 0}
    fScore: ScoreDict = {(0, 0): h((0, 0))}

    while openSet:
        current = min(openSet, key= lambda x: fScore[x])
        openSet.remove(current)
        if current == (size, size):
            return gScore[current]
        for neighbor in neighbors(current):
            tentative_gScore = gScore[current] + 1
            if tentative_gScore < gScore.get(neighbor, float("inf")):
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = tentative_gScore + h(neighbor)
                if neighbor not in openSet:
                    openSet.add(neighbor)
    return None

#size = 6
#bytes = 12

size = 70
bytes = 1024

all_corrupted: VecList = [(int(line.split(",", 1)[0]), int(line.split(",", 1)[1])) for line in open(0).read().splitlines()]
print(A_Star(size, set(all_corrupted[:bytes])))

while A_Star(size, set(all_corrupted[:bytes])):
    bytes += 1
print(f"{all_corrupted[bytes-1][0]},{all_corrupted[bytes-1][1]}")