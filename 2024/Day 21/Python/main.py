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


def get_key_seq(
    fromkey: str, tokey: str, keypos: dict[str, tuple[int, int]], isnum: bool
):
    """gets the sequence for the key"""
    if fromkey == tokey:  # same symbol, no repetition
        return [""]
    frompos = keypos[fromkey]
    topos = keypos[tokey]
    xdiff = topos[0] - frompos[0]
    ydiff = topos[1] - frompos[1]
    if xdiff == 0:  # on the same column
        if ydiff > 0:  # going down
            return [ydiff * "v"]
        # going up
        return [abs(ydiff) * "^"]
    if ydiff == 0:  # on the same row
        if xdiff > 0:  # going right
            return [xdiff * ">"]
        # going left
        return [abs(xdiff) * "<"]
    if ydiff < 0 < xdiff:  # up right
        if not isnum and frompos[0] == 0 and topos[1] == 0:
            return [xdiff * ">" + abs(ydiff) * "^"]
        return [abs(ydiff) * "^" + xdiff * ">", xdiff * ">" + abs(ydiff) * "^"]
    if ydiff > 0 > xdiff:  # down left
        if not isnum and frompos[1] == 0 and topos[0] == 0:
            return [ydiff * "v" + abs(xdiff) * "<"]
        return [ydiff * "v" + abs(xdiff) * "<", abs(xdiff) * "<" + ydiff * "v"]
    if ydiff > 0 and xdiff > 0:  # down right
        if isnum and frompos[0] == 0 and topos[1] == 3:
            return [xdiff * ">" + ydiff * "v"]
        return [ydiff * "v" + xdiff * ">", xdiff * ">" + ydiff * "v"]
    # up left
    if isnum and topos[0] == 0 and frompos[1] == 3:
        return [abs(ydiff) * "^" + abs(xdiff) * "<"]
    return [abs(ydiff) * "^" + abs(xdiff) * "<", abs(xdiff) * "<" + abs(ydiff) * "^"]


numkeymap: dict[str, list[str]] = {
    fromkey + tokey: get_key_seq(fromkey, tokey, numkeypos, True)
    for fromkey, tokey in product(numkeypos.keys(), repeat=2)
}
dirkeymap: dict[str, list[str]] = {
    fromkey + tokey: get_key_seq(fromkey, tokey, dirkeypos, False)
    for fromkey, tokey in product(dirkeypos.keys(), repeat=2)
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


def solve(depth: int):
    """solves the puzzle"""
    total = 0
    for code in codes:
        seqlist: list[str] = []
        build_seq(code, 0, "A", "", seqlist, numkeymap)
        total += int(code[:-1]) * min(shortest_seq(seq, depth) for seq in seqlist)
    return total


with open(0, encoding="utf-8") as f:
    codes = f.read().splitlines()

print(solve(2))
print(solve(25))
