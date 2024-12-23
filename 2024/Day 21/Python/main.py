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

def getnumKeySeq(fromkey: str, tokey: str):
    if fromkey == tokey: # same symbol, no repetition
        return [""]
    else:
        frompos = numkeypos[fromkey]
        topos = numkeypos[tokey]
        xdiff = topos[0] - frompos[0]
        ydiff = topos[1] - frompos[1]
        if xdiff == 0: # on the same column
            if ydiff > 0: # going down
                return [ydiff * "v"]
            else: # going up
                return [abs(ydiff) * "^"]
        elif ydiff == 0: # on the same row
            if xdiff > 0: # going right
                return [xdiff * ">"]
            else: # going left
                return [abs(xdiff) * "<"]
        elif ydiff < 0 and xdiff > 0: #up right
            return [abs(ydiff) * "^" + xdiff * ">", xdiff * ">" + abs(ydiff) * "^"]
        elif ydiff > 0 and xdiff < 0: #down left
            return [ydiff * "v" + abs(xdiff) * "<", abs(xdiff) * "<" + ydiff * "v"]
        elif ydiff > 0 and xdiff > 0: #down right
            if frompos[0] == 0 and topos[1] == 3:
                return [xdiff * ">" + ydiff * "v"]
            else:
                return [ydiff * "v" + xdiff * ">", xdiff * ">" + ydiff * "v"]
        else : #up left
            if topos[0] == 0 and frompos[1] == 3:
                return [abs(ydiff) * "^" + abs(xdiff) * "<"]
            else:
                return [abs(ydiff) * "^" + abs(xdiff) * "<", abs(xdiff) * "<" + abs(ydiff) * "^"]

numkeymap: dict[str, list[str]] = {}

for fromkey, tokey in product(numkeypos.keys(), repeat=2):
    s = fromkey + tokey
    numkeymap[s] = getnumKeySeq(fromkey, tokey)

dirkeypos = {
    "^": (1, 0),
    "A": (2, 0),
    "<": (0, 1),
    "v": (1, 1),
    ">": (2, 1),
}

def getdirKeySeq(fromkey: str, tokey: str):
    if fromkey == tokey: # same symbol, no repetition
        return [""]
    else:
        frompos = dirkeypos[fromkey]
        topos = dirkeypos[tokey]
        xdiff = topos[0] - frompos[0]
        ydiff = topos[1] - frompos[1]
        if xdiff == 0: # on the same column
            if ydiff > 0: # going down
                return [ydiff * "v"]
            else: # going up
                return [abs(ydiff) * "^"]
        elif ydiff == 0: # on the same row
            if xdiff > 0: # going right
                return [xdiff * ">"]
            else: # going left
                return [abs(xdiff) * "<"]
        elif ydiff < 0 and xdiff > 0: #up right
            if frompos[0] == 0 and topos[1] == 0:
                return [xdiff * ">" + abs(ydiff) * "^"]
            else:
                return [abs(ydiff) * "^" + xdiff * ">", xdiff * ">" + abs(ydiff) * "^"]
        elif ydiff > 0 and xdiff < 0: #down left
            if frompos[1] == 0 and topos[0] == 0:
                return [ydiff * "v" + abs(xdiff) * "<"]
            else:
                return [ydiff * "v" + abs(xdiff) * "<", abs(xdiff) * "<" + ydiff * "v"]
        elif ydiff > 0 and xdiff > 0: #down right
            return [ydiff * "v" + xdiff * ">", xdiff * ">" + ydiff * "v"]
        else: #up left
            return [abs(ydiff) * "^" + abs(xdiff) * "<", abs(xdiff) * "<" + abs(ydiff) * "^"]

dirkeymap: dict[str, list[str]] = {}

for fromkey, tokey in product(dirkeypos.keys(), repeat=2):
    s = fromkey + tokey
    dirkeymap[s] = getdirKeySeq(fromkey, tokey)

def buildSeq(keys: str, index: int, prevKey: str, currPath: str, result: list[str], keymap: dict[str, list[str]]):
    if index == len(keys):
        result.append(currPath)
        return
    for path in keymap[prevKey + keys[index]]:
        buildSeq(keys, index+1, keys[index], currPath + path + "A", result, keymap)

@cache
def shortestSeq(keys: str, depth: int):
    if depth == 0:
        return len(keys)
    subkeys = [s+"A" for s in keys.split("A")][:-1]
    total = 0
    for subkey in subkeys:
        seqlist = []
        buildSeq(subkey, 0, "A", "", seqlist, dirkeymap)
        total += min(shortestSeq(seq, depth-1) for seq in seqlist)
    return total

def solve(codes, depth):
    total = 0
    for code in codes:
        seqlist = []
        buildSeq(code, 0, "A", "", seqlist, numkeymap)
        total += int(code[:-1]) * min(shortestSeq(seq, depth) for seq in seqlist)
    return total
codes = open(0).read().splitlines()

print(solve(codes, 2))
print(solve(codes, 25))