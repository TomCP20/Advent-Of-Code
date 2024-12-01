from collections import Counter

input = open(0).read().splitlines()
lists = [line.split("   ") for line in input]
left = [int(line[0]) for line in lists]
right = Counter(int(line[1]) for line in lists)
print(sum(l*right[l] for l in left))