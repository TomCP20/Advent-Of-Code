"""Advent of Code - 2025 - Day 5"""

IDRange = tuple[int, int]


def get_range(r: str) -> IDRange:
    """Create a range based on the string r"""
    dash = r.find("-")
    return (int(r[:dash]), int(r[dash + 1 :]))


def in_range(r: IDRange, i: int):
    """Checks if ID i is in Range r"""
    start, end = r
    return start <= i <= end


def merge_ranges(ranges: list[IDRange]) -> list[IDRange]:
    """Consolidates and merges the ranges"""
    out: list[IDRange] = []
    ranges.sort(key=lambda r: r[1])
    top: IDRange = ranges.pop()
    while ranges:
        below_top = ranges.pop()
        if below_top[1] < top[0]:  # no overlap
            out.append(top)
            top = below_top
        else:  # overlap
            top = (min(below_top[0], top[0]), top[1])
    out.append(top)
    return out


def main():
    """Solves Part 1 and 2 of Day 5"""
    with open(0, encoding="utf-8") as f:
        a, b = f.read().split("\n\n")
    ranges = list(map(get_range, a.splitlines()))
    ids = map(int, b.splitlines())
    print(sum(any(in_range(r, i) for r in ranges) for i in ids))
    print(sum(end - start + 1 for start, end in merge_ranges(ranges)))


main()
