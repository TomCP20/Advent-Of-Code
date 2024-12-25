from itertools import product

schematics = list(map(lambda x : x.splitlines(), open(0).read().split("\n\n")))
locks = [[[line[x] for line in lock].count("#") for x in range(5)] for lock in schematics if lock[0] == "#####"]
keys = [[[line[x] for line in key].count("#") for x in range(5)] for key in schematics if key[0] == "....."]

print(sum(all(((k + l) <= 7) for (k, l) in zip(key, lock)) for key, lock in product(keys, locks)))