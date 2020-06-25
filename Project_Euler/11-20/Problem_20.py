import math
def solve(n):
    return sum(int(i) for i in str(math.factorial(n)))
print(solve(100))