"""Advent of Code - 2025 - Day 11"""

from functools import cache


def parse_line(line: str) -> tuple[str, list[str]]:
    """parses a line of input"""
    head, *tail = line.split()
    return (head[:-1], tail)


def count_paths(graph: dict[str, list[str]], start: str, goal: str):
    """Counts the number of paths using Depth first search"""

    @cache
    def dfs(node: str) -> int:
        if node == goal:
            return 1
        return sum(dfs(next) for next in graph[node])

    return dfs(start)


def main():
    """Solves Part 1 and 2 of Day 10"""
    with open(0, encoding="utf-8") as f:
        graph: dict[str, list[str]] = dict(map(parse_line, f.readlines()))
    graph["out"] = []
    print(count_paths(graph, "you", "out"))
    a = count_paths(graph, "svr", "fft")
    b = count_paths(graph, "fft", "dac")
    c = count_paths(graph, "dac", "out")
    print(a * b * c)


main()
