def fib(n, d):
    # Uses dynamic programming
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib(10, d))

