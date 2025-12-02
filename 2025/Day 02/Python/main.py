"""Advent of Code - 2025 - Day 2"""

def get_range(r: str):
    """create a range based on the string r"""
    start = int(r[:r.find("-")])
    end = int(r[r.find("-")+1:])
    return range(start, end+1)

def is_invalid1(id_str: str) -> bool:
    """Checks if the id is valid based on part 1 rules"""
    return id_str[:len(id_str)//2] == id_str[len(id_str)//2:]

def part_1(ids: list[int]):
    """Solves Part 1 of Day 1"""
    return sum(int(id) for id in ids if is_invalid1(str(id)))

def main():
    """Solves Part 1 of Day 1"""
    with open(0, encoding="utf-8") as f:
        line = "".join(f.read().splitlines())
    ranges = (get_range(r) for r in line.split(","))
    ids = [id_int for r in ranges for id_int in r]
    print(part_1(ids))

main()
