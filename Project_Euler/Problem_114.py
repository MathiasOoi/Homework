import time
cache = {}
def solve(n):
    if n < 3: return 1
    if n in cache: return cache[n]
    total = sum(solve(n-start-length-1) for start in range(0, n-2) for length in range(3, n-start+1)) + 1
    cache[n] = total
    return total

start = time.time()
print(solve(300))
print(time.time() - start)

