"""Advent of Code - 2025 - Day 2"""

def getRange(r: str):
    start = int(r[:r.find("-")])
    end = int(r[r.find("-")+1:])
    return range(start, end+1)

def isInvalid(ID: str) -> bool:
    return ID[:len(ID)//2] == ID[len(ID)//2:]

def main():

    with open(0, encoding="utf-8") as f:
        line = "".join(f.read().splitlines())

    ranges = (getRange(r) for r in line.split(","))

    ids = [id for r in ranges for id in r]
    res = sum(int(id) for id in ids if isInvalid(str(id)))
    print(res)

main()
