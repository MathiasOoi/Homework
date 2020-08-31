cache = {}
def fill(n, m):
    if n < m: return 1
    if n in cache: return cache[n]
    total = 1
    for start in range(0, n-m+1):
        for length in range(m, n-start+1):
            total += fill(n - start - length - 1, m)
    cache[n] = total
    return total


if __name__ == "__main__":
    n = 1
    while True:
        if fill(n, 50) > 10**6:
            print(n)
            break
        n += 1





