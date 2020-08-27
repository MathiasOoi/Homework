from math import factorial

def ncr(n, r):
    return factorial(n)/(factorial(r)*factorial(n-r))

counter = 0
for n in range(23, 101):
    for r in range(2, n-1):
        if ncr(n, r) > 1000000:
            counter += 1
print(counter)
