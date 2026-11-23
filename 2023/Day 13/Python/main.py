"""Advent of Code - 2023 - Day 13"""

def compare_strings(str1: str, str2: str) -> bool:
    """compares 2 strings to see if they are exactly one character off"""
    diff_count = 0
    for a, b in zip(str1, str2):
        if a != b:
            if diff_count:
                return False
            diff_count += 1
    if diff_count == 1:
        return True
    return False

def reflection_score_1(pattern: list[str]) -> int:
    """Calculates the reflection score for part 1"""
    for row_i in range(1, len(pattern)): # rows
        l = min(row_i, len(pattern)-row_i)
        if pattern[row_i-l:row_i] == pattern[row_i:row_i+l][::-1]:
            return 100*row_i
    for col_i in range(1, len(pattern[0])): # rows
        l = min(col_i, len(pattern[0])-col_i)
        left = [row[col_i-l:col_i] for row in pattern]
        right = [row[col_i:col_i+l][::-1] for row in pattern]
        if left == right:
            return col_i
    assert False

def reflection_score_2(pattern: list[str]) -> int:
    """Calculates the reflection score for part 2"""
    for row_i in range(1, len(pattern)): # rows
        l = min(row_i, len(pattern)-row_i)
        top = "".join(pattern[row_i-l:row_i])
        bottom = "".join(pattern[row_i:row_i+l][::-1])
        if compare_strings(top, bottom):
            return 100*row_i
    for col_i in range(1, len(pattern[0])): # rows
        l = min(col_i, len(pattern[0])-col_i)
        left = "".join(row[col_i-l:col_i] for row in pattern)
        right = "".join(row[col_i:col_i+l][::-1] for row in pattern)
        if compare_strings(left, right):
            return col_i
    return 0


def main():
    """Solves Part 1 and 2 of Day 13"""
    with open(0, encoding="utf-8") as f:
        patterns = [pattern.split("\n") for pattern in f.read().split("\n\n")]
        print(sum(map(reflection_score_1, patterns)))
        print(sum(map(reflection_score_2, patterns)))


main()
