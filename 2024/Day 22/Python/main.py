from collections import Counter, deque

def step(n: int) -> int:
    n = ((n*64)^n)%16777216
    n = ((n//32)^n)%16777216
    n = ((n*2048)^n)%16777216
    return n

def step2000(n: int) -> int:
    for _ in range(2000):
        n = step(n)
    return n


def sequenceToPrice(n: int) -> Counter[tuple[int, ...]]:
    slice: deque[int] = deque([], maxlen=4)
    prices = Counter()

    for i in range(2000):
        if i >= 4:
            key = tuple(slice)
            if key not in prices:
                prices[key] = n % 10

        next = step(n)
        slice.append((next%10)-(n%10))
        n = next

    return prices

initial = list(map(int, open(0).read().splitlines()))
print(sum(step2000(n) for n in initial))

all_prices = Counter()
for n in initial:
    all_prices += sequenceToPrice(n)
print(all_prices.most_common(1)[0][1])