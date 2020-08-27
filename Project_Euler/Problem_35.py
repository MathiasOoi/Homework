def cycles(n):
    n = str(n)
    for _ in range(len(n)):
        yield int(n)
        n = n[1:] + n[0]

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


counter = 0
for i in range(2, 1000000):
    if all(isPrime(cycle) for cycle in cycles(i)):
        counter += 1
print(counter)

