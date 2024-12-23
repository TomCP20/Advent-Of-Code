from itertools import permutations

pairs = [set(line.split("-")) for line in open(0).read().splitlines()]
computers = {c for pair in pairs for c in pair}
tcomputers = {c for c in computers if c[0] == "t"}
res = []
for tcomputer in tcomputers:
    tpairs = [p for p in pairs if tcomputer in p]
    for a, b in permutations(tpairs, 2):
        triple = (a | b)
        if (triple - {tcomputer}) in pairs:
            if triple not in res:
                res.append(triple)
print(len(res))

def getNeighbors(computer: str) -> set[str]:
    npairs = [pair-{computer} for pair in pairs if computer in pair]
    return {c for pair in npairs for c in pair}

def BronKerbosch(R: set[str], P: set[str], X: set[str]):
    if not P and not X:
        yield R
    while P:
        computer = P.pop()
        neighbors = getNeighbors(computer)
        yield from BronKerbosch( R | {computer}, P & neighbors, X & neighbors )
        X |= {computer}

max_clique = set()
for clique in BronKerbosch(set(), computers, set()):
    if len(clique) > len(max_clique):
        max_clique = clique
print(",".join(sorted(list(max_clique))))