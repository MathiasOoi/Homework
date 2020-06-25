def sum_of_divisors(n):
    return sum(set(k for x in ([i, n//i] for i in range(2, int(n**0.5) + 1) if not n % i) for k in x)) + 1

def solve():
    abundant_nums, sums = [n for n in range(28123) if sum_of_divisors(n) > n][1:], set()
    for a in abundant_nums:
        for b in abundant_nums:
            sums.add(a+b)
    return sum(i for i in range(28123) if i not in sums)

print(solve())