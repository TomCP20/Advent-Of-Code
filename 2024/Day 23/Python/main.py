"""Advent of Code - 2024 - Day 23"""

from itertools import combinations
from collections import defaultdict
from typing import Iterable


def bron_kerbosch(
    n: dict[str, set[str]], r: set[str], p: set[str], x: set[str]
) -> Iterable[set[str]]:
    """Bron-Kerbosch algorithm"""
    if not p and not x:
        yield r
    while p:
        v = p.pop()
        yield from bron_kerbosch(n, r | {v}, p & n[v], x & n[v])
        x.add(v)


connections: dict[str, set[str]] = defaultdict(set)
with open(0, encoding="utf-8") as f:
    for a, b in (line.split("-") for line in f.read().splitlines()):
        connections[a].add(b)
        connections[b].add(a)
t_computers = (t for t in connections if t[0] == "t")

print(
    len(
        {
            frozenset({a, b, t})
            for t in t_computers
            for a, b in combinations(connections[t], 2)
            if b in connections[a]
        }
    )
)
print(
    ",".join(
        sorted(max(bron_kerbosch(connections, set(), set(connections), set()), key=len))
    )
)
