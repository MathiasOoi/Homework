from decimal import *
getcontext().prec = 102

def sqrt(n, e):
    x = Decimal(n)

    while True:
        root = Decimal(Decimal(0.5) * (x+(n/x)))
        if abs(root-x) < e:
            break
        x = root

    return root

def solve():
    total = 0
    for n in range(1, 101):
        if n in [i**2 for i in range(10)]:
            continue
        s = str(sqrt(n, float("0."+"0"*100+"1"))).replace(".", "", 1)[:100]
        total += sum(int(i) for i in s)
    return total


if __name__ == "__main__":
    print(solve() - 1)
