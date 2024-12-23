from itertools import permutations

neighbors: dict[str, set[str]] = {}
for a, b in (line.split("-") for line in open(0).read().splitlines()):
    if a in neighbors:
        neighbors[a].add(b)
    else:
        neighbors[a] = {b}
    if b in neighbors:
        neighbors[b].add(a)
    else:
        neighbors[b] = {a}

res: set[frozenset[str]] = set()
for computer in neighbors.keys():
    if computer[0] == "t":
        for a, b in permutations(neighbors[computer], 2):
            if b in neighbors[a]:
                res.add(frozenset({a, b, computer}))
print(len(res))

def BronKerbosch(R: set[str], P: set[str], X: set[str]):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch( R | {v}, P & neighbors[v], X & neighbors[v] )
        X |= {v}

max_clique = set()
for clique in BronKerbosch(set(), set(neighbors.keys()), set()):
    if len(clique) > len(max_clique):
        max_clique = clique
print(",".join(sorted(list(max_clique))))