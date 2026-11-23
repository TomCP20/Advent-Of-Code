"""Advent of Code - 2023 - Day 15"""

import re


def hash_algorithm(s: str) -> int:
    """Holiday ASCII String Helper algorithm"""
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def get_label_index(box: list[tuple[str, int]], label: str) -> int:
    """Search for the label index"""
    for i, lens in enumerate(box):
        if lens[0] == label:
            return i
    return -1


def part_2(steps: list[str]):
    boxes: dict[int, list[tuple[str, int]]] = {}
    for step in steps:
        matches = re.match(r"([a-z]+)(-|(=(\d)))", step)
        assert matches, step
        label = matches.group(1)
        box_i = hash_algorithm(label)
        if matches.group(2) == "-":
            if box_i in boxes:
                label_index = get_label_index(boxes[box_i], label)
                if label_index != -1:
                    boxes[box_i].remove(boxes[box_i][label_index])
        elif matches.group(2) != "-":
            focal_length = int(matches.group(4))
            if box_i in boxes:
                label_index = get_label_index(boxes[box_i], label)
                if label_index != -1:
                    boxes[box_i][label_index] = (label, focal_length)
                else:
                    boxes[box_i].append((label, focal_length))
            else:
                boxes[box_i] = [(label, focal_length)]

    focusing_power = 0
    for key, box in boxes.items():
        for j, (_, focal_length) in enumerate(box, 1):
            focusing_power += (key + 1) * j * focal_length
    return focusing_power


def main():
    """Solves Part 1 and 2 of Day 15"""
    with open(0, encoding="utf-8") as f:
        steps = f.read().split(",")
    print(sum(hash_algorithm(step) for step in steps))
    print(part_2(steps))


main()
