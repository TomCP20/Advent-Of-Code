from itertools import product

schematics = list(map(lambda x : x.splitlines(), open(0).read().split("\n\n")))
w = 5
h = 7
locks = [schematic for schematic in schematics if schematic[0] == "#"*w]
keys = [schematic for schematic in schematics if schematic[0] == "."*w]
locks = [[[line[x] for line in lock].count("#")-1 for x in range(w)] for lock in locks]
keys = [[[line[x] for line in key].count("#")-1 for x in range(w)] for key in keys]

print(sum(all(((k + l) <= h-2) for (k, l) in zip(key, lock)) for key, lock in product(keys, locks)))