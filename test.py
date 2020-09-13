from math import factorial as f

def ncr(n, r):
    return int(f(n)/(f(r)*f(n-r)))

if __name__ == "__main__":
    print([[ncr(n, r) for r in range(0, n+1)] for n in range(15)])


