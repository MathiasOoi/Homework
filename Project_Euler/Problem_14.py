# http://radiusofcircle.blogspot.com

# time module for calculating execution time
import time

start = time.time()

dic = {1: 1, 2: 2}


for n in range(3, 1000000):
    counter = 0
    original_number = n
    while n > 1:
        if n < original_number:
            dic[original_number] = dic[n] + counter
            break

        if n % 2 == 0:
            n = n / 2
            counter += 1
        else:
            n = 3 * n + 1
            counter += 1

longest, n = 0, 0
for key, value in dic.items():
    if value > longest:
        longest = value
        n = key
print(n)