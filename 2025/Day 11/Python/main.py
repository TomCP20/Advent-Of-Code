"""Advent of Code - 2025 - Day 11"""


from collections import defaultdict


def parse_line(line: str) -> tuple[str, list[str]]:
    """parses a line of input"""
    head, *tail = line.split()
    return (head[:-1], tail)

def dfs_1(graph: dict[str, list[str]], node: str = "you") -> int:
    """Depth first search"""
    if node == "out":
        return 1
    return sum(dfs_1(graph, next) for next in graph[node])


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        connections: dict[str, list[str]] = defaultdict(list, map(parse_line, f.readlines()))
    print(dfs_1(connections))


main()
