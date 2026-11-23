"""Advent of Code - 2023 - Day 25"""

from collections import defaultdict
from copy import copy, deepcopy
from random import shuffle


def karger(graph: defaultdict[str, set[str]], target: int):
    """Karger's algorithm"""
    edges: list[list[str]] = []

    graph = deepcopy(graph)

    for node in graph:
        neighbors = graph[node]
        for neighbor in copy(neighbors):
            edge = [node, neighbor]
            edges.append(edge)
            graph[node].discard(neighbor)
            graph[neighbor].discard(node)

    saved = edges

    while True:
        edges = deepcopy(saved)
        nodes: defaultdict[str, list[list[str]]] = defaultdict(list)
        nodesize: defaultdict[str, int] = defaultdict(lambda: 1)

        for edge in edges:
            a, b = edge
            nodes[a].append(edge)
            nodes[b].append(edge)

        # By shuffling, we can simply pop edges off the end
        shuffle(edges)

        while len(nodes) > 2:
            edge = edges.pop()
            a, b = edge

            # Skip self edges
            if a == b:
                continue

            # move all edges from b to a
            for edge in nodes[b]:
                # Rename the edge
                if edge[0] == b:
                    edge[0] = a
                if edge[1] == b:
                    edge[1] = a

                nodes[a].append(edge)
            del nodes[b]

            # update the nodesize
            nodesize[a] += nodesize[b]
            del nodesize[b]

            # remove any self edges in a.
            newedges: list[list[str]] = []
            for edge in nodes[a]:
                x, y = edge
                if x != y:
                    newedges.append(edge)
            nodes[a] = newedges

        # We should now have exactly two nodes.
        # They should have identical sets of edges.
        keys = list(nodes)

        if len(nodes[keys[0]]) <= target:
            # print(f"nodes = {nodes}")
            # print(f"nodesizes = {nodesize}")
            break

    return nodesize[keys[0]] * nodesize[keys[1]]


def main():
    """Solves Part 1 and 2 of Day 25"""
    with open(0, encoding="utf-8") as f:
        lines = f.read().splitlines()

    graph: defaultdict[str, set[str]] = defaultdict(set)
    for line in lines:
        node, neighbors = line.split(": ")
        neighbors = neighbors.split(" ")
        graph[node] |= set(neighbors)
        for neighbor_node in neighbors:
            graph[neighbor_node].add(node)

    print(karger(graph, 3))


main()
