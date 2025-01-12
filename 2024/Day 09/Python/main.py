"""Advent of Code - 2024 - Day 9"""

def part1(disk: list[int|None]):
    """Day 9 Part 1"""
    l: int = 0
    r: int = len(disk)-1

    while l < r:
        if disk[r] is None:
            r -= 1
        elif disk[l] is not None:
            l += 1
        else:
            disk[l], disk[r] = disk[r], None

    return sum(i*n for i, n in enumerate(disk) if n is not None)

def part2(disk: list[int|None], max_id: int):
    """Day 9 Part 1"""
    for file_id in range(max_id, -1, -1):
        file_size = disk.count(file_id)
        file_start = disk.index(file_id)
        space_size = 0
        space_start = None
        for i in range(file_start):
            if disk[i] is not None:
                space_size = 0
                space_start = None
            else:
                space_size +=1
                if space_start is None:
                    space_start = i
                if space_size >= file_size:
                    for j in range(file_size):
                        disk[space_start+j], disk[file_start+j] = disk[file_start+j], None
                    break

    return sum(i*n for i, n in enumerate(disk) if n is not None)

with open(0, encoding="utf-8") as f:
    line = f.readline()
og_disk: list[int|None] = []
for index, n in enumerate(map(int, line)):
    og_disk += n*[index//2 if index % 2 == 0 else None]

print(part1(og_disk.copy()))
print(part2(og_disk.copy(), (len(line)-1)//2))
