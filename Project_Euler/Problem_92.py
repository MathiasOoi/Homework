def foo(n):
    while n != 1 and n != 89:
        s = str(n)
        n = sum(int(i)**2 for i in s)
    return n

if __name__ == "__main__":
    counter, cache = 0, {}
    for i in range(1, 10000001):
        lst = []
        while i != 1 and i != 89:
            if i in cache:
                i = cache[i]
                break
            s = str(i)
            lst.append(i)
            i = sum(int(k)**2 for k in s)
        if i == 89:
            counter += 1
        for x in lst:
            cache[x] = i
    print(counter)

