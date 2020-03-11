primeNumbers = 0
compositeNumbers = 0


def prime(x):
    if x >= 2:
        for i in range(2, x/2):
            if not (x % i):
                return False
    else:
        return False
    return True


for i in range(2, 1001):
    if prime(i):
        primeNumbers += i
    else:
        compositeNumbers += i
print(compositeNumbers - primeNumbers)
