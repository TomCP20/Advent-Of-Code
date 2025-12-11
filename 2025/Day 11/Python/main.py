"""Advent of Code - 2025 - Day 11"""


from collections import defaultdict


def parse_line(line: str) -> tuple[str, list[str]]:
    """parses a line of input"""
    head, *tail = line.split()
    return (head[:-1], tail)

def dfs(graph: dict[str, list[str]]):
    """Depth first search"""
    stack = ["you"]
    count = 0
    while stack:
        v = stack.pop()
        for w in graph[v]:
            stack.append(w)
            if w == "out":
                count += 1
    return count


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        connections: dict[str, list[str]] = defaultdict(list, map(parse_line, f.readlines()))
    print(dfs(connections))


main()
