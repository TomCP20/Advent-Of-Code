from itertools import combinations, pairwise
from typing import Iterable

def is_safe(report: Iterable[int]) -> bool:
    return (all(1 <= a-b <= 3 for (a, b) in pairwise(report))) or (all(1 <= b-a <= 3 for (a, b) in pairwise(report)))

reports = list(map(lambda x : list(map(int, x.split())), open(0).read().splitlines()))

print(sum(is_safe(report) for report in reports))

print(sum(is_safe(report) or any(is_safe(comb) for comb in combinations(report, len(report)-1)) for report in reports))