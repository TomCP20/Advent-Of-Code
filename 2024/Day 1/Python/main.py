from collections import Counter

input = open(0).read().splitlines()
lists = [line.split("   ") for line in input]
left = [int(line[0]) for line in lists]
right = [int(line[1]) for line in lists]

print(sum(abs(l-r) for (l, r) in zip(sorted(left), sorted(right))))

c = Counter(right)
print(sum(l*c[l] for l in left))