"""Advent of Code - 2023 - Day 8"""

import itertools
import re
import math


def get_path_length(
    position: str,
    network: dict[str, tuple[str, str]],
    directions: str,
    is_part_2: bool = False,
) -> int:
    """Calculates the number of steps from the start to the end"""
    steps = 0
    for direction in itertools.cycle(directions):
        steps += 1
        match direction:
            case "L":
                position = network[position][0]
            case "R":
                position = network[position][1]
            case _:
                assert False
        if is_part_2 and position[-1] == "Z" or position == "ZZZ":
            return steps
    assert False


def main():
    """Solves Part 1 and 2 of Day 8"""
    with open(0, encoding="utf-8") as f:
        directions, tail = f.read().split("\n\n")
        nodes = tail.split("\n")

    network: dict[str, tuple[str, str]] = {}
    for node in nodes:
        m = re.match(r"^([A-Z]{3}) = [(]([A-Z]{3}), ([A-Z]{3})[)]", node)
        assert m
        parent = m.group(1)
        left = m.group(2)
        right = m.group(3)
        network[parent] = (left, right)

    print(get_path_length("AAA", network, directions))

    positions = [node for node in network if node[-1] == "A"]
    lengths = [
        get_path_length(position, network, directions, True) for position in positions
    ]
    print(math.lcm(*lengths))


main()
