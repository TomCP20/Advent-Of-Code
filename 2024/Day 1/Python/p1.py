input = open(0).read().splitlines()
lists = [line.split("   ") for line in input]
left = sorted(int(line[0]) for line in lists)
right = sorted(int(line[1]) for line in lists)
print(sum(abs(l-r) for (l, r) in zip(left, right)))