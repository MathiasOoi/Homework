def d(n):
    return sum(k for x in ([i, n//i] for i in range(2, int(n**0.5) + 1) if not n % i) for k in x) + 1

def solve():
    cache = {n: d(n) for n in range(10000)}
    output = set()
    for a in range(10000):
        for b in range(10000):
            if cache[a] == b and cache[b] == a and a != b:
                output.add(a), output.add(b)
                break
    return sum(output)

print(solve())