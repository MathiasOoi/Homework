def fib_gen():
    i, a, b = 1, 1, 1
    while True:
        yield a, i
        a, b, i = b, b+a, i+1

for k, i in fib_gen():
    if len(str(k)) == 1000:
        print(i)
        break

