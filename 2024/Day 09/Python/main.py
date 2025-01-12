"""Advent of Code - 2024 - Day 9"""
from itertools import groupby

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

def part2(disk: list[int|None]):
    """Day 9 Part 1"""
    for file_id in range(max_id, -1, -1):
        size = disk.count(file_id)
        start = disk.index(file_id)
        for val, l in groupby(enumerate(disk), key=lambda x : x[1]):
            if val is None:
                group = list(l)
                if len(group) >= size and start > group[0][0]:
                    for i in range(size):
                        disk[group[i][0]], disk[start+i] = disk[start+i], None
    return sum(i*n for i, n in enumerate(disk) if n is not None)

with open(0, encoding="utf-8") as f:
    og_disk: list[int|None] = []
    max_id: int = 0
    for index, n in enumerate(map(int, f.readline())):
        if index % 2 == 0:
            og_disk += n*[index//2]
            max_id = index//2
        else:
            og_disk+= n*[None]

print(part1(og_disk.copy()))

print(part2(og_disk.copy()))
