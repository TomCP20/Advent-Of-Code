from itertools import permutations

antennas = {}

input = open(0).read().splitlines()
height = len(input)
width = len(input[0])
for y, line in enumerate(input):
    for x, char in enumerate(line):
        if char != ".":
            if char in antennas:
                antennas[char].append((x, y))
            else:
                antennas[char] = [(x, y)]

antinodes1 = set()
for locations in antennas.values():
    for (a, b) in permutations(locations, 2):
        pos = (2*a[0]-b[0], 2*a[1]-b[1])
        if 0 <= pos[0] < width and 0 <= pos[1] < height:
            antinodes1.add(pos)

antinodes2 = set()
for locations in antennas.values():
    for (a, b) in permutations(locations, 2):
        diff = (a[0]-b[0], a[1]-b[1]) # b to a
        pos = a
        while 0 <= pos[0] < width and 0 <= pos[1] < height:
            antinodes2.add(pos)
            pos = (pos[0]+diff[0], pos[1]+diff[1])

print(len(antinodes1))
print(len(antinodes2))