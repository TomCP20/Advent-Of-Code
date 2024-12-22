def step(n: int) -> int:
    n = ((n*64)^n)%16777216
    n = ((n//32)^n)%16777216
    n = ((n*2048)^n)%16777216
    return n

def step2000(n: int) -> int:
    for _ in range(2000):
        n = step(n)
    return n

def getPrices(n: int):
    for _ in range(2000):
        n = step(n)
        yield n % 10

initial = map(int, open(0).read().splitlines())
print(sum(step2000(n) for n in initial))