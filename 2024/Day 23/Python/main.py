from itertools import permutations
from collections import defaultdict

def BronKerbosch(N: dict[str, set[str]], R: set[str], P: set[str], X: set[str]):
    if not P and not X:
        yield R
    while P:
        v = P.pop()
        yield from BronKerbosch(N, R | {v}, P & N[v], X & N[v])
        X.add(v)

N: dict[str, set[str]] = defaultdict(set)
for a, b in (line.split("-") for line in open(0).read().splitlines()):
    N[a].add(b)
    N[b].add(a)
print(len({frozenset({a, b, t}) for t in N if t[0] == "t" for a, b in permutations(N[t], 2) if b in N[a]}))
print(",".join(sorted(max(BronKerbosch(N, set(), set(N), set()), key=len))))