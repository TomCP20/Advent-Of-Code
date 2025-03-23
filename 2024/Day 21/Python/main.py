"""Advent of Code - 2024 - Day 21"""

from functools import cache
from itertools import product

numkeypos = {
    "9": (2, 0),
    "8": (1, 0),
    "7": (0, 0),
    "6": (2, 1),
    "5": (1, 1),
    "4": (0, 1),
    "3": (2, 2),
    "2": (1, 2),
    "1": (0, 2),
    "0": (1, 3),
    "A": (2, 3),
}

dirkeypos = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}


def get_key_seq(frompos: tuple[int, int], topos: tuple[int, int], isnum: bool):
    """gets the sequence for the key"""
    if frompos == topos:
        return [""]
    xdiff = topos[0] - frompos[0]
    ydiff = topos[1] - frompos[1]
    up = abs(ydiff) * "^"
    down = abs(ydiff) * "v"
    left = abs(xdiff) * "<"
    right = abs(xdiff) * ">"
    if xdiff == 0:
        return [down] if ydiff > 0 else [up]
    if ydiff == 0:
        return [right] if xdiff > 0 else [left]
    match (xdiff > 0, ydiff > 0):
        case (True, True):  # down right
            if isnum and frompos[0] == 0 and topos[1] == 3:
                return [right + down]
            return [down + right, right + down]
        case (True, False):  # up right
            if not isnum and frompos[0] == 0 and topos[1] == 0:
                return [right + up]
            return [up + right, right + up]
        case (False, True):  # down left
            if not isnum and frompos[1] == 0 and topos[0] == 0:
                return [down + left]
            return [down + left, left + down]
        case (False, False):  # up left
            if isnum and topos[0] == 0 and frompos[1] == 3:
                return [up + left]
            return [up + left, left + up]


numkeymap: dict[str, list[str]] = {
    fromkey + tokey: get_key_seq(frompos, topos, True)
    for (fromkey, frompos), (tokey, topos) in product(numkeypos.items(), repeat=2)
}
dirkeymap: dict[str, list[str]] = {
    fromkey + tokey: get_key_seq(frompos, topos, False)
    for (fromkey, frompos), (tokey, topos) in product(dirkeypos.items(), repeat=2)
}


def build_seq(
    keys: str,
    index: int,
    prev_key: str,
    curr_path: str,
    result: list[str],
    keymap: dict[str, list[str]],
):
    """builds the sequence"""
    if index == len(keys):
        result.append(curr_path)
        return
    for path in keymap[prev_key + keys[index]]:
        build_seq(keys, index + 1, keys[index], curr_path + path + "A", result, keymap)


@cache
def shortest_seq(keys: str, depth: int):
    """finds the shortest sequence"""
    if depth == 0:
        return len(keys)
    subkeys = [s + "A" for s in keys.split("A")][:-1]
    total = 0
    for subkey in subkeys:
        seqlist: list[str] = []
        build_seq(subkey, 0, "A", "", seqlist, dirkeymap)
        total += min(shortest_seq(seq, depth - 1) for seq in seqlist)
    return total


def solve(codes: list[str], depth: int):
    """solves the puzzle"""
    total = 0
    for code in codes:
        seqlist: list[str] = []
        build_seq(code, 0, "A", "", seqlist, numkeymap)
        total += int(code[:-1]) * min(shortest_seq(seq, depth) for seq in seqlist)
    return total


def main():
    """solves part 1 and 2"""
    with open(0, encoding="utf-8") as f:
        codes = f.read().splitlines()

    print(solve(codes, 2))
    print(solve(codes, 25))


main()
