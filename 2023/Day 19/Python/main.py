"""Advent of Code - 2023 - Day 19"""

import math
import re

Range = tuple[int, int]
PartRange = dict[str, Range]


def rule_result(rule: str, part: dict[str, int]):
    """Find the result of applying a rule"""
    m = re.match(r"([xmas])([<>])(\d+):(([a-z]+)|([AR]))", rule)
    assert m, rule
    category = m.group(1)
    val = part[category]
    comparison = m.group(2)
    match comparison:
        case ">":
            if val > int(m.group(3)):
                return m.group(4)
        case "<":
            if val < int(m.group(3)):
                return m.group(4)
        case _:
            assert False, comparison
    return ""


def process(
    workflows: dict[str, list[str]], part: dict[str, int], key: str = "in"
) -> bool:
    """Process a part"""
    workflow = workflows[key]
    for rule in workflow[:-1]:
        next_key = rule_result(rule, part)
        match next_key:
            case "A":
                return True
            case "R":
                return False
            case "":
                continue
            case _:
                return process(workflows, part, next_key)
    next_key = workflow[-1]
    match next_key:
        case "A":
            return True
        case "R":
            return False
        case _:
            return process(workflows, part, next_key)


def new_part_range(
    old_part_range: PartRange, category: str, new_range: Range
) -> PartRange:
    """Update a part range"""
    part_range = old_part_range.copy()
    part_range[category] = new_range
    return part_range


def rule_result_range(
    rule: str, part_range: PartRange
) -> tuple[PartRange, PartRange, str]:
    """find the result of applying a rule to a range."""
    m = re.match(r"([xmas])([<>])(\d+):(([a-z]+)|([AR]))", rule)
    assert m, rule
    category = m.group(1)
    category_range = part_range[category]
    comparison_type = m.group(2)
    comparison_value = int(m.group(3))
    pass_key = str(m.group(4))
    match comparison_type:
        case ">":
            if category_range[0] < comparison_value < category_range[1]:
                fail_range = (category_range[0], comparison_value)
                pass_range = (comparison_value + 1, category_range[1])
                return (
                    new_part_range(part_range, category, pass_range),
                    new_part_range(part_range, category, fail_range),
                    pass_key,
                )
        case "<":
            if category_range[0] < comparison_value < category_range[1]:
                pass_range = (category_range[0], comparison_value - 1)
                fail_range = (comparison_value, category_range[1])
                return (
                    new_part_range(part_range, category, pass_range),
                    new_part_range(part_range, category, fail_range),
                    pass_key,
                )
        case _:
            assert False, comparison_type
    assert False


def process_range(
    workflows: dict[str, list[str]], part_range: PartRange, key: str = "in"
) -> int:
    """process a range of parts"""
    if key == "A":
        return math.prod(
            (max_val - min_val + 1) for _, (min_val, max_val) in part_range.items()
        )
    if key == "R":
        return 0
    workflow = workflows[key]
    result = 0
    for rule in workflow[:-1]:
        pass_part_range, fail_part_range, pass_key = rule_result_range(rule, part_range)
        result += process_range(workflows, pass_part_range, pass_key)
        part_range = fail_part_range
    result += process_range(workflows, part_range, workflow[-1])
    return result


def main():
    """Solves Part 1 and 2 of Day 19"""
    with open(0, encoding="utf-8") as f:
        workflows_data, parts_data = f.read().split("\n\n")

    workflows: dict[str, list[str]] = {}
    for workflow in workflows_data.splitlines():
        m = re.search(r"([a-z]+)[{](.+)[}]", workflow)
        assert m
        key = m.group(1)
        workflow = m.group(2).split(",")
        workflows[key] = workflow

    parts: list[dict[str, int]] = []
    for row in parts_data.splitlines():
        m = re.match(r"[{]x=(\d+),m=(\d+),a=(\d+),s=(\d+)[}]", row)
        assert m
        part = {
            "x": int(m.group(1)),
            "m": int(m.group(2)),
            "a": int(m.group(3)),
            "s": int(m.group(4)),
        }
        parts.append(part)

    print(sum(sum(part.values()) for part in parts if process(workflows, part)))
    part_range: PartRange = {
        "x": (1, 4000),
        "m": (1, 4000),
        "a": (1, 4000),
        "s": (1, 4000),
    }
    print(process_range(workflows, part_range))


main()
