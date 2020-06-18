def T(n):
    return n*(n + 1)/2

def factors(n):
    return len(set(factor for i in range(1, int(n**0.5) + 1) if n % i == 0 for factor in (i, n//i)))

n = 1
while True:
    if factors(T(n)) > 500:
        print(T(n))
        break
    n += 1