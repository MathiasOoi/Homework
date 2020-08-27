from math import factorial
from collections import defaultdict

d = defaultdict(int)
for i in range(10):
    d[i] = factorial(i)

print(sum(i for i in range(3, 100000) if sum(d[int(k)] for k in str(i)) == i))
