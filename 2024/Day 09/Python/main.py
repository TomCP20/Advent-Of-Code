from itertools import groupby


input = map(int, open(0).readline())
disk = []
max_id = 0
for i, n in enumerate(input):
    if i % 2 == 0:
        disk += n*[int(i/2)]
        max_id = int(i/2)
    else:
        disk+= n*[None]

disk1 = disk.copy()
l = 0
r = len(disk1)-1

while l < r:
    if disk1[r] == None:
        r -= 1
    elif disk1[l] != None:
        l += 1
    else:
        disk1[l], disk1[r] = disk1[r], None

print(sum(i*n for i, n in enumerate(disk1) if n != None))

disk2 = disk.copy()

for id in range(max_id, -1, -1):
    size = disk2.count(id)
    start = disk2.index(id)
    for _, l in groupby(filter(lambda x : x[1] == None, enumerate(disk2)), key=lambda x : x[1]):
        group = list(l)
        if len(group) >= size and start > group[0][0]:
                print(disk2[group[i][0]], disk2[start+i])
                disk2[group[i][0]], disk2[start+i] = disk2[start+i], None

print(sum(i*n for i, n in enumerate(disk2) if n != None))
