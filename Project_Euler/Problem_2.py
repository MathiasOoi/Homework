def fib(n, d):
    # Uses dynamic programming
    if n in d:
        return d[n]
    else:
        ans = fib(n-1, d) + fib(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
sum = 0
i = 1
while sum < 4000000:
    if fib(i, d) % 2 == 0:
        sum += fib(i, d)
    i += 1
print(sum)

