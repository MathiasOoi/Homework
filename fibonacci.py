def fibonacci(n):
    if n == 1:
        return 1
    else:
        n1 = 0
        n2 = 1
        for i in range(2, n):
            x = n1 + n2
            n1 = n2
            n2 = x

    return x


print(fibonacci(10))
