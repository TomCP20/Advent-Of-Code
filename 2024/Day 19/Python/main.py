import re

cols = "wubrg"

class Trie:
    def __init__(self) -> None:
        self.end: bool = False
        self.children: list[None | Trie] = [None]*len(cols)


    def insertTowl(self, towl: str) -> None:
        prev = self
        for col in towl[::-1]:
            index = cols.index(col)
            if not prev.children[index]:
                prev.children[index] = Trie()
            prev = prev.children[index]
            assert prev
        prev.end = True

    def waysOfFormingDesign(self, design: str) -> int:
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

lines = open(0).read().splitlines()
towls = lines[0].split(", ")
designs = lines[2:]
pattren = "(" + "|".join(towls) + ")+"
possible_designs = [d for d in designs if re.fullmatch(pattren, d)]
print(len(possible_designs))

root = Trie()
for towl in towls:
    root.insertTowl(towl)

print(sum(root.waysOfFormingDesign(design) for design in possible_designs))
