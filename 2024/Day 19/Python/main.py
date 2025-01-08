"""Advent of Code - 2024 - Day 19"""
import re

cols = "wubrg"

class Trie:
    """class representing the node of a Trie"""
    def __init__(self) -> None:
        self.end: bool = False
        self.children: list[None | Trie] = [None]*len(cols)

    def insert_towl(self, towl: str) -> None:
        """inserts a towl into the Trie"""
        prev = self
        for col in towl[::-1]:
            index = cols.index(col)
            if not prev.children[index]:
                prev.children[index] = Trie()
            prev = prev.children[index]
            assert prev
        prev.end = True

    def ways_of_forming_design(self, design: str) -> int:
        """returns the number of ways of forming the design"""
        n = len(design)
        count = [0]*n
        for i in range(n):
            ptr = self
            for j in range(i, -1, -1):
                index = cols.index(design[j])
                if ptr.children[index] is None:
                    break
                ptr = ptr.children[index]
                assert ptr

                if ptr.end:
                    if j > 0:
                        count[i] += count[j - 1]
                    else:
                        count[i] += 1
        return count[-1]

with open(0, encoding="utf-8") as f:
    lines = f.read().splitlines()
towls = lines[0].split(", ")
designs = lines[2:]
pattren: str = "(" + "|".join(towls) + ")+"
possible_designs = [d for d in designs if re.fullmatch(pattren, d)]
print(len(possible_designs))

root = Trie()
for t in towls:
    root.insert_towl(t)

print(sum(root.ways_of_forming_design(design) for design in possible_designs))
