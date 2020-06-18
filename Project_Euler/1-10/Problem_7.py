from math import sqrt; from itertools import count, islice
k = 1
n = 1
while k != 10001:
    if n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1))):
        k += 1
    n += 2
print(n)

