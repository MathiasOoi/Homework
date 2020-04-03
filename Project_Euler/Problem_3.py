x = 600851475143
k = x
largest = 0
i = 2
# All integers (except for 1) can be written as a product of prime numbers
while i**2 <= x:
    if k % i == 0:
        k /= i
        largest = i
    else:
        i += 1
print(largest)


