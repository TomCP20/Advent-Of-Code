input = open(0).read().splitlines()
lists = [line.split("   ") for line in input]
left = [int(line[0]) for line in lists]
right = [int(line[1]) for line in lists]
left.sort()
right.sort()
print(sum(abs(l-r) for (l, r) in zip(left, right)))