"""Advent of Code - 2024 - Day 22"""
from collections import Counter, deque

def step(secret_num: int) -> int:
    """steps the secret number"""
    secret_num = ((secret_num*64)^secret_num)%16777216
    secret_num = ((secret_num//32)^secret_num)%16777216
    secret_num = ((secret_num*2048)^secret_num)%16777216
    return secret_num

def step2000(secret_num: int) -> int:
    """applies step 2000 times"""
    for _ in range(2000):
        secret_num = step(secret_num)
    return secret_num


def sequence_to_price(secret_num: int) -> Counter[tuple[int, ...]]:
    """gets price from sequence"""
    q_slice: deque[int] = deque([], maxlen=4)
    prices = Counter()

    for i in range(2000):
        if i >= 4:
            key = tuple(q_slice)
            if key not in prices:
                prices[key] = secret_num % 10

        next_val = step(secret_num)
        q_slice.append((next_val%10)-(secret_num%10))
        secret_num = next_val

    return prices
with open(0, encoding="utf-8") as f:
    initial = list(map(int, f.read().splitlines()))
print(sum(step2000(n) for n in initial))

all_prices = Counter()
for n in initial:
    all_prices += sequence_to_price(n)
print(all_prices.most_common(1)[0][1])
